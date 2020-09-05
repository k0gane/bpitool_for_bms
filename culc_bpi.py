import math

def PGF(x,m):
    try:
        return 1+(x-0.5)/(1-x)
    except:
        return m

def BPI_calc(s,k,z,m,p):
    S=PGF(s/m,m)
    K=PGF(k/m,m)
    Z=PGF(z/m,m)
    S_dash=S/K
    Z_dash=Z/K
    if(s>=k):
        return 100*(pow(math.log(S_dash),p))/(pow(math.log(Z_dash),p))
    else:
        return max(-100*(pow(-math.log(S_dash),p))/(pow(math.log(Z_dash),p)), -15)

def sougou_BPI(BPI_list):
    n = len(BPI_list)
    if(n == 0):
        return -20
    k = math.log2(n)
    s = 0
    for i in range(n):
        if(BPI_list[i] < 0):
            s -= pow(-BPI_list[i], k)
        else:
            s += pow(BPI_list[i], k)
    s /= n
    if(s < 0):
        return max(-pow(-s, 1/k), -15)
    else:
        return pow(s, 1/k)

def culc_stob(zenichi, average, p, mscore, BPI):
    a = (BPI/100)**(1/p)
    try:
        z = mscore/(2 * (mscore-zenichi))
    except ZeroDivisionError:
        z = mscore
    k = mscore / (2 * (mscore - average))
    zz = math.log(z / k) * a
    u = k * math.exp(zz)
    return int((2*mscore*u- mscore)/(2 * u))