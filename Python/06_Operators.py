# OEPERATORS:


#(1). Arithmatic Operators:-

"""
The common arithmatic operators are :
    (a) Addition(+)
    (b) Subtraction(-)
    (c) Multiplication(*)
    (d) Division(/)
    (e) floor division(//)
    (f) Modulus|Remainder(%)
    (g) Exponentiation(**)
    
    """
    
#Ex:01
a = 20
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)    
print(a**b)

#O/P:
26
14
120
3.3333333333333335
3
2
64000000

#Ex:02
x = 17
y = 212
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)    
print(x**y)

#O/P: 
229
-195
3604
0.08018867924528301
0
17
716425989505823792538648540073767626675892576849694732684326913196580735298167964731010124669685975067898374061831880656292000030046430685032024215980154922470642416483879645297157019372574748349503234182198215945149340726204603292122144554876114298662164605761



#(2). Assignment Operators:-

#Ex:01

x = 10
print(x)
#O/P: 10

x += 2
print(x)
#O/P: 12

x -= 6
print(x)
#O/P: 6 

x *= 3
print(x)
#O/P: 18

x /= 3
print(x)
#O/P: 6.0 

x %= 2
print(x)
#O/P: 0.0


#Ex:02

x = 99
print(x)
#O/P: 99

x += 20
print(x)
#O/P: 119

x -= 30
print(x)
#O/P: 89

x *= 5
print(x)
#O/P: 445

x /= 4
print(x)
#O/P: 111.25

x %= 3
print(x)
#O/P: 0.25




#(3). Comparison Operators:-

#Ex:01

a = 10
b = 20

print(a==b)
#O/P: False 

print(a!=b)
#O/P: True

print(a>b)
#O/P: False

print(a<b)
#O/P: True

print(a>=b)
#O/P: False

print(a<=b)
#O/P: True


#Ex:02

x = (9*9)
print(x)
#O/P: 81

print(x==81)
#O/P: True

print(x!=81)
#O/P: False

print (x>80)
#O/P: True

print(x<100)
#O/P: True

print(x>=90)
#O/P: False

print(x<=90)
#O/P: True



#(4). Logical Operators:-


#Ex:01

x = 50
y= 100

print(x>20 and y<200)
#O/P: True

print(x>20 or y<200)
#O/P: True

print(not(x>20))
#O/P: False 

print(x<100 and y==50)
#O/P: False

print(x<100 or y==50)
#O/P: True

print(not(y==50))
#O/P: True


#Ex:02

x = "Ram"
y = "Raj"

print(x=="Ram" and y=="Raj")
#O/P: True

print(x=="Ram" or y=="Raj")
#O/P: True

print(x!="Raj" and y=="Ram")
#O/P: False

print(not(x=="Ram"))
#O/P: False



#(5). Memberships Operators:-

#Ex:01

x = "sangamesh"

print("a" in x)
#O/P: True

print("m" not in x)
#O/P: False 

print("r" in x)
#O/P: False 

print("z" not in x)
#O/P: True


#Ex:02

x = "10, 20, 40, 50, 100"

print("10" in x)
#O/P: True

print("30" not in x)
#O/P: True 

print("100" not in x)
#O/P: False

print("1000" in x)
#O/P: False


#Ex:03

my_list = ["sangamesh", 100, "ram", 5, 20, 50, "raj"]

print(100 in my_list)
#O/P: True

print("raj" in my_list)
#O/P: True

print(50 not in my_list)
#O/P: False

print("raj" in my_list)
#O/P: True


#Ex:04

my_tuple = (95, "sangamesh", "ram", 88, 102)

print(95 in my_tuple)
#O/P: True

print("sangamesh" not in my_tuple)
#O/P: False 

print(100 in my_tuple)
#O/P: False

print("ram" in my_tuple)
#O/P: True




#(6). Bitwise Operators:-


'''
Decimal   Binary
------------------
1         00001
2         00010
3         00011
4         00100
5         00101
6         00110
7         00111
8         01000
9         01001
10        01010
11        01011
12        01100
13        01101
14        01110
15        01111
16        10000
17        10001
18        10010
19        10011
20        10100

'''

#(a). Bitwise AND(&)


#Ex:01

a = 6
b = 2
print(a&b)
#O/P: 2


#Ex:02

a = 15
b = 9
print(a&b)
#O/P: 9

#(b). Bitwise OR(|)

#Ex:01

a = 5
b = 3 
print(a|b)
#O/P: 7

#Ex:02

a = 13
b = 20
print(a|b)
#O/P: 29


#(c). Bitwise XOR(^) 

#Ex:01

a = 18
b = 8
print(a^b)
#O/P: 26


#Ex:02

a = 5
b = 19
print(a^b)
#O/P: 22


#(d). Bitwise NOT(~) 

#Ex:01

a = 5
print(~a)
#O/P: -5


#Ex:02

x = 10
print(~x)
#O/P: -10


#(e). Bitwise left shift(<<)

#Ex:01

a = 5
print(a<<1) 
#O/P: 10

#Ex:02

x = 19
print(x<<1)
#O/P: 38




#(f). Bitwise right shift(>>)

#Ex:01

a = 5
print(a>>1)
#O/P: 2


#Ex:02

x = 13
print(x>>1)
#O/P: 6

print(x>>2)
#O/P: 3



