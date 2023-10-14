from typing import List, Dict

db_config: Dict[str, str] = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'db',
    'port': '5432',
}

# Создайте строку подключения
db_config['connection_string'] = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"


category_urls: List[str] = [
    "https://web.samokat.ru/category/hleb-i-vypechka-vypechka",
    'https://web.samokat.ru/category/hleb-i-vypechka-hlebcy-suhari-i-sushki'
]
