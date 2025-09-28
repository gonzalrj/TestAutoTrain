# region Abstract base class
from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(ABC):
    def __init__(self, driver, base_url="https://example.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10  # default wait

    @abstractmethod
    def open(self):
        """Force subclasses to implement how the page opens"""
        pass

    @abstractmethod
    def validate(self):
        """Force subclasses to implement how the page validates"""
        pass

    # Shared utility (protected)
    def _wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )


# endregion

# region Concrete subclass: Login page
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    def open(self):
        self.driver.get(f"{self.base_url}/login")

    def validate(self):
        # Ensure login button is visible
        return self._wait_for_visibility(self.LOGIN_BUTTON)

    def login(self, username, password):
        self._wait_for_visibility(self.USERNAME_INPUT).send_keys(username)
        self._wait_for_visibility(self.PASSWORD_INPUT).send_keys(password)
        self._wait_for_visibility(self.LOGIN_BUTTON).click()


# endregion

# region Concrete subclass: Checkout page
class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkoutBtn")
    CART_ITEMS = (By.CLASS_NAME, "cart-item")

    def open(self):
        self.driver.get(f"{self.base_url}/checkout")

    def validate(self):
        # Ensure checkout button is visible
        return self._wait_for_visibility(self.CHECKOUT_BUTTON)

    def proceed_to_checkout(self):
        self._wait_for_visibility(self.CHECKOUT_BUTTON).click()


# endregion

# region Usage in Test
from selenium import webdriver

driver = webdriver.Chrome()

# Abstraction in action
pages = [LoginPage(driver), CheckoutPage(driver)]

for page in pages:
    page.open()  # "what" is consistent
    page.validate()  # each defines its own "how"

# Using LoginPage functionality
login = LoginPage(driver)
login.open()
login.validate()
login.login("testuser", "password123")

driver.quit()
# endregion
