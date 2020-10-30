'''
Created on Oct 17, 2019

@author: Big
'''
#the "working on" array A
A=[]
print("Hello!")
print("   You can apply the following operations to an array:")

#interface function:

def UI(n):
    #DEF: User Interface; returns messages corresponding to different situations
    #INPUT: string 'n' representing the corresponding code linked to the message
    #OUTPUT: no direct output; prints messages
    if n=="error":
        print("Error! There is already another number at this position!")
    elif n=="success":
        print("Success! The number was successfully added.")
    elif n=="start":
        print("To add numbers insert '1'")
        print("To modify elements insert '2'")
        print("To print numbers with a give property '3'")
        print("To obtain different characteristics '4'")
        print("To filter values '5'")
        print("To add random values to the array '6'")
        print("To quit insert '0'")
        return 0
    elif n=="after":
        print("The array looks like this after the operations:",A)
    elif n=="quit":
        print("Program closed")
        print("See ya!")
        return 0
    elif n=="wrong":
        print("Input was not as specified. Insert again:")
        return 0
    elif n=="notf":
        print("Sequence was not found!")
    elif n=="any":
        print("Insert any key to continue.")
        y=input()
        if y:
            y=0
        return 0
    print("Insert any key to continue.")
    y=input()
    if y:
        y=0

#auxiliary functions:

def input_p(p,n):
    while p<0 or p>n:
        UI("wrong")
        p=int(input())
    return p

def rand():
    #D: this functions gives A elements that can be verified by most functions
    #I: no input, only gets called
    #O: no output, only changes A values
    B=[0,34,8,-9,5,24,-1,2,0,-16,64,7,-128]
    for el in B:
        A.append(el)

def rmvneg():
    i=0
    while i<len(A):
        if A[i]<0:
            del A[i]
        i+=1

def rmvprimes():
    i=0
    while i<len(A):
        if vfprime(A[i]):
            del A[i]
        i+=1

def maxof(s,e):
    maxs=A[s]
    for i in range(s+1,e+1):
        if maxs<A[i]:
            maxs=A[i]
    return maxs     

def gcd(a,b):
    if a==b:
        return a
    else:
        if a>b:
            return gcd(a-b,b)
        else:
            return gcd(a,b-a)

def gcdof(s,e):
    g=A[s]
    for i in range(s+1,e+1):
        g= gcd(A[i],g)
    return g

def sumof(s,e):
    se=0
    for i in range(s,e+1):
        se+=A[i]
    return se

def odd(s,e):
    B=[]
    for i in range(s,e+1):
        if not A[i]%2==0:
            B.append(A[i])
    return B

def showprime(s,e):
    B=[]
    for i in range(s,e+1):
        if not A[i]%2==0:
            B.append(A[i])
    return B

def vfprime(n):
    if n==1:
        return False
    if n==2:
        return True
    d=2
    while d<=n//2:
        if n%d==0:
            return False
        if d==2:
            d=3
        else:
            d+=2
    return True

def rmvseq(B,C):
    (start,end)=find_seq(B)
    while end!=0:
        A[start:end+1]=C
        (start,end)=find_seq(B)

def read_to_array_int(s,B):
    ok=0
    nr=0
    
    for el in s:
        if el!=" ":
            nr=nr*10+int(el)
            ok=1
        else:
            if ok==1:
                B.append(nr)
                nr=0
                ok=0
    if ok==1:
        B.append(nr)

def find_seq(B):
    #D: finds the given seq
    #I: an array of nbrs
    #O: the start and end index of the found seq
    s=0
    e=0
    ok=0
    c=0
    
    for i in range(len(A)):
        if c<=len(B)-1:
            if A[i]==B[c]:
                if ok==0:
                    s=i
                    e=i
                    ok=1
                    c+=1
                else:
                    e=i
                    c+=1
            else:
                ok=0
                s=0
                e=0
                c=0
        else:
            if c==len(B):
                return s,e
    return 0,0

def rplcarray():
    #D: replaces the sub-arrays with the given sub-arrays
    #I: no input
    #O: no output
    B=[]
    C=[]
    print("Insert the sub-array to be modified:")
    s=input()
    read_to_array_int(s, B)
    print("Insert the sub-array to modify with:")
    s=input()
    read_to_array_int(s, C)
    rmvseq(B, C)

def rmvarray(s,e):
    #D: removes array from A
    #I: start pos and end pos
    #O: A without the given seq
    #        for i in range(1,e-s+2):
    #            del A[s]
    for i in range(e+1,len(A)):
        A[i-(e-s+1)]=A[i]
    #then i wanted to pop the end of the list
    for i in range(e-s+1):
        del A[len(A)-1]

def insertin(nbr,k,A):
    #D: inserts a nbr in the array
    #I: the number nbr
    #O: no actual output
    
    #checks if the position is already in the allocated array
    #if not, allocates space in the array until that pos
    while k>len(A)-1:
            A.append(0)
    #checks if there is already a number in that position
    if len(A)>1:
        A[k+1:]=A[k:]
        A[k]=nbr
    else:
        A[k]=nbr
    return A

#test functions for aux:

def test_input_p():
    assert(input_p(3,5)==3)
    assert(input_p(53,100)==53)
    assert(input_p(2,4)==2)
    assert(input_p(4,5)==4)
    assert(input_p(70,79)==70)


def addnbr():
    #D: the branch for number insertion
    #I: no input, only gets called
    #O: no output, only calls branches
    
    #interface
    print("To add at the end '1'")
    print("To add inside '2'")
    
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),2)
    #number to be inserted
    nbr=int(input("Insert the number:"))
    
    if p==1:
        #end branch
        A.append(nbr)
        UI("success")
    elif p==2:
        #inside branch
        insertin(nbr,int(input("Insert position:")),A)

def rmvnbr():
    #D: the branch for number removal
    #I: no input, only gets called
    #O: no output, only calls branches
    #Interface
    print("To remove an element '1'")
    print("To remove a sub-array '2'")
    print("To replace sub-arrays with arrays '3'")
    
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),3)
    if p==1:
        k=int(input("Insert element position:"))
        del A[k]
    elif p==2:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        rmvarray(s, e)
    elif p==3:
        rplcarray()

def propnbr():
    #D: the branch for number properties
    #I: no input, only gets called
    #O: no output, only calls branches
    #Interface
    print("To return prime numbers '1'")
    print("To return odd numbers '2'")
    
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),2)
    if p==1:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        print("The numbers are:",showprime(s,e))
    elif p==2:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        print("The numbers are:",odd(s,e))

def charnbr():
    #D: the branch for number characteristics
    #I: no input, only gets called
    #O: no output, only calls branches
    #Interface
    print("To return sum '1'")
    print("To return greatest common divisor '2'")
    print("To return max '3'")
    
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),3)
    if p==1:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        print("The sum is:",sumof(s, e))
    elif p==2:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        print("The greatest common divisor is:",gcdof(s,e))
    elif p==3:
        s=int(input("Insert the start position:"))
        e=int(input("Insert the end position:"))
        print("The max is:",maxof(s, e))

def filternbr():
    #D: the branch for number filter
    #I: no input, only gets called
    #O: no output, only calls branches
    #Interface
    print("To delete primes '1'")
    print("To delete negative '2'")
    
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),2)
    if p==1:
        rmvprimes()
    elif p==2:
        rmvneg()

#main function:

def run():
    #DEF: The main function; the interface for the user
    UI("start")
    test_input_p()
    # p represents the branch of operations the user chooses
    p=input_p(int(input()),6)
    if p==0:
        UI("quit")
        return 0
    elif p==1:
        addnbr()
        UI("after")
    elif p==2:
        rmvnbr()
        UI("after")
    elif p==3:
        propnbr()
        UI("any")
    elif p==4:
        charnbr()
        UI("any")
    elif p==5:
        filternbr()
        UI("after")
    elif p==6:
        rand()
        UI("after")
    #returns back to the beggining until insert 0
    run()
run()