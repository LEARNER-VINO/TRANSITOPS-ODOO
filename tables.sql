-- =========================
-- VEHICLES
-- =========================
CREATE TABLE vehicles (
    id BIGSERIAL PRIMARY KEY,
    registration_number VARCHAR(30) UNIQUE NOT NULL,
    vehicle_name VARCHAR(100),
    vehicle_type VARCHAR(50),
    max_load_capacity DECIMAL(10,2),
    odometer INT DEFAULT 0,
    acquisition_cost DECIMAL(12,2),
    status VARCHAR(30) DEFAULT 'Available'
        CHECK(status IN ('Available','On Trip','In Shop','Retired'))
);

-- =========================
-- DRIVERS
-- =========================
CREATE TABLE drivers (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    license_category VARCHAR(20),
    license_expiry DATE,
    phone VARCHAR(20),
    safety_score DECIMAL(5,2) DEFAULT 100,
    status VARCHAR(20) DEFAULT 'Available'
        CHECK(status IN ('Available','On Trip','Off Duty','Suspended'))
);

-- =========================
-- TRIPS
-- =========================
CREATE TABLE trips (
    id BIGSERIAL PRIMARY KEY,

    vehicle_id BIGINT REFERENCES vehicles(id),

    driver_id BIGINT REFERENCES drivers(id),

    source VARCHAR(100),

    destination VARCHAR(100),

    cargo_weight DECIMAL(10,2),

    planned_distance DECIMAL(10,2),

    actual_distance DECIMAL(10,2),

    revenue DECIMAL(12,2),

    status VARCHAR(20) DEFAULT 'Draft'
        CHECK(status IN ('Draft','Dispatched','Completed','Cancelled')),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- MAINTENANCE
-- =========================
CREATE TABLE maintenance (

    id BIGSERIAL PRIMARY KEY,

    vehicle_id BIGINT REFERENCES vehicles(id),

    issue TEXT,

    maintenance_cost DECIMAL(10,2),

    maintenance_date DATE,

    status VARCHAR(20) DEFAULT 'Pending'
);

-- =========================
-- FUEL LOGS
-- =========================
CREATE TABLE fuel_logs (

    id BIGSERIAL PRIMARY KEY,

    vehicle_id BIGINT REFERENCES vehicles(id),

    liters DECIMAL(10,2),

    cost DECIMAL(10,2),

    fuel_date DATE,

    distance DECIMAL(10,2)
);

-- =========================
-- EXPENSES
-- =========================
CREATE TABLE expenses (

    id BIGSERIAL PRIMARY KEY,

    vehicle_id BIGINT REFERENCES vehicles(id),

    expense_type VARCHAR(50),

    amount DECIMAL(10,2),

    expense_date DATE,

    description TEXT
);