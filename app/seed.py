from datetime import datetime, timedelta

from app import db
from app.models import Driver, MaintenanceRecord, Trip, Vehicle

REGIONS = ["north", "south", "east", "west"]
VEHICLE_TYPES = ["van", "truck", "mini"]


def seed_database():
    if Vehicle.query.first():
        return

    drivers = []
    for idx in range(1, 33):
        drivers.append(
            Driver(
                name=f"Driver {idx:02d}",
                region=REGIONS[(idx - 1) % 4],
                on_duty=idx <= 26,
            )
        )
    drivers[0].name = "Alex"
    drivers[1].name = "John"
    drivers[2].name = "Priya"
    db.session.add_all(drivers)
    db.session.flush()

    vehicles = []
    type_counters = {"van": 0, "truck": 0, "mini": 0}
    prefixes = {"van": "VAN", "truck": "TRK", "mini": "MINI"}

    for vehicle_type, count in [("van", 20), ("truck", 20), ("mini", 15)]:
        for _ in range(count):
            type_counters[vehicle_type] += 1
            vehicles.append(
                Vehicle(
                    code=f"{prefixes[vehicle_type]}-{type_counters[vehicle_type]:02d}",
                    vehicle_type=vehicle_type,
                    region=REGIONS[(type_counters[vehicle_type] - 1) % 4],
                    status="available",
                )
            )

    # Wireframe: 42 available, 6 on trip, 5 in shop, 2 retired = 55 total, 53 active
    featured_on_trip = [
        next(v for v in vehicles if v.code == "VAN-05"),
        next(v for v in vehicles if v.code == "TRK-12"),
        next(v for v in vehicles if v.code == "MINI-08"),
    ]
    for vehicle in featured_on_trip:
        vehicle.status = "on_trip"

    remaining_on_trip = [v for v in vehicles if v.status == "available"][:3]
    for vehicle in remaining_on_trip:
        vehicle.status = "on_trip"

    for vehicle in [v for v in vehicles if v.status == "available"][:5]:
        vehicle.status = "in_shop"
    for vehicle in [v for v in vehicles if v.status == "available"][:2]:
        vehicle.status = "retired"

    db.session.add_all(vehicles)
    db.session.flush()

    now = datetime.utcnow()
    on_trip_vehicles = [v for v in vehicles if v.status == "on_trip"]
    available_vehicles = [v for v in vehicles if v.status == "available"]

    trips = [
        Trip(
            trip_code="TR001",
            vehicle=featured_on_trip[0],
            driver=drivers[0],
            status="on_trip",
            eta_minutes=45,
            created_at=now - timedelta(minutes=30),
        ),
        Trip(
            trip_code="TR002",
            vehicle=featured_on_trip[1],
            driver=drivers[1],
            status="completed",
            eta_minutes=0,
            created_at=now - timedelta(hours=2),
        ),
        Trip(
            trip_code="TR003",
            vehicle=featured_on_trip[2],
            driver=drivers[2],
            status="dispatched",
            eta_minutes=70,
            created_at=now - timedelta(minutes=10),
        ),
        Trip(
            trip_code="TR004",
            vehicle=None,
            driver=None,
            status="draft",
            eta_label="Awaiting vehicle",
            created_at=now - timedelta(minutes=5),
        ),
    ]

    # 18 active trips (on_trip), 9 pending (dispatched + draft)
    for idx in range(5, 22):
        trips.append(
            Trip(
                trip_code=f"TR{idx:03d}",
                vehicle=on_trip_vehicles[(idx - 1) % len(on_trip_vehicles)],
                driver=drivers[(idx - 1) % len(drivers)],
                status="on_trip",
                eta_minutes=30 + idx,
                created_at=now - timedelta(hours=idx),
            )
        )

    for idx in range(22, 29):
        trips.append(
            Trip(
                trip_code=f"TR{idx:03d}",
                vehicle=available_vehicles[(idx - 22) % len(available_vehicles)] if idx % 3 else None,
                driver=drivers[(idx - 1) % len(drivers)] if idx % 4 else None,
                status="dispatched" if idx % 2 else "draft",
                eta_label="Awaiting vehicle" if idx % 3 == 0 else None,
                eta_minutes=None if idx % 3 == 0 else 20 + idx,
                created_at=now - timedelta(minutes=idx * 3),
            )
        )

    db.session.add_all(trips)

    shop_vehicles = [v for v in vehicles if v.status == "in_shop"]
    maintenance = [
        MaintenanceRecord(
            vehicle=shop_vehicles[0],
            description="Brake inspection",
            status="in_progress",
            started_at=now - timedelta(days=1),
        ),
        MaintenanceRecord(
            vehicle=shop_vehicles[1],
            description="Oil change",
            status="scheduled",
            started_at=now + timedelta(days=1),
        ),
    ]
    db.session.add_all(maintenance)

    db.session.commit()
