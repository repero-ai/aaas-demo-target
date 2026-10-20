# aaas-demo-target

Small, deliberately boring Python package used as the **test repository** of the
Agent Execution Plane / Git Cache Engine PoC (`repero-ai/agent-execution-plane`).

Agents receive tasks against this repo (e.g. "add a function + tests"), the PoC runs
`pytest` in an isolated utility pod and produces commits on `agent/*` branches.
Nothing here is production code.

```bash
uv run --with pytest pytest -q
```
