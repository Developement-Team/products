# NYU DevOps Project-- Product Team

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://github.com/Products-Development-Team/products/actions/workflows/tdd.yml/badge.svg)](https://github.com/Products-Development-Team/products/actions)
[![Build Status](https://github.com/Products-Development-Team/products/actions/workflows/bdd.yml/badge.svg)](https://github.com/Products-Development-Team/products/actions)
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org/)
[![codecov](https://codecov.io/gh/Products-Development-Team/products/branch/master/graph/badge.svg?token=PZG0GGW7VJ)](https://codecov.io/gh/Products-Development-Team/products)

This is an NYU DevOps project that creates a RESTful microservice of Products using Python Flask and PostgreSQL. The application is currently deployed to a Kubernetes cluster on IBM cloud. The IP address is [**here**](http://159.122.174.17:31002/). You can also run it locally with the following setup. 

- [Prerequisites](#prerequisites)
  - [Software Installation](#software-installation)
  - [Bring up development environment](#bring-up-development-environment)
- [Services](#services)
  - [Run TDD tests](#run-tdd-tests)
  - [Run BDD tests](#run-bdd-tests)
  - [RESTful API](#restful-api)
- [Features in the project](#features-in-the-project)
- [License](#license)


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
|`/products   `                               | **POST**      | Creates a new Product |
|`/products/<int:product_id>    `             | **DELETE**    | Deletes a product with the given product_id |
|`/ `                                         | **GET**       | Gets the details of all available API's |
|`/products `                                 | **GET**       | Gets the details of all the products |
|`/products/<int:product_id>    `             | **GET**       | Get the details of a particular product |
`/products/<int:product_id>        `         | **PUT**       | Updates multiple fields of a product |
|`/products/<int:product_id>/category     `   | **PUT**       | Updates the category of the product |
|`/products/<int:product_id>/description `    | **PUT**       | Updates the description of a product |
|`/products/<int:product_id>/price   `        | **PUT**       | Updates the price of a product |
|`/products/<int:product_id>/rating`          | **PUT**       | Updates the rating of a product |

The method : `GET /products` supports Query Strings with multiple constraints.  
For example : `GET /products?rating=3&price=50` will return the list of all products with `Rating >= 3` and `Price <= 50`.  


## Features in the project
* app/routes.py -- the main Service routes using Python Flask
* app/models.py -- the data model using SQLAlchemy
* tests/test_routes.py -- test cases against the Product service
* tests/test_models.py -- test cases against the Product model
## License

Copyright (c) John Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU masters class: **CSCI-GA.2820-001 DevOps and Agile Methodologies** created and taught by *John Rofrano*, Adjunct Instructor, NYU Courant Institute, Graduate Division, Computer Science, and NYU Stern School of Business.
