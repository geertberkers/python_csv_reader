-- Create the database (optional, comment out if already using an existing DB)
-- CREATE DATABASE IF NOT EXISTS business_card_db; --only MySQL
--USE business_card_db;

-- Drop the table if it exists
DROP TABLE IF EXISTS geert_berkers;

-- Create the table with 'id' as the primary key
CREATE TABLE geert_berkers (
--    id SERIAL PRIMARY KEY,
    "Key" TEXT,
    "Value" TEXT
);

-- Insert sample data
INSERT INTO geert_berkers ("Key", "Value") VALUES
('name', 'Geert Berkers'),
('email', 'info@gb-coding.com'),
('website', 'https://gb-coding.nl'),
('phone', '+31 618344318'),
('github', 'https://github.com/geertberkers');

SELECT * FROM public.geert_berkers;

