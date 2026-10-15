# ml-service-template — Phase 0, Module 1

**Status:** An instructor-designed learning project. This is a deterministic business rule, **not a trained ML model**.

## Why it exists

Provide an installable Python package with a stable CLI, explicit failure behavior, pure domain logic, and unit/integration tests. This is only Module 1 of Phase 0, not a completed production service.

## Setup (recommended: uv; internet needed once for first dependency resolution)

Install Python 3.12 and uv. In repository root:

```bash
uv sync
uv run --with pytest pytest -q
uv run ml-service --amount 2500 --past-due 2
```

Or, in a virtual environment with pip:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e . pytest
python -m pytest -q
ml-service --amount 2500 --past-due 2
```

Expected output: `{"category": "medium", "score": 50}`. Invalid input must exit with code `2`, log an error to stderr, and not write JSON to stdout.

## Boundary

`src/ml_service/domain.py` holds deterministic domain logic without I/O. `src/ml_service/cli.py` parses human inputs, validates them, calls domain logic, serializes JSON output, and determines the process exit status.

## Deliberate failure drills

1. `uv run ml-service --amount -1 --past-due 0` → nonzero exit.
2. Remove package installation and run from elsewhere → diagnose import boundary.
3. Change function behavior (threshold) without updating tests → red unit test.
4. Inject `float('nan')` or negative count in a unit test → rejected inputs.

## Next modules

Module 2: configuration vs secrets, config validation, logging, runtime state.
Module 3: comprehensive tests, typing, linting, formatting.
Module 4: Linux, subprocess, SQL, DNS/HTTP/TLS.
Module 5: Docker/Compose.
Module 6: Git/CI/immutable artifacts.
Module 7: incident and clean-checkout defense.

A lockfile will be generated as part of the reproducibility lesson; commit it. `uv run --with pytest` is a **learning convenience only**; Phase 0 acceptance must use a committed locked development dependency, not an ad hoc dependency.
