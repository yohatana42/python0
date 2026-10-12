import datetime

now = datetime.datetime.now()
print("Seconds since January 1, 1970: "
      f"{now.timestamp():,.4f}" " or "
      f"{now.timestamp():.2e}" " in scientific notation")
print(now.strftime("%b %d %Y"))
