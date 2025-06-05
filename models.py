from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(Integer, primary_key=True)
    vehicle_number = Column(String, primary_key=False)
    vehicle_type = Column(String, primary_key=False)
    owner_name = Column(String, primary_key=False)


class TrafficOfficers(Base):
    __tablename__ = 'traffic_officers'
    officer_id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    badge_number = Column(String, primary_key=False)
    station = Column(String, primary_key=False)


class TrafficSignals(Base):
    __tablename__ = 'traffic_signals'
    signal_id = Column(Integer, primary_key=True)
    location = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    last_maintenance = Column(Date, primary_key=False)


class Violations(Base):
    __tablename__ = 'violations'
    violation_id = Column(Integer, primary_key=True)
    vehicle_number = Column(String, primary_key=False)
    officer_badge = Column(String, primary_key=False)
    violation_type = Column(String, primary_key=False)
    fine_amount = Column(String, primary_key=False)
    violation_date = Column(Date, primary_key=False)


class Payments(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    violation_id = Column(Integer, primary_key=False)
    amount_paid = Column(String, primary_key=False)
    payment_date = Column(Date, primary_key=False)
    payment_method = Column(String, primary_key=False)


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)


