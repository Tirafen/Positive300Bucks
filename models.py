from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
import uuid


class User(Base):  # Таблица со списком пользователей
    __tablename__ = "clients"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    orders = relationship("Orders", back_populates="owner")


class Orders(Base):  # Таблица заказов
    __tablename__ = "orders"
    owner_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), default=uuid.uuid4, primary_key=True)
    coffee_type = Column(String)
    order_number = Column(Integer)
    ready = Column(Boolean)
    wait = Column(Boolean)
    in_progress = Column(Boolean)

    owner = relationship("User", back_populates="orders")
