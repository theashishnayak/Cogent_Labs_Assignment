Feature: Partial purchase Flow use path 
    
    Scenario: Navigate to the homepage and validate the title and number of items
        Given the user navigates to "https://practicesoftwaretesting.com"
        Then the title should be "Practice Software Testing - Toolshop - v5.0"
        And the number of items in the page should be 9
        When the mouse hovers over first item image
        Then the image changes

    Scenario Outline: Validate the items under the conditions set
        Given the user is on the page "https://practicesoftwaretesting.com"
        When the user selects the "<sort_option>" in sorting list
        And selects the price range minimum "<min>" and maximum "<max>"
        And selects the "<category>" category
        And selects the "<brand>" brand
        Then the items should be as per the filters set
        Examples:
            | sort_option | min | max | category | brand |
            | name,desc | 1 | 20 | hammer | ForgeFlex Tools |

    Scenario: Purchase Flow
        Given the user navigates to the homepage "https://practicesoftwaretesting.com"
        When the user click on first item
        Then can navigate to the item page
        And product name and price matches the homepage
        When the user clicks on + button 
        Then the quantity of the item should be increased by 1
        When the user clicks on "Add to Cart" button
        Then the item should be added to the cart and green notification should be displayed
        And validate api call "https://api.practicesoftwaretesting.com/carts" contains product id and quantity and return "200" 
        When the user clicks on "View Cart" button
        Then the user should be redirected to the cart page
        When user click on checkout button
        Then the user can navigate to the sign in page
        When click on cart icon
        When click on cross(x) button
        Then the item should be removed from the cart




        