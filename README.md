# python_psql


```bash
# Update the package list
sudo apt update

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo service postgresql start

# Set up PostgreSQL user and database
sudo -u postgres psql
CREATE DATABASE newlearndb;
CREATE USER vvs_root WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE newlearndb TO vvs_root;
\q

# Install Python 3 and pip
sudo apt install python3 python3-pip

# Install psycopg2-binary
pip3 install psycopg2-binary

# Install Flask
pip3 install flask

# Verify installations
psql --version
python3 --version
python3 -c "import psycopg2; print(psycopg2.__version__)"
python3 -c "import flask; print(flask.__version__)"

# Run Flask app
python3 pdconn.py

```
## Flask API with PostgreSQL Integration

This repository provides a simple Flask application that interacts with a PostgreSQL database. The application supports basic CRUD operations on an `employees` table, including:

- Creating the table if it doesn't exist.
- Inserting new employee data.
- Retrieving all employees' data.
- Updating existing employee details.
- Deleting employees by their ID.
- Changing the port on which the Flask app is running.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Sample Requests](#sample-requests)
- [Troubleshooting](#troubleshooting)


## Prerequisites

Before you begin, ensure that you have met the following requirements:

- Python 3.x or later
- PostgreSQL running on your local machine or a remote server
- `psycopg2` and `Flask` installed in your environment

You can install the required Python libraries using `pip`:

```bash
pip install flask psycopg2
```

Also, ensure that you have a running PostgreSQL instance with the correct database and user credentials.

### PostgreSQL Database Setup
Make sure to create a database (e.g., `newlearndb`) and ensure the user (`vvs_root`) has access to it.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/flask-postgresql-api.git
cd flask-postgresql-api
```

2. Set up your PostgreSQL database with the appropriate credentials:

- **DB_NAME**: The name of your PostgreSQL database.
- **DB_USER**: The PostgreSQL username.
- **DB_PASSWORD**: The password for your PostgreSQL user.
- **DB_HOST**: The host where your PostgreSQL is running (default: `localhost`).
- **DB_PORT**: The port your PostgreSQL service is running on (default: `5432`).

3. Ensure the database and table are set up by visiting `/create_table` route once you run the app.

## Usage

### Running the Flask Application

To run the Flask application, use the following command:

```bash
python3 pdconn.py
```

This will start the Flask app on port 5000. You can access the API at:

- `http://localhost:5000/` - Home route
- `http://localhost:5000/create_table` - Creates the `employees` table
- `http://localhost:5000/insert_data` - Inserts new employee data (POST)
- `http://localhost:5000/get_emply` - Retrieves all employee data
- `http://localhost:5000/update_emply/<id>` - Updates employee data by `id` (PUT)
- `http://localhost:5000/del_emply/<id>` - Deletes an employee by `id` (DELETE)
- `http://localhost:5000/change_port` - Change the port the app runs on

### API Endpoints

Here are the details of the available API endpoints:

#### 1. `GET /create_table`

- Creates the `employees` table if it doesn't exist.
- Returns a message confirming table creation.

#### 2. `POST /insert_data`

- Inserts a new employee into the `employees` table.
- **Request Body**: JSON object with the following fields:
  ```json
  {
      "name": "John Doe",
      "age": 30,
      "dept": "Engineering"
  }
  ```

- **Response**: A message indicating whether the data insertion was successful.

#### 3. `GET /get_emply`

- Retrieves all employees from the `employees` table.
- **Response**: List of all employees with their details.

#### 4. `PUT /update_emply/<id>`

- Updates the employee data for the employee with the specified `id`.
- **Request Body**: JSON object with the following fields:
  ```json
  {
      "name": "John Doe",
      "age": 31,
      "dept": "Marketing"
  }
  ```

- **Response**: A message indicating whether the employee data was successfully updated.

#### 5. `DELETE /del_emply/<id>`

- Deletes the employee with the specified `id`.
- **Response**: A message indicating whether the employee was successfully deleted.

#### 6. `POST /change_port`

- Changes the port the Flask app runs on.
- **Request Body**: JSON object with the following field:
  ```json
  {
      "port": "5433"
  }
  ```

- **Response**: A message indicating the port has been changed.

### Sample Requests

Here are examples of how to make requests to the API:

1. **Insert Data**:
   ```bash
   curl -X POST http://localhost:5000/insert_data -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30, "dept": "Engineering"}'
   ```

2. **Update Data**:
   ```bash
   curl -X PUT http://localhost:5000/update_emply/1 -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 31, "dept": "Marketing"}'
   ```

3. **Delete Data**:
   ```bash
   curl -X DELETE http://localhost:5000/del_emply/1
   ```

4. **Change Port**:
   ```bash
   curl -X POST http://localhost:5000/change_port -H "Content-Type: application/json" -d '{"port": "5433"}'
   ```

### Troubleshooting

1. **500 Internal Server Error**:
   - This usually indicates an issue with the server code or database. Check the error message returned by the API and make sure your database connection is configured correctly.
   - Make sure the database exists and the user has sufficient privileges.

2. **400 Bad Request**:
   - This error occurs if the request body is malformed or missing required fields. Ensure you send valid JSON data with the correct keys.

3. **404 Not Found**:
   - This means the route you are trying to access does not exist. Make sure you're using the correct URL and HTTP method.

