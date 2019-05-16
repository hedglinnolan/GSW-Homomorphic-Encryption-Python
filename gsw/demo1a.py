import numpy as np
np.set_printoptions(edgeitems=8, linewidth=200)

from util   import text2array
from keygen import keygen
from enc    import encrypt
from dec    import decrypt

keys = keygen(16)

a = int(input('\n    A = '))
b = int(input('    B = '))
print()

ca = encrypt(keys, a)
cb = encrypt(keys, b)

print('\nCiphertext of A \x1B[38;5;203m-> /home/kade/cA\x1B[0m\n\x1B[38;5;33m')
print(ca)
print('\x1B[0m\nCiphertext of B \x1B[38;5;203m-> /home/kade/cB\x1B[0m\n\x1B[38;5;33m')
print(cb)

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
fhA = open('/home/kade/cA', 'w')
fhB = open('/home/kade/cB', 'w')
print(ca, file=fhA)
print(cb, file=fhB)
fhA.close()
fhB.close()

while True:
    fn = input('\x1B[0m\nCiphertext of f(A,B) \x1B[38;5;203m<- ')
    fh = open(fn, 'r')
    ciphertext = fh.read()
    fh.close()

    cf = text2array(ciphertext) % keys.q

    print('\x1B[0m')
    f = decrypt(keys, cf)

    print('\nDecrypted message = \x1B[32;1m%d\x1B[0m' % f)
