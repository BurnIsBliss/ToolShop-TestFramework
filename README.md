# ToolShop-TestFramework

In this project I've build a test automation framework harnessing the power of Python and Selenium to test the [ToolShopDemo](https://v1.practicesoftwaretesting.com/#/) website. Pytest and pytest-html has been used to run tests and generate html reports respectively.

## Project Structure

The framework has been designed in way, so as provide readability and maintainability. Here's is quick short description of each directory's used here:

    1. PageObjects: Includes all the pages within the website where we run the tests
    2. Tests: Houses the test files within it, for each page mentioned within the 'PageObjects' directory.
    3. Utilities: Contains the BaseClass class that is necessary for each test case within project.
    4. Logs: Place to save the log file for each run.
    5. Reports: Contains the 'report.html' file that displays the outcomes of the executed tests.
    6. conftest.py: Implemented a custom commandline parameter and SetUp() fixture within the file.

## Project Features

-   Framework follows the Page Object Model (POM).
-   Have implemented and used logging through all of the test cases.
-   Has got a custom commandline parameter which can be used to select the browser environment (Firefox/Chrome) for testing.

## Test Cases

    * Tool name, brand name and pricing tests (test_Tools.py)
        1. Check the total number of tools within the home page.
        2. Check for the proper naming format for the tool names.
        3. Check whether all the prices are mentioned in '$'.
        4. Check whether the tool details mentioned within the home page and the product page are the same.
        5. Check the brand name for each tool.
    * Tool category tests (test_category.py)
        1. Check the respective headings for both (Hand tools and Power tools) tool categories are right.
        2. Check whether the correct tools are mentioned for the two tool categories.
        3. Check the category names for both set of tools.
    * Contact page tests (test_contactPage.py)
        1. Check with various values for the name field, email field, select dropdown and the message field.
