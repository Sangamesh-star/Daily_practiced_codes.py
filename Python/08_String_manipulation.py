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
#O/P: ================================================== 
WELCOME TO MY APP   ==================================================


#Ex:03 Password Masking (Visual only)

password = "mysecrete3421"
mask = "•"*len(password)

print("password:", mask)
#O/P: password: •••••••••••••





   
   
