from QAP_final.pages.base_page import BasePage
from QAP_final.pages.locators import AuthLocators

class AuthPage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.phone = driver.find_element(*AuthLocators.AUTH_PHONE)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.reg = driver.find_element(*AuthLocators.REG_LINK)
        self.phone_tab_element = driver.find_element(*AuthLocators.PHONE_TAB_ELEMENT)
        self.mail_tab_element = driver.find_element(*AuthLocators.MAIL_TAB_ELEMENT)
        self.login_tab_element = driver.find_element(*AuthLocators.LOGIN_TAB_ELEMENT)
        self.ls_tab_element = driver.find_element(*AuthLocators.LS_TAB_ELEMENT)
        self.logo_element = driver.find_element(*AuthLocators.LOGO_ELEMENT)
        self.info_element = driver.find_element(*AuthLocators.INFO_ELEMENT)
        self.forgot_password_element = driver.find_element(*AuthLocators.FORGOT_PASSW)
        self.vk_btn = driver.find_element(*AuthLocators.VK_BTN)
        self.mail_btn = driver.find_element(*AuthLocators.MAIL_BTN)
        self.odn_btn = driver.find_element(*AuthLocators.ODN_BTN)
        self.ya_btn = driver.find_element(*AuthLocators.YA_BTN)

    def get_phone_element(self):
        return self.phone_tab_element
    def get_mail_element(self):
        return self.mail_tab_element
    def get_login_element(self):
        return self.login_tab_element
    def get_ls_element(self):
        return self.ls_tab_element
    def get_login_field(self):
        return self.phone
    def get_passw_field(self):
        return self.password
    def get_logo_element(self):
        return self.logo_element
    def get_info_element(self):
        return self.info_element
    def get_forgot_passw_element(self):
        return self.forgot_password_element
    def get_btn_element(self):
        return self.btn
    def get_error_massage(self):
        return self.driver.find_element(*AuthLocators.ERROR_AUTH).text

    def enter_phone(self, value):
        self.phone.send_keys(value)
    def enter_email(self, value):
        self.email.send_keys(value)
    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
    def reg_click(self):
        self.reg.click()
    def phone_element_click(self):
        self.phone_tab_element.click()

    def get_address_element(self):
        return self.driver.find_element(*AuthLocators.REG_ADDRESS)
    def get_first_element(self):
        return self.driver.find_element(*AuthLocators.REG_FIRSTNAME)
    def get_lastname(self):
        return self.driver.find_element(*AuthLocators.REG_LASTNAME)
    def get_region(self):
        return self.driver.find_element(*AuthLocators.REG_REGION)
    def get_passw_element(self):
        return self.driver.find_element(*AuthLocators.AUTH_PASS)
    def get_passw_confirm_element(self):
        return self.driver.find_element(*AuthLocators.REG_PASSW_CONFIRM)
    def get_link_confidental_element(self):
        return self.driver.find_element(*AuthLocators.REG_LINK_CONFIDENTAL)
    def get_reg_logo_element(self):
        return self.driver.find_element(*AuthLocators.REG_LOGO)
    def get_confirm_element(self):
        return self.driver.find_element(*AuthLocators.CONFIRM_EMAIL)

    def get_reg_btn(self):
        return self.driver.find_element(*AuthLocators.REG_BTN)

    def get_reg_name_error(self):
        return self.driver.find_element(*AuthLocators.REG_ERROR_NAME)
    def get_reg_lastname_error(self):
        return self.driver.find_element(*AuthLocators.REG_ERROR_LASTNAME)
    def get_diff_passw_error(self):
        return self.driver.find_element(*AuthLocators.REG_DIFF_PASSW)
    def get_wrong_pass_message(self):
        return self.driver.find_element(*AuthLocators.REG_WRONG_PASSW)

    def get_register_exist_mail(self):
        return self.driver.find_element(*AuthLocators.REG_EXIST_MAIL)

    def get_register_mail(self):
        return self.driver.find_element(*AuthLocators.MAIL_PAGE)

    def get_register_vk(self):
        return self.driver.find_element(*AuthLocators.VK_PAGE)

    def get_register_odn(self):
        return self.driver.find_element(*AuthLocators.ODN_PAGE)

    def get_register_yandex(self):
        return self.driver.find_element(*AuthLocators.YANDEX_PAGE)

class RestorePage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=LuLoWsuA3wg"
        driver.get(url)
        self.phone = driver.find_element(*AuthLocators.AUTH_PHONE)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.phone_tab_element = driver.find_element(*AuthLocators.PHONE_TAB_ELEMENT)
        self.mail_tab_element = driver.find_element(*AuthLocators.MAIL_TAB_ELEMENT)
        self.login_tab_element = driver.find_element(*AuthLocators.LOGIN_TAB_ELEMENT)
        self.ls_tab_element = driver.find_element(*AuthLocators.LS_TAB_ELEMENT)
        self.captcha_element = driver.find_element(*AuthLocators.CAPTCHA_ELEMENT)
        self.reset_btn = driver.find_element(*AuthLocators.RESET_BTN)
        self.reset_back = driver.find_element(*AuthLocators.RESET_BACK)

    def get_phone_element(self):
        return self.phone_tab_element
    def get_mail_element(self):
        return self.mail_tab_element
    def get_login_element(self):
        return self.login_tab_element
    def get_ls_element(self):
        return self.ls_tab_element
    def get_login_field(self):
        return self.phone

    def get_captcha_element(self):
        return self.captcha_element
    def get_reset_btn_element(self):
        return self.reset_btn




