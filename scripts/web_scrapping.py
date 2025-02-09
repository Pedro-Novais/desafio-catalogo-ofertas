import sys
import sqlite3
import os
import time

from sqlite3 import Connection

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebElement

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.edge.options import Options


def main() -> None:
    try:
        conn = create_database()

        products = scrapping()

        insert_data_in_database(
            conn=conn,
            products=products
        )

    except Exception as e:
        print('Erro ao realizar o web scrapping, erro: {}'.format(e))
        sys.exit()

def create_database() -> Connection:
    dir_script = os.path.dirname(os.path.abspath(__file__))
    dir_database = os.path.join(dir_script, '..', 'database', 'data.db')

    conn = sqlite3.connect(dir_database)

    cursor = conn.cursor()

    msg_create_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        price_full VARCHAR(255),
        installments VARCHAR(255) NOT NULL,
        link VARCHAR(255) NOT NULL,
        price_final VARCHAR(255),
        porcentage_discount VARCHAR(255),
        type_ship VARCHAR(255),
        ship_free VARCHAR(255),
        image VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(msg_create_table)

    msg_delete_datas = "DELETE FROM products"
    cursor.execute(msg_delete_datas)

    conn.commit()
    cursor.close()

    return conn
     
def scrapping() -> list[dict]:

    URL = "https://lista.mercadolivre.com.br/computador-gamer-i7-16gb-ssd-1tb"

    driver = get_driver()
    driver.get(URL)

    scroll_pause_time = 1
    scroll_step = 1000  
    last_height = 0

    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_step});") 
        time.sleep(scroll_pause_time)

        new_height = driver.execute_script("return window.scrollY")
        if new_height + scroll_step >= 15000 or new_height == last_height:
            break

        last_height = new_height

    products = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-search-layout__item"))
    )

    items = get_datas(products=products)

    return items

def get_driver():

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    except WebDriverException:
        pass

    try:
        options = Options()
        options.add_argument("--headless")  
        options.add_argument("--disable-gpu")  
        options.add_argument("--no-sandbox") 
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        return driver
    except WebDriverException:
        pass

    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        return driver
    except WebDriverException:
        pass

    print("Falha ao inicializar o WebDriver.")
    raise Exception("Impossibilidade de inicializar Web Driver")

def get_datas(
        products: list[WebElement]
        ) -> list[dict]:
    
    list_products = []

    for product in products[:50]:

        try:
            image = product.find_element(By.CSS_SELECTOR, ".poly-component__picture")
            src_image = image.get_attribute("src")

            title = product.find_element(By.CSS_SELECTOR, ".poly-component__title")
            tile_name = title.text

            options_installments = product.find_element(By.CSS_SELECTOR, ".poly-price__installments").text

            product_link = title.get_attribute("href")

            prices = product.find_elements(By.CSS_SELECTOR, ".andes-money-amount__fraction")
            price_full = prices[0].text
            if len(prices) > 2:
                price_with_dicount = prices[1].text
            else:
                price_with_dicount = None

            try:
                discount_porcentage = product.find_element(By.CSS_SELECTOR, ".andes-money-amount__discount").text
            except Exception as e:
                discount_porcentage = None

            try:
                type_ship = product.find_element(By.CSS_SELECTOR, ".poly-component__shipped-from").text
            except Exception as e:
                type_ship = None
            
            try:
                free_ship = product.find_element(By.CSS_SELECTOR, ".poly-component__shipping").text
            except Exception as e:
                free_ship = None

            data = parse_datas(
                image=src_image,
                name=tile_name,
                price_full=price_full,
                installments=options_installments,
                link=product_link,
                price_with_discount=price_with_dicount,
                porcentage_disocunt=discount_porcentage,
                type_ship=type_ship ,
                ship_free=free_ship
            )
            
            list_products.append(data)

        except Exception as e:
            print(f"Erro ao coletar um produto: {e}")
            pass
    
    return list_products

def parse_datas(
        image: str,
        name: str,
        price_full: str,
        installments: str,
        link: str,
        price_with_discount: str,
        porcentage_disocunt: str,
        type_ship: str,
        ship_free: str,
    )-> dict:
    
    data = {
        "image": image,
        "name": name,
        "price_full": price_full,
        "installments": installments,
        "link": link,
        "price_with_discount": price_with_discount,
        "porcentage_discount": porcentage_disocunt,
        "type_ship_full": True if type_ship else False,
        "ship_free": ship_free
    }

    return data

def insert_data_in_database(conn: Connection, products: list[dict]) -> None:
    cursor = conn.cursor()

    for product in products:
        msg_insert = """
        INSERT INTO products
        (name, price_full, installments, link, price_final, porcentage_discount, type_ship, ship_free, image)
        VALUES (?,?,?,?,?,?,?,?, ?)
        """

        cursor.execute(
            msg_insert,
            (
                product.get('name'),
                product.get('price_full'),
                product.get('installments'),
                product.get('link'),
                product.get('price_with_discount'),
                product.get('porcentage_discount'),
                product.get('type_ship_full'),
                product.get('ship_free'),
                product.get('image')
            )
            )
        
    conn.commit()
    cursor.close()
    conn.close()

if "__main__" == __name__:
    main()