"""Поизитивные и негативные тесты логирования"""

import allure
import time
from pages.login import Login


@allure.feature("Смоук тест логирования")
@allure.story("Проверка входа в профиль")
@allure.severity("BLOCKER")
def test_login(web_browser):
    """ Вход и авторизация на сайте с заполнением корректных данных. """

    page = Login(web_browser)

    with allure.step("Нажатие кнопки входа"):
        page.home_login_button.click()

    with allure.step("Ввод почты"):
        page.input_log_email.send_keys("golovnina.margarita@yandex.ru")

    with allure.step("Ввод пароля"):
        page.input_pass.send_keys("9980553")

    with allure.step("Показ пароля"):
        page.show_pass_btn.click()

    with allure.step("Вход в кабинет"):
        page.form_sign_in_btn.click()
        time.sleep(2)

    with allure.step("Результаты входа в профиль"):
        assert (
            page.name_user.get_text() == "golovnina.margarita@yandex.ru"
        ), f"Вход в профиль {page.name_user.get_text()} не произошел"


@allure.feature("Смоук тест логирования")
@allure.story("Проверка входа в профиль")
@allure.severity("BLOCKER")
def test_login_invalid_mail(web_browser):
    """ Вход и авторизация на сайте c некорректной почтой. """

    page = Login(web_browser)

    with allure.step("Нажатие кнопки входа"):
        page.home_login_button.click()

    with allure.step("Ввод почты"):
        page.input_log_email.send_keys("margarit")

    with allure.step("Ввод пароля"):
        page.input_pass.send_keys("9980553")

    with allure.step("Показ пароля"):
        page.show_pass_btn.click()

    with allure.step("Вход в кабинет"):
        page.form_sign_in_btn.click()
        time.sleep(2)

    with allure.step("Результаты входа в профиль c некорректной почтой"):
        assert (
            page.error_email == page.error_email
        ), "Произошел вход с некорректной почтой"


@allure.feature("Смоук тест логирования")
@allure.story("Проверка входа в профиль")
@allure.severity("BLOCKER")
def test_login_invalid_pass(web_browser):
    """ Вход и авторизация на сайте c неверным паролем. """

    page = Login(web_browser)

    with allure.step("Нажатие кнопки входа"):
        page.home_login_button.click()

    with allure.step("Ввод почты"):
        page.input_log_email.send_keys("golovnina.margarita@yandex.ru")

    with allure.step("Ввод пароля"):
        page.input_pass.send_keys("998")

    with allure.step("Показ пароля"):
        page.show_pass_btn.click()

    with allure.step("Вход в кабинет"):
        page.form_sign_in_btn.click()
        time.sleep(2)

    with allure.step("Результаты входа в профиль с неверным паролем"):
        assert page.error_pass == page.error_pass, "Произошел вход с неверным паролем"
