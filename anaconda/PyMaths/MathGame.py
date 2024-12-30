import time
from datetime import datetime, timedelta

started = datetime.now()
started = started.strftime("%M:%S.%f")[:-3]
print(started)
