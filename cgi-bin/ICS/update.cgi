#!/usr/bin/env python

#Kody Bloodworth
#ICS Time sheet

import cgi
import cgitb
import os
import csv
import datetime as dt
cgitb.enable()

print "Content-type: text/html"							#HTML Requirement stuff. 
print
print "<html><head><title>ICS</title></head>"
print "<body>"
form = cgi.FieldStorage()
##form2 = cgi.MiniFieldStorage()
if "Action" not in form and "Employee" not in form:		#We check to see if we've been given the right kind of data.
	print "<H1> ERROR </H1>"
else:
	print "<center><H1> ICS TIMELOG </H1></center>"		#We get our data.
	name = form.getvalue('Employee')
	action = form.getvalue('Action')
	#print userData	
	rows = list([])
	userData = None
	print name;
	fields_tl = ['Name', "TimeIn", 'DateIn', 'TimeOut','DateOut', 'Hours']
	fields_ci = ['Name', 'TimeIn', 'DateIn']
	with open('clockedIn.csv', 'r') as clockedin_read:
			reader = csv.DictReader(clockedin_read)
			for row in reader:
				rows.append(row)
				if row["Name"] == name:
					if action == "Clock Out" or action == "Clear":
						userData = row
					elif action == "Clock In":
						print "<center>ALREADY CLOCKED IN</center>"
						print "</body></html>"
						exit()
	if action == "Clock Out":
		if userData == None:
			print "<center>NOT CLOCKED IN</center>"
			print "</body></html>"
			exit()
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
			##print shifthours;
			writer.writerow({'Name':userData['Name'], "TimeIn":userData['TimeIn'],'DateIn':userData['DateIn'], "TimeOut":str(curTime.hour%12).zfill(2)+":"+str(curTime.minute).zfill(2), 'DateOut': str(curTime.date())})
	elif action == "Clock In":
	#	continue
		with open('clockedIn.csv', 'a') as clockingin_append:
			curTime = dt.datetime.now()

			writer = csv.DictWriter(clockingin_append, fieldnames = fields_ci)
			writer.writerow({'Name':name, 'TimeIn':str(curTime.hour%12)+":"+str(curTime.minute), 'DateIn':str(curTime.date())})
		print "<center>You've been clocked in, "+ userData['Name'].split(" ")[0]+"!</center>" 
	elif action == "Clear":
		if userData != None:
			rows.remove(userData);
			with open('clockedIn.csv', 'w') as clockedin_write:
				writer = csv.DictWriter(clockedin_write, fieldnames = fields_ci)
				writer.writeheader()
				for row in rows:
					writer.writerow(row)
					
	#print "<p>" + str(form) + "</p>"
	#f = open("file.txt", "a")
	#log = " "+str(form["Action"].value)+ " "+ str(datetime.datetime.now().hour % 12)+":"+str(datetime.datetime.now().minute)+"\n"
	#f.write(log)
	#f.close()
print "</body>"
print "</html>"


