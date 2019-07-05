import time

print time.strftime("%a, %d %b %Y %H:%M:%S %p %W", time.localtime())

time.sleep(5)

print time.strftime("%a, %d %b %Y %H:%M:%S %p", time.localtime())

