import datetime
import calendar
 
today=datetime.datetime.now()
 
dateMonthStart="%s-%s-01" % (today.year, today.month)
dateMonthEnd="%s-%s-%s" % (today.year, today.month, calendar.monthrange(today.year-1, today.month-1)[1])
 
print "primer dia del mes: %s" % dateMonthStart
print "segundo dia del mes: %s" % dateMonthEnd