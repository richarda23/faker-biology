# faker-biology

A Faker extension library providing fake biological data. Public PyPI package — keep the API stable.

## Workflow

- `main` is branch-protected; all changes go via PR
- Always work on a named branch (`fix/issue-number` or `release/x.y.z`)
- **Write a failing test first**, then fix, then confirm the test passes
- Run the full suite before pushing: `poetry run python -m pytest faker_biology/tests/`

## Release process

See `RELEASING.md`. Short version: release branch → update deps + changelog + version → PR → merge → tag → `poetry publish`.

## Stack

- Python, Poetry, pytest
- No external APIs or databases; all data is in-memory

## Conventions

- Each provider lives in its own submodule under `faker_biology/`
- Tests live in `faker_biology/tests/`
- Data files are co-located with their provider module
