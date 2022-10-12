""" Проверка кода стараниц методами GET POST """

import time
import requests
import allure
from url.url_page import Url


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/77.0.3865.120 Mobile Safari/537.36 ",
}


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на главную страницу")
def test_get_home_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_home, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Разработка и продвижение сайтов")
def test_get_marketplace_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_marketplace, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Сообщить о нарушении")
def test_get_abuse_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_abuse, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу WHOIS")
def test_get_whois_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_whois, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Способы оплаты")
def test_get_payments_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_payments, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Регистрация в БелГИЭ")
def test_get_belgie_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_belgie, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Кейсы")
def test_get_cases_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_cases, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Партнерам")
def test_get_partners_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_partners, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу О компании")
def test_get_clients_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу FAQ")
def test_get_public_clients_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_public_clients, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на главную страницу")
def test_get_help_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_help, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Онлайн трансляции")
def test_get_media_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_media, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу ПО для хостинга")
def test_get_saas_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_saas, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Администрирование")
def test_get_administration_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_administration, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Отказоустойчивый кластер")
def test_get_cluster_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_cluster, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Выделенный сервер")
def test_get_dedicated_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_dedicated, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачный VPS")
def test_get_cloud_server_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_cloud_server, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения")
def test_get_cloud_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_cloud, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Защищенная почта")
def test_get_secure_email_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_secure_email, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Хостинг персональных данных")
def test_get_personalnye_dannye_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_personalnye_dannye, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Защищенный виртуальный хостинг")
def test_get_secure_unix_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_secure_unix, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Лицензии Битрикс24")
def test_get_tarify_bitrix24_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_tarify_bitrix24, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Электронная почта")
def test_get_email_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_email, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу SSL-сертификаты")
def test_get_ssl_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_ssl, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Joomla-хостинг")
def test_get_joomla_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_joomla, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Drupal-хостинг")
def test_get_drupal_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_drupal, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Windows-хостинг")
def test_get_windows_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_windows, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Битрикс-хостинг")
def test_get_bitrix_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_bitrix, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу WordPress-хостинг")
def test_get_wordpress_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_wordpress, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Unix-хостинг")
def test_get_unix_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_unix, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу регистрация доменов")
def test_get_domains_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_domains, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Новости")
def test_get_heder_clients_news_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_news, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Акции")
def test_get_clients_actions_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_actions, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Программа лояльности")
def test_get_clients_loyalty_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_loyalty, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Спонсорство")
def test_get_clients_sponsorship_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_sponsorship, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Рекламное партнерство")
def test_get_clients_partners_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_partners, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Документы")
def test_get_clients_documents_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_documents, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Карьера")
def test_get_clients_career_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_career, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Контакты")
def test_get_clients_contacts_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_contacts, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу ДОГОВОРЫ СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ")
def test_get_clients_documents_personal_data_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_documents_personal_data, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу ДОКУМЕНТЫ Положение о cookie-файлах")
def test_get_clients_documents_cookies_policy_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_documents_cookies_policy, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу ДОКУМЕНТЫ Свидетельства")
def test_get_clients_documents_license_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_documents_license, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу https://hoster.by/service/")
def test_get_service_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу отзывы клиентов")
def test_get_clients_otzyvy_klientov_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_clients_otzyvy_klientov, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story(
    "Вход на страницу Хостинг сайтов Быстрый и надежный виртуальный хостинг сайтов"
)
def test_get_service_hosting_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_hosting, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения 1С:Бухгалтерия в облаке")
def test_get_service_cloud_1c_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_cloud_1c, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения Битрикс24 в облаке")
def test_get_service_cloud_bitrix24_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_cloud_bitrix24, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения Облачный диск")
def test_get_service_cloud_disk_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_cloud_disk, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения Облачный хостинг")
def test_get_service_cloud_hosting_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_cloud_hosting, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Лицензии Панель управления ISPmanager")
def test_get_service_cloud_isp_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_cloud_isp, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения Почта в облаке")
def test_get_service_cloud_mail_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_cloud_mail, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Облачные решения Облачный офис")
def test_get_service_cloud_office_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_cloud_office, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу USB-ключ в облаке")
def test_get_cloud_usb_key_cloud_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_cloud_usb_key_cloud, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Как зарегистрировать домен бесплатно?")
def test_get_domains_poluchit_domen_besplatno_page():
    """ Проверка кода ответа. """

    response = requests.get(
        Url.url_service_domains_poluchit_domen_besplatno, headers=headers, timeout=10
    )
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу УСЛУГИ Защищенный VPS-хостинг")
def test_get_service_hosting_secure_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_hosting_secure, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Услуги Защищенный Битрикс-хостинг")
def test_get_hosting_secure_bitrix_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_hosting_secure_bitrix, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу СПЕЦИАЛИЗИРОВАННЫЙ ХОСТИНГ Защищенный сервер")
def test_get_hosting_secure_server_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_service_hosting_secure_server, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Инфраструктура 3-фл/3-юл")
def test_get_service_solutions_3fl_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_service_solutions_3fl, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Услуги администрирования Администрирование сервера")
def test_get_url_administration_web_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_administration_web, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу УСЛУГИ Резервное копирование (BaaS)")
def test_get_solutions_baas_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_solutions_baas, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Сделайте и запустите сайт уже сегодня")
def test_get_fast_start_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_solutions_fast_start, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Решения в области информационной безопасности")
def test_get_informatsionnaya_bezopasnost_page():
    """ Проверка кода ответа. """

    response = requests.get(
        Url.url_solutions_informatsionnaya_bezopasnost, headers=headers, timeout=10
    )
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Квиз-опрос")
def test_get_informatsionnaya_bezopasnost_quiz_php_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(
        Url.url_informatsionnaya_bezopasnost_quiz_php, headers=headers, timeout=10
    )
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Лицензии 1С-Битрикс: Управление сайтом")
def test_get_licenziya_cms_1c_bitrix_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_solutions_licenziya_cms_1c_bitrix, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Дополнительно к хостингу Мониторинг сайта")
def test_get_solutions_maas_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_solutions_maas, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Выгодный переезд Переносите сайт в hoster.by")
def test_get_move_hoster_by_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_move_hoster_by, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Защищенная облачная инфраструктура PCI DSS")
def test_get_solutions_pci_dss_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_solutions_pci_dss, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Конструктор сайтов")
def test_get_sozdanie_saita_besplatno_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_sozdanie_saita_besplatno, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Мультимедиа")
def test_get_solutions_streaming_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_solutions_streaming, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Бесплатные домены SITE, ONLINE и XYZ")
def test_get_domen_besplatno_free_domain_xyz_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(
        Url.url_poluchit_domen_besplatno_free_domain_xyz, headers=headers, timeout=10
    )
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом POST")
@allure.story("Регистрация на сайте как юр. лицо")
def test_post_reg_yr_face():
    """ Проверка кода ответа. """

    url = "https://hoster.by/ajax/ajax.php"

    payload1 = {
        "action": "registration_lk",
        "reg_client_type": "1",
        "1_resident": "1",
        "1_email": "margarita.test@testhoster.of.by",
        "1_password": "655GimX",
        "1_password_conf": "655GimX",
        "1_unp": "520020217",
        "1_name": "Общество с ограниченной ответственностью МАРГАРИТАБАЙ",
        "1_r_name": "TEST",
        "1_entity_phone": " 375292112054",
        "1_news": "1",
        "1_entity_pers_data": "1",
    }

    response1 = requests.request("POST", url, headers=Url.headers1, data=payload1, timeout=10)

    print(response1.text)

    with allure.step("Проверка кода ответа"):
        assert (
            response1.status_code == 200
        ), f"Неверный код ответа, получен {response1.status_code}"


@allure.feature("Тестирование кода ответа методом POST")
@allure.story("Регистрация на сайте как физ. лицо")
def test_post_reg_phiz_face():
    """ Проверка кода ответа. """

    url = "https://hoster.by/ajax/ajax.php"

    payload2 = {
        "action": "registration_lk",
        "reg_client_type": "2",
        "2_resident": "1",
        "2_email": "margarita.test@testhoster.of.by",
        "2_password": "655GimX",
        "2_password_conf": "655GimX",
        "2_name": "Сокол Маргарита Юрьевна",
        "2_entity_phone": " 375292112054",
        "2_news": "1",
    }

    response2 = requests.request("POST", url, headers=Url.headers1, data=payload2, timeout=10)

    print(response2.text)

    with allure.step("Проверка кода ответа"):
        assert (
            response2.status_code == 200
        ), f"Неверный код ответа, получен {response2.status_code}"


@allure.feature("Тестирование кода ответа методом POST")
@allure.story("Регистрация на сайте как ИП")
def test_post_reg_ip():
    """ Проверка кода ответа . """

    url = "https://hoster.by/ajax/ajax.php"

    payload3 = {
        "action": "registration_lk",
        "reg_client_type": "3",
        "3_resident": "1",
        "3_email": "margarita.test@testhoster.of.by",
        "3_password": "655GimX",
        "3_password_conf": "655GimX",
        "3_unp": "791260214",
        "3_name": "Иванов Иван Иванович",
        "3_entity_phone": " 375292112054",
        "3_news": "1",
    }

    response3 = requests.request("POST", url, headers=Url.headers1, data=payload3, timeout=10)

    print(response3.text)

    with allure.step("Проверка кода ответа"):
        assert (
            response3.status_code == 200
        ), f"Неверный код ответа, получен {response3.status_code}"


@allure.feature("Тестирование кода ответа методом POST")
@allure.story("Регистрация на сайте как гос.орг")
def test_post_reg_gov():
    """ Проверка кода ответа. """

    url = "https://hoster.by/ajax/ajax.php"

    payload4 = {
        "action": "registration_lk",
        "reg_client_type": "gov",
        "gov_email": "margarita.test@testhoster.of.by",
        "gov_password": "655GimX",
        "gov_password_conf": "655GimX",
        "gov_unp": "791260214",
        "gov_name": "Сокол Маргарита Юрьевна TEST",
        "gov_r_name": "Сокол Маргарита Юрьевна TEST",
        "gov_entity_phone": " 375292112054",
        "gov_news": "1",
    }

    response4 = requests.request("POST", url, headers=Url.headers1, data=payload4, timeout=10)

    print(response4.text)

    with allure.step("Проверка кода ответа"):
        assert (
            response4.status_code == 200
        ), f"Неверный код ответа, получен {response4.status_code}"
