
-- Profile Table
CREATE TABLE Profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(150),
    profile_picture VARCHAR(255)
);

-- ChargingPoint Table
CREATE TABLE ChargingPoint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    address VARCHAR(255) DEFAULT 'Unknown Address',
    city VARCHAR(100),
    country VARCHAR(100),
    capacity INT UNSIGNED NOT NULL,
    available_slots INT UNSIGNED NOT NULL,
    created_at DATETIME,
    latitude DOUBLE,
    longitude DOUBLE,
    availability BOOLEAN,
    charging_speed_kW INT,
    base_price DECIMAL(6,2) DEFAULT 10,
    peak_price DECIMAL(6,2),
    off_peak_price DECIMAL(6,2),
    is_active BOOLEAN DEFAULT TRUE,
    off_peak_start TIME,
    off_peak_end TIME,
    created_by_id INT,
    updated_by_id INT,
    FOREIGN KEY (created_by_id) REFERENCES auth_user(id) ON DELETE SET NULL,
    FOREIGN KEY (updated_by_id) REFERENCES auth_user(id) ON DELETE SET NULL
);

-- ChargingSession Table
CREATE TABLE ChargingSession (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    station_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    energy_consumed_kwh FLOAT,
    costs DECIMAL(10,2) DEFAULT 0.0,
    status VARCHAR(100) DEFAULT 'Confirmed',
    duration TIME,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id)
);

-- PaymentMethod Table
CREATE TABLE PaymentMethod (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    payment_type VARCHAR(15),
    last_four_digits VARCHAR(4),
    expiration_date DATE,
    email VARCHAR(100),
    created_at DATETIME,
    updated_at DATETIME,
    is_default BOOLEAN DEFAULT FALSE,
    UNIQUE(user_id, payment_type, last_four_digits, email),
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);

-- Booking Table
CREATE TABLE Booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    station_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    costs DECIMAL(6,2) NOT NULL,
    status VARCHAR(10) DEFAULT 'pending',
    created_at DATETIME,
    payment_id INT,
    created_by_id INT,
    updated_by_id INT,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id),
    FOREIGN KEY (payment_id) REFERENCES PaymentMethod(id),
    FOREIGN KEY (created_by_id) REFERENCES auth_user(id),
    FOREIGN KEY (updated_by_id) REFERENCES auth_user(id),
    UNIQUE (user_id, station_id, start_time, end_time)
);

-- Notification Table
CREATE TABLE Notification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);

-- Payment Table
CREATE TABLE Payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    payment_method_id INT,
    amount DECIMAL(10,2) NOT NULL CHECK (amount >= 0.01),
    status VARCHAR(15) DEFAULT 'pending',
    currency VARCHAR(3),
    charging_session_id INT,
    gateway_transaction_id VARCHAR(255),
    gateway_response JSON,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (payment_method_id) REFERENCES PaymentMethod(id),
    FOREIGN KEY (charging_session_id) REFERENCES ChargingSession(id),
    INDEX (gateway_transaction_id),
    INDEX (status, created_at)
);

-- Rating Table
CREATE TABLE Rating (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    station_id INT NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    created_at DATETIME,
    created_by_id INT,
    updated_by_id INT,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id),
    FOREIGN KEY (created_by_id) REFERENCES auth_user(id),
    FOREIGN KEY (updated_by_id) REFERENCES auth_user(id),
    UNIQUE (user_id, station_id)
);

-- IssueReport Table
CREATE TABLE IssueReport (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    station_id INT NOT NULL,
    issue_description TEXT NOT NULL,
    created_at DATETIME,
    resolved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id)
);

-- Comment Table
CREATE TABLE Comment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    station_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at DATETIME,
    parent_id INT,
    upvotes INT DEFAULT 0,
    downvotes INT DEFAULT 0,
    updated_at DATE,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id),
    FOREIGN KEY (parent_id) REFERENCES Comment(id),
    UNIQUE (user_id, station_id)
);

-- SubscriptionPlan Table
CREATE TABLE SubscriptionPlan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    price DECIMAL(10,2),
    duration_in_days TIME,
    features TEXT,
    created_at DATETIME
);

-- UserSubscription Table
CREATE TABLE UserSubscription (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (plan_id) REFERENCES SubscriptionPlan(id)
);

-- ChargingStationAnalitics Table
CREATE TABLE ChargingStationAnalitics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    station_id INT NOT NULL,
    total_sessions INT DEFAULT 0,
    total_energy_consumed FLOAT DEFAULT 0.0,
    total_revenue DECIMAL(10,2) DEFAULT 0.0,
    created_at DATETIME,
    FOREIGN KEY (station_id) REFERENCES ChargingPoint(id)
);
