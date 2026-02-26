# HRMS

A Human Resource Management System REST API built with Django REST Framework.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Deployment:** Render

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees/` | List all employees |
| POST | `/api/employees/` | Add new employee |
| DELETE | `/api/employees/<employee_id>/` | Delete employee |
| GET | `/api/attendance/` | List all attendance records |
| POST | `/api/attendance/` | Mark attendance |
| GET | `/api/attendance/?employee=EMP001` | Filter by employee |
| GET | `/api/attendance/?date=2025-02-24` | Filter by date |
| GET | `/api/dashboard/` | Summary stats |

## Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Gandharv99/hrms.git
cd hrms
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file in root**
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=hrms_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Start server**
```bash
python manage.py runserver
```

## Assumptions & Limitations

- Single admin user, no authentication required
- Attendance can only be marked for present or past dates, not future
- One attendance record per employee per day