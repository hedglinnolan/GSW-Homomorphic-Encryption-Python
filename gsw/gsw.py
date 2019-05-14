''' This file is an implementation of Gentry-Sahai-Waters (GSW) fully-
homomorphic encryption scheme. GSW transforms a plaintext bit into a
ciphertext matrix and relies on the Decisional Learning With Errors
assumption for computational security.

Authors: Nolan Hedglin, Kade Phillips, Andrew Reilley '''

import numpy as np
import util
import keygen
import enc
import dec
