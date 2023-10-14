from typing import List
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from aiohttp import ClientSession, ClientTimeout
from database import save_product
import config
from concurrent.futures import ThreadPoolExecutor


async def fetch_product_info(session: ClientSession, url: str, executor: ThreadPoolExecutor):
    """
    Получает информацию о продуктах с заданной страницы.

    Args:
        session (ClientSession): Сессия aiohttp.
        url (str): URL страницы для сканирования.
        executor (ThreadPoolExecutor): Пул потоков для выполнения задач.

    Returns:
        None
    """
    driver = webdriver.Chrome()
    driver.get(url)
    await asyncio.sleep(2)  # Дайте странице время для загрузки (по вашим потребностям)

    # Найдите все ссылки, начинающиеся с /product/
    product_links = driver.find_elements(By.XPATH, '//a[starts-with(@href, "/product/")]')

    for link in product_links:
        product_name_element = link.find_element(By.XPATH, './/div[contains(@class, "ProductCard_name__czrVx")]/span')
        product_name = product_name_element.text if product_name_element else "N/A"
        product_url = link.get_attribute("href")

        print(f"Product Name: {product_name}")
        print(f"Product URL: {product_url}")
        # Сохраните продукт в базе данных
        save_product(product_name, product_url)

    driver.quit()


async def scrape_products_in_categories():
    """
    Сканирует продукты в заданных категориях и сохраняет информацию в базе данных.
    """
    async with ClientSession(timeout=ClientTimeout(total=10)) as session:
        with ThreadPoolExecutor(max_workers=5) as executor:
            tasks = [fetch_product_info(session, url, executor) for url in config.category_urls]
            await asyncio.gather(*tasks)
