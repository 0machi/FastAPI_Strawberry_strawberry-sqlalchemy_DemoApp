import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class Country(MappedAsDataclass, Base):
    __tablename__ = "countries"

    country_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    country_name: Mapped[str] = mapped_column(String(100), nullable=False)

    cities: Mapped[list["City"]] = relationship(backref="cities")


class City(MappedAsDataclass, Base):
    __tablename__ = "cities"

    city_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.country_id"))
    city_name: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)


class Users(MappedAsDataclass, Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    encrypted_password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
