class Const:
    SHADOW = "shadow"
    LOCATOR = "locator"


class MainMenu:
    """
    Mapping between main menu items and appropriate web element locator components
    to make selecting menu elements more friendly.
    """
    OUR_MODELS = "1"
    BUY_ONLINE = "2"
    OFFERS_FINANCE = "3"
    OWNERS_AREA = "4"
    OUR_BRAND = "5"


class ModelsMenu:
    SALOONS = "1"
    SUV = "2"
    ESTATES = "3"
    HATCHBACKS = "4"
    COUPES = "5"
    CABRIOLETS = "6"
    MVP = "7"
    MARCO = "8"
    POLO = "9"


class HatchMenu:
    A_CLASS = "1"
    B_CLASS = "2"


class ShadowRoot:
    MENU = "owc-header"
    SUB_MENU = "vmos-flyout"
    COOKIE_BANNER = "cmm-cookie-banner.hydrated"
    MODEL_PAGE = "div > owc-stage"
    CONFIGURATOR = "owcc-car-configurator"


class FuelType:
    DIESEL = "1"
    PREMIUM = "2"
    SUPER = "3"


class Dir:
    ARTEFACTS = "artefacts"


class Menu:
    MAIN = "main"
    POPUP = "popup"
    SUB_MODEL = "sub_model"


class SupportedBrowser:
    CHROME = "chrome"
    FIREFOX = "firefox"
