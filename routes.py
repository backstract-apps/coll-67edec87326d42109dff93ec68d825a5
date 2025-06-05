from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/vehicles/')
async def post_vehicles(raw_data: schemas.PostVehicles, db: Session = Depends(get_db)):
    try:
        return await service.post_vehicles(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/document')
async def post_document(document123: Annotated[UploadFile, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_document(db, document123)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/')
async def get_vehicles(db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/vehicle_id')
async def get_vehicles_vehicle_id(vehicle_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles_vehicle_id(db, vehicle_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/vehicles/vehicle_id/')
async def put_vehicles_vehicle_id(vehicle_id: Annotated[int, Query(max_length=100)], vehicle_number: Annotated[str, Query(max_length=100)], vehicle_type: Annotated[str, Query(max_length=100)], owner_name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_vehicles_vehicle_id(db, vehicle_id, vehicle_number, vehicle_type, owner_name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/vehicles/vehicle_id')
async def delete_vehicles_vehicle_id(vehicle_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.delete_vehicles_vehicle_id(db, vehicle_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/traffic_officers/')
async def get_traffic_officers(db: Session = Depends(get_db)):
    try:
        return await service.get_traffic_officers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/traffic_officers/officer_id')
async def get_traffic_officers_officer_id(officer_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.get_traffic_officers_officer_id(db, officer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/traffic_officers/')
async def post_traffic_officers(raw_data: schemas.PostTrafficOfficers, db: Session = Depends(get_db)):
    try:
        return await service.post_traffic_officers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/violations/violation_id/')
async def put_violations_violation_id(violation_id: Annotated[int, Query(max_length=100)], vehicle_number: Annotated[str, Query(max_length=100)], officer_badge: Annotated[str, Query(max_length=100)], violation_type: Annotated[str, Query(max_length=100)], fine_amount: Annotated[str, Query(max_length=100)], violation_date: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_violations_violation_id(db, violation_id, vehicle_number, officer_badge, violation_type, fine_amount, violation_date)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/traffic_officers/officer_id/')
async def put_traffic_officers_officer_id(officer_id: Annotated[int, Query(max_length=100)], name: Annotated[str, Query(max_length=100)], badge_number: Annotated[str, Query(max_length=100)], station: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_traffic_officers_officer_id(db, officer_id, name, badge_number, station)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/traffic_officers/officer_id')
async def delete_traffic_officers_officer_id(officer_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.delete_traffic_officers_officer_id(db, officer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/traffic_signals/')
async def get_traffic_signals(db: Session = Depends(get_db)):
    try:
        return await service.get_traffic_signals(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/traffic_signals/signal_id')
async def get_traffic_signals_signal_id(signal_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.get_traffic_signals_signal_id(db, signal_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/traffic_signals/')
async def post_traffic_signals(raw_data: schemas.PostTrafficSignals, db: Session = Depends(get_db)):
    try:
        return await service.post_traffic_signals(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/traffic_signals/signal_id/')
async def put_traffic_signals_signal_id(signal_id: Annotated[int, Query(max_length=100)], location: Annotated[str, Query(max_length=100)], status: Annotated[str, Query(max_length=100)], last_maintenance: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_traffic_signals_signal_id(db, signal_id, location, status, last_maintenance)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/traffic_signals/signal_id')
async def delete_traffic_signals_signal_id(signal_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.delete_traffic_signals_signal_id(db, signal_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/violations/')
async def get_violations(db: Session = Depends(get_db)):
    try:
        return await service.get_violations(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/violations/violation_id')
async def get_violations_violation_id(violation_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.get_violations_violation_id(db, violation_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/violations/')
async def post_violations(raw_data: schemas.PostViolations, db: Session = Depends(get_db)):
    try:
        return await service.post_violations(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/violations/violation_id')
async def delete_violations_violation_id(violation_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.delete_violations_violation_id(db, violation_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payments/')
async def get_payments(db: Session = Depends(get_db)):
    try:
        return await service.get_payments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payments/payment_id')
async def get_payments_payment_id(payment_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.get_payments_payment_id(db, payment_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/payments/')
async def post_payments(raw_data: schemas.PostPayments, db: Session = Depends(get_db)):
    try:
        return await service.post_payments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/payments/payment_id/')
async def put_payments_payment_id(payment_id: Annotated[int, Query(max_length=100)], violation_id: Annotated[int, Query(max_length=100)], amount_paid: Annotated[str, Query(max_length=100)], payment_date: Annotated[str, Query(max_length=100)], payment_method: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_payments_payment_id(db, payment_id, violation_id, amount_paid, payment_date, payment_method)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/payments/payment_id')
async def delete_payments_payment_id(payment_id: Annotated[int, Query(max_length=500)], db: Session = Depends(get_db)):
    try:
        return await service.delete_payments_payment_id(db, payment_id)
    except Exception as e:
        raise HTTPException(500, str(e))

