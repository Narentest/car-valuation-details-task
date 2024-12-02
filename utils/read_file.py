import re

def get_car_registration_numbers(input_file_name):
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
    reg_numbers = []
    reg_pattern = re.compile(r'^[A-Z]{2}[0-9]{2}([A-Z]{3}|\s[A-Z]{3})$')
    for line in lines:
        words = line.split()
        for word in words:
            if reg_pattern.match(word):
                reg_numbers.append(word)
    return reg_numbers

def get_expected_details(output_file_name):
    with open(output_file_name, 'r') as file:
        lines = file.readlines()
    expected_map = {}
    for line in lines[1:]:  # Skip header
        parts = line.strip().split(',')
        expected_map[parts[0]] = parts[1:]
    return expected_map