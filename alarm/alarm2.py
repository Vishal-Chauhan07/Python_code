import datetime
from playsound import playsound
alarmHour=int(input("Enter hours:"))
alarmMin=int(input("Enter minute:"))
alarmAmPm=input(" am / pm :")
if alarmAmPm=="pm":
    alarmHour+=12
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing .........")
        playsound("alarm_music.mp3")
        break