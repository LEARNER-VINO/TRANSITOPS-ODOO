from flask import Blueprint, jsonify, request

from app.filters import filtered_drivers_on_duty, filtered_trips, filtered_vehicles, parse_filters
from app.models import Driver, Trip, Vehicle

dashboard_bp = Blueprint("dashboard", __name__)

STATUS_LABELS = {
    "on_trip": "On Trip",
    "completed": "Completed",
    "dispatched": "Dispatched",
    "draft": "Draft",
}

DISTRIBUTION_LABELS = {
    "available": "Available",
    "on_trip": "On Trip",
    "in_shop": "In Shop",
    "retired": "Retired",
}


def format_eta(trip):
    if trip.eta_label:
        return trip.eta_label
    if trip.eta_minutes is None:
        return None
    if trip.eta_minutes < 60:
        return f"{trip.eta_minutes} min"
    hours = trip.eta_minutes // 60
    minutes = trip.eta_minutes % 60
    if minutes:
        return f"{hours}h {minutes}m"
    return f"{hours}h"


@dashboard_bp.get("/summary")
def dashboard_summary():
    vehicle_type, status, region = parse_filters(request.args)
    vehicles = filtered_vehicles(vehicle_type, status, region)
    trips = filtered_trips(vehicle_type, status, region)

    active_vehicles = len([v for v in vehicles if v.status != "retired"])
    available_vehicles = len([v for v in vehicles if v.status == "available"])
    maintenance_vehicles = len([v for v in vehicles if v.status == "in_shop"])
    active_trips = len([t for t in trips if t.status == "on_trip"])
    pending_trips = len([t for t in trips if t.status in ("dispatched", "draft")])
    drivers_on_duty = filtered_drivers_on_duty(vehicle_type, status, region)

    total_drivers = Driver.query.count()
    utilization = round((drivers_on_duty / total_drivers) * 100) if total_drivers else 0

    return jsonify(
        {
            "activeVehicles": active_vehicles,
            "availableVehicles": available_vehicles,
            "vehiclesInMaintenance": maintenance_vehicles,
            "activeTrips": active_trips,
            "pendingTrips": pending_trips,
            "driversOnDuty": drivers_on_duty,
            "fleetUtilization": utilization,
        }
    )


@dashboard_bp.get("/recent-trips")
def recent_trips():
    vehicle_type, status, region = parse_filters(request.args)
    trips = filtered_trips(vehicle_type, status, region)
    trips = sorted(trips, key=lambda trip: trip.created_at, reverse=True)[:10]

    return jsonify(
        [
            {
                "id": trip.trip_code,
                "vehicle": trip.vehicle.code if trip.vehicle else None,
                "driver": trip.driver.name if trip.driver else None,
                "status": STATUS_LABELS.get(trip.status, trip.status),
                "eta": format_eta(trip),
            }
            for trip in trips
        ]
    )


@dashboard_bp.get("/vehicle-status")
def vehicle_status():
    vehicle_type, status, region = parse_filters(request.args)
    vehicles = filtered_vehicles(vehicle_type, status, region)
    total = len(vehicles)

    counts = {key: 0 for key in DISTRIBUTION_LABELS}
    for vehicle in vehicles:
        counts[vehicle.status] = counts.get(vehicle.status, 0) + 1

    distribution = [
        {
            "status": DISTRIBUTION_LABELS[key],
            "count": counts[key],
            "percentage": round((counts[key] / total) * 100) if total else 0,
        }
        for key in ("available", "on_trip", "in_shop", "retired")
    ]

    return jsonify({"total": total, "distribution": distribution})


@dashboard_bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "transitops-backend"})
