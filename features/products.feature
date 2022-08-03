Feature: The product management service back-end
    As a Product management Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description              | category          | price     | available  | rating   | no_of_users_rated |
        | t_shirt    | Blue T-Shirt             | Men's Clothing    | 95.26     | True       | 4.62     | 5                 |
        | Shirt-B    | Black Shirt              | Men's Clothing    | 26.25     | False      | 3.57     | 3                 |
        | Jeans      | Denim Jeans              | Women's Clothing  | 25.45     | True       | 4.9      | 7                 |
        | SportsWear | White Tees for Sports    | Women's Clothing  | 56.26     | True       | 4.62     | 5                 |

Scenario: The server is running
    When I visit the "home page"
    Then I should see "Products Demo REST API Service"
    And I should not see "404 Not Found"

Scenario: List all products
    When I visit the "home page"
    And I press the "search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Shirt-B" in the results
    And I should see "Jeans" in the results
    And I should see "SportsWear" in the results

Scenario: Delete a Product
    When I visit the "home page"
    And I set the "Name" to "Shirt-B"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Shirt-B" in the "Name" field
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

Scenario: Search for Men's Clothing
    When I visit the "home Page"
    And I set the "Category" to "Men's Clothing"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Shirt-B" in the results
    And I should not see "Jeans" in the results
    And I should not see "SportsWear" in the results

Scenario: Search for available
    When I visit the "home Page"
    And I select "True" in the "Available" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Jeans" in the results
    And I should see "SportsWear" in the results
    And I should not see "Shirt-B" in the results

Scenario: Search for Women's Clothing with Rating > 4 and Price < 30
    When I visit the "home Page"
    And I set the "Category" to "Women's Clothing"
    And I set the "Price" to "30"
    And I set the "Rating" to "4"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Jeans" in the results

<<<<<<< HEAD
Scenario: Add a rating
    When I visit the "home Page"
    And I set the "Name" to "Shirt-B"
    And I press the "Search" button
    Then I should see the message "Success"
    # And I should see "3" in the "Number of ratings" field 
    When I copy the "Id" field
    When I set the "Id" field
    And I add the "Rating" to "2"
    And I press the "Add-Rating" button
    Then I should see the message "Rating added"
    # When I paste the "Id" field 
    # And I press the "Retrieve" button
    # Then I should see "4" in the "Number of ratings" field
=======
Scenario: Create a product
    When I visit the "Home Page"
    And I set the "Name" to "jacket"
    And I set the "Category" to "Men's clothing"
    And I set the "Description" to "black winter jacket"
    And I select "True" in the "Available" dropdown
    And I set the "Price" to "18"
    And I set the "Rating" to "3"
    And I set the "num rating" to "4"
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
    And I should see "jacket" in the "Name" field
    And I should see "Men's clothing" in the "Category" field
    And I should see "black winter jacket" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "8" in the "Price" field
    And I should see "3" in the "Rating" field
    And I should see "4" in the "Num Rating" field

Scenario: Update a Product name
    When I visit the "Home Page"
    And I set the "Name" to "Jeans"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    And I should see "Women's Clothing" in the "Category" field
    When I change "Name" to "JeanA"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "JeanA" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "JeanA" in the results

Scenario: Update a Product price
    When I visit the "Home Page"
    And I set the "Name" to "Jeans"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    And I should see "Women's Clothing" in the "Category" field
    When I change "Price" to "50"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "50" in the "Price" field

Scenario: Update a Product availability
    When I visit the "Home Page"
    And I set the "Name" to "Jeans"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Jeans" in the "Name" field
    And I should see "Women's Clothing" in the "Category" field
    When I select "False" in the "Available" dropdown
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "False" in the "Available" dropdown
>>>>>>> c1c852497cb666813dac873b446d7cf864aab769
