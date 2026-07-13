import csv
import arrow
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "attendance.csv")
REPORT_FILE = os.path.join(BASE_DIR, "report.txt")

OFFICE_START = arrow.get("09:00", "HH:mm")


def calculate_working_hours(login, logout):
    login_time = arrow.get(login, "YYYY-MM-DD HH:mm")
    logout_time = arrow.get(logout, "YYYY-MM-DD HH:mm")

    duration = logout_time - login_time

    hours = duration.total_seconds() / 3600

    return round(hours, 2)


def is_late(login):

    login_time = arrow.get(login, "YYYY-MM-DD HH:mm")

    office_time = login_time.replace(
        hour=OFFICE_START.hour,
        minute=OFFICE_START.minute
    )

    return login_time > office_time


def generate_report():

    report = []

    with open(CSV_FILE, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            hours = calculate_working_hours(
                row["Login"],
                row["Logout"]
            )

            late = is_late(row["Login"])

            report.append(
                {
                    "Employee": row["Employee"],
                    "Hours": hours,
                    "Late": late
                }
            )

    with open(REPORT_FILE, "w") as file:

        file.write("=" * 40 + "\n")
        file.write("EMPLOYEE ATTENDANCE REPORT\n")
        file.write("=" * 40 + "\n\n")

        for employee in report:

            status = "Late" if employee["Late"] else "On Time"

            file.write(
                f"{employee['Employee']}\n"
            )

            file.write(
                f"Working Hours : {employee['Hours']}\n"
            )

            file.write(
                f"Status        : {status}\n"
            )

            file.write("-" * 40 + "\n")

    print("Report Generated Successfully!")


if __name__ == "__main__":
    generate_report()