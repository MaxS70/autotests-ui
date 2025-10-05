from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_disabled()

    email_input=page.locator('//div[@data-testid="registration-form-email-input"]//div/input')
    email_input.fill("user.name@gmail.com")

    user_name_input=page.locator('//div[@data-testid="registration-form-username-input"]//div/input')
    user_name_input.fill('username')

    password_input=page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_enabled()



    page.wait_for_timeout(5000)