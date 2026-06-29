from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

scheduler = BlockingScheduler()

def show_time():
    print("Current Time:", datetime.now().strftime("%H:%M:%S"))

# Run every 5 seconds
scheduler.add_job(show_time, "interval", seconds=5)

print("Scheduler started... Press Ctrl+C to stop.")

scheduler.start()