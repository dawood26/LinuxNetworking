#!/usr/bin/python
import os

for x in range(1,11):
    command = 'ip netns delete ns{}'.format(x)
    os.system(command)
    res = "Successfully deleted ns{}".format(x)
    print(res)
os.system("ip link delete br0")
