
from alarm_clock import AlarmClock

alarm_one = AlarmClock()
alarm_two = AlarmClock()

print(f"Current time is {alarm_one.current_time}")
alarm_one.set_current_time("10:15PM")
alarm_one.toggle_alarm()
alarm_one.toggle_alarm()

print(f"Current time is {alarm_two.current_time}")
alarm_two.set_current_time("11:27PM")
alarm_two.toggle_alarm()
alarm_two.set_alarm_time("7:30PM") 
