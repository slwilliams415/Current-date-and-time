# Current-date-and-time
Display current date and time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
#24-hours format 
print (now.strftime("   %m-%d-%Y %H:%M:%S "))
#12-hours format 
print (now.strftime("   %m-%d-%Y %I:%M:%S "))
