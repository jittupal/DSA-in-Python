a = 2
b = 4


ans = a ^ b
print("XOR Of A and B :: ", ans)
count = 0
for i in range(0, 32):
    if ans & (1 << i) != 0:
        count += 1
print("Number Of Flips Required  ::  ", count)