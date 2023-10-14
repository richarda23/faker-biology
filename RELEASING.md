Notes for maintainers on how to release / publish the project

- create a release branch
- update dependencies using `poetry update`
- create a tag for the release
- oadd new contributors,
- update changelog
- publish using `poetry build` and `poetry publish -u __token__ -p <your pypi api token>`
- 
