import os

url = os.environ.get("TEST_URL", "")

org_userid = os.environ.get("ORG_ADMIN_EMAIL", "")
org_pass = os.environ.get("ORG_ADMIN_PASSWORD", "")

facility_userid = os.environ.get("FACILITY_ADMIN_EMAIL", "")
facility_pass = os.environ.get("FACILITY_ADMIN_PASSWORD", "")

department_userid = os.environ.get("DEPARTMENT_ADMIN_EMAIL", "")
department_pass = os.environ.get("DEPARTMENT_ADMIN_PASSWORD", "")

stm1_userid = os.environ.get("STM_EMAIL", "")
stm1_pass = os.environ.get("STM_PASSWORD", "")

stm2_userid = os.environ.get("STM2_EMAIL", "")
stm2_pass = os.environ.get("STM2_PASSWORD", "")

ulink_userid = os.environ.get("ULINK_EMAIL", "")
ulink_pass = os.environ.get("ULINK_PASSWORD", "")

otp = os.environ.get("TEST_OTP", "")
browser = os.environ.get("TEST_BROWSER", "chrome")
user = os.environ.get("TEST_USER", "")
