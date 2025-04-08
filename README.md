# Playwright Coding Assignment

This assignment demonstrates the use of Playwright for browser automation, Python for scripting, and Behave for implementing Behavior-Driven Development (BDD).

## Overview

This assignment is as per the guidelines specified.

## Technologies Used

* **Playwright:** A library for automating web browsers.  This project uses the Playwright Python bindings.
* **Python:** The scripting language used to write the automation code.
* **Behave:** A Behavior-Driven Development (BDD) framework.  Behave uses Gherkin syntax to define test scenarios.

## Setup Instructions

Follow these steps to set up the project:

1.  **Prerequisites:**

    * **Python:** Ensure Python 3.7 or later is installed.  Download from [https://www.python.org/downloads/](https://www.python.org/downloads/).
    * **pip:** Python's package installer (usually included with Python).

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Pandoranayak/Assignment.git
    ```

3.  **Activate the virtual environment in the project**

    * Open a terminal in the project root and enter the following command:
    ```bash
    source bin/activate
    ```



## Running the Tests

To run the Behave tests:

* Run the below command in the project root directory
  
```bash
behave
```

To run the tests with report generation:

* Run the below command in the project root directory
  
```bash
python run_tests.py
```

This will execute all feature files in the features/ directory.

```bash
Project Structure. Here's my project structure:
├── features/
│   ├── menu_item_validation.feature     # Feature files in Gherkin
│   └── partial_purchase_flow.feature
├── steps/
│   ├── menu_item_validation_step.py           # Python code to implement Gherkin steps
│   └── partial_purchase_flow_steps.py
├── requirements.txt         # Python dependencies
├── environment.py        # Browser context and logger functionality
├── run_test.py        
├── behave.ini       
└── README.md                 # This file
```

**Debugging**
For debugging i have added follwoing checks:
1. Custom logger - Logging is added in every step to verify where the script is getting error.
2. Screenshots - Screenshots will be saved for the error screen.
3. Screenrecord - A screenrecord of every scenario will be saved.


## Features tested in this assignment

***Part 1***

**1. Feature: Partial purchase flow for the website**

*Scenario 1: Open the website and validate the title and number of items in the page*
```text
- Open the URL
- Title is validated
- Number of items in the page is validated
- Mouse hover over the image
- Validates that the hover changes the image
```
*Scenario 2: Validate the items in the page after putting certain filters*
```text
- Open the URL
- User selects the sorting order
- User selects the price range (Drags the min and max value)
- User selects the category checkbox
- User selects the brand checkbox
- Validates that the items in the page after the filters are as per the conditions set by the filters
```
*Scenario 3: Validate the purchase flow when checking out a item*
```text
- Open the URL
- User clicks on a item
- User can navigate to the selected item page
- Validates that the item page information for the product matches the homepage
- User clicks on "+" button to increase the quantity
- Validates that the item quantity is increased by 1
- User clicks on "Add to cart button"
- Validates Item is added to cart and green notification is visible
- Validates the API call
- User clicks on "View cart" button
- Validate that the user is naviagted to the cart page
- User clicks on "Checkout" button
- Validates that the user is redirected to the sign in page
- User clicks on cart icon
- User clicks on the "x" button
- Validates that the item is removed from the cart
```

***Part 2***

**2. Feature: Validating menu item categories**

*Scenario : Validating menu item category dropdown*
```text
- Open the URL
- User clicks on category
- Validating the items in the dropdown and the order of the items
- User clicks on one of the category
- Validated that the user is redirected to the selected category page and the url contains the category
- Validates the title of the landing page
```




***Part 3***

*Question : How would you go about testing performance limitations [Loading times or users
capacity...] for such a website and how you would go about testing it [Tools,
priorities...].*

*Step-by-Step Approach*

*Define Objectives:*

1. Loading Times: Measure how quickly pages and elements load.
2. User Capacity: Determine how many users the website can handle without performance degradation.

Select Tools:

1. JMeter: Ideal for simulating load testing across different scenarios such as peak traffic or sustained high usage.
2. BlazeMeter: Extension for JMeter in cloud environments for scalability and detailed reporting.

*Create a Test Strategy:*

Determine Key Performance Indicators (KPIs):

1. Response time
2. Error rates

Set Priorities:

1. Test frequently accessed pages and features.
2. Simulate realistic user behavior based on site analytics.

*Design Test Scenarios:*

1. Load Testing: Simulate normal expected traffic with a gradual ramp-up.
2. Stress Testing: Push the system to its limits by increasing users until performance drops
3. Spike Testing: Introduce sudden bursts of load to check how the system handles peak traffic.
4. Endurance Testing: Run tests over an extended period to detect memory leaks and ensure sustained performance.

*Configure JMeter Test Plan:*

1. Thread Group: Define the number and behavior of simulated users.
2. HTTP Samplers: Configure requests to the website’s endpoints.
3. Timers: Introduce delays to simulate real user behavior.
4. Listeners: Utilize to capture and visualize test data.

*Execution and Monitoring:*

1. Begin by executing the test plans using JMeter or command-line modes.
2. Use Grafana or similar tools to monitor server health and resource usage in real-time.

*Analyze Results:*

1. Identify bottlenecks by analyzing response times, throughput graphs, and server metrics.
2. Focus on any errors in requests or significant slowdowns under load.

*Optimize and Retest:*

1. Implement changes based on analysis, such as code optimizations or infrastructure scaling.
2. Retest to verify improvements and continue iterating as needed.

*Reporting:*

1. Generate detailed reports that summarize the findings, including performance metrics, identified issues, and recommendations for optimization.
2. Use the data gathered to inform stakeholders and guide further development or infrastructure decisions.



   

