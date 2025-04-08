Feature: Validating the menu item category dropdown

    Background: The user navigates to the website
        Given the user is on page "https://practicesoftwaretesting.com"


    Scenario: Validate the menu item category dropdown
        When the user clicks on categories
        Then the dropdown should be displayed with all items in order
        When user click on the category "Rentals"
        Then the user is taken to the landing page for "Rentals"
        And the title of the landing page should be "Rentals Overview - Practice Software Testing - Toolshop - v5.0"
