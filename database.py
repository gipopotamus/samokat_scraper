from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import db_config

# Создаем подключение к базе данных
engine = create_engine(db_config['connection_string'])
Session = sessionmaker(bind=engine)

Base = declarative_base()


# Определяем модель данных
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)


# Создаем таблицу, если она не существует
Base.metadata.create_all(engine)


def save_product(name: str, price: str):
    # Создаем сессию
    session = Session()

    # Создаем объект Product и сохраняем его в базе данных
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()

    # Закрываем сессию
    session.close()
