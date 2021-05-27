from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc) # UTC time
dt = utc_dt.astimezone() # local time

print (utc_dt)
print (dt)