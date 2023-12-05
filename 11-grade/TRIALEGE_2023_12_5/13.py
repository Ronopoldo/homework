from ipaddress import *

newtwork = ip_network('217.19.128.131/255.255.192.0')

for adress in newtwork:
    print(adress)