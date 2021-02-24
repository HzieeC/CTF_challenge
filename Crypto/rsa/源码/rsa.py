from Crypto.Util.number import *
from gmpy2 import *
from flag import flag

m = bytes_to_long(flag.encode())
p = getPrime(512)
sa=getPrime(300)
q = next_prime(p+sa)
n = p*q
e=0x10001
c = pow(m,e,n)

print("e = %d"%e)
print("n = %d"%n)
print("c = %d"%c)
print("sa = %d"%sa)
'''
output:
e = 65537
n = 100148073604335289554095291467545577982001752696042647772358970233372673280794973170134304852503602106037497335670016915327020337317268585205468781705636418138265402246350877474710554180048071922329029978013803472729220266642130377653389784918947642513706467657830115682198986208029563125486999001415401591141
c = 63373697589430128472539764741716538550990268953811272228714547431317073117085340058808310362301482546966584855958704511815799038341668632355519314346172217334749982628687153653605857939891805598299174553089204231407259706726053939419199619157253782924171029993034834544348308035645202340632096133381337000730
sa = 1311945984620309311987416651473000695161468148977851596139553884414631534694355100608689433
'''