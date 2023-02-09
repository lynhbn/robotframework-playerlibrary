from robotlibcore import DynamicCore
from .api_context import APIContext
from .button_handler import ButtonHandler
from .checkbox_handler import CheckboxHandler
from .datepicker_handler import DatePickerHandler
from .dropdown_handler import DropdownHandler
from .iframe_handler import IframeHandler
from .page_handler import PageHandler
from .popup_handler import PopupHandler
from .table_handler import TableHandler
from .textbox_handler import TextboxHandler
from .ui_context import UIContext
from .misc import Misc


class PlayerLibrary(DynamicCore):

    def __init__(self):
        libraries = [APIContext(), UIContext(), ButtonHandler(), CheckboxHandler(), DatePickerHandler(),
                     DropdownHandler(), IframeHandler(), PageHandler(), PopupHandler(), TableHandler(),
                     TextboxHandler(), Misc()]
        DynamicCore.__init__(self, libraries)
