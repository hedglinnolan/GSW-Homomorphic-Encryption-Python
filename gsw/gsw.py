'''This file is an implementation of Gentry-Sahai-Waters (GSW) 2011 fully homomorphic encryption scheme.
GSW transforms a plaintext bit into a ciphertext matrix and relies on the Decisional Learning With Errors
assumption for computational security.

It imports several files where key generation and functions are defined.

Authors: Nolan Hedglin, Kade Phillips, Andrew Reilley'''

import numpy as np
import gswEncrypt as enc
import gswDecrypt as dec
import gswUtilities as utils
import keygen as kg