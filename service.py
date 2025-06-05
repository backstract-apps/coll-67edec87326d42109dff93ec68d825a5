from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def post_vehicles(db: Session, raw_data: schemas.PostVehicles):
    vehicle_id: int = raw_data.vehicle_id
    vehicle_number: str = raw_data.vehicle_number
    vehicle_type: str = raw_data.vehicle_type
    owner_name: str = raw_data.owner_name

    record_to_be_added = {
        "owner_name": owner_name,
        "vehicle_id": vehicle_id,
        "vehicle_type": vehicle_type,
        "vehicle_number": vehicle_number,
    }
    new_vehicles = models.Vehicles(**record_to_be_added)
    db.add(new_vehicles)
    db.commit()
    db.refresh(new_vehicles)
    vehicles_inserted_record = new_vehicles.to_dict()

    res = {
        "vehicles_inserted_record": vehicles_inserted_record,
    }
    return res


async def post_document(db: Session, document123: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document123.read()

    name = document123.filename
    file_path = file_path + "/" + name

    import mimetypes

    document123.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document123.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document123.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    xccgvhbjnm = file_url
    res = {
        "sdfghjk": xccgvhbjnm,
    }
    return res


async def get_vehicles(db: Session):

    query = db.query(models.Vehicles)

    vehicles_all = query.all()
    vehicles_all = (
        [new_data.to_dict() for new_data in vehicles_all]
        if vehicles_all
        else vehicles_all
    )
    res = {
        "vehicles_all": vehicles_all,
    }
    return res


async def get_vehicles_vehicle_id(db: Session, vehicle_id: int):

    query = db.query(models.Vehicles)
    query = query.filter(and_(models.Vehicles.vehicle_id == vehicle_id))

    vehicles_one = query.first()

    vehicles_one = (
        (
            vehicles_one.to_dict()
            if hasattr(vehicles_one, "to_dict")
            else vars(vehicles_one)
        )
        if vehicles_one
        else vehicles_one
    )

    res = {
        "vehicles_one": vehicles_one,
    }
    return res


async def put_vehicles_vehicle_id(
    db: Session,
    vehicle_id: int,
    vehicle_number: str,
    vehicle_type: str,
    owner_name: str,
):

    query = db.query(models.Vehicles)
    query = query.filter(and_(models.Vehicles.vehicle_id == vehicle_id))
    vehicles_edited_record = query.first()

    if vehicles_edited_record:
        for key, value in {
            "owner_name": owner_name,
            "vehicle_id": vehicle_id,
            "vehicle_type": vehicle_type,
            "vehicle_number": vehicle_number,
        }.items():
            setattr(vehicles_edited_record, key, value)

        db.commit()
        db.refresh(vehicles_edited_record)

        vehicles_edited_record = (
            vehicles_edited_record.to_dict()
            if hasattr(vehicles_edited_record, "to_dict")
            else vars(vehicles_edited_record)
        )
    res = {
        "vehicles_edited_record": vehicles_edited_record,
    }
    return res


async def delete_vehicles_vehicle_id(db: Session, vehicle_id: int):

    query = db.query(models.Vehicles)
    query = query.filter(and_(models.Vehicles.vehicle_id == vehicle_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        vehicles_deleted = record_to_delete.to_dict()
    else:
        vehicles_deleted = record_to_delete
    res = {
        "vehicles_deleted": vehicles_deleted,
    }
    return res


async def get_traffic_officers(db: Session):

    query = db.query(models.TrafficOfficers)

    traffic_officers_all = query.all()
    traffic_officers_all = (
        [new_data.to_dict() for new_data in traffic_officers_all]
        if traffic_officers_all
        else traffic_officers_all
    )
    res = {
        "traffic_officers_all": traffic_officers_all,
    }
    return res


async def get_traffic_officers_officer_id(db: Session, officer_id: int):

    query = db.query(models.TrafficOfficers)
    query = query.filter(and_(models.TrafficOfficers.officer_id == officer_id))

    traffic_officers_one = query.first()

    traffic_officers_one = (
        (
            traffic_officers_one.to_dict()
            if hasattr(traffic_officers_one, "to_dict")
            else vars(traffic_officers_one)
        )
        if traffic_officers_one
        else traffic_officers_one
    )

    res = {
        "traffic_officers_one": traffic_officers_one,
    }
    return res


async def post_traffic_officers(db: Session, raw_data: schemas.PostTrafficOfficers):
    officer_id: int = raw_data.officer_id
    name: str = raw_data.name
    badge_number: str = raw_data.badge_number
    station: str = raw_data.station

    record_to_be_added = {
        "name": name,
        "station": station,
        "officer_id": officer_id,
        "badge_number": badge_number,
    }
    new_traffic_officers = models.TrafficOfficers(**record_to_be_added)
    db.add(new_traffic_officers)
    db.commit()
    db.refresh(new_traffic_officers)
    traffic_officers_inserted_record = new_traffic_officers.to_dict()

    res = {
        "traffic_officers_inserted_record": traffic_officers_inserted_record,
    }
    return res


async def put_violations_violation_id(
    db: Session,
    violation_id: int,
    vehicle_number: str,
    officer_badge: str,
    violation_type: str,
    fine_amount: str,
    violation_date: str,
):

    query = db.query(models.Violations)
    query = query.filter(and_(models.Violations.violation_id == violation_id))
    violations_edited_record = query.first()

    if violations_edited_record:
        for key, value in {
            "fine_amount": fine_amount,
            "violation_id": violation_id,
            "officer_badge": officer_badge,
            "vehicle_number": vehicle_number,
            "violation_date": violation_date,
            "violation_type": violation_type,
        }.items():
            setattr(violations_edited_record, key, value)

        db.commit()
        db.refresh(violations_edited_record)

        violations_edited_record = (
            violations_edited_record.to_dict()
            if hasattr(violations_edited_record, "to_dict")
            else vars(violations_edited_record)
        )
    res = {
        "violations_edited_record": violations_edited_record,
    }
    return res


async def put_traffic_officers_officer_id(
    db: Session, officer_id: int, name: str, badge_number: str, station: str
):

    query = db.query(models.TrafficOfficers)
    query = query.filter(and_(models.TrafficOfficers.officer_id == officer_id))
    traffic_officers_edited_record = query.first()

    if traffic_officers_edited_record:
        for key, value in {
            "name": name,
            "station": station,
            "officer_id": officer_id,
            "badge_number": badge_number,
        }.items():
            setattr(traffic_officers_edited_record, key, value)

        db.commit()
        db.refresh(traffic_officers_edited_record)

        traffic_officers_edited_record = (
            traffic_officers_edited_record.to_dict()
            if hasattr(traffic_officers_edited_record, "to_dict")
            else vars(traffic_officers_edited_record)
        )
    res = {
        "traffic_officers_edited_record": traffic_officers_edited_record,
    }
    return res


async def delete_traffic_officers_officer_id(db: Session, officer_id: int):

    query = db.query(models.TrafficOfficers)
    query = query.filter(and_(models.TrafficOfficers.officer_id == officer_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        traffic_officers_deleted = record_to_delete.to_dict()
    else:
        traffic_officers_deleted = record_to_delete
    res = {
        "traffic_officers_deleted": traffic_officers_deleted,
    }
    return res


async def get_traffic_signals(db: Session):

    query = db.query(models.TrafficSignals)

    traffic_signals_all = query.all()
    traffic_signals_all = (
        [new_data.to_dict() for new_data in traffic_signals_all]
        if traffic_signals_all
        else traffic_signals_all
    )
    res = {
        "traffic_signals_all": traffic_signals_all,
    }
    return res


async def get_traffic_signals_signal_id(db: Session, signal_id: int):

    query = db.query(models.TrafficSignals)
    query = query.filter(and_(models.TrafficSignals.signal_id == signal_id))

    traffic_signals_one = query.first()

    traffic_signals_one = (
        (
            traffic_signals_one.to_dict()
            if hasattr(traffic_signals_one, "to_dict")
            else vars(traffic_signals_one)
        )
        if traffic_signals_one
        else traffic_signals_one
    )

    res = {
        "traffic_signals_one": traffic_signals_one,
    }
    return res


async def post_traffic_signals(db: Session, raw_data: schemas.PostTrafficSignals):
    signal_id: int = raw_data.signal_id
    location: str = raw_data.location
    status: str = raw_data.status
    last_maintenance: datetime.date = raw_data.last_maintenance

    record_to_be_added = {
        "status": status,
        "location": location,
        "signal_id": signal_id,
        "last_maintenance": last_maintenance,
    }
    new_traffic_signals = models.TrafficSignals(**record_to_be_added)
    db.add(new_traffic_signals)
    db.commit()
    db.refresh(new_traffic_signals)
    traffic_signals_inserted_record = new_traffic_signals.to_dict()

    res = {
        "traffic_signals_inserted_record": traffic_signals_inserted_record,
    }
    return res


async def put_traffic_signals_signal_id(
    db: Session, signal_id: int, location: str, status: str, last_maintenance: str
):

    query = db.query(models.TrafficSignals)
    query = query.filter(and_(models.TrafficSignals.signal_id == signal_id))
    traffic_signals_edited_record = query.first()

    if traffic_signals_edited_record:
        for key, value in {
            "status": status,
            "location": location,
            "signal_id": signal_id,
            "last_maintenance": last_maintenance,
        }.items():
            setattr(traffic_signals_edited_record, key, value)

        db.commit()
        db.refresh(traffic_signals_edited_record)

        traffic_signals_edited_record = (
            traffic_signals_edited_record.to_dict()
            if hasattr(traffic_signals_edited_record, "to_dict")
            else vars(traffic_signals_edited_record)
        )
    res = {
        "traffic_signals_edited_record": traffic_signals_edited_record,
    }
    return res


async def delete_traffic_signals_signal_id(db: Session, signal_id: int):

    query = db.query(models.TrafficSignals)
    query = query.filter(and_(models.TrafficSignals.signal_id == signal_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        traffic_signals_deleted = record_to_delete.to_dict()
    else:
        traffic_signals_deleted = record_to_delete
    res = {
        "traffic_signals_deleted": traffic_signals_deleted,
    }
    return res


async def get_violations(db: Session):

    query = db.query(models.Violations)

    violations_all = query.all()
    violations_all = (
        [new_data.to_dict() for new_data in violations_all]
        if violations_all
        else violations_all
    )
    res = {
        "violations_all": violations_all,
    }
    return res


async def get_violations_violation_id(db: Session, violation_id: int):

    query = db.query(models.Violations)
    query = query.filter(and_(models.Violations.violation_id == violation_id))

    violations_one = query.first()

    violations_one = (
        (
            violations_one.to_dict()
            if hasattr(violations_one, "to_dict")
            else vars(violations_one)
        )
        if violations_one
        else violations_one
    )

    res = {
        "violations_one": violations_one,
    }
    return res


async def post_violations(db: Session, raw_data: schemas.PostViolations):
    violation_id: int = raw_data.violation_id
    vehicle_number: str = raw_data.vehicle_number
    officer_badge: str = raw_data.officer_badge
    violation_type: str = raw_data.violation_type
    fine_amount: str = raw_data.fine_amount
    violation_date: datetime.date = raw_data.violation_date

    record_to_be_added = {
        "fine_amount": fine_amount,
        "violation_id": violation_id,
        "officer_badge": officer_badge,
        "vehicle_number": vehicle_number,
        "violation_date": violation_date,
        "violation_type": violation_type,
    }
    new_violations = models.Violations(**record_to_be_added)
    db.add(new_violations)
    db.commit()
    db.refresh(new_violations)
    violations_inserted_record = new_violations.to_dict()

    res = {
        "violations_inserted_record": violations_inserted_record,
    }
    return res


async def delete_violations_violation_id(db: Session, violation_id: int):

    query = db.query(models.Violations)
    query = query.filter(and_(models.Violations.violation_id == violation_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        violations_deleted = record_to_delete.to_dict()
    else:
        violations_deleted = record_to_delete
    res = {
        "violations_deleted": violations_deleted,
    }
    return res


async def get_payments(db: Session):

    query = db.query(models.Payments)

    payments_all = query.all()
    payments_all = (
        [new_data.to_dict() for new_data in payments_all]
        if payments_all
        else payments_all
    )
    res = {
        "payments_all": payments_all,
    }
    return res


async def get_payments_payment_id(db: Session, payment_id: int):

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.payment_id == payment_id))

    payments_one = query.first()

    payments_one = (
        (
            payments_one.to_dict()
            if hasattr(payments_one, "to_dict")
            else vars(payments_one)
        )
        if payments_one
        else payments_one
    )

    res = {
        "payments_one": payments_one,
    }
    return res


async def post_payments(db: Session, raw_data: schemas.PostPayments):
    payment_id: int = raw_data.payment_id
    violation_id: int = raw_data.violation_id
    amount_paid: str = raw_data.amount_paid
    payment_date: datetime.date = raw_data.payment_date
    payment_method: str = raw_data.payment_method

    record_to_be_added = {
        "payment_id": payment_id,
        "amount_paid": amount_paid,
        "payment_date": payment_date,
        "violation_id": violation_id,
        "payment_method": payment_method,
    }
    new_payments = models.Payments(**record_to_be_added)
    db.add(new_payments)
    db.commit()
    db.refresh(new_payments)
    payments_inserted_record = new_payments.to_dict()

    res = {
        "payments_inserted_record": payments_inserted_record,
    }
    return res


async def put_payments_payment_id(
    db: Session,
    payment_id: int,
    violation_id: int,
    amount_paid: str,
    payment_date: str,
    payment_method: str,
):

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.payment_id == payment_id))
    payments_edited_record = query.first()

    if payments_edited_record:
        for key, value in {
            "payment_id": payment_id,
            "amount_paid": amount_paid,
            "payment_date": payment_date,
            "violation_id": violation_id,
            "payment_method": payment_method,
        }.items():
            setattr(payments_edited_record, key, value)

        db.commit()
        db.refresh(payments_edited_record)

        payments_edited_record = (
            payments_edited_record.to_dict()
            if hasattr(payments_edited_record, "to_dict")
            else vars(payments_edited_record)
        )
    res = {
        "payments_edited_record": payments_edited_record,
    }
    return res


async def delete_payments_payment_id(db: Session, payment_id: int):

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.payment_id == payment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        payments_deleted = record_to_delete.to_dict()
    else:
        payments_deleted = record_to_delete
    res = {
        "payments_deleted": payments_deleted,
    }
    return res
