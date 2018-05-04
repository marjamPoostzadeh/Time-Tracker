# -*- coding: utf-8 -*-
"""
Created on Fri May  4 12:40:53 2018

@author: marjan
"""

#!/usr/bin/env python
from socket import *
from netaddr import *

# port scanner
def port_scan(port, host)
   s = socket(AF_INET, SOCK_STREAM)
   try:
      s = s.connect((host, port))
      print "Port ", port, " is open"
   except Exception, e:
      pass

# get user input for range in form xxx.xxx.xxx.xxx-xxx.xxx.xxx.xxx and xx-xx
ipStart, ipEnd = raw_input ("Enter IP-IP: ").split("-")
portStart, portEnd = raw_input ("Enter port-port: ").split("-")

# cast port string to int
portStart, portEnd = [int(portStart), int(portEnd)]

# define IP range
iprange = IPRange(ipStart, ipEnd)

# this is where my problem is
for ip in iprange:
   host = ip
   for port in range(startPort, endPort + 1)
      port_scan(port, host)
      