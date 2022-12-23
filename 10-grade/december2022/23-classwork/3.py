# 333009

def findQ(b2, b1):
    return b2 / b1

def find4 (b3, q):
    return b3 * q

nums = [-1024, -256, -64, find4(-64, findQ(-256, -1024)), find4(find4(-64, findQ(-256, -1024)), findQ(-256, -1024))]
print(sum(nums))