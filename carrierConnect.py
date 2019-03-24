# Author: Jüttner Domokos (Rudolf)

import telnetlib
import sys
import os
from time import sleep
test = False 

##############################
#  Usage:
#
#  $ python3 carrierConnect.py <server_adress> <carrier_callsign>
#
#  These are the minimal args to run the program. Additional FlightGear command
#  line arguments can be added after these in the same fashoin as it would be
#  used when starting FG from shell
#
##############################
host = sys.argv[1]
carrier = sys.argv[2]
data ='No target found'
args = ''

for i in range(3, len(sys.argv)):
    args += sys.argv[i] + ' '


print(host)
print(args)
print('###############')
tn = telnetlib.Telnet(host, 5001)

for s in tn.read_all().decode('ascii').split('\n'):
    if s.startswith(carrier):
        data = s
        break

print(data)
lat = data.split(' ')[4]
lon = data.split(' ')[5]

cmd = ('fgfs --telnet=7700 --multiplay=in,10,,5000 --multiplay=out,10,' + host + ',5000' + 
       ' --prop:/sim/mp-carriers/vinson-callsign=' + carrier + ' --lat=' + lat +
       ' --lon=' + lon + ' --altitude=70 ' + args) 


print(cmd, '\n')

if not test and data != 'No target found':
    os.system(cmd)

sleep(30)

tn = telnetlib.Telnet(host, 5001)

for s in tn.read_all().decode('ascii').split('\n'):
    if s.startswith(carrier):
        data = s
        break

ac = telnetliv.Telnet("lockalhost", 7700)
ac.write(('set position/latitude-deg=' + lat).encode('ascii'))
ac.write(('set position/longitude-deg=' + lon).encode('ascii'))
ac.write('set position/altitude-ft=78'.encode('ascii'))

print('-----DONE-----')
