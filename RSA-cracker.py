import numpy
delers = []

def factors(n):
    
    if n%2==0:
        delers.append(2)
        delers.append(int(n/2))
    
    else:
        x=numpy.ceil(numpy.sqrt(n))
        while True:
            y=numpy.sqrt(numpy.power(x, 2)-n)
            yf=int(y)
            if (yf*yf==numpy.power(x, 2)-n):
                delers.append(int(x+y))
                delers.append(int(x-y))
                p1=int((x+y)-1)
                p2=int((x-y)-1)
                phi=p1*p2
                return phi
                break
            else:
                x=x+1

def modinverse(a, m):
    for x in range(0, m):
        if (((a%m) * (x%m)) % m == 1):
            M=(r**x)%n
            print("j: " + str(x))
            print("Decrypted message: " + str(int(M)))

while True:
    print("----RSA-cracker----")
    n=int(input("Enciphering modulus: "))
    k=int(input("Enciphernig exponent: "))
    r=int(input("Encrypted message: "))
    phi=factors(n)
    print("Primes: " + str(delers))
    print("Phi("+str(n)+"): " + str(phi))
    modinverse(k, phi)
    delers.clear()
