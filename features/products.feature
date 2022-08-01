Feature: The product management service back-end
    As a Product management Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description              | category          | price     | available  | rating   | no_of_users_rated |
        | t_shirt    | Blue T-Shirt             | Men's Clothing    | 95.26     | true       | 4.62     | 5                 |
        | Shirt      | Black Shirt              | Men's Clothing    | 26.25     | false      | 3.57     | 3                 |
        | Jeans      | Denim Jeans              | Women's Clothing  | 25.45     | true       | 4.9      | 7                 |
        | SportsWear | White Tees for Sports    | Women's Clothing  | 56.26     | true       | 4.62     | 5                 |

Scenario: The server is running
    When I visit the "home page"
    Then I should see "Products Demo REST API Service"
    And I should not see "404 Not Found"

Scenario: List all products
    When I visit the "home page"
    And I press the "search" button
    Then I should see the message "Success"
    And I should see "t_shirt" in the results
    And I should see "Shirt" in the results
    And I should see "Jeans" in the results
    And I should see "SportsWear" in the results