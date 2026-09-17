# Human operating sequence

1. Verify that the work is explicitly authorized and record the exact scope and authorization basis.
2. Confirm an in-scope asset before mapping interfaces.
3. Record at least five key interfaces from permitted observation and organize them into an interface map.
4. Select one hypothesis tied to the recorded interfaces and define the expected safe behavior.
5. Perform any target-side validation manually, with a baseline and one controlled change.
6. Record security-tool output as Candidate. Do not mark it Confirmed without manual replay and a concrete impact statement.
7. Stop immediately when a boundary issue, sensitive non-owned data, or service instability is observed.
8. Produce a minimum redacted recap and close the session once the validation path ends.

The runtime enforces only the documented selected gates. The human remains responsible for authorizations, action-level judgment, and evidence handling.
