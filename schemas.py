from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List,Optional,Field,field_validator Tuple

import re

class Vehicles(BaseModel):
    vehicle_id: int
    vehicle_number: str
    vehicle_type: str
    owner_name: str


class ReadVehicles(BaseModel):
    vehicle_id: int
    vehicle_number: str
    vehicle_type: str
    owner_name: str
    class Config:
        from_attributes = True


class TrafficOfficers(BaseModel):
    officer_id: int
    name: str
    badge_number: str
    station: str


class ReadTrafficOfficers(BaseModel):
    officer_id: int
    name: str
    badge_number: str
    station: str
    class Config:
        from_attributes = True


class TrafficSignals(BaseModel):
    signal_id: int
    location: str
    status: str
    last_maintenance: datetime.date


class ReadTrafficSignals(BaseModel):
    signal_id: int
    location: str
    status: str
    last_maintenance: datetime.date
    class Config:
        from_attributes = True


class Violations(BaseModel):
    violation_id: int
    vehicle_number: str
    officer_badge: str
    violation_type: str
    fine_amount: Any
    violation_date: datetime.date


class ReadViolations(BaseModel):
    violation_id: int
    vehicle_number: str
    officer_badge: str
    violation_type: str
    fine_amount: Any
    violation_date: datetime.date
    class Config:
        from_attributes = True


class Payments(BaseModel):
    payment_id: int
    violation_id: int
    amount_paid: Any
    payment_date: datetime.date
    payment_method: str


class ReadPayments(BaseModel):
    payment_id: int
    violation_id: int
    amount_paid: Any
    payment_date: datetime.date
    payment_method: str
    class Config:
        from_attributes = True


class Profile(BaseModel):
    id: int


class ReadProfile(BaseModel):
    id: int
    class Config:
        from_attributes = True




class PostVehicles(BaseModel):
    vehicle_id: int = Field( max_length=100)
    vehicle_number: str = Field( max_length=100)
    vehicle_type: str = Field( max_length=100)
    owner_name: str = Field( max_length=100)

    class Config:
        from_attributes = True



class PostTrafficOfficers(BaseModel):
    officer_id: int = Field( max_length=100)
    name: str = Field( max_length=100)
    badge_number: str = Field( max_length=100)
    station: str = Field( max_length=100)

    class Config:
        from_attributes = True



class PostTrafficSignals(BaseModel):
    signal_id: int = Field( max_length=100)
    location: str = Field( max_length=100)
    status: str = Field( max_length=100)
    last_maintenance: Any = Field( max_length=100)

    class Config:
        from_attributes = True



class PostViolations(BaseModel):
    violation_id: int = Field( max_length=100)
    vehicle_number: str = Field( max_length=100)
    officer_badge: str = Field( max_length=100)
    violation_type: str = Field( max_length=100)
    fine_amount: str = Field( max_length=100)
    violation_date: Any = Field( max_length=100)

    class Config:
        from_attributes = True



class PostPayments(BaseModel):
    payment_id: int = Field( max_length=100)
    violation_id: int = Field( max_length=100)
    amount_paid: str = Field( max_length=100)
    payment_date: Any = Field( max_length=100)
    payment_method: str = Field( max_length=100)

    class Config:
        from_attributes = True

