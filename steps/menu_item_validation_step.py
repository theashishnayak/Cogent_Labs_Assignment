from behave import given, then, when
from playwright.sync_api import expect

@given('the user is on page "{url}"')
def step_impl(context, url):
    context.logger.info(f"Navigating to: {url}")
    context.page.goto(url, wait_until="networkidle")
    context.logger.info("Navigation completed.")

@when('the user clicks on categories')
def click_categories(context):
    context.logger.info("Clicking on categories...")
    context.page.locator('[data-test=\"nav-categories\"]').click()
    context.logger.info("Clicked on categories.")

@then('the dropdown should be displayed with all items in order')
def check_dropdown_items(context):
    context.logger.info("Checking if the dropdown is displayed...")
    dropdown = context.page.locator("ul[aria-label='nav-categories'] ")
    expect(dropdown).to_be_visible()
    context.logger.info("Dropdown is visible.")

    expected_items = [
        "Hand Tools",
        "Power Tools",
        "Other",
        "Special Tools",
        "Rentals",
    ]
    
    context.logger.info("Verifying dropdown items...")
    for item in expected_items:
        expect(dropdown.locator(f"text={item}")).to_be_visible()
        context.logger.info(f"Item '{item}' is visible in the dropdown.")

@when('user click on the category "Rentals"')
def click_category(context):
    context.logger.info(f"Clicking on category: Rentals")
    context.page.locator("[data-test='nav-rentals']").click()
    context.logger.info(f"Clicked Rental category")


@then('the user is taken to the landing page for "Rentals"')
def check_landing_page(context,):
    context.logger.info(f"Checking landing page for category: Rentals")
    expect(context.page).to_have_url("https://practicesoftwaretesting.com/rentals")
    context.logger.info("Landing page URL is correct.")

@then('the title of the landing page should be "Rentals Overview - Practice Software Testing - Toolshop - v5.0"')
async def check_landing_page_title(context):
    context.logger.info(f"Checking landing page title.")
    act_title = await context.page.title()
    exp_title = "Rentals Overview - Practice Software Testing - Toolshop - v5.0"
    expect(act_title).to_equal(exp_title)
    context.logger.info(f"Actual Title: '{act_title}'")  # Added logging
    assert act_title == exp_title, f"Expected title '{exp_title}', but got '{act_title}'"
    context.logger.info("Title validation passed.")
