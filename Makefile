# Define variables
DOCKER_IMAGE_NAME = wallet_user_identity_service_image
DOCKER_CONTAINER_NAME = wallet_user_identity_service_container 

export FLASK_APP=src/app/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export PYTHONPATH=$(shell pwd)

dev:
	flask run --port=8082 

clean:
	rm -rf __pycache__/

# Build the Docker image
build:
		docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d -p 8082:8082 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop and remove the Docker container
stop:
		docker stop $(DOCKER_CONTAINER_NAME)
		docker rm $(DOCKER_CONTAINER_NAME)

db-migrate:
	cat src/infra/db/database/migration.sql | sqlite3 src/infra/db/database/database.db

