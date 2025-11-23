from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input=page.locator('//div[@data-testid="registration-form-email-input"]//div/input')
    email_input.fill("user.name@gmail.com")

    user_name_input=page.locator('//div[@data-testid="registration-form-username-input"]//div/input')
    user_name_input.fill('username')

    password_input=page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill('password')

    button_registration=page.locator('//button[@data-testid="registration-page-registration-button"]')
    button_registration.click()

    dashboard_title = page.locator('//*[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    page.wait_for_timeout(5000)


