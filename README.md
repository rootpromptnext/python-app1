# Student Management CRUD App

A simple full-stack CRUD application built using:

* **Python (Flask)**
* **MySQL**
* **HTML5 + Bootstrap 5**
* Secure database user (least privilege principle)

## Features

* Create Student
* View Students
* Update Student
* Delete Student
* Flash messages
* Bootstrap responsive UI
* MySQL database integration
* Dedicated DB user (no root usage)

# System Requirements

* Ubuntu 22.04 (or similar Debian-based system)
* Python 3.10+
* MySQL Server

# Install System Dependencies

Update system:

```bash
sudo apt update
sudo apt install -y git curl unzip
```

## Install Python venv support

```bash
sudo apt update
sudo apt install python3.10-venv
```

If required:

```bash
sudo apt update && sudo apt install python3.10-venv
```

## Install MySQL Build Dependencies (Required for mysqlclient)

```bash
sudo apt update

sudo apt install -y \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

sudo apt install -y libmariadb-dev
```

# Install MySQL Server

```bash
sudo apt install -y mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
```

Login:

```bash
sudo mysql
```

# Create Database & Table

Inside MySQL:

```sql
CREATE DATABASE crud_demo;

USE crud_demo;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

# Create Dedicated Database User (Recommended)

```sql
CREATE USER 'crudapp'@'localhost' IDENTIFIED BY 'StrongPass@123';

GRANT SELECT, INSERT, UPDATE, DELETE
ON crud_demo.* 
TO 'crudapp'@'localhost';

FLUSH PRIVILEGES;
EXIT;
```

# Clone Repository

```bash
git clone <your-repo-url>
cd python-app
```

# Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

# Install Python Dependencies

```bash
pip install flask flask-mysqldb mysqlclient
```

(Optional)

```bash
pip freeze > requirements.txt
```

# Export vars before running app:

export DB_HOST=localhost
export DB_USER=crudapp
export DB_PASS=StrongPass@123
export DB_NAME=crud_demo
```

# Run Application

```
python app.py
```

If configured to run on all interfaces:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

Access in browser:

```
http://localhost:5000
```

Or:

```
http://<server-ip>:5000
```

