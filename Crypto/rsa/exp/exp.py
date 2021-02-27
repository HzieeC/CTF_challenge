from Crypto.Util.number import *
import gmpy2

e=0x10001
n = 100148073604335289554095291467545577982001752696042647772358970233372673280794973170134304852503602106037497335670016915327020337317268585205468781705636418138265402246350877474710554180048071922329029978013803472729220266642130377653389784918947642513706467657830115682198986208029563125486999001415401591141
sa = 1311945984620309311987416651473000695161468148977851596139553884414631534694355100608689433
low=0
hei=n
p=0
#二分法爆破p
for i in range(1000000):
    mid=(low+hei)//2
    n_pri=(p+mid)*gmpy2.next_prime(p+mid+sa)
    if n_pri>n:
        print(1)
        hei=mid
    if n_pri<n:
        print(0)
        low=mid
    if n_pri==n:
        print(p+mid)
        p=p+mid
        break
q=n//p
print(p*q==n)
c = 63373697589430128472539764741716538550990268953811272228714547431317073117085340058808310362301482546966584855958704511815799038341668632355519314346172217334749982628687153653605857939891805598299174553089204231407259706726053939419199619157253782924171029993034834544348308035645202340632096133381337000730
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
flag=long_to_bytes(m)
print(flag)