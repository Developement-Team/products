"""
My Service

Describe what your service does here
"""

# import os
# import sys
# import logging
# from flask import Flask, request, url_for, jsonify, make_response, abort
from flask import jsonify, request, abort  # url_for
from flask_restx import Resource, fields, reqparse, inputs  # Api,
from service.utils import status  # HTTP Status Codes
from service.models import Product, MIN_PRICE, MAX_PRICE, MAX_DESCRIPTION_LENGTH

# Import Flask application
from . import app, api

MAX_CATEGORY_LENGTH = 63
######################################################################
# GET INDEX
######################################################################


@app.route("/")
def index():
    """Root URL response"""
    app.logger.info("Request for Root URL")
    return app.send_static_file("index.html")


# Define the model so that the docs reflect what can be sent
create_model = api.model(
    "Product",
    {
        "name": fields.String(required=True, description="The name of the product"),
        "category": fields.String(
            required=True,
            description="The category of product (e.g., men's clothing, women's clothing etc.)",
        ),
        "available": fields.Boolean(
            required=True, description="Is the product available for purchase?"
        ),
        "description": fields.String(
            required=True, description="The description of the product"
        ),
        "price": fields.Float(required=True, description="The price of the product"),
        "rating": fields.Float(description="The cumulative rating of the product"),
        "number of ratings": fields.Integer(
            description="The number of people who rated the product"
        ),
    },
)

product_model = api.inherit(
    "ProductModel",
    create_model,
    {
        "id": fields.String(
            readOnly=True, description="The unique id assigned internally by service"
        ),
    },
)

# query string arguments
product_args = reqparse.RequestParser()
product_args.add_argument(
    "name", type=str, required=False, help="List Products by name"
)
product_args.add_argument(
    "category", type=str, required=False, help="List Products by category"
)
product_args.add_argument(
    "available",
    type=inputs.boolean,
    required=False,
    help="List Products by availability",
)
product_args.add_argument(
    "price", type=float, required=False, help="List Products by price"
)
product_args.add_argument(
    "rating", type=float, required=False, help="List Products by rating"
)


######################################################################
#  PATH: /products/{id}
######################################################################
@api.route("/products/<product_id>")
@api.param("product_id", "The Product identifier")
class ProductResource(Resource):
    """
    ProductResource class

    Allows the manipulation of a single Product
    GET /product{id} - Returns a Product with the id
    PUT /product{id} - Update a Product with the id
    DELETE /product{id} -  Deletes a Product with the id
    """

    # ------------------------------------------------------------------
    # RETRIEVE A PRODUCT
    # ------------------------------------------------------------------
    @api.doc("get_products")
    @api.response(404, "Product not found")
    @api.marshal_with(product_model)
    # @app.route("/products/<int:product_id>", methods=["GET"])
    def get(self, product_id):
        """
        Retrieve a single Product

        This endpoint will return a Product based on it's id
        """
        app.logger.info("Request for product with id: %s", product_id)
        product = Product.find(product_id)
        if not product:
            abort(
                status.HTTP_404_NOT_FOUND,
                f"Product with id '{product_id}' was not found.",
            )

        app.logger.info("Returning product: %s", product.name)
        return product.serialize(), status.HTTP_200_OK

    # ------------------------------------------------------------------
    # UPDATE AN EXISTING PRODUCT
    # ------------------------------------------------------------------
    @api.doc('update_pets', security='apikey')
    @api.response(404, 'Product not found')
    @api.response(400, 'The posted Product data was not valid')
    @api.expect(product_model)
    @api.marshal_with(product_model)
    #@app.route("/products/<int:product_id>", methods=["PUT"])
    def put(self, product_id):
        """
        Update a Product

        This endpoint will update a Product based the body that is posted
        """
        app.logger.info("Request to update product with id: %s", product_id)
        check_content_type("application/json")

        product = Product.find(product_id)
        if not product:
            abort(
                status.HTTP_404_NOT_FOUND,
                f"Product with id '{product_id}' was not found.",
            )
        app.logger.info('Payload = %s ', api.payload)
        data = api.payload;
        product.deserialize(data)
        product.id = product_id
        product.update()
        app.logger.info("Product with ID [%s] updated.", product.id)
        return product.serialize(), status.HTTP_200_OK

    # ------------------------------------------------------------------
    # DELETE A PRODUCT
    # ------------------------------------------------------------------
    #@app.route("/products/<int:product_id>", methods=["DELETE"])
    @api.response(204, 'Pet deleted')
    def delete(self, product_id):
        """Delete a Product"""
        app.logger.info("Request to delete product with id: %s", product_id)
        product = Product.find(product_id)
        if product:
            product.delete()

        app.logger.info("Product with ID [%s] delete complete.", product_id)
        return "", status.HTTP_204_NO_CONTENT


######################################################################
#  PATH: /products
######################################################################
@api.route("/products", strict_slashes=False)
class ProductCollection(Resource):
    """Handles all interactions with collections of Products"""

    # ------------------------------------------------------------------
    # LIST ALL PRODUCTS
    # ------------------------------------------------------------------

    @api.doc("list_products")
    @api.expect(product_args, validate=True)
    @api.marshal_list_with(product_model)
    def check_category(self, category):
        products = Product.find_by_category(category)
        results = [product.serialize() for product in products]
        app.logger.info("Returning %d products", len(results))
        return results

    def check_price(self, price):
        price = float(price)
        if price < 0:
            raise ValueError
        products = Product.find_by_price(price)
        results = [product.serialize() for product in products]
        results.sort(key=lambda n: n["price"], reverse=True)
        return results

    def check_rating(self, rating_str):
        rating = float(rating_str)
        if rating < 1 or rating > 5:
            raise ValueError
        products = Product.find_by_rating(rating)
        results = [
            product.serialize() for product in products if product.rating is not None
        ]
        results.sort(key=lambda n: n["rating"], reverse=True)
        return results

    def check_name(self, name_str):
        products = Product.find_by_name(name_str)
        results = [product.serialize() for product in products]
        return results

    def eliminate_product(self, products_all, products):
        result = []
        tmpset = set()
        for product in products:
            tmpset.add(int(product["id"]))
        for product in products_all:
            if int(product["id"]) in tmpset :
                result.append(product)
        return result

    def check_availability(self, available):
        # if available != "True" or available != "true":
        #    raise ValueError
        products = Product.find_by_availability()
        results = [product.serialize() for product in products]
        return results

    # @app.route("/products", methods=["GET"])
    def get(self):
        app.logger.info("Request for Product List")
        products_all = Product.all()
        results_all = [product.serialize() for product in products_all]
        args = product_args.parse_args()
        try:
            if args['name']:
                results = self.check_name(args["name"])
                app.logger.info("Request for products with name : %s ", args["name"])
                results_all = self.eliminate_product(results_all, results)
            if args['category']:
                results = self.check_category(args["category"])
                app.logger.info("Request for products with category : %s ", args["category"])
                app.logger.info("Length of results : %s ", results)
                results_all = self.eliminate_product(results_all, results)
                app.logger.info("Length of results_all : %s ", results_all)
            if args['price'] is not None :
                results = self.check_price(args["price"])
                results_all = self.eliminate_product(results_all, results)
            if args["rating"] is not None:
                results = self.check_rating(args["rating"])
                results_all = self.eliminate_product(results_all, results)
            if args["available"] is not None:
                results = self.check_availability(args["available"])
                app.logger.info("Request for products with available : %s ", args["available"])
                results_all = self.eliminate_product(results_all, results)
        except ValueError:
            return "", status.HTTP_406_NOT_ACCEPTABLE
        app.logger.info("Returning %d products", len(results_all))
        return results_all, status.HTTP_200_OK

    # ------------------------------------------------------------------
    # ADD A NEW PRODUCT
    # ------------------------------------------------------------------

    @api.doc("create_products")
    @api.response(400, "The posted data was not valid")
    @api.expect(create_model)
    @api.marshal_with(product_model, code=201)
    # @app.route("/products", methods=["POST"])
    def post(self):
        """
        Creates a Product
        This endpoint will create a Product based the data in the body that is posted
        """
        app.logger.info("Request to create a product")
        check_content_type("application/json")
        data = api.payload

        data["rating"] = (
            None
            if "rating" not in data or data["rating"] is None
            else float(data["rating"])
        )
        data["no_of_users_rated"] = (
            0
            if "no_of_users_rated" not in data or data["no_of_users_rated"] is None
            else int(data["no_of_users_rated"])
        )

        product = Product()
        product.deserialize(data)
        app.logger.info("Here Deserialization done")
        product.create()
        message = product.serialize()
        location_url = api.url_for(
            ProductResource, product_id=product.id, _external=True
        )

        app.logger.info("Product with ID [%s] created.", product.id)
        return message, status.HTTP_201_CREATED, {"Location": location_url}

######################################################################
#  PATH: /products/{id}/rating
######################################################################
# ------------------------------------------------------------------
# UPDATE THE RATING OF A PRODUCT
# ------------------------------------------------------------------
@api.route("/products/<product_id>/rating")
@api.param('product_id','The Product Identifier')
class RatingResource(Resource):
    '''Rating actions of a Product'''
    @api.doc('Update The Rating')
    @api.response(404, 'Product not found')
    @api.response(406, 'JSON Not acceptable')
    def put(self, product_id):
        """
        Updates the rating of a product on the basis of feedback provided.
        Args:
            product_id (_type_): _description_
        """
        app.logger.info(
            "Request to update the rating of the product with id: %s", product_id
        )
        check_content_type("application/json")
        product = Product.find(product_id)
        if not product:
            app.logger.info("Inside this condition")
            abort(
                status.HTTP_404_NOT_FOUND,
                description=f"Product with id '{product_id}' was not found.",
            )
        new_rating = api.payload
        if not isinstance(new_rating["rating"], int):
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Rating should be of integer datatype",
            )
        if new_rating["rating"] <= 0 or new_rating["rating"] > 5:
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="The ratings can be from [1,5]",
            )
        if new_rating["rating"] is not None:
            product.id = product_id
            myJson = product.serialize()
            product.deserialize(myJson)
            product.id = product_id
            if product.rating is None or product.no_of_users_rated == 0:
                product.no_of_users_rated = 1
                product.rating = float(new_rating["rating"])
            else:
                product.rating = float(
                    product.rating * product.no_of_users_rated + new_rating["rating"]
                ) / (product.no_of_users_rated + 1)
                product.no_of_users_rated = product.no_of_users_rated + 1
            product.update()
            app.logger.info("Product with ID [%s] updated.", product.id)
        return product.serialize(), status.HTTP_200_OK

######################################################################
#  PATH: /products/{id}/price
######################################################################
# ------------------------------------------------------------------
# UPDATE THE PRICE OF A PRODUCT
# ------------------------------------------------------------------
@api.route("/products/<product_id>/price")
@api.param('product_id','The Product Identifier')
class PriceResource(Resource):
    '''Price Actions of a Product'''
    @api.doc('Update The Price')
    @api.response(404, 'Product not found')
    @api.response(406, 'JSON Format Not acceptable')
    def put(self, product_id):
        """
        Updates the price of a product on the basis of feedback provided.
        Args:
            product_id (_type_): _description_
        """
        app.logger.info(
            "Request to update the price of the product with id: %s", product_id
        )
        check_content_type("application/json")
        product = Product.find(product_id)
        if not product:
            app.logger.info("Product_id not found.")
            abort(
                status.HTTP_404_NOT_FOUND,
                description=f"Product with id '{product_id}' was not found.",
            )
        new_price = request.get_json()
        if "price" not in new_price or new_price["price"] is None:
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Price should be in dict name 'price'.",
            )
        if not isinstance(new_price["price"], float) and not isinstance(
            new_price["price"], int
        ):
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Price should be of float or int datatype",
            )
        new_price["price"] = float(new_price["price"])
        if new_price["price"] < MIN_PRICE or new_price["price"] > MAX_PRICE:
            abort(status.HTTP_406_NOT_ACCEPTABLE, description="New price out of range.")
        product.price = new_price["price"]
        product.update()
        app.logger.info("Price of product with ID [%s] updated.", product.id)
        return jsonify(product.serialize()), status.HTTP_200_OK

    ######################################################################
    #  PATH: /products/{id}/description
    ######################################################################
    # ------------------------------------------------------------------
    # UPDATE THE DESCRIPTION OF A PRODUCT
    # ------------------------------------------------------------------
    @app.route("/products/<int:product_id>/description", methods=["PUT"])
    def update_description_of_product(product_id):
        """
        Updates the description of a product on the basis of feedback provided.
        Args:
            product_id (_type_): _description_
        """
        app.logger.info(
            "Request to update the description of the product with id: %s", product_id
        )
        check_content_type("application/json")
        product = Product.find(product_id)
        if not product:
            app.logger.info("Product_id not found.")
            abort(
                status.HTTP_404_NOT_FOUND,
                description=f"Product with id '{product_id}' was not found.",
            )
        new_description = request.get_json()
        if (
            "description" not in new_description
            or new_description["description"] is None
        ):
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Description should be in dict name 'description'.",
            )
        if not isinstance(new_description["description"], str):
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Description should be of str datatype",
            )
        if len(new_description["description"]) > MAX_DESCRIPTION_LENGTH:
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Description length over limit.",
            )
        product.description = new_description["description"]
        product.update()
        app.logger.info("Description of product with ID [%s] updated.", product.id)
        return jsonify(product.serialize()), status.HTTP_200_OK

    ######################################################################
    #  PATH: /products/{id}/category
    ######################################################################
    # ------------------------------------------------------------------
    # UPDATE THE CATEGORY OF A PRODUCT
    # ------------------------------------------------------------------
    @app.route("/products/<int:product_id>/category", methods=["PUT"])
    def update_category_of_product(product_id):
        """
        Updates the category of a product on the basis of feedback provided.
        Args:
            product_id (_type_): _category_
        """
        app.logger.info(
            "Request to update the category of the product with id: %s", product_id
        )
        check_content_type("application/json")
        product = Product.find(product_id)
        if not product:
            app.logger.info("Product_id not found.")
            abort(
                status.HTTP_404_NOT_FOUND,
                description=f"Product with id '{product_id}' was not found.",
            )
        new_category = request.get_json()
        if "category" not in new_category or new_category["category"] is None:
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Category should be in dict name 'category'.",
            )
        if not isinstance(new_category["category"], str):
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Category should be of str datatype",
            )
        if len(new_category["category"]) > MAX_CATEGORY_LENGTH:
            abort(
                status.HTTP_406_NOT_ACCEPTABLE,
                description="Category length over limit.",
            )
        product.category = new_category["category"]
        product.update()
        app.logger.info("Description of product with ID [%s] updated.", product.id)
        return jsonify(product.serialize()), status.HTTP_200_OK


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################


def init_db():
    """Initializes the SQLAlchemy app"""
    global app
    Product.init_db(app)


def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        "Content-Type must be {}".format(media_type),
    )


# @app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
# def method_not_supported(error):
#     """Handles unsupported HTTP methods with 405_METHOD_NOT_ALLOWED"""
#     return (
#         jsonify(
#             status=status.HTTP_405_METHOD_NOT_ALLOWED,
#             error="Method not Allowed",
#             message=str(error),
#         ),
#         status.HTTP_405_METHOD_NOT_ALLOWED,
#     )
