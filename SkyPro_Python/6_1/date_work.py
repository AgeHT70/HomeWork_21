from datetime import date
from datetime import time
from datetime import datetime

date_one = date(1815, 12, 12)  # 12 декабря 1815
print(date_one)

time_one = time(16, 20, 00)  # 16 часов 20 минут
print(time_one)

datetime_one = datetime(1986, 4, 26, 1, 23, 47)  # 26 апреля 1986 01:23:47
print(datetime_one)

thedate = datetime(1986, 4, 26, 1, 23, 47)  # 26 апреля 1986 01:23:47

print("Год", thedate.year)
print("Месяц", thedate.month)
print("День", thedate.day)
print("Час", thedate.hour)
print("Минута", thedate.minute)
print("Секунда", thedate.second)

thedate = date(1970, 1, 5)
date_formatted = thedate.strftime("%d %B %Y ")  # День Месяц Год
print(date_formatted)
# %y  Год, короткая версия    18
# %Y  Год, полная версия  2018
# %m  Месяц номером   04
# %B  Месяц словом    April
# %d  День, от 01 до 31   12
# %H  Час, от 00 до 23    04
# %M  Минуты, от 00 до 59 23
# %S  Секунды, от 00 до 59    07


