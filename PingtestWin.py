'''__Author__: Sushin K'''
'''Usage : python <script>'''
'''Platform : Windows'''

import os


def Ping_node(hostname):
	response = os.system("ping -c 1 " + hostname)

	if response == 1:
		print (hostname, " is up!")
		wx = open("ReachableIP.csv", "a")
		wx.write(hostname + "\n")
		wx.close()
	else:
		print (hostname, " is down!")
		ex = open("UnreachableIP.csv", "a")
		ex.write(hostname + "\n")
		ex.close()


with open("IPList.txt", "r") as inputfile:
        global iplist
        iplist = inputfile.readlines()


for i in iplist :
        Ping_node(i.strip("\n"))
