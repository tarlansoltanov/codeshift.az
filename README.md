# CodeShift

## Description

CodeShift is website for the "CodeShift" company. It is a platform for the company to provide information about their services, products, and contact information. The website is built with Django.

## Getting Started

### Dependencies

- [Python](https://www.python.org/downloads/) >= 3.10
- [Poetry](https://python-poetry.org/docs/#installation) >= 1.7.1
- [Docker](https://docs.docker.com/get-docker/) >= 24.0.7

### Installing

1. Clone the repository

    ```bash
    git clone https://github.com/tarlansoltanov/codeshift.az.git
    ```

2. Install dependencies

    ```bash
    make install
    ```

3. (Optional) Create environment file from example (Required for running project with Docker)

    ```bash
    make cp-env
    ```

### Executing program

1. Run project in local environment

    ```bash
    make run-local
    ```

2. Run project in local environment with Docker

    ```bash
    make run-local-docker
    ```

3. Run project in development environment with Docker

    ```bash
    make run-dev
    ```

4. Run project in production environment with Docker

    ```bash
    make run-prod
    ```
