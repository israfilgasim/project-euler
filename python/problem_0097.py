import sys
import time
start = time.time()
sys.set_int_max_str_digits(0) # for large numbers


prime = 28433 * (2 ** 7830457) + 1

st = ""
for i in range(10):
    digit = prime % 10
    st = str(digit) + st
    prime //= 10

print(time.time() - start) # 0.05 seconds
print(st) # 8739992577