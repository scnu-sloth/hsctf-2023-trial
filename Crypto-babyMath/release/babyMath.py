from Crypto.Util.number import getPrime, bytes_to_long
from os import urandom
from secret import flag

def padding(m, n):
    assert len(m) <= n
    return m + urandom(n - len(m))

n = getPrime(2048) * getPrime(2048)
g = n + 1

x = bytes_to_long(padding(flag, n.bit_length()//8-1))
c = pow(g, x, n*n)

print('n = %d' % n)
print('c = %d' % c)
