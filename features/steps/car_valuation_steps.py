import os
from behave import given, when, then
from pages.car_search_page import CarSearchPage
from pages.base_page import BasePage
from utils.read_file import get_car_registration_numbers, get_expected_details

@given('Reads the input text file {input_file}')
def step_impl(context, input_file):
    input_file_path = os.path.join(os.getcwd(), 'data', input_file)  # Correctly construct the file path
    context.registration_numbers = get_car_registration_numbers(input_file_path)

@when('Navigate to website and perform get my car valuation')
def step_impl(context):
    BasePage.initialize_browser()
    context.page = CarSearchPage()
    context.page.click_accept_link()
    context.list_map = {}
    for reg_number in context.registration_numbers:
        details_page = context.page.send_registration_num_and_random_mileage(reg_number)
        if details_page.get_registration_number():
            context.list_map[reg_number] = [
                details_page.get_registration_number(),
                details_page.get_make(),
                details_page.get_model(),
                details_page.get_year()
            ]
        else:
            print(f"Car details not found: {reg_number}")
        context.page = details_page.click_back_button_to_search_page()

@then('Compare the details in output text file {output_file}')
def step_impl(context, output_file):
    output_file_path = os.path.join(os.getcwd(), 'data', output_file)  # Correctly construct the file path
    expected_map = get_expected_details(output_file_path)
    assert expected_map == context.list_map, "Car Input details not matched with Output car details"
    BasePage.close_browser()

