import allure

from pages.registration_page import FormPage


@allure.title("Заполнение формы DemoQA")
def test_practice_form(setup_browser):
    browser = setup_browser
    form = FormPage(browser)

    with allure.step("Открываем страницу"):
        form.open()

    with allure.step("Заполняем имя и фамилию"):
        form.fill_last_name("Doe")
        form.fill_first_name("John")

    with allure.step("Вводим email"):
        form.fill_email('john.doe@example.com')

    with allure.step("Выбираем пол"):
        form.select_gender("male")
    
    with allure.step("Вводим номер телефона"):
        form.fill_mobile('1234567890')

    with allure.step("Отправляем форму"):
        form.submit()
