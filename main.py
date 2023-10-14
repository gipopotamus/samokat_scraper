import asyncio
from typing import List
import config
from scraper import scrape_products_in_categories
from database import create_table, save_product


async def main():
    # create_table()  # Создать таблицу в базе данных, если она еще не существует
    await scrape_products_in_categories()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
