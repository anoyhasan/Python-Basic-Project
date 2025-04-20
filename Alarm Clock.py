import time
from datetime import datetime

alarm_times = input("Enter alarm time (HH:MM): ")

print("⏳ Waiting for the alarm...")

while True:
    current_time = datetime.now().strftime("%H:%H")
    if current_time == alarm_times:
        print("Wake up! Alarm time reached!")
        break
    time.sleep(10)
