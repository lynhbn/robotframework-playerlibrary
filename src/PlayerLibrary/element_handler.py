from playwright.sync_api import expect
from .base_context import BaseContext
from .config import *
from .utils import *


class ElementHandler(BaseContext):

    def __init__(self, ctx):
        super().__init__(ctx)


    @keyword("number of element should be")
    def number_of_element_should_be(self, locator, expected_number: int):
        expect(self.get_element(locator)).to_have_count(expected_number)

    @keyword("font size should be")
    def font_size_should_be(self, locator, expected_size):
        """
        Compare the font size from given element to the expected one
        :param locator:
        :param expected_size: Format is `15px` or `17px`
        :return:
        """
        size = self.get_css_property_value(locator, "font-size")
        if size != expected_size:
            raise AssertionError(
                f"Element {locator} has fontsize {size}, is not having expected fontsize {expected_size}")

    @keyword("get css property value")
    def get_css_property_value(self, locator, css_property):
        return self.get_element(locator).evaluate(
            f"e =>  window.getComputedStyle(e).getPropertyValue('{css_property}');")

    @keyword("element should have")
    def element_should_have(self, locator, text):
        expect(self.get_element(locator).get_by_text(text)).to_be_visible()

    @keyword("element should have these texts")
    def element_should_have_these_texts(self, locator, *texts):
        element = self.get_element(locator)
        for text in texts:
            expect(element.get_by_text(text)).to_be_visible()

    @keyword("element should not have")
    def element_should_not_have(self, locator, *texts):
        element = self.get_element(locator)
        for text in texts:
            expect(element.get_by_text(text)).to_be_hidden()

    @keyword("get inner element")
    def get_inner_element(self, locator, inner_locator):
        return self.get_element(locator).locator(f"xpath={inner_locator}")

    @keyword("element color should be")
    def element_color_should_be(self, locator, expected_hex_color, css_properties="color"):
        """
        :param locator: element's locator
        :param css_properties: "color" or "background-color"
        :param expected_hex_color: such as #008040
        :return: raise errors when the color properties are not the same
        """
        raw_color = self.get_css_property_value(locator, css_properties)
        print(raw_color)
        color_tuple = eval(raw_color.replace("rgba", "")) if "rgba" in raw_color else eval(raw_color.replace("rgb", ""))
        hex_color = rgb_to_hex((color_tuple[0], color_tuple[1], color_tuple[2]))
        print(hex_color)
        if hex_color != expected_hex_color:
            raise AssertionError(f"Element {locator} having color is {hex_color}, it is not {expected_hex_color}")

    @keyword("get element color")
    def get_element_color(self, locator, css_properties="color"):
        """
        :param locator: element's locator
        :param css_properties: "color" or "background-color"
        :return: css color of expected element
        """
        raw_color = self.get_css_property_value(locator, css_properties)
        print(raw_color)
        color_tuple = eval(raw_color.replace("rgba", "")) if "rgba" in raw_color else eval(raw_color.replace("rgb", ""))
        hex_color = rgb_to_hex((color_tuple[0], color_tuple[1], color_tuple[2]))
        return hex_color


    @keyword("element value should be trimmed")
    def element_value_should_be_trimmed(self, locator):
        raw_string = '123'
        element = self.get_element(locator)
        element.fill(f' {raw_string} ')
        self.lose_focus(element)
        Robot().should_be_equal_as_strings(raw_string, self.get_actual_text(element))

    @keyword("element value should not be trimmed")
    def element_value_should_not_be_trimmed(self, locator):
        raw_string = '123'
        element = self.get_element(locator)
        element.fill(f' {raw_string} ')
        self.lose_focus(element)
        Robot().should_not_be_equal_as_strings(raw_string, self.get_actual_text(element))

    @keyword("lose focus")
    def lose_focus(self, locator):
        self.get_element(locator).blur()

    @keyword("remove element attribute")
    def remove_element_attribute(self, locator, attribute):
        self.get_element(locator).evaluate(f"node => node.removeAttribute('{attribute}')")

    @keyword("drag and drop")
    def drag_and_drop(self, locator, target):
        self.get_element(locator).drag_to(self.get_element(target))

    @keyword("get attribute")
    def get_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute)

    @keyword("element should not have attribute")
    def element_should_not_have_attribute(self, locator, attribute, value=""):
        element = self.get_element(locator)
        expect(element).not_to_have_attribute(attribute, value)

    @keyword("element attribute should be")
    def element_attribute_should_be(self, locator, attribute, value):
        element = self.get_element(locator)
        expect(element).to_have_attribute(attribute, value)

    @keyword("element attribute should not be")
    def element_attribute_should_not_be(self, locator, attribute, value):
        element = self.get_element(locator)
        expect(element).not_to_have_attribute(attribute, value)

    @keyword('element attribute should contain')
    def element_attribute_should_contain(self, locator, attribute, expected_value):
        assert expected_value in self.get_attribute(locator, attribute)

    @keyword('element attribute should not contain')
    def element_attribute_should_not_contain(self, locator, attribute, expected_value):
        assert expected_value not in [self.get_attribute(locator, attribute), None]

    @keyword("element should be shown")
    def element_should_be_shown(self, locator, timeout=SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_visible(timeout=timeout)

    @keyword("element should not be shown")
    def element_should_not_be_shown(self, locator):
        expect(self.get_element(locator)).to_be_hidden()

    @keyword("hover on")
    def hover_on(self, locator):
        self.get_element(locator).hover()

    @keyword('get actual text')
    def get_actual_text(self, locator):
        element = self.get_element(locator)
        tag = self.get_element_tag(element)
        if tag in ('input', 'textarea', 'select'):
            actual_text = element.input_value()
        else:
            actual_text = element.inner_text()
        return actual_text

    @keyword("get element tag")
    def get_element_tag(self, locator):
        return self.get_element(locator).evaluate("node => node.tagName").lower()

    @keyword('get actual number')
    def get_actual_number(self, locator):
        text = self.get_actual_text(locator).replace(',', '')
        white_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
        number = "".join([char for char in list(text) if char in white_list])
        print(number)
        return number

    @keyword('get inner text')
    def get_inner_text(self, locator):
        return self.get_element(locator).inner_text()

    @keyword('element value should not be empty')
    def element_value_should_not_be_empty(self, locator):
        expect(self.get_element(locator)).not_to_be_empty()

    @keyword('append text')
    def append_text(self, locator, text):
        element = self.get_element(locator)
        original_text = self.get_actual_text(element)
        element.fill(f'{original_text}{text}')

    @keyword('actual text should be')
    def actual_text_should_be(self, locator, expected_value, timeout=SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(actual_text) == str(expected_value):
                break
            Robot().sleep(1)
        if str(actual_text) != str(expected_value):
            raise AssertionError(f"Actual text: '{actual_text}' are different with expected text: '{expected_value}'")

    @keyword('actual text should not be')
    def actual_text_should_not_be(self, locator, expected_value, timeout=SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(actual_text) != str(expected_value):
                break
            Robot().sleep(1)
        if str(actual_text) == str(expected_value):
            raise AssertionError(f"Actual text: '{actual_text}' are similar with expected text: '{expected_value}'")

    @keyword('actual text should contain')
    def actual_text_should_contain(self, locator, expected_value, timeout=SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(expected_value) in str(actual_text):
                break
            Robot().sleep(1)
        if str(expected_value) not in str(actual_text):
            raise AssertionError(f"Actual text: '{actual_text}' does not include the text: '{expected_value}'")

    @keyword('actual text should not contain')
    def actual_text_should_not_contain(self, locator, expected_value, timeout=SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(expected_value) not in str(actual_text):
                break
            Robot().sleep(1)
        if str(expected_value) in str(actual_text):
            raise AssertionError(f"Actual text: '{actual_text}' still includes the text: '{expected_value}'")

    @keyword('actual amount should be')
    def actual_amount_should_be(self, locator, expected_amount, deviation=0.01, timeout=SMALL_TIMEOUT):
        actual_text = self.get_actual_text(locator)
        difference = round(float(expected_amount) - float(actual_text), 4)
        if abs(difference) <= deviation:
            pass
        else:
            raise AssertionError(
                f"Actual amount: '{actual_text}' is different with expected amount: '{expected_amount}'")

    @keyword('actual amount should not be')
    def actual_amount_should_not_be(self, locator, expected_amount, deviation=0.01, timeout=SMALL_TIMEOUT):
        actual_text = self.get_actual_text(locator)
        difference = round(float(expected_amount) - float(actual_text), 4)
        if abs(difference) > deviation:
            pass
        else:
            raise AssertionError(
                f"Actual amount: '{actual_text}' is likely equal to expected amount: '{expected_amount}'")

    @keyword('actual number should be')
    def actual_number_should_be(self, locator, expected_value):
        should_be_equal_as_amounts(expected_value, self.get_actual_number(locator))

    @keyword('actual number should not be')
    def actual_number_should_not_be(self, locator, expected_value):
        should_be_equal_as_amounts(expected_value, self.get_actual_number(locator))

    @keyword('click')
    def click(self, locator, force=False):
        self.get_element(locator).click(force=force)

    @keyword('click and wait')
    def click_and_wait(self, locator, expected_item=None, expected_text=None, timeout=TIMEOUT):
        element = self.get_element(locator)
        element.click()
        if expected_item:
            expect(self.get_element(expected_item)).to_be_visible(timeout=timeout)
        if expected_text:
            expect(self.page.get_by_text(expected_text)).to_be_visible(timeout=timeout)

    @keyword('double click')
    def double_click(self, locator):
        self.get_element(locator).click(click_count=2)

    @keyword('click should open a new tab')
    def click_should_open_a_new_tab(self, locator, url=None, content=None):
        element = self.get_element(locator)
        assert "_blank" == element.get_attribute("target")
        with self.context.expect_page() as new_page_info:
            element.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        self.page = self.context.pages[-1]
        self.page.bring_to_front()
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('click should open a new window')
    def click_should_open_a_new_window(self, locator, url=None, content=None):
        element = self.get_element(locator)
        with self.context.expect_page() as new_page_info:
            element.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        self.page = self.context.pages[-1]
        self.page.bring_to_front()
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('click should open a new popup')
    def click_should_open_a_new_popup(self, locator, url=None, content=None):
        element = self.get_element(locator)
        with self.page.expect_popup() as new_popup_info:
            element.click()
        new_page = new_popup_info.value
        new_page.wait_for_load_state()
        self.page = self.context.pages[-1]
        self.page.bring_to_front()
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('close current page')
    def close_current_page(self):
        self.page.close()

    @keyword('open new window')
    def open_new_window(self):
        new_page = self.context.new_page()
        self.page = new_page

    @keyword("press key")
    def press_keys(self, locator, keys):
        self.get_element(locator).press(keys)