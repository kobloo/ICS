#!/usr/bin/env python


import cgi
import cgitb
import os
import csv
import datetime as dt
cgitb.enable()

print "Content-type: text/html"
print
print "<html><head><title>ICS</title></head>"
print "<body>"
form = cgi.FieldStorage()
##form2 = cgi.MiniFieldStorage()
if "Action" not in form and "Employee" not in form:
	print "<H1> ERROR </H1>"
else:
	print "<H1> No Error, enjoy yourself! </H1>"
	name = form.getvalue('Employee')
	action = form.getvalue('Action')
	#print userData	
	rows = list([])
	userData = None
	print name;
	fields_tl = ['Name', "TimeIn", 'DateIn', 'TimeOut','DateOut', 'Hours']
	fields_ci = ['Name', 'TimeIn', 'DateIn']
	if action == "Clock Out":
		with open('clockedIn.csv', 'r') as clockedin_read:
			reader = csv.DictReader(clockedin_read)
			for row in reader:
				rows.append(row)
				if row["Name"] == name:
					userData = row
		if userData == None:
			print "NOT CLOCKED IN"
			exit()
		print type(userData)
		rows.remove(userData)
		with open('clockedIn.csv', 'w') as clockedin_write:
			writer = csv.DictWriter(clockedin_write, fieldnames = fields_ci)
			
			writer.writeheader()
			#writer.writerow(["Name","TimeIn"])
			for row in rows:
				writer.writerow(row)
		with open('timelog.csv', 'a') as timelog_write:
			writer = csv.DictWriter(timelog_write, fieldnames = fields_tl)
			
			curTime = dt.datetime.now()
			hours, minutes = userData['TimeIn'].split(":")
			shifthours = str(int(curTime.hour%12)-int(hours)).zfill(2)+":"+str(int(curTime.minute)-int(minutes)).zfill(2)
			print shifthours;
			writer.writerow({'Name':userData['Name'], "TimeIn":userData['TimeIn'],'DateIn':userData['DateIn'], "TimeOut":str(curTime.hour%12).zfill(2)+":"+str(curTime.minute).zfill(2), 'DateOut': str(curTime.date())})
	elif action == "Clock In":
	#	continue
		with open('clockedIn.csv', 'a') as clockingin_append:
			curTime = dt.datetime.now()

			writer = csv.DictWriter(clockingin_append, fieldnames = fields_ci)
			writer.writerow({'Name':name, 'TimeIn':str(curTime.hour%12)+":"+str(curTime.minute), 'DateIn':str(curTime.date())})
	#print "<p>" + str(form) + "</p>"
	#f = open("file.txt", "a")
	#log = " "+str(form["Action"].value)+ " "+ str(datetime.datetime.now().hour % 12)+":"+str(datetime.datetime.now().minute)+"\n"
	#f.write(log)
	#f.close()
print "</body>"
print "</html>"


