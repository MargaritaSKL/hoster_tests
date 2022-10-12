""" Элементы страницы хостинг Unix """

import os
from pages.base_page import WebPage
from pages.elements import WebElement


class HostingUnixPage(WebPage):
    """Класс представляющий страницу хостинг Unix"""

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("HOSTING_UNIX_URL") or 'https://hoster.by/service/hosting/unix/'

        super().__init__(web_driver, url)

                                        ################# БЛОКИ #################

    # Главный блок
    section_main_unit = WebElement(id='banner-main4')

    # Блок тарифов
    section_tariffs = WebElement(id='tariffs')

    # Блок "в каждом тарифе есть"
    section_tariffhas = WebElement(id='advant-3icons-2rows')

    # Блок "упор на безопасность"
    section_security = WebElement(id='advant-photo')

    # Блок "450+ приложений и CMS"
    section_cms450 = WebElement(id='banner1-icon')

    # Блок слайдера компаний
    section_slider = WebElement(id='logo-slider')

    # Блок 'У нас есть уникальные решения'
    section_unique_solutions = WebElement(id='advant-2col')

    # Блок 'Ваш сайт у другого провайдера?'
    section_another_provider = WebElement(id='banner2-picture')

    # Блок 'Еще больше преимуществ'
    section_advantage = WebElement(id='tabs-tables-tariffs')

    # Блок 'Вопрос-ответ'
    section_qa_unix = WebElement(id='accordion')

                                    ################# ЭЛЕМЕНТЫ БЛОКА "ГЛАВНЫЙ БЛОК" #################

    # Заглавный текст
    text_head_main_unit = WebElement(xpath='//*[@id="banner-main4"]/div/div/div/div/div[1]/h1')

    # Описание текст
    text_description_main_unit = WebElement(xpath='//*[@id="banner-main4"]/div/div/div/div/div[1]/p')

    # Картинка блока
    img_main_unit = WebElement(css_selector='img[src="/upload/iblock/300/lqhjcwlfocfaa5poc8j10w2r9cv3fde8.png"]')

    # Кнопка 'Тестировать бесплатно'
    btn_test_free_main_unit = WebElement(css_selector='img[src="/upload/iblock/300/lqhjcwlfocfaa5poc8j10w2r9cv3fde8.png"]')

                                    ################# ЭЛЕМЕНТЫ БЛОКА "ТАРИФЫ" #################

    # Тариф ЛАЙТ
    tarif_lite_host_unix = WebElement(css_selector='div[data-slick-index="0"]')

    # Тариф СТАНДАРТ
    tarif_standart_host_unix = WebElement(css_selector='div[data-slick-index="1"]')

    # Тариф АКТУАЛЬНЫЙ
    tarif_actual_host_unix = WebElement(css_selector='div[data-slick-index="2"]')

    # Тариф ОПТИМА
    tarif_optema_host_unix = WebElement(css_selector='div[data-slick-index="3"]')

    # Тариф ПРОФИ
    tarif_profi_host_unix = WebElement(css_selector='div[data-slick-index="4"]')

    # Тариф МАКСИМА
    tarif_maxima_host_unix = WebElement(css_selector='div[data-slick-index="5"]')

    # Кнопка "Позвонить мне"
    btn_tarif_call_me_host_unix = WebElement(xpath='/html/body/div[10]/div[2]/button')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "ЛАЙТ" #################

    # Текст заглавное имя тарифа
    text_tarif_lite_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[2]')

    # Цена тарифа
    price_tarif_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[3]')

    # Кнопка периода аренды
    btn_tarif_period_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div')

    # Кнопка периода аренды 3 года
    btn_tarif_period3y_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[1]')

    # Кнопка периода аренды 2 года
    btn_tarif_period2y_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]')

    # Кнопка периода аренды 1 год
    btn_tarif_period1y_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[3]')

    # Кнопка периода аренды 6 месяцев
    btn_tarif_period6m_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[4]')

    # Кнопка периода аренды 3 месяца
    btn_tarif_period3m_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[5]')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/div[6]')

    # Описание тарифа (состав)
    description_tarif_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[5]')

    # Кнопка выбора тарифа
    btn_tarif_select_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[6]/a[1]')

    # Кнопка выбора тарифа бесплатно (на 14 дней)
    btn_tarif_selectfree_lite_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[1]/div/div/div[6]/a[2]')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "СТАНДАРТ" #################

    # Текст заглавное имя тарифа
    text_tarif_stand_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[2]')

    # Цена тарифа
    price_tarif_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[3]')

    # Кнопка периода аренды
    btn_tarif_period_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div')

    # Кнопка периода аренды 3 года
    btn_tarif_period3y_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[1]')

    # Кнопка периода аренды 2 года
    btn_tarif_period2y_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]')

    # Кнопка периода аренды 1 год
    btn_tarif_period1y_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[3]')

    # Кнопка периода аренды 6 месяцев
    btn_tarif_period6m_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[4]')

    # Кнопка периода аренды 3 месяца
    btn_tarif_period3m_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[5]')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[6]')

    # Описание тарифа (состав)
    description_tarif_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[5]')

    # Кнопка выбора тарифа
    btn_tarif_select_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[6]/a[1]')

    # Кнопка выбора тарифа бесплатно (на 14 дней)
    btn_tarif_selectfree_stand_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[2]/div/div/div[6]/a[2]')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "АКТУАЛЬНЫЙ" #################

    # Текст заглавное имя тарифа
    text_tarif_actual_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[1]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_actual_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[1]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_actual_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[2]')

    # Цена тарифа
    price_tarif_actual_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[3]')

    # Кнопка периода аренды
    btn_tarif_period_actual_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[4]/div')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_actual_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[4]/div/div[2]/div')

    # Описание тарифа (состав)
    description_tarif_actual_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[3]/div/div/div[5]')

    # Кнопка выбора тарифа
    btn_tarif_select_actual_host_unix = WebElement(css_selector='a[href="https://hoster.by/service/hosting/unix/actual/?time=5"]')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "ОПТИМА" #################

    # Текст заглавное имя тарифа
    text_tarif_optima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[2]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_optima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[2]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[3]')

    # Цена тарифа
    price_tarif_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[4]')

    # Кнопка периода аренды
    btn_tarif_period_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div')

    # Кнопка периода аренды 3 года
    btn_tarif_period3y_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[1]')

    # Кнопка периода аренды 2 года
    btn_tarif_period2y_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[2]')

    # Кнопка периода аренды 1 год
    btn_tarif_period1y_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[3]')

    # Кнопка периода аренды 6 месяцев
    btn_tarif_period6m_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[4]')

    # Кнопка периода аренды 3 месяца
    btn_tarif_period3m_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[5]')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[5]/div/div[2]/div[6]')

    # Описание тарифа (состав)
    description_tarif_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[6]')

    # Кнопка выбора тарифа
    btn_tarif_select_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[7]/a[1]')

    # Кнопка выбора тарифа бесплатно (на 14 дней)
    btn_tarif_selectfree_optima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[4]/div/div/div[7]/a[2]')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "ПРОФИ" #################

    # Текст заглавное имя тарифа
    text_tarif_profi_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[1]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_profi_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[1]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[2]')

    # Цена тарифа
    price_tarif_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[3]')

    # Кнопка периода аренды
    btn_tarif_period_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div')

    # Кнопка периода аренды 3 года
    btn_tarif_period3y_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[1]')

    # Кнопка периода аренды 2 года
    btn_tarif_period2y_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[2]')

    # Кнопка периода аренды 1 год
    btn_tarif_period1y_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[3]')

    # Кнопка периода аренды 6 месяцев
    btn_tarif_period6m_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[4]')

    # Кнопка периода аренды 3 месяца
    btn_tarif_period3m_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[5]')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[4]/div/div[2]/div[6]')

    # Описание тарифа (состав)
    description_tarif_profi_host_unix = WebElement(xpath='/html/body/div[10]/div[1]/div/div/div/div[5]/div/div/div[5]')

    # Кнопка выбора тарифа
    btn_tarif_select_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[6]/a[1]')

    # Кнопка выбора тарифа бесплатно (на 14 дней)
    btn_tarif_selectfree_profi_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[6]/a[2]')

                                    ################# ЭЛЕМЕНТЫ ТАРИФА "МАКСИМА" #################

    # Текст заглавное имя тарифа
    text_tarif_maxima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[1]/div[1]')

    # Текст поддтекст имя тарифа
    textsmall_tarif_maxima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[5]/div/div/div[1]/div[2]/div')

    # Текст скидка тарифа
    textseal_tarif_maxima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[2]')

    # Цена тарифа
    price_tarif_maxima_name_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[3]')

    # Кнопка периода аренды
    btn_tarif_period_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div')

    # Кнопка периода аренды 3 года
    btn_tarif_period3y_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[1]')

    # Кнопка периода аренды 2 года
    btn_tarif_period2y_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[2]')

    # Кнопка периода аренды 1 год
    btn_tarif_period1y_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[3]')

    # Кнопка периода аренды 6 месяцев
    btn_tarif_period6m_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[4]')

    # Кнопка периода аренды 3 месяца
    btn_tarif_period3m_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[5]')

    # Кнопка периода аренды 1 месяц
    btn_tarif_period1m_maxima_host_unix = WebElement(xpath='//*[@id="tariffs"]/div[1]/div/div/div/div[6]/div/div/div[4]/div/div[2]/div[6]')

    # Описание тарифа (состав)
    description_tarif_maxima_host_unix = WebElement(xpath='/html/body/div[10]/div[1]/div/div/div/div[5]/div/div/div[5]')

    # Кнопка выбора тарифа
    btn_tarif_select_maxima_host_unix = WebElement(css_selector='a[href="https://hoster.by/service/hosting/unix/profi/?time=5"]')

    # Кнопка выбора тарифа бесплатно (на 14 дней)
    btn_tarif_selectfree_maxima_host_unix = WebElement(css_selector='a[href="/service/hosting/unix/profi/?time=3&test=2"]')

                                ################# ЭЛЕМЕНТЫ БЛОКА "В КАЖДОМ ТАРИФЕ ЕСТЬ" #################

    # Картинка плитки "Конструктор сайтов"
    text_tariffhas_head_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/h2')

    # Картинка плитки "Конструктор сайтов"
    img1_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/8b1/iw9jxxbsla90pbk89jvqknnx7w247zht.svg"]')

    # Текст заглавное имя плитки "Конструктор сайтов"
    text1_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[1]/p[1]')

    # Текст описания плитки "Конструктор сайтов"
    textdescription1_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[1]/p[2]')

    # Картинка плитки "Бесплатный SSL-сертификат"
    img2_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/e1f/b7wop6o1f3me61dd1r3755szghzepfp6.svg"]')

    # Текст заглавное имя плитки "Бесплатный SSL-сертификат"
    text2_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[2]/p[1]')

    # Текст описания плитки "Бесплатный SSL-сертификат"
    textdescription2_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[2]/p[2]')

    # Картинка плитки "Почта уровня Pro"
    img3_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/2ce/m2c6vikgv9zexio8r38845087pjmqar1.svg"]')

    # Текст заглавное имя плитки "Почта уровня Pro"
    text3_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[3]/p[1]')

    # Текст описания плитки "Почта уровня Pro"
    textdescription3_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[3]/p[2]')

    # Картинка плитки "14 дней бесплатно"
    img4_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/d42/efl6qeqs8th1vvc8vssuufw670j3osj4.svg"]')

    # Текст заглавное имя плитки "14 дней бесплатно"
    text4_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[4]/p[1]')

    # Текст описания плитки "14 дней бесплатно"
    textdescription4_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[4]/p[2]')

    # Картинка плитки "Техподдержка 24/7"
    img5_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/9e8/qxoi3x2xed0f5jagkote6f8rwpts7az4.svg"]')

    # Текст заглавное имя плитки "Техподдержка 24/7"
    text5_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[5]/p[1]')

    # Текст описания плитки "Техподдержка 24/7"
    textdescription5_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[5]/p[2]')

    # Картинка плитки "BackUp-менеджер"
    img6_tariffhas_host_unix = WebElement(css_selector='img[src="/upload/iblock/db3/3p2o21chriqr22foka12grlvxzihjp54.svg"]')

    # Текст заглавное имя плитки "BackUp-менеджер"
    text6_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[6]/p[1]')

    # Текст описания плитки "BackUp-менеджер"
    textdescription6_tariffhas_host_unix = WebElement(xpath='//*[@id="advant-3icons-2rows"]/div/div/div/div[6]/p[2]')

                                ################# ЭЛЕМЕНТЫ БЛОКА "УПОР НА БЕЗОПАСНОСТЬ" #################

    # Заглавный текст блока"
    texthead_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[1]/h2')

    # Картинка блока
    img_security = WebElement(css_selector='img[src="/upload/iblock/c20/1gtpd0x4lmt6sf8lirbdxv3dmzaqqqx8.png"]')

    # Заглавный текст раздела "Проактивная защита"
    text1_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[1]/span')

    # Текст описание раздела "Проактивная защита"
    textdescription1_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[1]/p')

    # Заглавный текст раздела "Защита от DDoS-атак"
    text2_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[2]/span')

    # Текст описание раздела "Защита от DDoS-атак"
    textdescription2_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[2]/p')

    # Заглавный текст раздела "Сохранность копий сайта"
    text3_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[3]/span')

    # Текст описание раздела "Сохранность копий сайта"
    textdescription3_security = WebElement(xpath='//*[@id="advant-photo"]/div/div/div[2]/div[2]/div/div[3]/p')

                            ################# ЭЛЕМЕНТЫ БЛОКА "450+ ПРИЛОЖЕНИЙ И CMS" #################

    # Заглавный текст блока
    texthead_450cms = WebElement(xpath='//*[@id="banner1-icon"]/div/div/div/div[1]/h2')

    # Текст описания блока
    textdescription_450cms = WebElement(xpath='//*[@id="banner1-icon"]/div/div/div/div[1]/p')

    # Текст рекламы
    textadvertising_450cms = WebElement(xpath='//*[@id="banner1-icon"]/div/div/div/div[2]/p[2]')

    #Картинка блока
    img_450cms = WebElement(css_selector='img[src="/upload/iblock/1a6/bpqr47227wq1vzb12eqtgulmsx9737cj.svg"]')

                            ################# ЭЛЕМЕНТЫ БЛОКА "СЛАЙДЕРА" #################

    # Кнопка слайдера
    btn_slider = WebElement(css_selector='button[class="slick-next slick-arrow"]')

                            ################# ЭЛЕМЕНТЫ БЛОКА "У НАС ЕСТЬ УНИКАЛЬНЫЕ РЕШЕНИЯ" #################

    # Текст заглавный
    text_unique_solutions = WebElement(xpath='//*[@id="advant-2col"]/div/div/h2')

    # Картинка плитки1
    img1_unique_solutions = WebElement(css_selector='img[src="/upload/iblock/47e/v6rj5zitthecvkiv3h0ij978ir92m2ki.svg"]')

    # Картинка плитки2
    img2_unique_solutions = WebElement(css_selector='img[src="/upload/iblock/86c/o2q27lu4y4m621jzi1otbvfc7jk0s2dh.svg"]')

    # Картинка плитки3
    img3_unique_solutions = WebElement(css_selector='img[src="/upload/iblock/910/9dqu2hwv4abh5wrcu21t1gb5oorrojzz.svg"]')

    # Картинка плитки4
    img4_unique_solutions = WebElement(css_selector='img[src="/upload/iblock/802/9krgx635l4uhj5k00dx8wjnhq8ja963k.svg"]')

    # Описание плитки1
    description1_unique_solutions = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[1]/p')

    # Описание плитки2
    description2_unique_solutions = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[2]/p')

    # Описание плитки3
    description3_unique_solutions = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[3]/p')

    # Описание плитки4
    description4_unique_solutions = WebElement(xpath='//*[@id="advant-2col"]/div/div/div/div[4]/p')

                            ################# ЭЛЕМЕНТЫ БЛОКА "ВАШ САЙТ У ДРУГОГО ПРОВАЙДЕРА?" #################

    # Текст заглавный
    text_another_provider = WebElement(xpath='//*[@id="banner2-picture"]/div/div/div/div[1]/h2')

    # Текст описания блока
    description_another_provider = WebElement(xpath='//*[@id="banner2-picture"]/div/div/div/div[1]/p')

    # Кнопка "Переехать в hoster.by"
    btn_another_provider = WebElement(xpath='//*[@id="banner2-picture"]/div/div/div/div[1]/div[2]/a')

    # Картинка блока
    img_another_provider = WebElement(xpath='//*[@id="banner2-picture"]/div/div/div/div[2]/div')

                            ################# ЭЛЕМЕНТЫ БЛОКА "ЕЩЕ БОЛЬШЕ ПРЕИМУЩЕСТВ" #################

    # Текст заглавный
    text_head_advantage = WebElement(xpath='//*[@id="tabs-tables-tariffs"]/div/div/h2')

    # Раздел "Технические характеристики"
    section_advantagetth = WebElement(xpath='//*[@id="tabs-tables-tariffs"]/div/div/div/div[1]/div[1]/span')

    # Раздел "Программная платформа"
    section_advantageprog = WebElement(xpath='//*[@id="tabs-tables-tariffs"]/div/div/div/div[2]/div[1]/span')

    # Описание/содержание раздела "Технические характеристики"
    description_advantagetth = WebElement(xpath='//*[@id="tabs-tables-tariffs"]/div/div/div/div[1]/div[2]/div/ul[1]')

    # Описание/содержание раздела "Программная платформа"
    description_advantageprog = WebElement(xpath='//*[@id="tabs-tables-tariffs"]/div/div/div/div[1]/div[2]/div/ul[2]')

                            ################# ЭЛЕМЕНТЫ БЛОКА "ВОПРОС-ОТВЕТ" #################

    # Текст заглавный
    text_head_qa = WebElement(xpath='//*[@id="accordion"]/div/div/h2')

    # Текст заглавный
    q1 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[1]')

    # Текст заглавный
    q2 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[2]')

    # Текст заглавный
    q3 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[3]')

    # Текст заглавный
    q4 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[4]')

    # Текст заглавный
    a1 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[1]/div[2]')

    # Текст заглавный
    a2 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[2]/div[2]')

    # Текст заглавный
    a3 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[3]/div[2]')

    # Текст заглавный
    a4 = WebElement(xpath='//*[@id="accordion"]/div/div/ul/li[4]/div[2]')

                            ################# ПОП АП #################

    btn_pop_up = WebElement(css_selector="[class*='btn'][class*='Fill'].purpBtn")
