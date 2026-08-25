Simple python app for showing devops things - github actions, interaction with docker hub, etc.

# Running locally

The app itself is using FastAPI.
You can launch it locally via:
```
uv run fastapi dev
```

# Linting and testing

For linting, `ruff` is used:
```
uv run ruff check
```

For testing, `pytest` is used:
```
uv run pytest
```
You can also create your own HTML report:
```
uv run pytest --html=pytest_report.html --self-contained-html
```


# Docker

The app is later deployed 
To build the docker image:
```
docker build -f app.dockerfile -t mike239x/demo_app .
```
To run the image in a container:
```
docker container run -p 8000:8000/tcp --rm -ti mike239x/demo_app
```

# TODOs

- security gates?
- replace deployment to FastAPI with something that uses docker image we created
- add test report to the job summary
- code coverage (pytest can do it)
- "integration tests"?


# Things that didn't work

- docker build with attestation
- docker scout
- it appears a single `git push --tags` with both commits and a new tag only triggers one workflow (the staging one)
  not sure how to fix this currently