from selenium.webdriver.common.by import By

BASE_URL = "https://demoqa.com"


class FormPage:
    PATH = "/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    GENDER = {
        "male": (By.CSS_SELECTOR, "label[for='gender-radio-1']"),
        "female": (By.CSS_SELECTOR, "label[for='gender-radio-2']"),
        "other": (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    }
    SUBMIT = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL + self.PATH)
        self.remove_banners()

    def remove_banners(self):
        self.driver.execute_script("""
            const fixedban = document.getElementById('fixedban');
            if (fixedban) { fixedban.remove(); }
            const footer = document.getElementById('footer');
            if (footer) { footer.remove(); }
        """)

    def fill_first_name(self, value):
        self.driver.find_element(*self.FIRST_NAME).send_keys(value)

    def fill_last_name(self, value):
        self.driver.find_element(*self.LAST_NAME).send_keys(value)

    def fill_email(self, value):
        self.driver.find_element(*self.EMAIL).send_keys(value)

    def select_gender(self, gender: str):
        self.driver.find_element(*self.GENDER[gender]).click()

    def fill_mobile(self, value):
        self.driver.find_element(*self.MOBILE).send_keys(value)

    def submit(self):
        self.remove_banners()
        button = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()