from Crypto.Util.number import long_to_bytes

with open('./out', 'r') as f:
    exec(f.read())

assert (c - 1) % n == 0
m = (c - 1) // n
flag = long_to_bytes(m)[:43]
print(flag)
