import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Login credentials
login = {
    'userName': '<inputUserName>',
    'password': '<inputPassword>'
}

# Form information
credentials = {
    'firstName': '<inputFirstName>',
    'lastName': '<inputLastName>',
    'city': '<inputCity>',
    'email': '<inputEmail>',
    'phone': '<inputPhone>',
    'age': '<inputAge>'
}

def initialize_browser(website):
    browser = webdriver.Chrome()
    print("---- Initializing Browser ----")
    # Browser will load website specified in parameter
    browser.get(website) 
    return browser

def get_login(browser):
    print("---- Clicking on login link ----")
    # Click on login link 
    browser.execute_script("document.getElementsByClassName('ex-content-click log-in-link capture_modal_open')[0].click();")

    print("---- Filling in login credentials ----")
    # Wait until login page loads or after 5 seconds and then fill in username and password
    usernameInput = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID,'capture_signIn_traditionalSignIn_emailAddress')))
    usernameInput.send_keys(login['userName'])
    passwordInput = browser.find_element_by_id('capture_signIn_traditionalSignIn_password')
    passwordInput.send_keys(login['password'])
    
    print("---- Submitting ----")
    # Find the login button and submit
    submitInput = browser.find_element_by_id('capture_signIn_traditionalSignIn_signInButton')
    submitInput.submit()
    

def fill_submit_form(browser):
    print("---- Finding iFrame form ----")
    # Wait until the iFrame loads and switch selection into it
    wait = WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[data-ss-embed="iframe"][scrolling="no"]')))

    print("---- Finding Input in iFrame form ----")
    # Wait until the class name loads inside iFrame and select for it by class name
    wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ssRegistrationField')))
    frameElems = browser.find_elements_by_class_name('ssRegistrationField')
    labels = browser.find_elements_by_css_selector('span.ssLabelText')

    # Fill in form according to the credentials dictionary
    for i, elem in enumerate(frameElems): 
        print(f"---- Filling in credentials: {labels[i].text} with {list(credentials.values())[i]} ----")
        elem.send_keys(list(credentials.values())[i])
    
    print("---- Submitting ----")
    # Find submit button and click it
    browser.execute_script("document.getElementsByClassName('ssButtonContinue')[0].click();")

def closeBrowser(browser):
    print("---- Closing browser in 5 seconds ----")
    time.sleep(5)
    browser.quit()

# Entry point for program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        browser = initialize_browser(sys.argv[1])
    else:
        browser = initialize_browser('https://www.680news.com/2019/02/05/win-passes-to-the-2019-canadian-international-autoshow/')
    get_login(browser)
    fill_submit_form(browser)
    closeBrowser(browser)
