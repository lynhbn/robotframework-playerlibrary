from playwright.sync_api import expect
from robotlibcore import keyword
from .base_context import BaseContext
from .config import *


class CheckboxHandler(BaseContext):

    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword('checkbox should be enabled')
    def checkbox_should_be_enabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_enabled(timeout=SMALL_TIMEOUT)

    @keyword('checkbox should be disabled')
    def checkbox_should_be_disabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_disabled(timeout=SMALL_TIMEOUT)

    @keyword('tick checkbox')
    def tick_checkbox(self, locator):
        element = self.get_element(locator)
        element.check()

    @keyword('untick checkbox')
    def untick_checkbox(self, locator):
        element = self.get_element(locator)
        element.uncheck()

    @keyword('checkbox should be checked')
    def checkbox_should_be_checked(self, locator):
        expect(self.get_element(locator)).to_be_checked()

    @keyword('checkbox should not be checked')
    def checkbox_should_not_be_checked(self, locator):
        expect(self.get_element(locator)).not_to_be_checked()

    @keyword('get current checkbox checking status')
    def get_current_checkbox_checking_status(self, locator):
        return self.get_element(locator).is_checked()

    @keyword('checkbox should be correct')
    def checkbox_should_be_correct(self, locator, state='enabled', status='unchecked'):
        element = self.get_element(locator)
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            expect(element).to_be_disabled()
        if status == 'unchecked':
            expect(element).not_to_be_checked()
        elif status == 'checked':
            expect(element).to_be_checked()

    @keyword('select a radio option')
    def select_a_radio_option(self, locator):
        radio = self.get_element(locator)
        if not radio.is_checked():
            radio.click()

    @keyword('radio button should be disabled')
    def radio_button_should_be_disabled(self, locator):
        expect(self.get_element(locator)).to_be_disabled()

    @keyword('radio button should be enabled')
    def radio_button_should_be_enabled(self, locator):
        expect(self.get_element(locator)).to_be_enabled()

    @keyword('radio button should be checked')
    def radio_button_should_be_checked(self, locator):
        expect(self.get_element(locator)).to_be_checked()

    @keyword('radio button should not be checked')
    def radio_button_should_not_be_checked(self, locator):
        expect(self.get_element(locator)).not_to_be_checked()

    @keyword('get current radio button checking status')
    def get_current_radio_button_checking_status(self, locator):
        return self.get_element(locator).is_checked()

    @keyword('radio should be correct')
    def radio_should_be_correct(self, locator, state='enabled', status='unchecked'):
        element = self.get_element(locator)
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            expect(element).to_be_disabled()
        if status == 'unchecked':
            expect(element).not_to_be_checked()
        elif status == 'checked':
            expect(element).to_be_checked()
