from playwright.sync_api import expect
from robotlibcore import keyword
from .base_context import BaseContext



class TableHandler(BaseContext):

    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword('Table column should have')
    def table_column_should_have(self, locator, *items):
        """
        Check for table header contains some labels or not
        :param locator: element locator
        :param items: list of strings
        :return:
        """
        element = self.get_element(locator)
        for item in items:
            expect(element.locator(f'//th[contains(.,"{item}")]')).to_be_visible()

    @keyword('Table row should have')
    def table_row_should_have(self, locator, row_index, *items):
        """
        Check for table row contains some labels or not
        :param row_index: index of row starting from 1
        :param locator: element locator
        :param items: list of strings
        :return:
        """
        element = self.get_element(locator)
        for item in items:
            expect(element.locator(f'//tr[{row_index}][contains(.,"{item}")]')).to_be_visible()


    @keyword('Table cell value should be')
    def table_cell_value_should_be(self, locator, row_key, column_name, expected_cell_value):
        """
        Check for specific cell in a table that has expected value
        :param row_key: a specific value in a row that can be identified with others
        :param column_name: name of the column that has the expected cell
        :param expected_cell_value: the expected cell's value
        :return:
        """
        element = self.get_element(locator)
        col_title_pos = element.locator(f'//th[text()="{column_name}"]/preceding-sibling::*').count() + 1
        expect(element.locator(f'//tr[.//*[text()="{row_key}"]][.//td[position()={col_title_pos} '
                                 f'and text()="{expected_cell_value}"]]')).to_be_visible()
