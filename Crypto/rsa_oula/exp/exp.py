import binascii
import gmpy2

p=13033106278343285620059299905064279114838449640655438024483885677020059221896469674413702337636166199345402960716788071525599292740080050613763901793385253
e=0x9a36a9e6e39e814913617d3c1
c=0x354ceba52f14b444c4ea85e6bdc261e25a79ab03e2e9a25f94c61f2417010d4f274e3627ec515c05ba34d3f87a145ba313372dfc8aa86c54a5084b4e97c5d1debad155c5855faea99ffe3b4beaafb2b2de1ea14281d4556df7e9f0389e95c71b1a48fe59a849a8650e01b8942e829ca190252d32c9c08f4c6373ec2438443a3567bf1528acc3833538016b9b22a4911f0b29ba55bc4f210927a7b6e54b3d75469776bf13b20aa965d017fce193d5449a27532bd6a7a5c406ac0af50c1508be4c
n=pow(p,3)
phi=(p-1)*p*p
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
print(binascii.unhexlify(hex(m)[2:].strip("L")))