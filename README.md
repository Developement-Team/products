# NYU DevOps Project-- Product Team

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://github.com/Products-Development-Team/products/actions/workflows/tdd.yml/badge.svg)](https://github.com/Products-Development-Team/products/actions)
[![Build Status](https://github.com/Products-Development-Team/products/actions/workflows/bdd.yml/badge.svg)](https://github.com/Products-Development-Team/products/actions)
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org/)
[![codecov](https://codecov.io/gh/Products-Development-Team/products/branch/master/graph/badge.svg?token=PZG0GGW7VJ)](https://codecov.io/gh/Products-Development-Team/products)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
  - [Software Installation](#software-installation)
  - [Bring up development environment](#bring-up-development-environment)
- [Services](#services)
  - [Run TDD tests](#run-tdd-tests)
  - [Run BDD tests](#run-bdd-tests)
  - [RESTful API](#restful-api)
- [Features in the project](#features-in-the-project)
- [Project File Structure](#project-file-structure)
- [License](#license)

## Overview
This is an NYU DevOps project that creates a RESTful microservice using Python Flask and PostgreSQL. In particular, we have created a Product Resource as an important part of a E-commerce website. We utilized the template code provided at https://github.com/nyu-devops/ by Professor Rofrano arcoss various repositories. The application is currently deployed to a Kubernetes cluster on IBM cloud. The IP address is [**here**](http://159.122.174.17:31002/). You can also run it locally with the following setup. 

## Prerequisites
### Software Installation
This project uses Docker and VS Code with the Remote Containers extension to provide a consistent repeatable disposable development environment. 

You will need the following software installed: 
- Docker Desktop
- VS Code
- Remote Containers extension from the VS Code Marketplace

### Bring up development environment
To bring up the development environment you should clone this repo, change into the repo directory, and then open Visual Studio Code using the code . command. VS Code will prompt you to reopen in a container and you should select it. This will take a while the first time as it builds the Docker image and creates a container from it to develop in.

```bash
git clone git@github.com:Products-Development-Team/products.git
cd products
code .
```
## Services
### Run TDD tests
You can run the tests in a ```bash``` terminal using the following command: 
```bash
make test
```
This will run the test suite and report the code coverage. 

### Run BDD tests
You can start with a ```bash``` terminal and run the REST service using the following command:
```bash
make run
```
You should be able to open a web page on a local browser
Then start another ```bash``` terminal and run the ```behave``` test:
```bash
behave
```
### RESTful API
We provide a Swagger API Documentation [here](http://159.122.174.17:31002/apidocs). You can see the details of the Product Model and route services we provide. You can try the functionalities out using the Swagger API. Main routes are also listed below in the chart: 
| Endpoint                                  | Method    | Description |
|-------------------------------------------|-----------|-------------|
|`api/products   `                               | **POST**      | Creates a new Product |
|`api/products/<int:product_id>    `             | **DELETE**    | Deletes a product with the given product_id |
|`/ `                                         | **GET**       | Gets the details of all available API's |
|`api/products `                                 | **GET**       | Gets the details of all the products |
|`api/products/<int:product_id>    `             | **GET**       | Get the details of a particular product |
`api/products/<int:product_id>        `         | **PUT**       | Updates multiple fields of a product |
|`api/products/<int:product_id>/category     `   | **PUT**       | Updates the category of the product |
|`api/products/<int:product_id>/description `    | **PUT**       | Updates the description of a product |
|`api/products/<int:product_id>/price   `        | **PUT**       | Updates the price of a product |
|`api/products/<int:product_id>/rating`          | **PUT**       | Updates the rating of a product |

The method : `GET /products` supports Query Strings with multiple constraints.  
For example : `GET /products?rating=3&price=50` will return the list of all products with `Rating >= 3` and `Price <= 50`.  


## Features in the project
* app/routes.py -- the main Service routes using Python Flask
* app/models.py -- the data model using SQLAlchemy
* tests/test_routes.py -- test cases against the Product service
* tests/test_models.py -- test cases against the Product model

## Project File Structure
```text
.
├── Dockerfile
├── LICENSE
├── Makefile
├── Procfile
├── README.md
├── __pycache__
│   └── config.cpython-39.pyc
├── config.py
├── coverage.xml
├── deploy
│   ├── deployment.yaml
│   ├── postgresql.yaml
│   ├── service.yaml
│   ├── dev.yaml
├── dot-env-example
├── features
│   ├── environment.py
│   ├── steps
│   │   ├── web_steps.py
│   │   └── products_steps.py
│   └── products.feature
├── requirements.txt
├── service
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
|   |   ├── config.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   └── routes.cpython-39.pyc
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── blue_bootstrap.min.css
│   │   │   ├── cerulean_bootstrap.min.css
│   │   │   ├── darkly_bootstrap.min.css
│   │   │   ├── flatly_bootstrap.min.css
│   │   │   └── slate_bootstrap.min.css
│   │   ├── images
│   │   │   └── newapp-icon.png
│   │   ├── index.html
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery-3.6.0.min.js
│   │       └── rest_api.js
│   └── utils
│       ├── __pycache__
│       │   ├── cli_commands.cpython-39.pyc
│       │   ├── error_handlers.cpython-39.pyc
│       │   ├── log_handlers.cpython-39.pyc
│       │   └── status.cpython-39.pyc
│       ├── cli_commands.py
│       ├── error_handlers.py
│       ├── log_handlers.py
│       └── status.py
├── setup.cfg
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── factories.cpython-39.pyc
    │   ├── test_models.cpython-39.pyc
    │   └── test_routes.cpython-39.pyc
    ├── factories.py
    ├── test_models.py
    └── test_routes.py
```

## License

Copyright (c) John Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU masters class: **CSCI-GA.2820-001 DevOps and Agile Methodologies** created and taught by *John Rofrano*, Adjunct Instruct
## License

Copyright (c) John Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU masters class: **CSCI-GA.2820-001 DevOps and Agile Methodologies** created and taught by *John Rofrano*, Adjunct Instructor, NYU Courant Institute, Graduate Division, Computer Science, and NYU Stern School of Business.
