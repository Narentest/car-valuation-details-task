
# Car Valuation Details

This project is a Python-based automation framework for verifying car valuation details using Selenium, Behave (Cucumber for Python), and Allure reports. The project follows the Page Object Model (POM) design pattern.

## Project Structure

## Prerequisites

- Python 3.13
- Pip (Python package installer)
- Chrome browser

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   
2. **Install dependencies:**
pip install -r requirements.txt

3. **Ensure the data files are in place:**
data/car_input.txt
data/car_output.txt

**Configuration**
[DEFAULT]
url=https://www.webuyanycar.com
browser=chrome

1.**Running the Tests:**
 behave --tags=@carSearch

2.**Generate Allure report:** 
allure serve reports/


