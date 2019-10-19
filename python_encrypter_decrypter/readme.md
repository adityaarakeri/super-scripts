A simple python program which shows on how to encrpyt and decrypt a string message
Since Python does not come with anything that can encrypt files, we will need to use a third party module.


`python -m pip install cryptography`


PyCrypto is quite popular but since it does not offer built wheels, if you don't have Microsoft Visual C++ Build Tools installed, you will be told to install it. Instead of installing extra tools just to build this, I will be using the cryptography module.
