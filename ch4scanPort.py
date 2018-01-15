#!/usr/bin/python
# -*- coding:utf-8 -*-
# 实现快速高效端口扫描功能
import sys
import nmap
scan_row=[]
input_data = raw_input("please input hosts and port: ")
scan_row = input_data.split(" ")
if len(scan_row)!=2:
	print "input errors,example \"192.168.1.0/24 80,443,22\""
	sys.exit(0)
hosts=scan_row[0]
port=scan_row[1]

try:
	nm=nmap.PortScanner()
except nmap.PortScannerError:
	print ('Nmap not found',sys.exc_info()[0])
	sys.exit(0)
except:
	print("Unexpected errors:",sys.exec_info()[0])
	sys.exit(0)

try:
	nm.scan(hosts=hosts,arguments=' -v -sS -p'+port)
except Exception,e:
	print "scan errors:"+str(e)
for hosts in nm.all_hosts():
	print('-----------------------------------------')
	print('Host : %s (%s)' % (host,nm[host].hostname()))
	print('State : %s' %nm[host].state())

for proto in nm[host].all_hosts():
	print('----------------------------------------')
	print('Protocol : %s ' %proto)
	lport = nm[host][proto].keys()
	lport.sort()
	for port in lport:
		print('port : %s \t state :%s' %(port,nm[host][proto][port]['state']))
		