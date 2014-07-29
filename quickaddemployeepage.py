import time
from common import Common
from main_logged.basepagelogged import BasePageLogged
from main_logged import quickaddemployeepagelocators


class QuickAddEmployeePage(BasePageLogged):

    url = "https://www.naturalhr.com/hr/employee/employee-quick-add"

    #########################   Locators    ####################################
    Employment_status_field = "//select[@name='status']"
    Works_ID_field = "//input[@name='works_id']"
    Lastname_field = "//input[@name='sur_name']"
    Forename_field = "//input[@name='first_name']"
    Gender_selector = "//select[@name='gender']"
    Social_Security_field = "//input[@name='national_insurance']"

    # With calendar:
    Date_of_Birth_field = "//input[@name='dob']"
    Start_date_field = "//input[@name='start_date']"
    # #

    # Add before may require:
    Job_title_selector = "//select[@name='job_title']"
    New_job_title_field = "//*[@id='title_name']"
    New_job_status_field = "//*[@id='status_name']"
    managerLevel_field = "//*[@id='manager']"
    Job_status_selector = "//select[@name='job_status']"
    Department_selector = "//select[@name='department']"
    New_department_field = "//*[@id='dept_name']"
    Manager_selector = "//select[@name='manager']"
    Work_email_address_field = "//input[@name='work_email']"

    Holidays_per_year_field = "//input[@name='holidays_per_year']"
    Holidays_per_year_selector = "//select[@name='meter']"
    # #

    # Refresh buttons:
    refresh_job_title_button = "//*[@class='refresh-title']/input[@class='refresh16']"
    refresh_job_status_button = "//*[@class='refresh-status']/input[@class='refresh16']"
    refresh_department_button = "//*[@class='refresh-dept']/input[@class='refresh16']"
    # #

    # Add buttons:
    Add_Job_title_button = "//*[@id='mws-form-dialog-title-btn']"
    Add_Job_job_status_button = "//*[@id='mws-form-dialog-status-btn']"
    Add_Department_button = "//*[@id='mws-form-dialog-dept-btn']"
    Submit_new_title_button = "html/body/div[6]/div[11]/div/button[1]"
    Submit_new_status_button = "/html/body/div[7]/div[11]/div/button[1]"
    Submit_new_department_button = "/html/body/div[5]/div[11]/div/button[1]"

    Add_Job_title_sumbit_button = "//div[@class='ui-dialog-buttonset']/button[1]"
    # #

    # Other:
    yes = "Yes"
    no = "No"
    submit_page_button = "//button[@type='submit']"
    cancel_page_button = "//div/a[@href='/hr/employee']"
    # #


    ########################################################################

    def selectEmployeeStatus(self, status, reservedValue=None):
        Common(self.driver).select_from_dropdown("xpath", self.Employment_status_field, status, reservedValue)

    def setWorksID(self,ID):
        Common(self.driver).fill_field("xpath", self.Works_ID_field, ID)

    def setLastName(self,lastname):
        Common(self.driver).fill_field("xpath", self.Lastname_field, lastname)

    def setForeName(self, firstname):
        Common(self.driver).fill_field("xpath", self.Forename_field, firstname)

    def selectGender(self, gender, reservedValue=None):
        Common(self.driver).select_from_dropdown("xpath", self.Gender_selector, gender, reservedValue)

    def setSocialSecurity(self, socialSecurity):
        Common(self.driver).fill_field("xpath", self.Social_Security_field, socialSecurity)

    def setDOB(self, DOB):
        Common(self.driver).fill_field("xpath", self.Date_of_Birth_field, DOB)

    def setStartDate(self, startdate):
        Common(self.driver).fill_field("xpath", self.Start_date_field, startdate)

    def selectJobTitle(self, jobtitle, ifnewjobtitle, createNew=False, managerLevel=False):
        if not Common(self.driver).select_from_dropdown("xpath", self.Job_title_selector, jobtitle):
            if createNew:
                self.driver.find_element_by_xpath(self.Add_Job_title_button).click()
                time.sleep(1)  # TODO: Replace sleep with wait for element displayed
                Common(self.driver).fill_field("xpath", self.New_job_title_field, ifnewjobtitle)
                if managerLevel==True:
                    Common(self.driver).select_from_dropdown("xpath", self.managerLevel_field, self.yes)
                elif managerLevel==False:
                    Common(self.driver).select_from_dropdown("xpath", self.managerLevel_field, self.no)
                # Click submit button:
                self.driver.find_element_by_xpath(self.Submit_new_title_button).click()
                # refresh result do get fresh added:
                self.driver.find_element_by_xpath(self.refresh_job_title_button).click()
                time.sleep(1)
                Common(self.driver).select_from_dropdown("xpath", self.Job_title_selector, jobtitle)
            else:
                print("Job title ", jobtitle + "not found. And create new new parameter is ", createNew)
                return False

    def selectJobStatus(self, jobstatus, newjobstatus, createNew=False):
        if not Common(self.driver).select_from_dropdown("xpath", self.Job_status_selector, jobstatus):
            if createNew:
                self.driver.find_element_by_xpath(self.Add_Job_job_status_button).click()
                time.sleep(1)  # TODO: Replace sleep with wait for element displayed
                Common(self.driver).fill_field("xpath", self.New_job_status_field, newjobstatus)
                # Click submit button:
                self.driver.find_element_by_xpath(self.Submit_new_status_button).click()
                # refresh result do get fresh added:
                self.driver.find_element_by_xpath(self.refresh_job_status_button).click()
                time.sleep(1)
                Common(self.driver).select_from_dropdown("xpath", self.Job_status_selector, jobstatus)
            else:
                print("Job status ", jobstatus + " not found. And create new new parameter is ", createNew)
                return False

    def selectDepartment(self, department, newdepartment, createNew=False):
        if not Common(self.driver).select_from_dropdown("xpath", self.Department_selector, department):
            if createNew:
                self.driver.find_element_by_xpath(self.Add_Department_button).click()
                time.sleep(1)  # TODO: Replace sleep with wait for element displayed
                Common(self.driver).fill_field("xpath", self.New_department_field, newdepartment)
                # Click submit button:
                self.driver.find_element_by_xpath(self.Submit_new_department_button).click()
                # refresh result do get fresh added:
                self.driver.find_element_by_xpath(self.refresh_department_button).click()
                time.sleep(1)
                Common(self.driver).select_from_dropdown("xpath", self.Department_selector, department)
            else:
                print("Department ", department + " not found. And create new new parameter is ", createNew)
                return False

    def selectManager(self, manager, reservedValue=None):
        """
        Select manager from dropdownlist. If not found select reserved by index
        :param manager: Manager name
        :param reservedValue: Index from drop down to select
        """
        Common(self.driver).select_from_dropdown("xpath", self.Manager_selector, manager, reservedValue)

    def setWorkEmail(self, email):
        Common(self.driver).fill_field("xpath", self.Work_email_address_field, email)

    def setHolidaysPerYear(self, amount, dayormonth):
        Common(self.driver).fill_field("xpath", self.Holidays_per_year_field, amount)
        Common(self.driver).select_from_dropdown("xpath",self.Holidays_per_year_selector, dayormonth)

    def submitQuickAddemployee(self):
        Common(self.driver).press_button("xpath", self.submit_page_button)
