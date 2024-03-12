# Sample Fast API

## Local Setup

This project requires a minimum of Python 3.12.

To run API locally:

```bash

# 1. Install pipenv package manager
pip install pipenv==2023.10.3

# 2. Install project dependencies (this will automatically set up a virtual env)
PIPENV_VENV_IN_PROJECT=1 pipenv install

# 3. Start the local server
pipenv run server
```

### Alternative option for local setup

As an alternative to pipenv, the project dependencies may be installed using pip, following the creation of a virtual environment.

To run the API locally using pip:

```bash
# 1. Create a virtual environment to isolate the project dependencies
python -m venv .venv

# 2. Activate the virtual environment
# Linux/Bash:
source .venv/Scripts/activate
# MacOS:
source .venv/bin/activate
# Windows:
.venv/Scripts/activate.bat

# 3. Install project dependencies inside the virtual environment
pip install -r requirements.txt

# 4. Start the local server
uvicorn src.main:app --reload

# 5. Build docker image
docker build --file Dockerfile --platform=linux/amd64  --tag "saikrishnakuppa/fast-api-docker-example" .

# 6. Apply Tag to Docker image
docker tag "saikrishnakuppa/fast-api-docker-example:latest" "saikrishnakuppa/fast-api-docker-example:latest"

# 7. Push Docker image to DockerHub
docker push "saikrishnakuppa/fast-api-docker-example:latest"

# 8. Run Terrform to create AWS Infra
terraform apply

# 9. Test Application ALB after deploying
https://application-load-balancer-1903635959.us-east-1.elb.amazonaws.com/sample/fast-api/docs

# 10. Destroy AWS Infra after testing/validating (to save cost)
terraform destroy
```

## Formatting

Run `pipenv run format` to run formatting for the project via Black.

## Linting

Run `pipenv run lint` to run linting for the project via Pylint.

## Testing

Run `pipenv run test` to run unit tests for the project via Pytest.