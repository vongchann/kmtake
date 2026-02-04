# Contributing

Thanks for contributing! A few quick guidelines to get started.

Setup
1. Create and activate a virtualenv:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   pip install pre-commit ruff
   ```

2. Run pre-commit hooks locally before committing:
   ```powershell
   .\.venv\Scripts\pre-commit.exe run --all-files
   ```

Testing
- Run unit tests:
  ```powershell
  .\.venv\Scripts\python.exe -m pytest -q
  ```

Branching & PRs
- Create a feature branch: `git checkout -b feature/your-feature`
- Commit changes with clear messages and push the branch.
- Open a PR; CI will run tests and linters.

Code style
- This repo uses `ruff` and `black` via `pre-commit`. Run `ruff format .` to auto-format.

If you're unsure about anything, open an issue or a draft PR and request feedback.
