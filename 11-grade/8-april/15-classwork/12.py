from ipaddress import *
net = ip_network('105.224.200.224/255.255.255.225', 0)

for i in net:
    print(net)