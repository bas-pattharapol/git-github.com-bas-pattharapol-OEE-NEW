import datetime

date = datetime.datetime(2000, 1, 1) # Replace with whatever you want
now = datetime.datetime.now() # You can even find the current date and time using this expression

if date < now:
    print('past')
elif date > now:
    print('future')
else:
    print('present')
# This would print "past"