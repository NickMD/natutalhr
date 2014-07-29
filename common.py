from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium import webdriver

class Common(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def fill_field(self, locatortype, locator, value):
        """
        Simply fill the filed
        """
        if locatortype == "css":
            elem = self.driver.find_element_by_css_selector(locator)
            elem.clear()
            elem.send_keys(value)
        elif locatortype == "xpath":
            elem = self.driver.find_element_by_xpath(locator)
            elem.clear()
            elem.send_keys(value)
        elif locatortype == "id":
            elem = self.driver.find_element_by_id(locator)
            elem.clear()
            elem.send_keys(value)

    def press_button(self, locatortype, locator):
        if locatortype == "css":
            elem = self.driver.find_element_by_css_selector(locator)
            elem.click()
        elif locatortype == "xpath":
            elem = self.driver.find_element_by_xpath(locator)
            elem.click()
        elif locatortype == "id":
            elem = self.driver.find_element_by_id(locator)
            elem.click()

    def wait_for_element(self, locatortype, locator, time="30"):
        wait = WebDriverWait(self.driver, time)
        if locatortype == "xpath":
            wait.until(lambda driver: self.driver.find_element_by_xpath("locator"))

    def select_from_dropdown(self, locatortype, locator, value, reserve=None):
        # TODO: Id,CSS... locators
        if locatortype == "xpath":
            select = self.driver.find_element_by_xpath(locator)  #get the select element
            options = select.find_elements_by_tag_name("option") #get all the options into a list
            optionList = []
            # if reserve in None:
            for option in options:
                optionList.append(option.get_attribute("value"))
                optionList.append(option.text)
            for optionValue in optionList:
                if optionValue == value:
                    try:
                        select = Select(self.driver.find_element_by_xpath(locator))
                        select.select_by_value(value)
                        break
                    except NoSuchElementException:
                        self.driver.find_element_by_xpath(locator + "/option[contains(text(),'{0}')]".format(value)).click()
                        break
            else:
                # print("VALUE BROKEN! Select from reserve option number %s" % (reserve))
                if reserve is not None:
                    select = Select(self.driver.find_element_by_xpath(locator))
                    select.select_by_index(reserve)
                else:
                    return False
