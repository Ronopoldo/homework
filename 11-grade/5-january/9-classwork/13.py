from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240', 0)

for user in net:
    print(bin(int(user)).count('1'))

    # temp = str(user).split('.')
    # out = 0
    # for part in temp:
    #     out+=str(bin(int(part))).count('1')
    #
    # print(out)