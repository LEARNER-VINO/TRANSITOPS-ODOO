from app.models import Driver, Trip, Vehicle


def parse_filters(args):
    vehicle_type = args.get("vehicle_type", "all").lower()
    status = args.get("status", "all").lower()
    region = args.get("region", "all").lower()
    return vehicle_type, status, region


def apply_vehicle_filters(query, vehicle_type, status, region):
    if vehicle_type != "all":
        query = query.filter(Vehicle.vehicle_type == vehicle_type)
    if region != "all":
        query = query.filter(Vehicle.region == region)
    if status == "active":
        query = query.filter(Vehicle.status.in_(["available", "on_trip", "in_shop"]))
    elif status == "maintenance":
        query = query.filter(Vehicle.status == "in_shop")
    elif status == "retired":
        query = query.filter(Vehicle.status == "retired")
    return query


def filtered_vehicles(vehicle_type, status, region):
    query = Vehicle.query
    return apply_vehicle_filters(query, vehicle_type, status, region).all()


def filtered_trips(vehicle_type, status, region):
    query = Trip.query.join(Vehicle, Trip.vehicle_id == Vehicle.id, isouter=True)

    if vehicle_type != "all":
        query = query.filter(Vehicle.vehicle_type == vehicle_type)
    if region != "all":
        query = query.filter(Vehicle.region == region)
    if status == "active":
        query = query.filter(Vehicle.status.in_(["available", "on_trip", "in_shop"]))
    elif status == "maintenance":
        query = query.filter(Vehicle.status == "in_shop")
    elif status == "retired":
        query = query.filter(Vehicle.status == "retired")

    return query.all()


def filtered_drivers_on_duty(vehicle_type, status, region):
    query = Driver.query.filter_by(on_duty=True)
    if region != "all":
        query = query.filter(Driver.region == region)
    return query.count()
