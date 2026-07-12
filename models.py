from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import datetime

app = Flask(__name__)

# FIX: Corrected the URI syntax (Username:Password@Host:Port/DBName)
# Assuming 'vinosabkeerthi' is your password
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vinosabkeerthi@localhost:5432/postgres'
app.config['JWT_SECRET_KEY'] = 'transit-ops-super-secret-2024'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100)) # Fixed 'Column' and indentation
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(50)) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_name = db.Column(db.String(100))
    vehicle_type = db.Column(db.String(50)) 
    max_load_capacity = db.Column(db.Float)
    odometer = db.Column(db.Integer)
    acquisition_cost = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(20), default='Available')
    
class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    license_category = db.Column(db.String(20))
    license_expiry = db.Column(db.Date) 
    phone = db.Column(db.String(20))
    safety_score = db.Column(db.Float, default=5.0) 
    status = db.Column(db.String(20), default='Active')

class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    issue = db.Column(db.String(255), nullable=False)
    maintenance_cost = db.Column(db.Numeric(10, 2))
    maintenance_date = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(50))

class FuelLog(db.Model):
    __tablename__ = 'fuel_logs'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    liters = db.Column(db.Float)
    cost = db.Column(db.Numeric(10, 2))
    fuel_date = db.Column(db.Date, default=datetime.utcnow)
    distance = db.Column(db.Integer)

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    expense_type = db.Column(db.String(100))
    amount = db.Column(db.Numeric(10, 2))
    expense_date = db.Column(db.Date, default=datetime.utcnow)
    description = db.Column(db.Text)

class Trip(db.Model):
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    trip_number = db.Column(db.String(20), unique=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    status = db.Column(db.String(50))
    eta = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
