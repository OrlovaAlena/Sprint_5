from selenium.webdriver.common.by import By


class Elements:
    SIGN_IN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    MAKE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"
    CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"
    LOGO = By.XPATH, './/div[contains(@class, "header__logo")]'

    CREATE_ACCOUNT_BUTTON = By.CSS_SELECTOR, "a[href = '/register'"
    COMPLETE_BUTTON = By.XPATH, ".//form/button[text() = 'Зарегистрироваться']"
    CONFIRM_LOGIN_BUTTON = By.XPATH, ".//form/button[text() = 'Войти']"
    LOG_IN_BUTTON = By.CSS_SELECTOR, "a[href = '/login'"
    PASSWORD_BUTTON = By.CSS_SELECTOR, "a[href = '/forgot-password'"

    USERNAME_INPUT = By.XPATH, ".//div[label[text()='Имя']]/input"
    EMAIL_INPUT = By.XPATH, ".//div[label[text()='Email']]/input"
    PASSWORD_INPUT = By.NAME, 'Пароль'
    ENTER_SIGN = By.XPATH, ".//h2[text()='Вход']"
    INPUT_ERROR_MASSAGE = By.XPATH, ".//p[contains(@class, 'input__error')]"

    PROFILE_BUTTON = By.XPATH, ".//a[text()='Профиль']"
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"

    SAUCES_TAB = By.XPATH, ".//span[text()='Соусы']/parent::div"
    BUNS_TAB = By.XPATH, ".//span[text()='Булки']/parent::div"
    FILLINGS_TAB = By.XPATH, ".//span[text()='Начинки']/parent::div"
