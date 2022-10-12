""" Элементы страницы хостинга """

import os
from pages.base_page import WebPage
from pages.elements import WebElement


class HostingPage(WebPage):
    """Класс представляющий страницу хостинга"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = os.getenv("HOSTING_URL") or "https://hoster.by/service/hosting/"

        super().__init__(web_driver, url)

        ################# БЛОКИ #################

    # Главный блок
    section_main = WebElement(id="banner-main4")

    # Блок Стандартные тарифы для .PHP и .ASP
    section_php = WebElement(xpath="/html/body/div[10]")

    # Блок с видами хостинга ОС (windows, unix)
    section_os = WebElement(xpath="/html/body/div[11]")

    # Блок Специализированные тарифы
    section_spectarif = WebElement(xpath="/html/body/div[12]")

    # Блок с видами спец.хостингов
    section_kindscpectariff = WebElement(xpath="/html/body/div[13]")

    # Блок Наш виртуальный хостинг уже заряжен
    section_venvhost = WebElement(id="advant-2col")

    # Блок Вопросы и ответы
    section_qa = WebElement(id="accordion")

    ################# ЭЛЕМЕНТЫ БЛОКА "ГЛАВНЫЙ БЛОК" #################

    # Заглавный текст
    text_head_main = WebElement(
        xpath='//*[@id="banner-main4"]/div/div/div/div/div[1]/h1'
    )

    # Текст описания
    text_description_main = WebElement(
        xpath='//*[@id="banner-main4"]/div/div/div/div/div[1]/p'
    )

    # Картинка блока
    img_head_main = WebElement(
        css_selector='img[src="/upload/iblock/e7c/y643p7sp8mcpg4l6tgivvjnosvuhkz0e.png"]'
    )

    ################# ЭЛЕМЕНТЫ БЛОКА "СТАНДАРТНЫЕ ТАРИФЫ ДЛЯ .РНР и .ASP" #################

    # Заглавный текст
    text_php_head = WebElement(xpath="/html/body/div[10]/div/div")

    # Текст описания блока
    text_php_description = WebElement(xpath="/html/body/div[10]/div/p")

    ################# ЭЛЕМЕНТЫ БЛОКА "С ВИДАМИ ХОСТИНГА ОС (WINDOWS, UNIX)" #################

    # Плитка unix
    title_unix = WebElement(xpath="/html/body/div[11]/div/div/div/div[1]")

    # Плитка windows
    title_windows = WebElement(xpath="/html/body/div[11]/div/div/div/div[2]")

    # Заглавный текст unix
    text_head_title_unix = WebElement(
        xpath="/html/body/div[11]/div/div/div/div[1]/div[2]/div"
    )

    # Заглавный текст windows
    text_head_title_windows = WebElement(
        xpath="/html/body/div[11]/div/div/div/div[2]/div[2]/div"
    )

    # Текст описания unix
    text_description_title_unix = WebElement(
        xpath="/html/body/div[11]/div/div/div/div[1]/div[2]/p"
    )

    # Текст описания windows
    text_description_title_windows = WebElement(
        xpath="/html/body/div[11]/div/div/div/div[2]/div[2]/p"
    )

    # Картинка unix
    img_title_unix = WebElement(
        css_selector='img[src="/upload/iblock/fe3/rgb7h9acn64r33qcn6wp03hitl1udx51.svg"]'
    )

    # Картинка windows
    img_title_windows = WebElement(
        css_selector='img[src="/upload/iblock/1da/ht830ctqd6ohzvkbyenkt2kpw5r9d6ai.svg"]'
    )

    # Кнопка unix
    btn_title_unix = WebElement(css_selector='a[href="/service/hosting/unix/"]')

    # Кнопка windows
    btn_title_windows = WebElement(css_selector='a[href="/service/hosting/windows/"]')

    ################# ЭЛЕМЕНТЫ БЛОКА "СПЕЦИАЛИЗИРОВАННЫЕ ТАРИФЫ" #################

    # Заглавный текст
    text_spec_head = WebElement(xpath="/html/body/div[12]/div/div/div")

    # Текст описания блока
    text_spec_description = WebElement(xpath="/html/body/div[12]/div/p")

    ################# ЭЛЕМЕНТЫ БЛОКА "С ВИДАМИ СПЕЦ. ХОСТИНГОВ" #################

    # Плитка Битрикс
    title_bitrix = WebElement(xpath="/html/body/div[13]/div/div/div/div[1]")

    # Плитка Wordpress
    title_woerdpress = WebElement(xpath="/html/body/div[13]/div/div/div/div[2]")

    # Плитка Joomla
    title_joomla = WebElement(xpath="/html/body/div[13]/div/div/div/div[3]")

    # Плитка Drupal
    title_drupal = WebElement(xpath="/html/body/div[13]/div/div/div/div[4]")

    # Плитка Tilda
    title_tilda = WebElement(xpath="/html/body/div[13]/div/div/div/div[5]")

    # Плитка Пакет «Быстрый старт»
    title_faststart = WebElement(xpath="/html/body/div[13]/div/div/div/div[6]")

    # Заглавный текст Битрикс
    text_head_title_bitrix = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[1]/div[2]/div"
    )

    # Заглавный текст Wordpress
    text_head_title_wordpress = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[2]/div[2]/div"
    )

    # Заглавный текст Joomla
    text_head_title_joomla = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[3]/div[2]/div"
    )

    # Заглавный текст Drupal
    text_head_title_drupal = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[4]/div[2]/div"
    )

    # Заглавный текст Tilda
    text_head_title_tilda = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[5]/div[2]/div"
    )

    # Заглавный текст Пакет «Быстрый старт»
    text_head_title_faststart = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[6]/div[2]/div"
    )

    # Текст описания Битрикс
    text_description_title_bitrix = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[1]/div[2]/p"
    )

    # Текст описания Wordpress
    text_description_title_wordpress = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[2]/div[2]/p"
    )

    # Текст описания Joomla
    text_description_title_joomla = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[3]/div[2]/p"
    )

    # Текст описания Drupal
    text_description_title_drupal = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[4]/div[2]/p"
    )

    # Текст описания Tilda
    text_description_title_tilda = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[5]/div[2]/p"
    )

    # Текст описания Пакет «Быстрый старт»
    text_description_title_faststart = WebElement(
        xpath="/html/body/div[13]/div/div/div/div[6]/div[2]/p"
    )

    # Картинка Битрикс
    img_title_bitrix = WebElement(
        css_selector='img[src="/upload/iblock/df8/8ygppd0lhz5klkg6tzu8qp29b6vz7bk4.svg"]'
    )

    # Картинка Wordpress
    img_title_wordpress = WebElement(
        css_selector='img[src="/upload/iblock/0c8/ju84c7a4mqlw045b8a3qjze0x9tf0typ.svg"]'
    )

    # Картинка Joomla
    img_title_joomla = WebElement(
        css_selector='img[src="/upload/iblock/1d6/nlz8b6e9d246ci6nixsj2svrp779gs1o.svg"]'
    )

    # Картинка Drupal
    img_title_drupal = WebElement(
        css_selector='img[src="/upload/iblock/51e/php75krc7w040s8l5c1idx2l9ci0gb2d.svg"]'
    )

    # Картинка Tilda
    img_title_tilda = WebElement(
        css_selector='img[src="/upload/iblock/f33/6wjdtqwzigc6d4cgnbftqsnmo7yqvm3n.svg"]'
    )

    # Картинка Пакет «Быстрый старт»
    img_title_faststart = WebElement(
        css_selector='img[src="/upload/iblock/b8a/wrj4c330obkpslo6zx1t39gj53mjstnp.svg"]'
    )

    # Кнопка Битрикс
    btn_title_bitrix = WebElement(css_selector='a[href="/service/hosting/bitrix/"]')

    # Кнопка Wordpress
    btn_title_wordpress = WebElement(
        css_selector='a[href="/service/hosting/wordpress/"]'
    )

    # Кнопка Joomla
    btn_title_joomla = WebElement(css_selector='a[href="/service/hosting/joomla/"]')

    # Кнопка Drupal
    btn_title_drupal = WebElement(css_selector='a[href="/service/hosting/drupal/"]')

    # Кнопка Tilda
    btn_title_tilda = WebElement(css_selector='a[href="/service/hosting/tilda/"]')

    # Кнопка Пакет «Быстрый старт»
    btn_title_faststart = WebElement(
        css_selector='a[href="/service/solutions/fast-start/"]'
    )

    ################# ЭЛЕМЕНТЫ БЛОКА "НАШ ВИРТУАЛЬНЫЙ ХОСТИНГ УЖЕ ЗАРЯЖЕН" #################

    # Заглавный текст
    text_head_charj = WebElement(xpath='//*[@id="advant-2col"]/div/div/h2')

    # Плитка Корпоративная почта
    title_charj1 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[1]')

    # Плитка SSL-сертификат
    title_charj2 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[2]')

    # Плитка Резервное копирование
    title_charj3 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[3]')

    # Плитка Конструктор сайтов
    title_charj4 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[4]')

    # Плитка Проактивная защита Imunify360
    title_charj5 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[5]')

    # Плитка Заботливая поддержка
    title_charj6 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[6]')

    # Заглавный текст Корпоративная почта
    text_head_charj1 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[1]/p')

    # Заглавный текст SSL-сертификат
    text_head_charj2 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[2]/p')

    # Заглавный текст Резервное копирование
    text_head_charj3 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[3]/p')

    # Заглавный текст Конструктор сайтов
    text_head_charj4 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[4]/p')

    # Заглавный текст Проактивная защита Imunify360
    text_head_charj5 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[5]/p')

    # Заглавный текст Заботливая поддержка
    text_head_charj6 = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[6]/p')

    # Картинка Корпоративная почта
    img_title_charj1 = WebElement(
        css_selector='img[src="/upload/iblock/ec4/80zco3czg6befzakvbnl1b0dztdzrwfy.svg"]'
    )

    # Картинка SSL-сертификат
    img_title_charj2 = WebElement(
        css_selector='img[src="/upload/iblock/df0/7uj572tftfq06h562f9o2qdicogr0a8p.svg"]'
    )

    # Картинка Резервное копирование
    img_title_charj3 = WebElement(
        css_selector='img[src="/upload/iblock/aef/312iieqhygrovvaqp939v2yab44bckvf.svg"]'
    )

    # Картинка Конструктор сайтов
    img_title_charj4 = WebElement(
        css_selector='img[src="/upload/iblock/a76/0dni8jw7zrj5c4uxn85he41ruxugn2f3.svg"]'
    )

    # Картинка Проактивная защита Imunify360
    img_title_charj5 = WebElement(
        css_selector='img[src="/upload/iblock/f8f/337pccc5xj1re79k9ufe1edna60rscu6.svg"]'
    )

    # Картинка Заботливая поддержка
    img_title_charj6 = WebElement(
        css_selector='img[src="/upload/iblock/882/fq7owia4pikinnqak6sqb1set45hg620.svg"]'
    )

    ################# ЭЛЕМЕНТЫ БЛОКА "ВОПРОС-ОТВЕТ" #################

    # Текст заглавный
    text_head_qa = WebElement(xpath='//*[@id="accordion"]/div/div/h2')

    # Вопрос 1
    q1 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[1]')

    # Вопрос 2
    q2 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[2]')

    # Вопрос 3
    q3 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[3]')

    # Вопрос 4
    q4 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[4]')

    # Вопрос 5
    q5 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[5]')

    # Вопрос 6
    q6 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[6]')

    # Ответ 1
    a1 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[1]/div[2]/p')

    # Ответ 2
    a2 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[2]/div[2]/p')

    # Ответ 2
    a3 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[3]/div[2]/p')

    # Ответ 3
    a4 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[4]/div[2]/p')

    # Ответ 4
    a5 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[5]/div[2]/p')

    # Ответ 5
    a6 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[6]/div[2]/p')

    ################# ПОП АП #################

    btn_pop_up = WebElement(css_selector="[class*='btn'][class*='Fill'].purpBtn")
