# ToolShop-TestFramework

In this project I've built an automation testing framework by harnessing the powers of Python and Selenium to validate the [ToolShopDemo](https://v1.practicesoftwaretesting.com/#/) website for various issues and bugs. I have used pytest and pytest-html plugin to run tests and generate HTML reports.

## Project Structure

The framework has been designed in a way, as to provide easy comprehension and maintainability. Here's a quick short description of each directory:

    1. PageObjects: Includes the different pages where we'll be running the tests.
    2. Tests: Houses the test files which inturn contains valid test cases for each page mentioned within the 'PageObjects' directory.
    3. Utilities: Contains the 'BaseClass' class that is necessary for each test case.
    4. Logs: Place to save the log file, which contains necessary details of each run.
    5. Reports: Contains the 'report.html' file that displays the outcomes of the executed tests in HTML format.
    6. conftest.py: Implemented a custom commandline parameter and SetUp() fixture within the file.

## Project Features

-   Framework follows the Page Object Model (POM).
-   Have implemented and used logging functionality throughout all of the test cases.
-   Has got a custom commandline parameter which can be used to select the browser environment (Firefox/Chrome).

## Test Cases

    * Tool name, brand name and pricing tests (test_Tools.py)
        1. Check the total number of tools within the page.
        2. Check for the proper naming format for each tool.
        3. Check whether all the prices are displayed in '$' format.
        4. Check whether the tool details mentioned within the home page and the product page are the same.
        5. Check the brand name for each tool.
    * Tool category tests (test_category.py)
        1. Check the respective headings for both (Hand tools and Power tools) tool categories.
        2. Check whether the correct tools are mentioned for both tool categories.
        3. Check the category name for both set of tools.
    * Contact page tests (test_contactPage.py)
        1. Check with various values for the name, email, select dropdown and the message fields.
