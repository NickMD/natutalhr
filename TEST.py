import unittest

from selenium import webdriver
import time

from before_login_pages.loginpage import LoginPage
from before_login_pages.basepagebeforelogin import BasePageBeforeLogin
from main_logged.quickaddemployeepage import QuickAddEmployeePage
from main_logged.quickstartpage import BasePageLogged


class MyTestCase(unittest.TestCase):


    #########################   Data    ####################################
    email = "mader.nikita@gmail.com"
    password = "1qazxcvbnm"

    ########################################################################

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_01_verify_login(self):
        """
        Verify user can login with valid data
        """
        BasePageBeforeLogin(self.driver).navigateLoginPage()
        LoginPage(self.driver).login_from_login_page(self.email, self.password)

    def test_01_add_new_employee(self):
        """
        """
        result = 1
        BasePageBeforeLogin(self.driver).navigateLoginPage()
        LoginPage(self.driver).login_from_login_page(self.email, self.password)
        QuickAddPage = QuickAddEmployeePage(self.driver)
        QuickAddPage.navigate()
        QuickAddPage.selectEmployeeStatus("Current")
        QuickAddPage.setWorksID("1")
        QuickAddPage.setForeName("Sdgsgs")
        QuickAddPage.setLastName("Nikita")
        QuickAddPage.selectGender("Male")
        QuickAddPage.setSocialSecurity("123456789")
        QuickAddPage.setDOB("11/12/2014")
        QuickAddPage.setStartDate("12/12/2014")
        QuickAddPage.selectJobTitle("TEST1", "TEST1", createNew=True)
        QuickAddPage.selectJobStatus("TEST1", "TEST1", createNew=True)
        QuickAddPage.selectDepartment("TEST1","TEST1", createNew=True)
        QuickAddPage.selectManager("No managers exist")
        QuickAddPage.setWorkEmail("rob@gmail.com")
        QuickAddPage.setHolidaysPerYear("5","Days")















if __name__ == '__main__':
    unittest.main()
