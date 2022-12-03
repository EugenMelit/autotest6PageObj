from selenium.webdriver.common.by import By


class WidgetAccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.XPATH, '//*[@id="section1Content"]/p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_SECOND_CONTENT = (By.XPATH, '//*[@id="section2Content"]/p[1]')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THIRD_CONTENT = (By.XPATH, '//*[@id="section3Content"]/p')

class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_VALUE =(By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')

class DataPickerPageLocators:
    DATA_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATA_MONTH =(By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATA_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATA_DAY_LIST=(By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')




class ProgresBarPageLocators:
    PROGRES_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRES_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')

class TabsPageLocators:

    TAB_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TAB_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TAB_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TAB_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TAB_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')

class ToolTipsPageLocators:

    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON_HOVER = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    INPUT_FIELD = (By.CSS_SELECTOR, 'div[id="texFieldToolTopContainer"] input[id="toolTipTextField"]')
    FIELD_LINK_HOVER = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')


    CONTRARY_LINK = (By.XPATH, '//*[@id="texToolTopContainer"]/a[1]')
    CONTRARY_LINK_HOVER = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[@id="texToolTopContainer"]/a[2]')
    SECTION_LINK_HOVER =(By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    pass





