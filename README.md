# Wallet Exchange Rate Service API

This repository contains the code for the Wallet Exchange Rate Service API. This microservice provides exchange rates between currencies using the ExchangeRate API.

## Installation

### Define variables

In the `Makefile`, you'll find the following variables:

```make
DOCKER_IMAGE_NAME = wallet_exchange_rate_service_api 
DOCKER_CONTAINER_NAME = wallet_exchange_rate_service_container
```

### Building the Docker Image
To build the Docker image, run the following command:

```bash
make build
```

This will create a Docker image named wallet_exchange_rate_service_api.

### Running the Docker Container
To run the Docker container, use the command:

```bash
make run
```
This command starts the container in detached mode, mapping port 5005 on your host machine to port 5003 in the container. The container will be named wallet_exchange_rate_service_container.

### Stopping and Removing the Docker Container
To stop and remove the Docker container, execute:

```bash
make stop
```
This command stops and removes the container named wallet_exchange_rate_service_container.

Make sure you have Docker installed on your system before running these commands.

## API Documentation

This project provides API documentation in the form of a Swagger YAML file. You can view the API documentation by following these steps:

1. Navigate to the `docs/open_api` directory in your project.
2. Locate the file named `swagger.yml`.
3. Open the swagger.yml file using a text editor or a Swagger viewer tool.
4. Go through the documentation and be happy! :)

## Integration to ExpressRate API 

ExpressRate API is a public API available through internet that doesn't require any account creation and can be accessed (https://www.exchangerate-api.com/docs/free)[here].

### License
This project is licensed under the MIT License.

