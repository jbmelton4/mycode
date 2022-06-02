#!/usr/bin/env python3

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# display the second item in the list
print("The second item in the list (port): " +  iplist[1] )

# display the third item in the list
print("The last item in the list (state): " + str(iplist[2]) )

