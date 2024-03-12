# python-fastapi-postgres-terraform-aws
Project is accompanied by working code examples of a Python-FastAPI Application, Docker Image & Terraform code.
# Architecture
![image](https://github.com/saikrishnakuppa/python-fastapi-postgres-terraform-aws/assets/8674115/26d9dfc8-710d-4b04-8c3d-b637b75358b7)

# Objectives
1. Create a FastAPI Application Using Python & Postgres as backend database.
2. Dockerize the FastAPI Application using Docker.
3. Create a Terraform template to provision & deploy docker image in AWS

Terraform enables you to create, change & improve infrastructure using code. By the end of this section we will be able to run one command to deploy entire application which gives us:
1. A Virtual Private Cloud with Public and private subnets
2. Internet Gateway to contact the outer world
3. Security groups for RDS Postgres and for ECS
4. A Load balancer distributing traffic between containers & database
5. RDS Postgres instance
6. Auto scaling group for ECS cluster with launch configuration
7. ECS cluster with task and service definition
8. AWS Certificate Manager with SSL/TLS certificte installed

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
docker build --file Dockerfile --platform=linux/amd64  --tag "<<your personal docker hub>>/fast-api-docker-example" .

# 6. Apply Tag to Docker image
docker tag "<<your personal docker hub>>/fast-api-docker-example:latest" "<<your personal docker hub>>/fast-api-docker-example:latest"

# 7. Push Docker image to DockerHub
docker push "<<your personal docker hub>>>/fast-api-docker-example:latest"

# 8. Run Terrform to create AWS Infra
terraform apply

# 9. Test Application ALB after deploying
Login to AWS Console to grab the application load balancer URL from EC2/Load Balancer tab
https://<<your application ALB URL>/sample/fast-api/docs

# 10. Destroy AWS Infra after testing/validating (to save cost)
terraform destroy
```

## Formatting

Run `pipenv run format` to run formatting for the project via Black.

## Linting

Run `pipenv run lint` to run linting for the project via Pylint.

## Testing

Run `pipenv run test` to run unit tests for the project via Pytest.
