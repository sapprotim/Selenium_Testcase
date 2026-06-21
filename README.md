# HPB Testcase Selenium

Automated end-to-end test suite for the HPB (Health Promotion Board) web application, built with Python, Selenium WebDriver, and pytest.

## Project Structure

```
HPB_Testcase_Selenium/
├── logindetails/
│   └── login info.xlsx          # Credentials and URL configuration
├── Login_logout/
│   └── test_login_logout.py
├── HPB Admin/
│   └── HPB Admin.py
├── Facility admin/
│   └── Test_Facility_admin.py
├── Department Admin/
│   └── test_department_admin.py
├── Facility and department/
│   └── Test_Facility_and_department.py
├── Invite User/
│   └── test_invite.py
├── User/
│   ├── test_User_page.py
│   └── test_user_onboarding.py
├── Clinician/
│   └── test_clinician.py
├── Programme Management/
│   ├── test_alerts_Nudges.py
│   ├── Test_challenge.py
│   ├── test_Links.py
│   ├── test_medichine.py
│   ├── test_Physiotherapy_Equipments.py
│   ├── test_Physiotherapy_Exercises.py
│   ├── test_Predefined_stm_Message.py
│   ├── test_Predefined_user_Messages.py
│   ├── test_Specialised Nutrition.py
│   └── test_Themes.py
├── Appnication Tacker/
│   └── test_Application_Tracker.py
├── user profile/
│   ├── Alerts_Reminders.py
│   ├── test_Patients_Logs.py
│   ├── test_Records.py
│   ├── test_Trends.py
│   └── test_wellness plan.py
├── screenshots/                 # Auto-generated test failure screenshots
├── reports/                     # Test run reports
├── excelfile.py                 # Login credentials loader utility
└── driver.py                   # Driver utility
```

## Test Coverage

| Module | Test File | Description |
|---|---|---|
| Login / Logout | `test_login_logout.py` | Valid/invalid credentials, OTP flow, logout |
| HPB Admin | `HPB Admin.py` | HPB admin portal tests |
| Facility Admin | `Test_Facility_admin.py` | Facility administrator workflows |
| Department Admin | `test_department_admin.py` | Department admin workflows |
| Facility & Department | `Test_Facility_and_department.py` | Combined facility and department management |
| Invite User | `test_invite.py` | User invitation flows |
| User | `test_User_page.py`, `test_user_onboarding.py` | User page and onboarding |
| Clinician | `test_clinician.py` | Clinician portal tests |
| Programme Management | Multiple files | Alerts, challenges, links, medicine, physiotherapy, nutrition, themes |
| Application Tracker | `test_Application_Tracker.py` | Application tracking features |
| User Profile | `test_Patients_Logs.py`, `test_Records.py`, `test_Trends.py`, `test_wellness plan.py` | Patient logs, records, health trends, wellness plans |

## Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd HPB_Testcase_Selenium
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install selenium pytest pandas openpyxl
   ```

## Configuration

All login credentials and the target URL are stored in `logindetails/login info.xlsx`.

The Excel file uses the following layout:

| Row | Column B | Column C | Column D |
|-----|----------|----------|----------|
| 1 | URL | | |
| 2 | org_userid | org_pass | |
| 3 | facility_userid | facility_pass | otp |
| 4 | department_userid | department_pass | |
| 5 | stm1_userid | stm1_pass | |
| 6 | stm2_userid | stm2_pass | |
| 7 | ulink_userid | ulink_pass | |
| 10 | browser | | |
| 11 | user | | |

Update this file with the correct credentials before running tests.

## Running Tests

Run all tests:
```bash
pytest
```

Run a specific module:
```bash
pytest "Login_logout/test_login_logout.py"
pytest "Clinician/test_clinician.py"
```

Run with HTML report:
```bash
pytest --html=reports/report.html
```

Run with verbose output:
```bash
pytest -v
```

## Screenshots

Screenshots are automatically captured on test failures and saved to the `screenshots/` directory, organised by module (e.g., `screenshots/login_logout/`).

## User Roles

The test suite covers the following user roles:

- **HPB Admin** — top-level administration
- **Facility Admin** — facility-level management
- **Department Admin** — department-level management
- **STM (Senior Team Member)** — clinical team workflows
- **Clinician** — patient-facing clinical workflows
- **ULink User** — connected life user
