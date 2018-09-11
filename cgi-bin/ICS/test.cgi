#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html"
print "<html><body>\n"

for x in range(0,7):
	print "<p>",str(x),"<p>\n"
print "</body></html>\n"

