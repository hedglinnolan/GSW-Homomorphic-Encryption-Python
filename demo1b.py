import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

from util import text2array

fh = open('/home/kade/cA', 'r')
ca = text2array(fh.read())
fh.close()

print('Loaded [ca] from /home/kade/cA')

fh = open('/home/kade/cB', 'r')
cb = text2array(fh.read())
fh.close()

print('Loaded [cb] from /home/kade/cB')

def write2file(c):
    fh = open('/home/kade/fAB', 'w')
    print(c, file=fh)
    fh.close()
    print('Wrote matrix to /home/kade/fAB')
