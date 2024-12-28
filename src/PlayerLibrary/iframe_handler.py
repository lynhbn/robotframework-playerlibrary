from playwright.sync_api import expect
from robotlibcore import keyword
from .base_context import BaseContext
from .config import *


class IframeHandler(BaseContext):

    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword('select iframe')
    def select_iframe(self, locator):
        iframe = self.get_element(locator)
        self.iframe = self.page.frame_locator(iframe)

    @keyword('unselect iframe')
    def unselect_iframe(self):
        self.iframe = None

    @keyword('iframe should contain')
    def iframe_should_contain(self, *texts, timeout=TIMEOUT):
        for text in texts:
            element = self.iframe.locator(f'.//body//*[not(self::script)][contains(text(),"{text}")]')
            expect(element).to_be_visible(timeout=timeout)

    @keyword('iframe should not contain')
    def iframe_should_not_contain(self, *texts, timeout=TIMEOUT):
        for text in texts:
            element = self.iframe.locator(f'.//body//*[not(self::script)][contains(text(),"{text}")]')
            expect(element).to_be_hidden(timeout=timeout)

    @keyword('input on iframe')
    def input_on_iframe(self, locator, text):
        self.get_iframe_element(locator).fill(text)

    @keyword('click on iframe')
    def click_on_iframe(self, locator):
        self.get_iframe_element(locator).click()

    @keyword('tick on iframe')
    def tick_on_iframe(self, locator):
        self.get_iframe_element(locator).check()

    @keyword('untick on iframe')
    def untick_on_iframe(self, locator):
        self.get_iframe_element(locator).uncheck()

    @keyword('select value on iframe')
    def select_value_on_iframe(self, locator, value):
        self.get_iframe_element(locator).select_option(label=value)

    @keyword('iframe should have element')
    def iframe_should_have_element(self, locator):
        expect(self.get_iframe_element(locator)).to_be_visible()
