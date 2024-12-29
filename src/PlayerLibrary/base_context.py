from playwright.sync_api import sync_playwright, Locator
from robotlibcore import keyword
from .custom_locator import *


class BaseContext:

    playwright = sync_playwright().start()

    def __init__(self, ctx):
        self.ctx = ctx
        self.ctx.player = BaseContext.playwright
        self.ctx.browser = None
        self.ctx.context = None
        self.ctx.page = None
        self.ctx.iframe = None
        self.ctx.api = None

    @property
    def player(self):
        return self.ctx.player

    @player.setter
    def player(self, value):
        self.ctx.player = value

    @property
    def browser(self):
        return self.ctx.browser

    @browser.setter
    def browser(self, value):
        self.ctx.browser = value

    @property
    def context(self):
        return self.ctx.context

    @context.setter
    def context(self, value):
        self.ctx.context = value

    @property
    def page(self):
        return self.ctx.page

    @page.setter
    def page(self, value):
        self.ctx.page = value

    @property
    def iframe(self):
        return self.ctx.iframe

    @iframe.setter
    def iframe(self, value):
        self.ctx.iframe = value

    @property
    def api(self):
        return self.ctx.api

    @api.setter
    def api(self, value):
        self.ctx.api = value

    @keyword("register custom locator")
    def register_custom_locator(self, strategy_name, xpath_mask):
        """
        Register a new locator strategy such as item:Login or btn:Save
        :param strategy_name: The custom strategy name
        :param xpath_mask: The xpath that point to a Locator
        Should contain a placeholder to store the value of the locator strategy
        E.g  xpath_mask = '//a[text()="${label}"]/following-sibling::*[1]'
        The "${label}" placeholder should be declared in the xpath_mask without modifying the name of it
        :return:
        """

        CUSTOM_QUERY.replace("xpath_mask", xpath_mask)
        self.player.selectors.register(strategy_name, CUSTOM_QUERY)

    def setup_custom_locators(self):
        self.player.selectors.register('link', QUERY_BY_LINK)
        for prefix in ATTR_PREFIXES:
            self.player.selectors.register(prefix, get_the_query_by_attribute(prefix))

    @keyword("get element")
    def get_element(self, locator, get_all=False):
        index = 1
        if isinstance(locator, Locator):
            return locator
        locator, index = standardize_locator(locator)
        print(f"Formatted locator is `{locator}`")
        print(f"Index of locator is `{index}`")
        return self.page.locator(locator).nth(index-1) if not get_all else self.page.locator(locator).all()

    @keyword("get iframe element")
    def get_iframe_element(self, locator, get_all=False):
        index = 1
        if isinstance(locator, Locator):
            return locator
        locator, index = standardize_locator(locator)
        print(f"Formatted locator is `{locator}`")
        print(f"Index of locator is `{index}`")
        return self.iframe.locator(locator).nth(index-1) if not get_all else self.iframe.locator(locator).all()