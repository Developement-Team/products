Feature: The product management service back-end
    As a Product management Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description              | category          | price     | available  | rating   | no_of_users_rated |
        | t_shirt    | Blue T-Shirt             | Men's Clothing    | 95.26     | True       | 4.62     | 5                 |
        | Shirt      | Black Shirt              | Men's Clothing    | 26.25     | False      | 3.57     | 3                 |
        | Jeans      | Denim Jeans              | Women's Clothing  | 25.45     | True       | 4.9      | 7                 |
        | SportsWear | White Tees for Sports    | Women's Clothing  | 56.26     | True       | 4.62     | 5                 |

Scenario: The server is running
    When I visit the "home page"
    Then I should see "Products Demo REST API Service"
    And I should not see "404 Not Found"

Scenario: Create a product
    When I visit the "Home Page"
    And I set the "Name" to "Jeans"
    And I set the "Category" to "Women's clothing"
    And I set the "Description" to "Denim Jeans"
    And I select "True" in the "Available" dropdown
    And I set the "Price" to "25.45"
    And I set the "Rating" to "4.9"
    And I set the "Number of rating" to "7"
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And the "Category" field should be empty
    And the "Description" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    And I should see "Women's clothing" in the "Category" field
    And I should see "Denim Jeans" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "25.45" in the "Price" field

Scenario: List all products
    When I visit the "home page"
    And I press the "search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Shirt" in the results
    And I should see "Jeans" in the results
    And I should see "SportsWear" in the results

Scenario: Delete a Product
    When I visit the "home page"
    And I set the "Name" to "Shirt"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Shirt" in the "Name" field
    When I press the "Delete" button
    And I press the "Clear" button
    And I press the "search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Jeans" in the results
    And I should see "SportsWear" in the results

Scenario: Retrieve a Product
    When I visit the "home page"
    And I set the "Name" to "Jeans"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    And I should see "Denim Jeans" in the "Description" field
    And I should see "Women's Clothing" in the "Category" field
    