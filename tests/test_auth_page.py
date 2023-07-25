import pytest
import time
from QAP_final.pages.auth_page import AuthPage, RestorePage
from QAP_final.settings import *

#1 Форма "Авторизация"
def test_auth_page_elements(selenium):
    page = AuthPage(selenium)
    assert page.get_phone_element().is_displayed() == True
    assert page.get_mail_element().is_displayed() == True
    assert page.get_login_element().is_displayed() == True
    assert page.get_ls_element().is_displayed() == True
    assert page.get_login_field().is_displayed() == True
    assert page.get_passw_field().is_displayed() == True
    assert page.get_forgot_passw_element().is_displayed() == True
    assert page.get_btn_element().is_displayed() == True
    assert page.get_logo_element().is_displayed() == True
    assert page.get_info_element().is_displayed() == True

#2 Позитивная авторизация
def test_positive_auth(selenium):
    page = AuthPage(selenium)
    page.enter_email(valid_mail)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(5)
    assert page.get_relative_link() == '/account_b2c/page'

#3 Негативная авторизация с неверным mail
def test_negative_auth_wrong_mail(selenium):
    page = AuthPage(selenium)
    page.enter_email(invalid_mail)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(1)
    assert page.get_error_massage() == "Неверный логин или пароль"

#4 Негативная авторизация с неверным паролем
def test_negative_auth_wrong_passw(selenium):
    page = AuthPage(selenium)
    page.enter_email(valid_mail)
    page.enter_pass(invalid_password)
    page.btn_click()
    time.sleep(1)
    assert page.get_error_massage() == "Неверный логин или пароль"


#5 По умолчанию стоит форма авторизации по телефону
def test_active_elements(selenium):
   page  = AuthPage(selenium)
   assert page.get_phone_element().get_attribute("class") == "rt-tab rt-tab--small rt-tab--active"
   assert page.get_phone_element().text == 'Телефон'
   assert page.get_mail_element().get_attribute("class") != "rt-tab rt-tab--small rt-tab--active"

#6 Смена таблицы выбора авторизации
def test_check_change_active_element(selenium):
    page = AuthPage(selenium)
    page.enter_email(valid_mail)
    page.enter_pass(valid_password)
    assert page.get_login_element().get_attribute("class") or page.get_phone_element().get_attribute("class") or page.get_mail_element().get_attribute("class") == "rt-tab " \
                                                                                                             "rt-tab--small rt-tab--active"
#7 Форма "Восстановление пароля"
def test_recovery_page_elements(selenium):
    page = RestorePage(selenium)
    assert page.get_phone_element().is_displayed() == True
    assert page.get_mail_element().is_displayed() == True
    assert page.get_login_element().is_displayed() == True
    assert page.get_ls_element().is_displayed() == True
    assert page.get_login_field().is_displayed() == True
    assert page.get_captcha_element().get_attribute("alt") == 'Captcha'
    assert page.get_captcha_element().is_displayed() == True
    assert page.get_reset_btn_element().is_displayed() == True
    assert page.reset_back.is_displayed() == True

#8 Форма "Регистрация"
def test_registration_page_elements(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    assert page.get_first_element().is_displayed() == True
    assert page.get_lastname().is_displayed() == True
    assert page.get_address_element().is_displayed() == True
    assert page.get_region().is_displayed() == True
    assert page.get_passw_element().is_displayed() == True
    assert page.get_passw_confirm_element().is_displayed() == True
    assert page.get_link_confidental_element().is_displayed() == True
    assert page.get_reg_logo_element().is_displayed() == True
    assert page.get_reg_btn().is_displayed() == True

#9 Позитивная регистрация
def test_positive_registration(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(name)
    page.get_lastname().send_keys(last_name)
    page.get_address_element().send_keys(new_mail)
    page.get_passw_element().send_keys(new_pass)
    page.get_passw_confirm_element().send_keys(new_pass)
    page.get_reg_btn().click()
    time.sleep(5)
    assert page.get_confirm_element().text == "Подтверждение email"

#10 Негативная регестрация - неверное имя
@pytest.mark.parametrize('x', ["NNN", "а"])
def test_negative_field_name(selenium, x):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(x)
    page.get_lastname().send_keys(last_name)
    page.get_address_element().send_keys(new_mail)
    page.get_passw_element().send_keys(new_pass)
    page.get_passw_confirm_element().send_keys(new_pass)
    page.get_reg_btn().click()
    time.sleep(5)
    assert page.get_reg_name_error().text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#11 Негативная регестрация - неверная фамилия
@pytest.mark.parametrize('x', ["NNN", "а"])
def test_negative_field_lastname(selenium, x):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(name)
    page.get_lastname().send_keys(x)
    page.get_address_element().send_keys(new_mail)
    page.get_passw_element().send_keys(new_pass)
    page.get_passw_confirm_element().send_keys(new_pass)
    page.get_reg_btn().click()
    time.sleep(5)
    assert page.get_reg_lastname_error().text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#12 Негативная регестрация - разные пароли
def test_diff_passw_registration(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(name)
    page.get_lastname().send_keys(last_name)
    page.get_address_element().send_keys(new_mail)
    page.get_passw_element().send_keys(new_pass)
    page.get_passw_confirm_element().send_keys("12gE@drh4")
    page.get_reg_btn().click()
    assert page.get_diff_passw_error().text == "Пароли не совпадают"

#13 Негативная регестрация - неверный пароль
@pytest.mark.parametrize('x', ["1234jdjdjfghkdffkkdfgjkdfsjfsf", "123", "ффj"])
def test_wrong_passw_registration(selenium, x):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys("Иван")
    page.get_lastname().send_keys("ааф")
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Super")
    page.get_passw_confirm_element().send_keys("Super")
    page.get_reg_btn().click()
    assert page.get_wrong_pass_message().text == "Длина пароля должна быть не менее 8 символов"

#14 Негативная регестрация - уже зарегистрированная почта
def test_register_exist_mail(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(name)
    page.get_lastname().send_keys(last_name)
    page.get_address_element().send_keys(valid_mail)
    page.get_passw_element().send_keys(new_pass)
    page.get_passw_confirm_element().send_keys(new_pass)
    page.get_reg_btn().click()
    time.sleep(5)
    assert page.get_register_exist_mail().text == "Учётная запись уже существует"

#15 Регестрация через VK.
def test_register_vk(selenium):
    page = AuthPage(selenium)
    page.vk_btn.click()
    time.sleep(5)
    assert page.get_base_url() == 'id.vk.com'

#16 Регестрация через MAIL.
def test_register_mail(selenium):
    page = AuthPage(selenium)
    page.mail_btn.click()
    time.sleep(5)
    assert page.get_base_url() == 'connect.mail.ru'

#17 Регестрация через Одноклассники.
def test_register_odn(selenium):
    page = AuthPage(selenium)
    page.odn_btn.click()
    time.sleep(5)
    assert page.get_base_url() == 'connect.ok.ru'


#18 Регестрация через Yandex.
def test_register_yandex(selenium):
    page = AuthPage(selenium)
    page.ya_btn.click()
    time.sleep(5)
    assert page.get_relative_link() == 'passport.yandex.ru'






