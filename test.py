import math 

def exp_func(x, y, m):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value % m
        if(exp[i:i+1]=='1'):
            value = value*x % m
    return value

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
    return amount

def step1(n):
    for b in range(2,int(math.log2(n)+1)):
        a = n**(1/b)
        if math.floor(a) == a:
            #print("[-]"+str(n)+" is no Prime 1")
            return False
    return True

def step2(n):
    mk = math.log2(n)**2
    nexr = True
    r = 1
    while nexr == True:
        r += 1
        nexr = False
        k = 0
        while k <= mk and nexr == False:
            k = k+1
            if exp_func(n,k,r) == 0 or exp_func(n,k,r) == 1:
                nexr = True
    return r
        

def step3 (n, r):
    for a in range(1,r+1):
        if ((1 < math.gcd(a, n)) and (math.gcd(a,n) < n)):
            #print("[-]"+str(n)+" is no Prime 3")
            return False

def step4(n, r):
    if n > 5690034:
        if n <= r:
            # print("[+]"+str(n)+" is a Prime Step 4")
            return True


def step5(n, r):
    x = 7
    max = math.sqrt(phi(r))
    rn = math.floor(max*math.log2(n))
    cache = exp_func(x,n,n)
    for a in range(1, rn+1):
        b = exp_func((x+a),n,n) #((x + a) ** n) % n
        l = (cache+a)%n #(x ** n + a) % n
        if b != l:
            #print("[-]"+str(n)+" is no Prime 5")
            return False
    # print("[+]"+str(n)+" is a Prime Number Step 5")
    return True


def aks(n):
    #print("Testing Number: "+str(n))
    if step1(n) == True:
        r = step2(n)
        if step3(n, r) != False:
            if step4(n, r) != True:
               return step5(n, r)
    return False

def find_unique_primes(num):
	unique = set()
	if num%2==0:
		unique.add(2)
		while num%2==0:
			num/=2
	for i in range(3,int(num**(1/2))+1,2):
		if num%i==0:
			unique.add(i)
			while num%i==0:
				num/=i 
	if num>2:
		unique.add(int(num))
	return unique

n = 1197060983074059442676331442468136267958543002047585409352167850146454379702101825405935828467629329874635873245
# (2996863034895*(2**(1290000))-1)
# while True:
res = math.ceil(math.pow(math.log(n,2),\
	math.log(math.log(n,2),2))**2)
end = math.ceil(n**(1/2))
print(aks(3))
print(end)
for i in range(2,end):
	if aks(i) and n%i==0:
		print(i)
	# n+=1 
print("Done")
