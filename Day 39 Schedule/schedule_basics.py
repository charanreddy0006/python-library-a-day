import schedule
import time

# --- task function ---
def study_reminder():
    print("📚 Time to study Python!")

# --- schedule task every 10 seconds ---
schedule.every(10).seconds.do(study_reminder)

print("Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(1)