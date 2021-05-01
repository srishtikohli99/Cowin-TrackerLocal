import requests
import beepy
import datetime
from dateutil.tz import gettz
import sched, time
todays_date = datetime.datetime.now(tz=gettz('Asia/Kolkata')).strftime("%d-%m-%Y")

s = sched.scheduler(time.time, time.sleep)
URL1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=143&date="+str(todays_date)
# URL2 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=143&date=03-05-2021"

def do_something(sc):
    print("requested")
    r=requests.get(url=URL1)
    print(r)
    data = r.json()
    for centre in data["centers"]:
        for session in centre["sessions"]:
                if session["min_age_limit"] == 18:
                    beepy.beep(sound=1)
                    print(centre["name"])
    s.enter(60, 1, do_something, (sc,))
    
s.enter(1, 1, do_something, (s,))
s.run()




