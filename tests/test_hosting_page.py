""" Проверка элементов страницы хостинг Unix. """

import time
import allure
from pages.hosting_unix import HostingUnixPage


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка блока на странице')
def test_check_section_page(web_browser):
    """ Убеждаемся, что блоки страницы отображаются на странцие. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка блока main'):
        main = page.section_main_unit
        assert main.is_visible()

    with allure.step('Проверка блока тарифа'):
        tariffs = page.section_tariffs
        assert tariffs.is_visible()

    with allure.step('Проверка блока "в каждом тарифе есть"'):
        tariffhas = page.section_tariffhas
        assert tariffhas.is_visible()

    with allure.step('Проверка блока "упор на безопасность"'):
        security = page.section_security
        assert security.is_visible()

    with allure.step('Проверка блока "450+ приложений и CMS"'):
        cms450 = page.section_cms450
        assert cms450.is_visible()

    with allure.step('Проверка блока слайдера компаний'):
        slider = page.section_slider
        assert slider.is_visible()

    with allure.step('Проверка блока "У нас есть уникальные решения"'):
        solutions = page.section_unique_solutions
        assert solutions.is_visible()

    with allure.step('Проверка блока "Ваш сайт у другого провайдера?"'):
        provider = page.section_another_provider
        assert provider.is_visible()

    with allure.step('Проверка блока "Еще больше преимуществ"'):
        advantage = page.section_advantage
        assert advantage.is_visible()

    with allure.step('Проверка блока "Вопрос-ответ"'):
        qa_unix = page.section_qa_unix
        assert qa_unix.is_visible()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока main')
def test_check_section_main(web_browser):
    """ Убеждаемся, что элементы блока main отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста'):
        textmain = page.text_head_main_unit
        assert textmain.is_visible()
        assert textmain.get_text() == 'Хостинг для сайта'

    with allure.step('Проверка отображения описания заглавного текста'):
        textdescription = page.text_description_main_unit
        assert textdescription.is_visible()

    with allure.step('Проверка отображения картинки блока main'):
        imgmain = page.img_main_unit
        assert imgmain.is_visible()

    with allure.step('Проверка отображения кнопки и кликабельности "Тестировать бесплатно"'):
        btnfree = page.btn_test_free_main_unit
        assert btnfree.is_visible()
        assert btnfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифы')
def test_check_section_tarif(web_browser):
    """ Убеждаемся, что элементы блока тарифы отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения тарифа ЛАЙТ'):
        lite = page.tarif_lite_host_unix
        assert lite.is_visible()

    with allure.step('Проверка отображения тарифа СТАНДАРТ'):
        standart = page.tarif_standart_host_unix
        assert standart.is_visible()

    with allure.step('Проверка отображения тарифа АКТУАЛЬНЫЙ'):
        actual = page.tarif_actual_host_unix
        assert actual.is_visible()

    with allure.step('Проверка отображения тарифа ОПТИМА'):
        optema = page.tarif_optema_host_unix
        assert optema.is_visible()

    with allure.step('Проверка отображения тарифа ПРОФИ'):
        profi = page.tarif_profi_host_unix
        assert profi.is_visible()

    with allure.step('Проверка отображения тарифа МАКСИМА'):
        maxima = page.tarif_maxima_host_unix
        assert maxima.is_visible()

    with allure.step('Проверка отображения кнопки "Позвонить мне"'):
        btn_call_me = page.btn_tarif_call_me_host_unix
        assert btn_call_me.is_visible()
        assert btn_call_me.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа ЛАЙТ')
def test_check_tarif_lite(web_browser):
    """ Убеждаемся, что элементы блока тарифа ЛАЙТ отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        lite_tariftext = page.text_tarif_lite_name_host_unix
        assert lite_tariftext.is_visible()
        assert lite_tariftext.get_text() == 'Лайт'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        lite_tariftextsmall = page.textsmall_tarif_lite_host_unix
        assert lite_tariftextsmall.is_visible()
        assert lite_tariftextsmall.get_text() == 'Удобен для промо-страниц и сайтов-визиток'

    with allure.step('Проверка отображения блока со скидкой'):
        lite_tarifseal = page.textseal_tarif_lite_host_unix
        assert lite_tarifseal.is_visible()
        assert lite_tarifseal.get_text() == '-20%\n5.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_lite_host_unix
        assert price.is_visible()
        assert price.get_text() == '4,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_lite_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_lite_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.btn_tarif_select_lite_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()

    with allure.step('Проверка отображения и кликабельности кнопки'
                     ' выбора тарифа бесплатно (на 14 дней)'):
        btn_tarif_selectfree = page.btn_tarif_selectfree_lite_host_unix
        assert btn_tarif_selectfree.is_visible()
        assert btn_tarif_selectfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа ЛАЙТ')
def test_check_tarif_lite_period(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа
     ЛАЙТ кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка кикабельности и изменении периода аренды'):
        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period3y_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.is_visible()
        assert page.textseal_tarif_lite_host_unix.get_text() == '-20%\n5.00'
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '4,00\nруб.\nза мес'

        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period2y_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.is_visible()
        assert page.textseal_tarif_lite_host_unix.get_text() == '-15%\n5.00'
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '4,25\nруб.\nза мес'

        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period1y_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.is_visible()
        assert page.textseal_tarif_lite_host_unix.get_text() == '-10%\n5.00'
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '4,50\nруб.\nза мес'

        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period6m_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.is_visible()
        assert page.textseal_tarif_lite_host_unix.get_text() == '-5%\n5.00'
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '4,75\nруб.\nза мес'

        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period3m_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.get_text() == ''
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '5,00\nруб.\nза мес'

        page.btn_tarif_period_lite_host_unix.click()
        page.btn_tarif_period1m_lite_host_unix.click()
        assert page.textseal_tarif_lite_host_unix.get_text() == ''
        assert page.price_tarif_lite_host_unix.is_visible()
        assert page.price_tarif_lite_host_unix.get_text() == '5,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа СТАНДАРТ')
def test_check_tarif_standart(web_browser):
    """ Убеждаемся, что элементы блока тарифа СТАНДАРТ отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        stand_tariftext = page.text_tarif_stand_name_host_unix
        assert stand_tariftext.is_visible()
        assert stand_tariftext.get_text() == 'Стандарт'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        stand_tariftextsmall = page.textsmall_tarif_stand_host_unix
        assert stand_tariftextsmall.is_visible()
        assert stand_tariftextsmall.get_text() == 'Рекомендован для корпоративных сайтов и блогов'

    with allure.step('Проверка отображения блока со скидкой'):
        stand_tarifseal = page.textseal_tarif_stand_host_unix
        assert stand_tarifseal.is_visible()
        assert stand_tarifseal.get_text() == '-20%\n15.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_stand_host_unix
        assert price.is_visible()
        assert price.get_text() == '12,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_stand_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_stand_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.btn_tarif_select_stand_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()

    with allure.step('Проверка отображения и кликабельности'
                     ' кнопки выбора тарифа бесплатно (на 14 дней)'):
        btn_tarif_selectfree = page.btn_tarif_selectfree_stand_host_unix
        assert btn_tarif_selectfree.is_visible()
        assert btn_tarif_selectfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа СТАНДАРТ')
def test_check_tarif_standart_price(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа СТАНДАРТ
     кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка  кикабельности и изменении периода аренды'):
        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period3y_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.is_visible()
        assert page.textseal_tarif_stand_host_unix.get_text() == '-20%\n15.00'
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '12,00\nруб.\nза мес'

        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period2y_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.is_visible()
        assert page.textseal_tarif_stand_host_unix.get_text() == '-15%\n15.00'
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '12,75\nруб.\nза мес'

        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period1y_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.is_visible()
        assert page.textseal_tarif_stand_host_unix.get_text() == '-10%\n15.00'
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '13,50\nруб.\nза мес'

        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period6m_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.is_visible()
        assert page.textseal_tarif_stand_host_unix.get_text() == '-5%\n15.00'
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '14,25\nруб.\nза мес'

        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period3m_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.get_text() == ''
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '15,00\nруб.\nза мес'

        page.btn_tarif_period_stand_host_unix.click()
        page.btn_tarif_period1m_stand_host_unix.click()
        assert page.textseal_tarif_stand_host_unix.get_text() == ''
        assert page.price_tarif_stand_host_unix.is_visible()
        assert page.price_tarif_stand_host_unix.get_text() == '15,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа АКТУАЛЬНЫЙ')
def test_check_tarif_actual(web_browser):
    """ Убеждаемся, что элементы блока тарифа АКТУАЛЬНЫЙ отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        actual_tariftext = page.text_tarif_actual_name_host_unix
        assert actual_tariftext.is_visible()
        assert actual_tariftext.get_text() == 'Актуальный*'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        actual_tariftextsmall = page.textsmall_tarif_actual_name_host_unix
        assert actual_tariftextsmall.is_visible()
        assert actual_tariftextsmall.get_text() == 'Универсальный тариф для малого' \
                                                   ' бизнеса. Оплата ежемесячно по карте'

    with allure.step('Проверка отображения блока со скидкой'):
        actual_tarifseal = page.textseal_tarif_actual_host_unix
        assert actual_tarifseal.is_visible()
        assert actual_tarifseal.get_text() == '-50%\n20.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_actual_host_unix
        assert price.is_visible()
        assert price.get_text() == '10,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_actual_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_actual_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.description_tarif_actual_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа АКТУАЛЬНЫЙ')
def test_check_tarif_actual_price(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа АКТУАЛЬНЫЙ
     кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка проверка кикабельности и изменении периода аренды'):
        page.btn_tarif_period_actual_host_unix.click()
        page.btn_tarif_period1m_actual_host_unix.click()
        assert page.textseal_tarif_actual_host_unix.is_visible()
        assert page.textseal_tarif_actual_host_unix.get_text() == '-50%\n20.00'
        assert page.price_tarif_actual_host_unix.is_visible()
        assert page.price_tarif_actual_host_unix.get_text() == '10,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа ОПТИМА')
def test_check_tarif_optima(web_browser):
    """ Убеждаемся, что элементы блока тарифа ОПТИМА отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        optima_tariftext = page.text_tarif_optima_name_host_unix
        assert optima_tariftext.is_visible()
        assert optima_tariftext.get_text() == 'Оптима'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        optima_tariftextsmall = page.textsmall_tarif_optima_name_host_unix
        assert optima_tariftextsmall.is_visible()
        assert optima_tariftextsmall.get_text() == 'Идеален для большинства сайтов' \
                                                   ' и интернет-магазинов'

    with allure.step('Проверка отображения блока со скидкой'):
        optima_tarifseal = page.textseal_tarif_optima_host_unix
        assert optima_tarifseal.is_visible()
        assert optima_tarifseal.get_text() == '-20%\n20.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_optima_host_unix
        assert price.is_visible()
        assert price.get_text() == '16,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_optima_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_optima_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.btn_tarif_select_optima_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()

    with allure.step('Проверка отображения и кликабельности кнопки выбора'
                     ' тарифа бесплатно (на 14 дней)'):
        btn_tarif_selectfree = page.btn_tarif_selectfree_optima_host_unix
        assert btn_tarif_selectfree.is_visible()
        assert btn_tarif_selectfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа ОПТИМА')
def test_check_tarif_optima_price(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа ОПТИМА
     кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка  кикабельности и изменении периода аренды'):
        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period3y_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.is_visible()
        assert page.textseal_tarif_optima_host_unix.get_text() == '-20%\n20.00'
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '16,00\nруб.\nза мес'

        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period2y_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.is_visible()
        assert page.textseal_tarif_optima_host_unix.get_text() == '-15%\n20.00'
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '17,00\nруб.\nза мес'

        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period1y_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.is_visible()
        assert page.textseal_tarif_optima_host_unix.get_text() == '-10%\n20.00'
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '18,00\nруб.\nза мес'

        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period6m_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.is_visible()
        assert page.textseal_tarif_optima_host_unix.get_text() == '-5%\n20.00'
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '19,00\nруб.\nза мес'

        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period3m_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.get_text() == ''
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '20,00\nруб.\nза мес'

        page.btn_tarif_period_optima_host_unix.click()
        page.btn_tarif_period1m_optima_host_unix.click()
        assert page.textseal_tarif_optima_host_unix.get_text() == ''
        assert page.price_tarif_optima_host_unix.is_visible()
        assert page.price_tarif_optima_host_unix.get_text() == '20,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа ПРОФИ')
def test_check_tarif_profi(web_browser):
    """ Убеждаемся, что элементы блока тарифа ПРОФИ отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        tariftext = page.text_tarif_profi_name_host_unix
        assert tariftext.is_visible()
        assert tariftext.get_text() == 'Профи'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        tariftextsmall = page.textsmall_tarif_profi_name_host_unix
        assert tariftextsmall.is_visible()
        assert tariftextsmall.get_text() == 'Расширенный тариф для веб-студий' \
                                            ' и нагруженных проектов'

    with allure.step('Проверка отображения блока со скидкой'):
        tarifseal = page.textseal_tarif_profi_host_unix
        assert tarifseal.is_visible()
        assert tarifseal.get_text() == '-20%\n35.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_profi_host_unix
        assert price.is_visible()
        assert price.get_text() == '28,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_profi_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_profi_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.btn_tarif_select_profi_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()

    with allure.step('Проверка отображения и кликабельности кнопки выбора'
                     ' тарифа бесплатно (на 14 дней)'):
        btn_tarif_selectfree = page.btn_tarif_selectfree_profi_host_unix
        assert btn_tarif_selectfree.is_visible()
        assert btn_tarif_selectfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа ПРОФИ')
def test_check_tarif_profi_price(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа ПРОФИ
     кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка кикабельности и изменении периода аренды'):
        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period3y_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.is_visible()
        assert page.textseal_tarif_profi_host_unix.get_text() == '-20%\n35.00'
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '28,00\nруб.\nза мес'

        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period2y_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.is_visible()
        assert page.textseal_tarif_profi_host_unix.get_text() == '-15%\n35.00'
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '29,75\nруб.\nза мес'

        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period1y_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.is_visible()
        assert page.textseal_tarif_profi_host_unix.get_text() == '-10%\n35.00'
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '31,50\nруб.\nза мес'

        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period6m_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.is_visible()
        assert page.textseal_tarif_profi_host_unix.get_text() == '-5%\n35.00'
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '33,25\nруб.\nза мес'

        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period3m_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.get_text() == ''
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '35,00\nруб.\nза мес'

        page.btn_tarif_period_profi_host_unix.click()
        page.btn_tarif_period1m_profi_host_unix.click()
        assert page.textseal_tarif_profi_host_unix.get_text() == ''
        assert page.price_tarif_profi_host_unix.is_visible()
        assert page.price_tarif_profi_host_unix.get_text() == '35,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока тарифа МАКСИМА')
def test_check_tarif_maxima(web_browser):
    """ Убеждаемся, что элементы блока тарифа МАКСИМА отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения заглавного текста (имя тарифа)'):
        tariftext = page.text_tarif_maxima_name_host_unix
        assert tariftext.is_visible()
        assert tariftext.get_text() == 'Максима'

    with allure.step('Проверка отображения поддекста имени тарифа'):
        tariftextsmall = page.textsmall_tarif_maxima_name_host_unix
        assert tariftextsmall.is_visible()
        assert tariftextsmall.get_text() == 'Расширенный тариф для веб-студий' \
                                            ' и нагруженных проектов'

    with allure.step('Проверка отображения блока со скидкой'):
        tarifseal = page.textseal_tarif_maxima_name_host_unix
        assert tarifseal.is_visible()
        assert tarifseal.get_text() == '-20%\n50.00'

    with allure.step('Проверка отображения цены'):
        price = page.price_tarif_maxima_name_host_unix
        assert price.is_visible()
        assert price.get_text() == '40,00\nруб.\nза мес'

    with allure.step('Проверка отображения кнопки выбора периода аренды тарифа'):
        btn_period = page.btn_tarif_period_maxima_host_unix
        assert btn_period.is_visible()
        assert btn_period.is_clickable()

    with allure.step('Проверка отображения описания тарифа/состав'):
        description_tarif = page.description_tarif_maxima_host_unix
        assert description_tarif.is_visible()

    with allure.step('Проверка отображения и кликабельности кнопки выбора тарифа'):
        btn_tarif_select = page.btn_tarif_select_maxima_host_unix
        assert btn_tarif_select.is_visible()
        assert btn_tarif_select.is_clickable()

    with allure.step('Проверка отображения и кликабельности кнопки выбора'
                     ' тарифа бесплатно (на 14 дней)'):
        btn_tarif_selectfree = page.btn_tarif_selectfree_maxima_host_unix
        assert btn_tarif_selectfree.is_visible()
        assert btn_tarif_selectfree.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка выбора периода аренды тарифа МАКСИМА')
def test_check_tarif_maxima_price(web_browser):
    """ Убеждаемся, что элементы периода аренды тарифа МАКСИМА
     кликабельны и цена со скидкой изменяется. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка кикабельности и изменении периода аренды'):
        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period3y_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.is_visible()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == '-20%\n50.00'
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '40,00\nруб.\nза мес'

        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period2y_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.is_visible()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == '-15%\n50.00'
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '42,50\nруб.\nза мес'

        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period1y_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.is_visible()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == '-10%\n50.00'
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '45,00\nруб.\nза мес'

        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period6m_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.is_visible()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == '-5%\n50.00'
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '47,50\nруб.\nза мес'

        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period3m_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == ''
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '50,00\nруб.\nза мес'

        page.btn_tarif_period_maxima_host_unix.click()
        page.btn_tarif_period1m_maxima_host_unix.click()
        assert page.textseal_tarif_maxima_name_host_unix.get_text() == ''
        assert page.price_tarif_maxima_name_host_unix.is_visible()
        assert page.price_tarif_maxima_name_host_unix.get_text() == '50,00\nруб.\nза мес'


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока В КАЖДОМ ТАРИФЕ ЕСТЬ')
def test_check_section_tariffhas(web_browser):
    """ Убеждаемся, что элементы блока 'В КАЖДОМ ТАРИФЕ ЕСТЬ' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    # Раздел "Конструктор сайтов"
    with allure.step('Проверка отображения картинки плитки "Конструктор сайтов"'):
        img1_tariffhas = page.img1_tariffhas_host_unix
        if img1_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "Конструктор сайтов"'):
        text1_tariffhas = page.text1_tariffhas_host_unix
        if text1_tariffhas.get_text() == 'Конструктор сайтов':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               text1_tariffhas.highlight_and_make_screenshot())

            allure.attach('Текст не верный', name="ERROR!!!")

        if text1_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки'
                     ' "Конструктор сайтов"'):
        textdescription1_tariffhas = page.textdescription1_tariffhas_host_unix
        if textdescription1_tariffhas.get_text() == 'Сделайте сайт самостоятельно уже сегодня.' \
                                                    ' Не потратив ни копейки на дизайнеров' \
                                                    ' и программистов.' \
                                                    ' 200+ шаблонов для любого проекта':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               textdescription1_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription1_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    # Раздел "Бесплатный SSL-сертификат"
    with allure.step('Проверка отображения картинки плитки "Бесплатный SSL-сертификат"'):
        img2_tariffhas = page.img2_tariffhas_host_unix
        if img2_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "Бесплатный SSL-сертификат"'):
        text2_tariffhas = page.text2_tariffhas_host_unix
        if text2_tariffhas.get_text() == 'Бесплатный SSL-сертификат':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               text2_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if text2_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки'
                     ' "Бесплатный SSL-сертификат"'):
        textdescription2_tariffhas = page.textdescription2_tariffhas_host_unix
        if textdescription2_tariffhas.get_text() == 'Повышайте доверие пользователей' \
                                                    ' сайта и увеличивайте конверсию' \
                                                    ' с помощью включенного SSL-сертификата.' \
                                                    ' Продлевается автоматически':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               textdescription2_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription2_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    # Раздел "Почта уровня Pro"
    with allure.step('Проверка отображения картинки плитки "Почта уровня Pro"'):
        img3_tariffhas = page.img3_tariffhas_host_unix
        if img3_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "Почта уровня Pro"'):
        text3_tariffhas = page.text3_tariffhas_host_unix
        if text3_tariffhas.get_text() == 'Почта уровня Pro':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               text3_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if text3_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки "Почта уровня Pro"'):
        textdescription3_tariffhas = page.textdescription3_tariffhas_host_unix
        if textdescription3_tariffhas.get_text() == 'Получите почту в собственном домене' \
                                                    ' (например, info@yourdomain.by).' \
                                                    ' Неограниченное число почтовых ящиков.' \
                                                    ' Доступ к почте через смартфон':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               textdescription3_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription3_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    # Раздел "14 дней бесплатно"
    with allure.step('Проверка отображения картинки плитки "14 дней бесплатно"'):
        img4_tariffhas = page.img4_tariffhas_host_unix
        if img4_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "14 дней бесплатно"'):
        text4_tariffhas = page.text4_tariffhas_host_unix
        if text4_tariffhas.get_text() == '14 дней бесплатно':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach.file('/Users/maksimcybulko/Desktop/diplom/element.png',
                               text4_tariffhas.highlight_and_make_screenshot())
            allure.attach('Текст не верный', name="ERROR!!!")

        if text4_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки'
                     ' "14 дней бесплатно"'):
        textdescription4_tariffhas = page.textdescription4_tariffhas_host_unix
        if textdescription4_tariffhas.get_text() == 'Получите полный доступ ко' \
                                                    ' всем возможностям наших тарифов' \
                                                    ' на 14 дней бесплатно':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription4_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    # Раздел "Техподдержка 24/7"
    with allure.step('Проверка отображения картинки плитки "Техподдержка 24/7"'):
        img5_tariffhas = page.img5_tariffhas_host_unix
        if img5_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "Техподдержка 24/7"'):
        text5_tariffhas = page.text5_tariffhas_host_unix
        if text5_tariffhas.get_text() == 'Техподдержка 24/7':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        if text5_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки'
                     ' "Техподдержка 24/7"'):
        textdescription5_tariffhas = page.textdescription5_tariffhas_host_unix
        if textdescription5_tariffhas.get_text() == 'Даже в выходные дни или новогоднюю' \
                                                    ' ночь с вами будут работать' \
                                                    ' высококлассные инженеры':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription5_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    # Раздел "BackUp-менеджер"
    with allure.step('Проверка отображения картинки плитки "BackUp-менеджер"'):
        img6_tariffhas = page.img6_tariffhas_host_unix
        if img6_tariffhas.is_visible():
            allure.attach('Картинка отображается на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и написания заглавного текста плитки'
                     ' "BackUp-менеджер"'):
        text6_tariffhas = page.text5_tariffhas_host_unix
        if text6_tariffhas.get_text() == 'BackUp-менеджер':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        if text6_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")

    with allure.step('Проверка отображения и написания описания текста плитки'
                     ' "BackUp-менеджер"'):
        textdescription6_tariffhas = page.textdescription5_tariffhas_host_unix
        if textdescription6_tariffhas.get_text() == 'Даже в выходные дни или новогоднюю' \
                                                    ' ночь с вами будут работать' \
                                                    ' высококлассные инженеры':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        if textdescription6_tariffhas.is_visible():
            allure.attach('Текст отображается на экарне', name="PASS")
        else:
            allure.attach('Текста нет на экарне', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока УПОР НА БЕЗОПАСНОСТЬ')
def test_check_section_security(web_browser):
    """ Убеждаемся, что элементы блока 'УПОР НА БЕЗОПАСНОСТЬ' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        texthead_security = page.texthead_security
        if texthead_security.is_visible():
            allure.attach('Текст отображается на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if texthead_security.get_text() == 'Упор на безопасность':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения картинки блока'):
        img_security = page.img_security
        if img_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

    # Блок "Проактивная защита"
    with allure.step('Проверка отображения текста раздела "Проактивная защита" '):
        text1_security = page.text1_security
        if text1_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if text1_security.get_text() == 'Проактивная защита':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения текста описания раздела "Проактивная защита" '):
        textdescription1_security = page.textdescription1_security
        if textdescription1_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if textdescription1_security.get_text() == 'Ваши сайты под защитой системы,' \
                                                   ' которая предотвращает заражения и взломы,' \
                                                   ' а не просто информирует вас об угрозе':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    # Блок "Защита от DDoS-атак"
    with allure.step('Проверка отображения текста раздела "Защита от DDoS-атак" '):
        text2_security = page.text2_security
        if text2_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if text2_security.get_text() == 'Защита от DDoS-атак':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения текста описания раздела "Защита от DDoS-атак"'):
        textdescription2_security = page.textdescription2_security
        if textdescription2_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if textdescription2_security.get_text() == 'Предотвращение DDoS и сетевых' \
                                                   ' атак на уровне дата-центра':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    # Блок "Сохранность копий сайта"
    with allure.step('Проверка отображения текста раздела "Сохранность копий сайта"'):
        text3_security = page.text3_security
        if text3_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if text3_security.get_text() == 'Защита от DDoS-атак':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения текста описания раздела "Сохранность копий сайта"'):
        textdescription3_security = page.textdescription3_security
        if textdescription3_security.is_visible():
            allure.attach('Картинка на экарне', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")

        if textdescription3_security.get_text() == 'Предотвращение DDoS и сетевых' \
                                                   ' атак на уровне дата-центра':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока 450+ ПРИЛОЖЕНИЙ И CMS')
def test_check_section_cms450(web_browser):
    """ Убеждаемся, что элементы блока '450+ ПРИЛОЖЕНИЙ И CMS' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        texthead_450cms = page.texthead_450cms
        if texthead_450cms.is_visible():
            allure.attach('Текст отображается на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if texthead_450cms.get_text() == '450+\nприложений и CMS':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности текста описания'):
        textdescription_450cms = page.textdescription_450cms
        if textdescription_450cms.is_visible():
            allure.attach('Текст отображается на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if textdescription_450cms.get_text() == 'Бесплатно. Моментальная' \
                                                ' установка.\nАвтоматические обновления':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности текста рекламы'):
        textadvertising_450cms = page.textadvertising_450cms
        if textadvertising_450cms.is_visible():
            allure.attach('Текст отображается на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if textadvertising_450cms.get_text() == 'Откройте автоустановщик Softaculous' \
                                                ' и легко разверните любое приложение':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности текста рекламы'):
        img = page.img_450cms
        if img.is_visible():
            allure.attach('Картинка на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока СЛАЙДЕРА')
def test_check_section_slider(web_browser):
    """ Убеждаемся, что элементы блока 'СЛАЙДЕРА' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и кликабельности кнопки слайдера'):
        btn_slider = page.btn_slider
        assert btn_slider.is_visible()
        assert btn_slider.is_clickable()


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока У НАС ЕСТЬ УНИКАЛЬНЫЕ РЕШЕНИЯ')
def test_check_section_unique_solutions(web_browser):
    """ Убеждаемся, что элементы блока 'У НАС ЕСТЬ УНИКАЛЬНЫЕ РЕШЕНИЯ'
     отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        text = page.text_unique_solutions
        if text.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if text.get_text() == 'У нас есть уникальные решения':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения картинок плиток раздела'):
        img1 = page.img1_unique_solutions
        img2 = page.img2_unique_solutions
        img3 = page.img3_unique_solutions
        img4 = page.img4_unique_solutions
        if img1.is_visible():
            allure.attach('Картинка1 на экране', name="PASS")
        else:
            allure.attach('Картинка1 нет на экране', name="ERROR!!!")

        if img2.is_visible():
            allure.attach('Картинка2 на экране', name="PASS")
        else:
            allure.attach('Картинка2 нет на экране', name="ERROR!!!")

        if img3.is_visible():
            allure.attach('Картинка3 на экране', name="PASS")
        else:
            allure.attach('Картинка3 нет на экране', name="ERROR!!!")

        if img4.is_visible():
            allure.attach('Картинка4 на экране', name="PASS")
        else:
            allure.attach('Картинка4 нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения текст описания'):
        description1 = page.description1_unique_solutions
        if description1.is_visible():
            allure.attach('Текст1 на экране', name="PASS")
        else:
            allure.attach('Текста1 нет на экране', name="ERROR!!!")

        if description1.get_text() == 'Хостинг для CMS Wordpress для высокой' \
                                      ' скорости работы сайта':
            allure.attach('Текст1 на экране', name="PASS")
        else:
            allure.attach('Текста1 нет на экране', name="ERROR!!!")

        description2 = page.description2_unique_solutions
        if description2.is_visible():
            allure.attach('Текст2 на экране', name="PASS")
        else:
            allure.attach('Текста2 нет на экране', name="ERROR!!!")

        if description2.get_text() == 'Хостинг для CMS Joomla. Повышенная мощность для сайта':
            allure.attach('Текст2 на экране', name="PASS")
        else:
            allure.attach('Текста2 нет на экране', name="ERROR!!!")

        description3 = page.description3_unique_solutions
        if description3.is_visible():
            allure.attach('Текст3 на экране', name="PASS")
        else:
            allure.attach('Текста3 нет на экране', name="ERROR!!!")

        if description3.get_text() == 'Хостинг для CMS Битрикс с производительностью' \
                                      ' выше требуемой самим Битриксом':
            allure.attach('Текст3 на экране', name="PASS")
        else:
            allure.attach('Текста3 нет на экране', name="ERROR!!!")

        description4 = page.description4_unique_solutions
        if description4.is_visible():
            allure.attach('Текст4 на экране', name="PASS")
        else:
            allure.attach('Текста4 нет на экране', name="ERROR!!!")

        if description4.get_text() == 'Хостинг для CMS Drupal. Специальные' \
                                      ' настройки сервера для работы сайта':
            allure.attach('Текст4 на экране', name="PASS")
        else:
            allure.attach('Текста4 нет на экране', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока ВАШ САЙТ У ДРУГОГО ПРОВАЙДЕРА?')
def test_check_section_another_provider(web_browser):
    """ Убеждаемся, что элементы блока 'ВАШ САЙТ У ДРУГОГО ПРОВАЙДЕРА?'
     отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        text_another_provider = page.text_another_provider
        if text_another_provider.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if text_another_provider.get_text() == 'Ваш сайт у другого провайдера?':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности текста описания'):
        description_another_provider = page.description_another_provider
        if description_another_provider.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if description_another_provider.get_text() == 'Бесплатно перенесем его в hoster.by!\n\n' \
                                                      'Все сделаем сами: от подбора' \
                                                      ' тарифа до миграции сайта.' \
                                                      ' Обеспечим бесшовный перенос без' \
                                                      ' простоя для бизнеса.':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и кликабельности кнопки'):
        btn_another_provider = page.btn_another_provider
        if btn_another_provider.is_visible():
            allure.attach('Кнопка на экране', name="PASS")
        else:
            allure.attach('Кнопки нет на экране', name="ERROR!!!")

        if btn_another_provider.is_clickable():
            allure.attach('Кнопка кликабельна', name="PASS")
        else:
            allure.attach('Кнопка не кликабельна', name="ERROR!!!")

    with allure.step('Проверка отображения картинки'):
        img_another_provider = page.img_another_provider
        if img_another_provider.is_visible():
            allure.attach('Картинка на экране', name="PASS")
        else:
            allure.attach('Картинки нет на экране', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока ЕЩЕ БОЛЬШЕ ПРЕИМУЩЕСТВ')
def test_check_section_advantage(web_browser):
    """ Убеждаемся, что элементы блока 'ЕЩЕ БОЛЬШЕ ПРЕИМУЩЕСТВ' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        text_head_advantage = page.text_head_advantage
        if text_head_advantage.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if text_head_advantage.get_text() == 'Еще больше преимуществ':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения, кликабельность и описание разделов'):
        section_advantagetth = page.section_advantagetth
        # Проверка отображения
        if section_advantagetth.is_visible():
            allure.attach('Раздел на экране', name="PASS")
        else:
            allure.attach('Раздела нет на экране', name="ERROR!!!")

        section_advantageprog = page.section_advantageprog
        if section_advantageprog.is_visible():
            allure.attach('Раздел на экране', name="PASS")
        else:
            allure.attach('Раздела нет на экране', name="ERROR!!!")

        # Проверка кликабелности
        description_advantagetth = page.description_advantagetth
        description_advantageprog = page.description_advantageprog
        page.description_advantagetth.click()
        if description_advantagetth.get_text() == description_advantagetth.get_text():
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        page.section_advantageprog.click()
        if description_advantageprog.get_text() == description_advantageprog.get_text():
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")


@allure.feature('Тест страницы хостинга Unix')
@allure.story('Проверка элементов блока ВОПРОС-ОТВЕТ')
def test_check_section_qa_unix(web_browser):
    """ Убеждаемся, что элементы блока 'ВОПРОС-ОТВЕТ' отображаются на странице. """

    page = HostingUnixPage(web_browser)

    page.btn_pop_up.click()

    with allure.step('Проверка отображения и правильности заглавного текста'):
        text_head_qa = page.text_head_qa
        if text_head_qa.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if text_head_qa.get_text() == 'Вопрос-ответ':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности вопроса и ответа 1'):
        question1 = page.q1
        if question1.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if question1.get_text() == 'Как перенести сайт в hoster.by?':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        page.q1.click()
        time.sleep(1)
        if page.a1.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности вопроса и ответа 2'):
        question2 = page.q2
        if question2.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if question2.get_text() == 'Можно ли протестировать хостинг бесплатно?':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        page.q2.click()
        time.sleep(1)
        if page.a2.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности вопроса и ответа 3'):
        question3 = page.q3
        if question3.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if question3.get_text() == 'Как настроить бесплатный SSL-сертификат?':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        page.q3.click()
        time.sleep(1)
        if page.a3.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

    with allure.step('Проверка отображения и правильности вопроса и ответа 4'):
        question4 = page.q4
        if question4.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")

        if question4.get_text() == 'Как настроить DNS-записи hoster.by?':
            allure.attach('Текст верный', name="PASS")
        else:
            allure.attach('Текст не верный', name="ERROR!!!")

        page.q4.click()
        time.sleep(1)
        if page.a4.is_visible():
            allure.attach('Текст на экране', name="PASS")
        else:
            allure.attach('Текста нет на экране', name="ERROR!!!")
