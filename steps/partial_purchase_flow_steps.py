from behave import given, then, when
from playwright.sync_api import *
import asyncio

import time


@given('the user navigates to "{url}"')
def navigate_to_website(context, url):
    context.logger.info(f"Navigating to: {url}")
    context.page.goto(url, wait_until="networkidle")
    context.logger.info("Navigation completed.")

@then('the title should be "{exp_title}"')
def validate_title(context, exp_title):
    context.logger.info(f"Validating title is :'{exp_title}'")
    actual_title = context.page.title()
    context.logger.info(f"Actual Title: '{actual_title}'")  # Added logging
    assert actual_title == exp_title, f"Expected title '{exp_title}', but got '{actual_title}'"
    context.logger.info("Title validation passed.")

@then('the number of items in the page should be 9')
def validate_items_count(context):
    context.logger.info("Validating number of items in the page.")
    product_grid = context.page.locator(".col-md-9")
    expect(product_grid.get_by_role("link")).to_have_count(9)
    context.logger.info(f"Expected items count: 9, Actual items count: {product_grid.get_by_role('link').count()}")
    context.logger.info("Items count validation passed.")

@when('the mouse hovers over first item image')
def hover_over_item(context):
    context.logger.info("Hovering over the first item image.")
    context.image = context.page.locator("img[alt=\"Combination Pliers\"]")
    context.initial_transform = context.image.evaluate("el => getComputedStyle(el).transform")
    context.logger.info(f"Initial image transform: {context.initial_transform}")

    context.image.hover()
    context.page.wait_for_timeout(5000)  # Wait for 5 seconds to observe the hover effect

@then('the image changes')
def validate_image_change(context):
    context.logger.info("Validating image change on hover.")
    hovered_transform = context.image.evaluate("el => getComputedStyle(el).transform")
    context.logger.info(f"Hovered image transform: {hovered_transform}")

    assert context.initial_transform != hovered_transform, "Image transform did not change on hover."
    context.logger.info("Hover effect validation passed.")

@given('the user is on the page "{url}"')
def navigate_to_website(context, url):
    context.logger.info(f"Navigating to: {url}")
    context.page.goto(url, wait_until="networkidle")
    context.logger.info("Navigation completed.")

@when('the user selects the "{sort_option}" in sorting list')
def select_sorting_option(context, sort_option):
    context.logger.info(f"Selecting sorting option: {sort_option}")
    context.page.locator("[data-test=\"sort\"]").select_option(sort_option)
    context.logger.info("Sorting option selected.")

@when('selects the price range minimum "{min_value}" and maximum "{max_value}"')
def select_price_range(context, min_value, max_value):
    context.logger.info(f"Selecting price range: Min = {min_value}, Max = {max_value}")
    
    # Locate the minimum and maximum sliders
    slider_min_locator = context.page.locator(".ngx-slider-pointer-min")
    slider_max_locator = context.page.locator(".ngx-slider-pointer-max")
    
    # Move the minimum slider
    slider_min_locator.focus()
    context.logger.info(f"Moving minimum slider from 0 to {min_value}")
    for _ in range(int(min_value) - 1):
        slider_min_locator.press("ArrowRight")
    
    # Move the maximum slider in steps of 5
    slider_max_locator.focus()
    context.logger.info(f"Moving maximum slider from 100 to {max_value} in steps of 5")
    current_value = 100
    while current_value > int(max_value):
        step = min(5, current_value - int(max_value))  # Calculate the step size
        for _ in range(step):
            slider_max_locator.press("ArrowLeft")
        current_value -= step
@when('selects the "{category}" category')
def select_category(context, category):
    context.logger.info(f"Selecting category: {category}")
    context.page.locator("#filters").get_by_text("Hammer").click()
    context.logger.info("Category selected.")

@when('selects the "{brand}" brand')
def select_brand(context, brand):
    context.logger.info(f"Selecting brand: {brand}")
    context.page.get_by_text("ForgeFlex Tools").click()
    context.logger.info("Brand selected.")

@then('the items should be as per the filters set')
def validate_items_after_filter(context):
    context.logger.info("Validating items after applying filters.")
    product_names = []
    product_prices = []
    
    # Locate product elements
    link_elements = context.page.locator(".col-md-9").all()
    price_elements = context.page.locator("span[data-test='product-price']").all()
    
    # Define expected price range
    expected_min_price = 1
    expected_max_price = 20
    
    # Iterate over each product element
    for link, price_element in zip(link_elements, price_elements):
        try:
            # Find the product name within each product element
            name_elements = link.locator("h5[data-test='product-name']").all()
            for name_element in name_elements:
                name = name_element.inner_text().strip()
                product_names.append(name)

            # Validate product price
            price_text = price_element.inner_text().strip().replace('$', '')
            price = float(price_text)
            product_prices.append(price)
            assert expected_min_price <= price <= expected_max_price, f"Price {price} is not within the expected range {expected_min_price}-{expected_max_price}."
            context.logger.info(f"Product price '{price}' is within the expected range.")
            
        except Exception as e:
            context.logger.error(f"Error retrieving product details: {e}")
            continue
    
    # Validate sorting order
    is_descending_order = all(product_names[i] >= product_names[i + 1] for i in range(len(product_names) - 1))
    if is_descending_order:
        context.logger.info("Items are sorted in descending order alphabetically.")
    else:
        context.logger.info("Items are not sorted in descending order alphabetically.")
        raise AssertionError("Items are not sorted in descending order alphabetically.")

@given('the user navigates to the homepage "https://practicesoftwaretesting.com"')
def navigate_to_homepage(context):
    context.logger.info("Navigating to homepage.")
    context.page.goto("https://practicesoftwaretesting.com", wait_until="networkidle")
    context.logger.info("Homepage navigation completed.")
    try:
        # 1. Locate the product name and price elements
        product_name_locator = context.page.locator("[data-test='product-name']").first
        product_price_locator = context.page.locator("[data-test='product-price']").first

        # 2. Get the text content of the name and price
        context.product_name_homepage = product_name_locator.inner_text()
        context.product_price_homepage = product_price_locator.inner_text()
        context.product_price_homepage = context.product_price_homepage.replace("$", "").strip()

        context.logger.info(f"Product name on homepage: '{context.product_name_homepage}'")
        context.logger.info(f"Product price on homepage: '{context.product_price_homepage}'")

    except Exception as e:
        context.logger.error(f"Error getting product name/price on homepage: {e}")
        assert False, "Error getting product name/price on homepage"

@when('the user click on first item')
def click_on_first_item(context):

    context.logger.info("Clicking on the first item.")
    context.page.get_by_text("Combination Pliers").click()
    context.logger.info("First item clicked.")
    
@then('can navigate to the item page')
def validate_item_page(context):
    context.logger.info("Validating item page navigation.")
    time.sleep(2)  # Wait for the page to load
    item_page_title  = context.page.title()
    exp_item_title =  "Combination Pliers - Practice Software Testing - Toolshop - v5.0"
    assert item_page_title == exp_item_title, f"Expected title '{exp_item_title}', but got '{item_page_title}'"    
    context.logger.info("Item page navigation validated.")

@then('product name and price matches the homepage')
def validate_product_name_and_price(context):
    context.logger.info("Validating product name and price match with homepage.")
    context.product_name = context.page.locator("[data-test=\"product-name\"]").inner_text()
    context.product_price = context.page.locator("[data-test=\"unit-price\"]").inner_text()
    context.logger.info(f"Product name: '{context.product_name}', Product price: '{context.product_price}'")
    assert context.product_name == context.product_name_homepage, "Product name does not match."
    assert context.product_price == context.product_price_homepage, "Product price does not match."
    context.logger.info("Product name and price validation passed.")

@when('the user clicks on + button')
def click_plus_button(context):
    context.logger.info("Clicking on '+' button.")
    context.page.locator("[data-test=\"increase-quantity\"]").click()
    context.logger.info("'+' button clicked.")
    context.page.wait_for_timeout(2000)

@then('the quantity of the item should be increased by 1')
def validate_quantity_increase(context):
    context.logger.info("Validating quantity increase.")
    quantity = context.page.locator("[data-test=\"quantity\"]").input_value()
    context.logger.info(f"Current quantity: '{quantity}'")
    assert int(quantity) == 2, f"Expected quantity to be 2, but got {quantity}"
    context.logger.info("Quantity increase validated.")

@when('the user clicks on "Add to Cart" button')
def add_to_cart(context):
    context.logger.info("Clicking on 'Add to Cart' button.")
    
    # Set up response listener before clicking
    context.post_response_promise = context.page.expect_response(
        lambda response: "https://api.practicesoftwaretesting.com/cart/" in response.url
    )
    
    # Click the button
    context.page.locator("[data-test=\"add-to-cart\"]").click()
    context.logger.info("'Add to Cart' button clicked.")
    context.page.wait_for_timeout(2000)
@then('the item should be added to the cart and green notification should be displayed')
def validate_cart_notification(context):
    context.logger.info("Validating cart notification.")
    cart_notification = context.page.get_by_role("alert", name="Product added to shopping").inner_text()
    context.logger.info(f"Cart notification: '{cart_notification}'")
    assert "Product added to shopping" in cart_notification, "Cart notification not displayed."
    context.logger.info("Cart notification validated.")


@then('validate api call "{api_url}" contains product id and quantity and return "{exp_status}"')
def validate_api_call(context, api_url, exp_status):
    context.logger.info("Validating POST API call for adding item to cart.")
    try:
        # Use expect_response to wait for the response
        with context.page.expect_response(lambda response: api_url in response.url and response.status == int(exp_status)) as response_info:
            # Perform the action that triggers the API call
            context.page.locator("[data-test=\"add-to-cart\"]").click()

        # Get the response object
        post_response = response_info.value
        context.logger.info(f"POST response status: {post_response.status}")
        assert post_response.status == int(exp_status), f"Expected status {exp_status}, but got {post_response.status}"
        
        # Parse and validate POST response
        post_response_json = post_response.json()
        context.logger.info(f"POST response JSON: {post_response_json}")
        
        # Validate product_id and quantity
        id = post_response_json.get('id')
        # Use:
        cart_items = post_response_json.get('cart_items', [])
        assert len(cart_items) > 0, "Cart items list is empty in the POST response JSON."

        # Get the first item for validation
        first_item = cart_items[0]
        quantity = first_item.get('quantity')
        assert id is not None, "Product ID is missing in the POST response JSON."
        assert quantity is not None, "Quantity is missing in the POST response JSON."
        context.logger.info(f"Product ID: {id}, Quantity: {quantity}")
        
        
        context.logger.info("POST API call validation completed.")
    except Exception as e:
        context.logger.error(f"Error validating POST API call: {e}")
        assert False, f"POST API call validation failed: {str(e)}"

@when('the user clicks on "View Cart" button')
def click_view_cart(context):
    context.logger.info("Clicking on 'View Cart' button.")
    context.page.locator("[data-test=\"nav-cart\"]").click()
    context.logger.info("'View Cart' button clicked.")
    context.page.wait_for_timeout(2000)

@then('the user should be redirected to the cart page')
def validate_cart_page(context):
    context.logger.info("Validating cart page redirection.")
    cart_page_title = context.page.title()
    context.logger.info(f"Cart page title: '{cart_page_title}'")
    assert "Checkout - Practice Software Testing - Toolshop - v5.0" in cart_page_title, "Not redirected to the cart page."
    context.logger.info("Cart page redirection validated.")

@when('user click on checkout button')
def click_checkout_button(context):
    context.logger.info("Clicking on 'Checkout' button.")
    context.page.locator("[data-test=\"proceed-1\"]").click()
    context.logger.info("'Checkout' button clicked.")
    context.page.wait_for_timeout(2000)

@then('the user can navigate to the sign in page')
def validate_sign_in_page(context):
    context.logger.info("Validating sign-in page navigation.")
    login_locator = context.page.locator("h3", has_text="Login")
    expect(login_locator).to_be_visible()
    context.logger.info("Sign-in page header is visible.")

@when('click on cart icon')
def click_cart_icon(context):
    context.logger.info("Clicking on cart icon.")
    context.page.get_by_text("Cart1").click()
    context.logger.info("Cart icon clicked.")
    context.page.wait_for_timeout(2000)

@when('click on cross(x) button')
def click_cross_button(context):
    context.logger.info("Clicking on cross (x) button.")
    context.page.get_by_role("row", name="Combination Pliers  Quantity").locator("a").click()
    context.logger.info("Cross (x) button clicked.")
    context.page.wait_for_timeout(2000)

@then('the item should be removed from the cart')
def validate_item_removal(context):
    context.logger.info("Validating item removal notification")
    cart_notification = context.page.get_by_role("alert", name="Product deleted.").inner_text()
    context.logger.info(f"Cart notification: '{cart_notification}'")
    assert "Product deleted." in cart_notification, "Cart notification not displayed."
    context.logger.info("Cart notification for item removal validated.")
