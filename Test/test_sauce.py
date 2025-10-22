import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
import time


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    espera = WebDriverWait(driver,10)

    try: 
      #1. Automatización de Login:
       driver.get('https://www.saucedemo.com')
       time.sleep(1)
       driver.find_element(By.ID, 'user-name').send_keys('standard_user')
       driver.find_element(By.ID, 'password').send_keys('secret_sauce')
       time.sleep(1)
       driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
       time.sleep(2)
       espera.until(EX.visibility_of_element_located((By.CLASS_NAME, 'title')))
       assert '/inventory.html' in driver.current_url
    except Exception as exe:
        print(f"Error en datos de login: {exe}")
    finally:
        driver.quit()

def test_navegacion():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    espera = WebDriverWait(driver,10)

    try: 
        #2. Navegación y Verificación del Catálogo:
        driver.get('https://www.saucedemo.com')
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        time.sleep(2)
        primer_producto = productos[0]
        nombre = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name').text
        precio = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price').text
        print(f"Primer producto: {nombre} _ Precio: {precio}")
        
        # Validaciones de titulos
        driver.find_element(By.CSS_SELECTOR,'#header_container > div.primary_header > div.header_label > div')
        assert driver.title == "Swag Labs" 
        titulo_catalogo = driver.find_element(By.CLASS_NAME, 'title').text
        assert titulo_catalogo == "Products"
        time.sleep(1)

        # Agregar primer producto al carrito
        espera.until(EX.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item')))
        agregar_producto = driver.find_elements(By.CLASS_NAME,'inventory_item')[0]
        agregar_producto.find_element(By.TAG_NAME,'button').click()
        time.sleep(2)
        espera.until(EX.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))

        #Verificacion de carrito
        carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
        assert carrito == '1'
    except Exception as exe:
        print(f"Error en navegación o carrito: {exe}")
    finally:
        driver.quit()


