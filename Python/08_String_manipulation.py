#(★). String manipulation:
        
#(1). Common string operations:

#(a).Concatenation:

#Ex:01 Username Generation:-

first_name = "Sangamesh"
last_name = "MK"
numerical = "94"
username = first_name + "_" + last_name + "." + numerical

print(username)
#O/P: Sangamesh_MK.94


#Ex:02 Username Generation:-

first_name = "matured"
last_name = "mind"
numerical = "3421"
username = first_name + "_" + last_name + numerical

print(username)
#O/P: matured_mind3421


#Ex: 03 Email Generation:-

name = "sangameshmk"
numerical = "94"
domain = "gmail.com"
Email = name + numerical + "@" + domain

print(Email)
#O/P: sangameshmk94@gmail.com

#Ex:04 Creating file paths:-

folder = "document"
file = "report"
format = "pdf"
file_path = folder + "/" + file + "." + format

print(file_path)
#O/P: document/report.pdf


#Ex:05 date format string:-

day = "08"
month = "08"
year = "2006"
date = day + "/" + month + "/" + year

print(date)
#O/P: 08/08/2006


#(b).Repeatation:

#Ex:01 Multiple times 

name = "Sangamesh \n"

print(name*10)

'''
#O/P: 
sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
'''


#Ex:02 Creating ASCII or Text-Bsed UI Elements:-

print("=" * 50)
print("WELCOME TO MY APP")
print("=" * 50)
#O/P:
'''
================================================== 

WELCOME TO MY APP

==================================================
'''

#Ex:03 Password Masking (Visual only)

password = "mysecrete3421"
mask = "•"*len(password)

print("password:", mask)
#O/P: password: •••••••••••••


# (2). String Methods:
    
#(a). upper()

#Ex:01

message = "Hello, World!" 

print(message. upper())
#O/P: HELLO, WORLD!

#Ex:02

stored_username = "SANGAMESH"
entered_username = "sangamesh"

if stored_username == entered_username.upper():
    print("Login successful")
#O/P: Login successful


#Ex:03

invoice_prefix = "inv"
invoice_number = "00789"

print((invoice_prefix + invoice_number).upper())
#O/P: INV00789


#Ex:04

message = "stop spamming!"
print("ALERT:", message.upper())
#O/P: ALERT: STOP SPAMMING!

 
#(b). lower()

#Ex:01

message = "Hello, World"

print(message. lower())
#O/P: hello, world


#Ex:02

user_input = "BENGALURU"
standard_city = user_input.lower()

print(standard_city)
#O/P: bengaluru


#Ex:03

email_from_user = "SANGAMESHMK94@GMAIL.COM"
registered_email = "sangameshmk94@gmail.com"

if email_from_user.lower() == registered_email:
    print("Email verified!")
#O/P: Email verified!


#Ex:04

search_query = "Python PROGRAMMING"
database_entry = "python programming"

if search_query.lower() == database_entry:
    print("Found in database!")
#O/P: Found in database!


#(c). Strip:
   
#Ex:01

message = " Hello, World! "
print(message. strip())
#O/P:Hello, World


#Ex:02

name = "    sangamesh    "
print(name. strip())
#O/P: sangamesh


#(d). replace("old", "new")

#Ex:01
message = "Hello, World"
print(message. replace("World","Python"))
#O/P: Hello, Python


#Ex:02
city_name = "ಬೆಂದಕಾಳೂರು"
print(city_name. replace("ಬೆಂದಕಾಳೂರು", "ಬೆಂಗಳೂರು"))
#O/P: ಬೆಂಗಳೂರು 


#(3). Accessing string characters:

#Ex:01

State = "Karnataka"

print(State[0])
print(State[2])
print(State[3])
print(State[5])
print(State[7])
print(State[1])

'''

#O/P: 
K
r
n
t
k
a

'''
#NOTE: WE CAN ALSO USE NEGATIVE INDEXING FROM THE END OF THE WORD.

State = "Karnataka"

print(State[-1])
print(State[-4])
print(State[-3])
print(State[-7])
print(State[-2])
print(State[-9])

'''

#O/P:
    
a
t
a
r
k
K

'''


#(4).Slicing strings:
 
'''
syntax:      
print(start:end:step)
         or
print(includes:excludes:skip)

'''

#Ex:01

username = "matured_mind3421"

print(username[ :7])
#O/P: matured 
print(username[8:16])
#O/P: mind3421
print(username[ : ])
#O/P: matured_mind3421
print(username[ : :2])
#O/P: mtrdmn32
print(username[ : :4])
#O/P: mrm3


#(★).Comments in python:

#(a). For single line comment:-

#Ex:01

#This is an single line comment.

#(b). For multilines comment:-

#Ex:01

"""
Hi, there... this is an multi-line comment. So we can write these type of comments in many lines as we want

"""

#Ex:02

'''
Hi, there... this is an multi-line comment. So we can write these type of comments in many lines as we want
'''


#(★). Escape Sequence:starts with the " \ " (backslash).

#(1). \n: new line

#Ex:01

text = "Ram\nLaxman"
print(text)

'''
#O/P: Ram
      Laxman
      
'''      
      
 
#Ex:02

greeting = "Good morning🥰🌄 \n"
print(greeting*5)

'''

#O/p:
Good morning🥰🌄
Good morning🥰🌄
Good morning🥰🌄
Good morning🥰🌄
Good morning🥰🌄

'''

#(2). \t: tab space

#Ex:01

name = "Sangamesh\tMK"
print(name)
#O/P: Sangamesh       MK

#Ex:02

text = "Hello!\t"
print(text*5)
#O/P: Hello!  Hello!  Hello!  Hello!  Hello!



#(3). \\: Back slash

#Ex:01

text = "Hello\\World"
print(text)
#O/P: Hello\World

message = "Hiii\\There"
print(message)
#O/P: Hiii\There












   
   
