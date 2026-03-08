Notes for maintainers on how to release / publish the project

Branch protection is enabled on `main` — all changes must go via a PR.

## Steps

1. Create a release branch:
   ```
   git checkout main && git pull
   git checkout -b release/x.y.z
   ```

2. Update dependencies:
   ```
   poetry update
   ```

3. Update `CHANGELOG.md` — move items from `Unreleased` into a new versioned section with today's date.

4. Bump the version in `pyproject.toml`.

5. Add any new contributors to `CONTRIBUTORS.md`.

6. Run the test suite to confirm everything passes:
   ```
   poetry run python -m pytest faker_biology/tests/
   ```

7. Commit and push, then open a PR from `release/x.y.z` into `main`:
   ```
   git add pyproject.toml poetry.lock CHANGELOG.md CONTRIBUTORS.md
   git commit -m "Release x.y.z"
   git push -u origin release/x.y.z
   ```

8. Merge the PR once approved.

9. Pull main, tag the release, and publish to PyPI:
   ```
   git checkout main && git pull
   git tag vx.y.z && git push origin vx.y.z
   poetry build
   poetry publish -u __token__ -p <your pypi api token>
   ```
