@app.route('/api/dashboard/summary', methods=['GET'])
@jwt_required()
def get_dashboard_data():
    current_user = get_jwt_identity()
    
    # 1. Calculate Stats for the top cards
    active_v = Vehicle.query.filter_by(status='Active').count()
    available_v = Vehicle.query.filter_by(status='Available').count()
    maint_v = Vehicle.query.filter_by(status='Maintenance').count()
    active_trips = Trip.query.filter(Trip.status != 'Completed').count()

    # 2. Fetch Recent Trips for the table
    # We grab the last 5 trips ordered by ID or Date
    recent_trips = Trip.query.order_by(Trip.id.desc()).limit(5).all()
    
    trips_list = []
    for trip in recent_trips:
        trips_list.append({
            "trip": trip.trip_number,
            "vehicle": trip.vehicle_name,
            "driver": trip.driver_name,
            "status": trip.status,
            "eta": trip.eta
        })

    return jsonify({
        "stats": {
            "active_vehicles": active_v,
            "available_vehicles": available_v,
            "in_maintenance": maint_v,
            "active_trips": active_trips
        },
        "recent_trips": trips_list
    }), 200