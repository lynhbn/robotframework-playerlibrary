from datetime import datetime
from playwright.sync_api import expect
from robotlibcore import keyword

from .base_context import BaseContext
from .config import *
from .utils import Robot



class DatePickerHandler(BaseContext):



    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword('input datetime')
    def input_datetime(self, locator, value):
        element = self.get_element(locator)
        element.evaluate("node => node.removeAttribute('readonly')")
        element.fill(value, force=True)
        self.get_element("xpath=//body").click()
        Robot().sleep(1)
        return value

    @keyword('datepicker should be correct')
    def datepicker_should_be_correct(self, locator, state='enabled', default=None):
        element = self.get_element(locator)
        # Verify state
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            expect(element).to_be_disabled()
        # Verify default value
        if default is not None:
            expect(element).to_have_value(default)

    @keyword('actual date should be')
    def actual_date_should_be(self, locator, expected_date, input_format=BASIC_DATE_FORMAT,
                              displayed_format=ALTERNATIVE_DATE_FORMAT, timeout=SMALL_TIMEOUT):
        actual_date = None
        for sec in range(int(timeout/1000)):
            actual_date = self.get_element(locator).input_value()
            if datetime.strptime(expected_date, input_format) == datetime.strptime(actual_date, displayed_format):
                break
            Robot().sleep(1)
        if datetime.strptime(expected_date, input_format) != datetime.strptime(actual_date, displayed_format):
            raise AssertionError(f"Actual date: '{actual_date}' is different with expected date: '{expected_date}'")

    @keyword('actual date should not be')
    def actual_date_should_not_be(self, locator, expected_date, input_format=BASIC_DATE_FORMAT,
                                  displayed_format=ALTERNATIVE_DATE_FORMAT, timeout=SMALL_TIMEOUT):
        actual_date = None
        for sec in range(int(timeout/1000)):
            actual_date = self.get_element(locator).input_value()
            if datetime.strptime(expected_date, input_format) != datetime.strptime(actual_date, displayed_format):
                break
            Robot().sleep(1)
        if datetime.strptime(expected_date, input_format) == datetime.strptime(actual_date, displayed_format):
            raise AssertionError(f"Actual date: '{actual_date}' is similar with expected text: '{expected_date}'")
