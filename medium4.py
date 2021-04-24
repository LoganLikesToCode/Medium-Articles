import time
import winsound

hours = int(input("How many hours until the timer sets off? "))
minutes = int(input("How many minutes until the timer sets off? "))

final_hours = hours * 3600
final_minutes = minutes * 60
final_time = final_hours + final_minutes

frequency = 500
duration = 5000

while(True):
  if final_time == 0:
    print("The time is finished!")
    winsound.Beep(frequency, duration)
    break;

  final_time -= 1
  time.sleep(1)
  time_shown = str(final_time+)
  print(f"The current time has {time_shown} seconds left!")
