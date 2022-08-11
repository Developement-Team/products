# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa

import os
import requests
from behave import given
from compare import expect


@given("the following products")
def step_impl(context):
    """Load the database with new products"""
    # List all of the products and delete them one by one
    rest_endpoint = f"{context.BASE_URL}/api/products"
    context.resp = requests.get(rest_endpoint)
    #expect(context.resp.status_code).to_equal(200)
    for product in context.resp.json():
        context.resp = requests.delete(f"{rest_endpoint}/{product['id']}")
        expect(context.resp.status_code).to_equal(204)
    for row in context.table:
        payload = {
            "name": row["name"],
            "description": row["description"],
            "category": row["category"],
            "price": float(row["price"]),
            "available": row["available"] in ["True", "true", "1"],
            "rating": row["rating"],
            "no_of_users_rated": row["no_of_users_rated"],
        }
        context.resp = requests.post(rest_endpoint, json=payload)
        expect(context.resp.status_code).to_equal(201)
