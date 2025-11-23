from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.button_registration = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, name: str, password: str):

        self.email_input.fill(email)
        self.username_input.fill(name)
        self.password_input.fill(password)

    def click_registration_form(self):
        self.button_registration.click()