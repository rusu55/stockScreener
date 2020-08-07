from datetime import datetime
from threading import Timer
import time
import schedule

wait = 120


def foo():
    print(time.ctime())
    Timer(wait, foo).start()


# foo()

def good_luck():
    print("ha ha ha")


schedule.every(1).minutes.do(good_luck)

while True:
    schedule.run_pending()
    time.sleep(1)
