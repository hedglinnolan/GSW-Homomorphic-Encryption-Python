''' This file is an implementation of Gentry-Sahai-Waters (GSW) fully-
homomorphic encryption scheme. GSW transforms a plaintext bit into a
ciphertext matrix and relies on the Decisional Learning With Errors
assumption for computational security.

Authors: Nolan Hedglin, Kade Phillips, Andrew Reilley '''

import numpy as np
from util   import *
from keygen import keygen
from enc    import encrypt
from dec    import decrypt
