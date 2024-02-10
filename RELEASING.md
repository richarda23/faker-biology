Notes for maintainers on how to release / publish the project

- create a release branch
- update dependencies using `poetry update`
- update changelog
- add new contributors
- create a tag for the release
- publish using `poetry build` and `poetry publish -u __token__ -p <your pypi api token>`
