from ipaddress import *
for x in range(256):
    for y in range(256):
        for z in range(256):
            for w in range(256):
                net = ip_network(f'{x}.{y}.{z}.{w}/255.255.255.192')

                for pc in net:
                    print(pc)
