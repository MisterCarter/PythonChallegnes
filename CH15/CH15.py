import datetime, calendar

x = datetime.datetime(1006, 1, 27)



for x in range(1006, 1996, 10):
    if datetime.datetime(x, 1, 27).weekday() == 1:
        print('1st uhuh',x)
        if calendar.isleap(x):

            print (x)

