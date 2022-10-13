import time

import pytest
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_language(browser, language):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    if language == 'fr':
        time.sleep(30)
        assert button.text == 'Ajouter au panier'
    elif language == 'es':
        assert button.text == 'Añadir al carrito'
    else:
        raise pytest.UsageError("Language should be es or fr")
