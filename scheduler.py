import schedule
import time
from pipeline.store_data import store_data

def job():
    print("🔄 Running scheduled data refresh...")
    store_data()

schedule.every().day.at("09:00").do(job)

print("⏰ Scheduler running — data refreshes daily at 9AM")
while True:
    schedule.run_pending()
    time.sleep(60)