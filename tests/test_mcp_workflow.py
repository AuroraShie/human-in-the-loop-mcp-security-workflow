from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src import pentestgpt_mcp as adapter


class PentestGPTMcpWorkflowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_session_root = adapter.SESSION_ROOT
        adapter.SESSION_ROOT = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        adapter.SESSION_ROOT = self.original_session_root
        self.temp_dir.cleanup()

    def create_session(self) -> str:
        result = adapter.create_authorized_session(
            task_description="Offline MCP workflow acceptance test; no network target.",
            target_scope="local.test only",
            authorization_basis="User owns the local test fixture and requested this offline test.",
            target_kind="local_lab",
            authorization_confirmed=True,
        )
        return result["session"]["session_id"]

    def add_confirmed_asset(self, session_id: str) -> None:
        adapter.record_asset(
            session_id=session_id,
            asset="local.test",
            ownership_evidence="Local offline fixture owned by the user.",
            status="confirmed",
            in_scope=True,
            tech_stack_evidence="Synthetic test application.",
            business_value="MCP workflow validation only.",
        )

    def add_five_endpoints(self, session_id: str) -> None:
        for number in range(1, 6):
            adapter.record_endpoint(
                session_id=session_id,
                asset="local.test",
                page=f"Page {number}",
                role="test user",
                object_type="test object",
                action="read",
                identifier=f"own-id-{number}",
                identity_context="owned test account",
                method="GET",
                path=f"/api/test/{number}",
                response_signature="Synthetic 200 JSON response.",
                expected_authorization="Only the owned test account can read its object.",
                candidate_hypothesis="Access-control consistency.",
                data_classification="own_or_test",
            )

    def test_authorization_is_required(self) -> None:
        with self.assertRaises(ValueError):
            adapter.create_authorized_session(
                task_description="Unauthorized workflow must be rejected.",
                target_scope="local.test",
                authorization_basis="No valid authorization for this negative test.",
                target_kind="local_lab",
                authorization_confirmed=False,
            )

    def test_five_endpoint_and_manual_replay_gates(self) -> None:
        session_id = self.create_session()
        self.add_confirmed_asset(session_id)
        with self.assertRaises(ValueError):
            adapter.select_hypothesis(
                session_id=session_id,
                direction="access control",
                rationale="Testing the five-endpoint gate.",
                endpoint_numbers=[1],
                expected_safe_behavior="Reject unauthorized access.",
            )

        self.add_five_endpoints(session_id)
        lead = adapter.record_scanner_lead(
            session_id=session_id,
            tool_name="Synthetic scanner",
            target_asset="local.test",
            claimed_issue="Possible access-control inconsistency",
            evidence_summary="Synthetic candidate only; no request was sent.",
        )
        self.assertEqual(lead["lead"]["status"], "candidate_manual_replay_required")

        hypothesis = adapter.select_hypothesis(
            session_id=session_id,
            direction="access control",
            rationale="Five mapped endpoints share an owned object boundary.",
            endpoint_numbers=[1, 2],
            expected_safe_behavior="Reject requests outside the owned test object.",
        )["hypothesis"]

        with self.assertRaises(ValueError):
            adapter.record_validation(
                session_id=session_id,
                hypothesis_id=hypothesis["hypothesis_id"],
                baseline_summary="Owned fixture returned its synthetic object.",
                single_change="Removed the synthetic identity context.",
                observed_result="Synthetic response still returned the object.",
                actual_impact="Synthetic unauthorized access in the fixture.",
                conclusion="confirmed",
                manual_replay_confirmed=False,
                sensitive_non_owned_data_seen=False,
                service_instability_seen=False,
            )

        result = adapter.record_validation(
            session_id=session_id,
            hypothesis_id=hypothesis["hypothesis_id"],
            baseline_summary="Owned fixture returned its synthetic object.",
            single_change="Removed the synthetic identity context.",
            observed_result="Synthetic response still returned the object.",
            actual_impact="The offline fixture demonstrates a reproducible access-control failure.",
            conclusion="confirmed",
            manual_replay_confirmed=True,
            sensitive_non_owned_data_seen=False,
            service_instability_seen=False,
        )
        self.assertTrue(result["workflow"]["report_ready"])
        self.assertEqual(result["workflow"]["phase"], "reporting")

    def test_sensitive_data_forces_stop(self) -> None:
        session_id = self.create_session()
        self.add_confirmed_asset(session_id)
        self.add_five_endpoints(session_id)
        hypothesis = adapter.select_hypothesis(
            session_id=session_id,
            direction="file authorization",
            rationale="Offline stop-condition test.",
            endpoint_numbers=[1],
            expected_safe_behavior="Only owned files are returned.",
        )["hypothesis"]
        result = adapter.record_validation(
            session_id=session_id,
            hypothesis_id=hypothesis["hypothesis_id"],
            baseline_summary="Synthetic owned file baseline.",
            single_change="Synthetic identity boundary comparison.",
            observed_result="Fixture flagged non-owned sensitive data.",
            actual_impact="No real data; this is an offline stop-condition test.",
            conclusion="suspected",
            manual_replay_confirmed=True,
            sensitive_non_owned_data_seen=True,
            service_instability_seen=False,
        )
        self.assertEqual(result["workflow"]["status"], "stopped")
        self.assertFalse(result["workflow"]["report_ready"])


if __name__ == "__main__":
    unittest.main()
