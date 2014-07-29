from common import Common
from before_login_pages.homepage import HomePage


class LoginPage(HomePage):

    url = "https://www.naturalhr.com/login/"

    #########################   Locators    ################################
    emailfrompage = "//form[@id='sign-in-form']/input[1]"
    passwordfrompage = "//form[@id='sign-in-form']/input[2]"
    submitfrompage = "//form[@id='sign-in-form']/input[3]"
    ########################################################################

    def submit(self):
        self.driver.find_element_by_class("continue button large green").click()
        return OnboardingInvitePage(self.driver)

    def login_from_login_page(self, email, password):
        self.fill_field("xpath", self.emailfrompage, email)
        self.fill_field("xpath", self.passwordfrompage, password)
        self.press_button("xpath", self.submitfrompage)
        assert "Home" in self.driver.title
#         TODO: Should return smth???

