-- Create tables and import data
-- Drop table if exists
DROP TABLE IF EXISTS company_dept;

-- Create new table
CREATE TABLE company_dept (
  dept_no VARCHAR,
  dept_name VARCHAR,	
);

-- Verify successful data import
SELECT * FROM bird_bands;

-- Drop if exists
DROP TABLE IF EXISTS age;

-- Create new table
CREATE TABLE age (
  AGE_CODE INT PRIMARY KEY,
  AGE_ALPHA_CODE VARCHAR,
  AGE_DESCRIPTION VARCHAR,
  AGE_EXPLAIN_TEXT VARCHAR
);

-- Verify successful data import
SELECT * FROM age;

-- Drop if exists
DROP TABLE IF EXISTS band_type;

-- Create new table
CREATE TABLE band_type (
  BAND_TYPE_CODE VARCHAR PRIMARY KEY,
  BAND_TYPE_DESCRIPTION VARCHAR,
  BAND_CLOSURE VARCHAR
);

-- Verify successful data import
SELECT * FROM band_type;

-- Drop if exists
DROP TABLE IF EXISTS bird_status;

-- Create new table
CREATE TABLE bird_status (
  BIRD_STATUS VARCHAR PRIMARY KEY,
  BIRD_STATUS_DESCRIPTION VARCHAR,
  BIRD_STATUS_EXPLAIN_TEXT VARCHAR
);

-- Verify successful data import
SELECT * FROM bird_status;

-- Drop if exists
DROP TABLE IF EXISTS country_state;

-- Create new table
CREATE TABLE country_state (
  COUNTRY_NAME VARCHAR,
  STATE_NAME VARCHAR,
  ISO_COUNTRY_CODE VARCHAR,
  ISO_SUBDIVISION_CODE VARCHAR
);

-- Verify successful data import
SELECT * FROM country_state;

-- Drop if exists
DROP TABLE IF EXISTS event_type;

-- Create new table
CREATE TABLE event_type (
  EVENT_TYPE VARCHAR PRIMARY KEY,
  EVENT_TYPE_DESC VARCHAR
);

-- Verify successful data import
SELECT * FROM event_type;

-- Drop if exists
DROP TABLE IF EXISTS extra_info;

-- Create new table
CREATE TABLE extra_info (
  EXTRA_INFO_CODE VARCHAR PRIMARY KEY,
  EXTRA_INFO_CODE_DESCRIPTION VARCHAR,
  EXTRA_INFO_LONG_DESCRIPTION VARCHAR
);

-- Verify successful data import
SELECT * FROM extra_info;

-- Drop if exists
DROP TABLE IF EXISTS sex;

-- Create new table
CREATE TABLE sex (
  SEX_CODE INT PRIMARY KEY,
  SEX_DESCRIPTION VARCHAR
);

-- Verify successful data import
SELECT * FROM sex;
