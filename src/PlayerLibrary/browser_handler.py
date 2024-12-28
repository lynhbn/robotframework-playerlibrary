from .config import *
from .base_context import BaseContext
from .utils import Robot
from robotlibcore import keyword

class BrowserHandler(BaseContext):

    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword('start blank browser')
    def start_blank_browser(self, browser="chromium", headless=False):
        self.setup_custom_locators()
        self.browser = self.player.__getattribute__(browser)
        self.context = self.browser.launch(headless=headless).new_context()
        self.page = self.context.new_page()

    @keyword('start browser with url')
    def start_browser_with_url(self, url, browser="chromium", headless=False):
        self.setup_custom_locators()
        self.browser = self.player.__getattribute__(browser)
        self.context = self.browser.launch(headless=headless).new_context()
        self.page = self.context.new_page()
        self.page.goto(url, timeout=BIG_TIMEOUT)


    @keyword('start new browser session')
    def start_new_browser_session(self, headless=False):
        if TRACING:
            self.context.tracing.stop(path="trace.zip")
        new_context = self.browser.launch(headless=headless).new_context()
        self.context.close()
        self.context = new_context
        self.page = self.context.new_page()
        self.page.reload()

    @keyword('quit all browsers')
    def quit_all_browsers(self):
        self.context.close()
        self.player.stop()
        BaseContext.playwright_context_manager = None




