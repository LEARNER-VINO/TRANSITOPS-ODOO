from datetime import datetime

from app import db


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    on_duty = db.Column(db.Boolean, default=False, nullable=False)

    trips = db.relationship("Trip", back_populates="driver")


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(20), nullable=False)  # van, truck, mini
    region = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # available, on_trip, in_shop, retired

    trips = db.relationship("Trip", back_populates="vehicle")
    maintenance_records = db.relationship("MaintenanceRecord", back_populates="vehicle")


class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    trip_code = db.Column(db.String(20), unique=True, nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.id"))
    status = db.Column(db.String(20), nullable=False)  # on_trip, completed, dispatched, draft
    eta_minutes = db.Column(db.Integer)
    eta_label = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    vehicle = db.relationship("Vehicle", back_populates="trips")
    driver = db.relationship("Driver", back_populates="trips")


class MaintenanceRecord(db.Model):
    __tablename__ = "maintenance_records"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # scheduled, in_progress, completed
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)

    vehicle = db.relationship("Vehicle", back_populates="maintenance_records")
