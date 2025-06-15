#CONDITIONAL STATEMENTS IN PYTHON: if, elif, and else.


#(1).The if statement:-

'''
syntax:
    
if condition:
    #code block to execute if the condition is true.
'''

#Ex:01

Time = int(input("Enter time: "))

if Time == 20:
    print("Its time for dinner!.")
#O/P: Its time for dinner!.

#NOTE:Make sure to type the time exactly as 20 to trigger the message.If the input is anything else (like 19 or 21), nothing will happen (no output), because there's no else.



#Ex:02

age = int(input("Enter your age: "))

if age == 19:
    print("You are eligible to vote!.")
#O/P: You are eligible to vote!.

#NOTE:Make sure to type the age exactly as 19 to trigger the message.If the input is anything else (like 18 or 21), nothing will happen (no output), because there's no else.  
      


#(2).The else statement:-

'''
syntax:

if condition:
    #code block if the condition is true.

else:
    #code block if the condition is false.

'''

#Ex:01

time = int(input("ENTER TIME: "))
if time == 18: #6PM
    print("It's time for dinner!.")

else:
    print("It's not dinner time yet!.") 

'''
#O/P: 

ENTER TIME: 18
It's time for dinner!.

ENTER TIME: anytime except 18
It's not dinner time yet!.

'''
      

#Ex:02

book = input("Which Book Are You Searching For Sir ?")

if book.upper() == "BHAGAVADGEETA":
    
    print("Yes😊, your book is there at corner of the rack Sir.")
else:
    print("Sorry😔, your book is out of stock Sir!.")  
    
'''
#O/P:
Which Book Are You Searching For Sir ?BHAGAVADGEETA
Yes😊, your book is there at corner of the rack Sir.

or

Which Book Are You Searching For Sir ?bhagavadgeeta
Yes😊, your book is there at corner of the rack Sir.


Which Book Are You Searching For Sir ?RAMAYANA
Sorry😔, your book is out of stock Sir!.

'''


#(3).The elif statement:-

'''
syntax:
    
if condition 1:
    #code block if the condition 1 is true.
elif condition 2:
    #code block if the condition 2 is true.
else:
    #code block if none of the above conditions are true.
    
'''


#Ex:01

time = int(input("What's the time: "))

if time == 8:
    print("It's time for Breakfast🍞!.")
    
elif time == 14:
    print("It's time for Lunch🍔!.")
    
elif time == 21:
    print("It's time for Dinner🍲!.")
    
else:
    print("It's not the right time to have Food❌!.")    
    
'''            
#O/P:
   
What's the time: 8
It's time for Breakfast🍞!.

What's the time: 14
It's time for Lunch🍔!.

What's the time: 21
It's time for Dinner🍲!.

What's the time: 19
It's not the right time to have Food❌!.

'''       


#(4).Comparison Operators in if statements:-

#Ex:01

age = int(input("ENTER YOUR AGE: "))
if age < 18:
    print("You are not eligible to vote❌")
else:
    print("You are eligible to vote✔️")
    
'''
#O/P:
     
ENTER YOUR AGE: 17
You are not eligible to vote❌

ENTER YOUR AGE: 22
You are eligible to vote✔️

'''    


#(5).Logical Operators in if statements:-

#Ex:01

age = int(input("ENTER YOUR AGE: "))
student_id = input("DO YOU HAVE STUDENT'S ID?(yes/no): ")
has_student_id = student_id == "yes"

if age < 18 and has_student_id:
    print("You are eligible for the discount!.")
elif age < 18 or has_student_id:
    print("You are eligible for the discount!.")
else:
    print("You are not eligible for the discount!.")  

'''
#O/P: 
ENTER YOUR AGE: 15
DO YOU HAVE STUDENT'S ID?(yes/no): yes
You are eligible for the discount!.

ENTER YOUR AGE: 15
DO YOU HAVE STUDENT'S ID?(yes/no): no
You are eligible for the discount!.

ENTER YOUR AGE: 19
DO YOU HAVE STUDENT'S ID?(yes/no): yes
You are eligible for the discount!.

ENTER YOUR AGE: 20
DO YOU HAVE STUDENT'S ID?(yes/no): no
You are not eligible for the discount!.

'''

# EX. ON KSRTC TICKET CHECKING:
    

#(6).Nested if statements:- (if inside the if statemens)

#Ex:01

day = input("WHAT'S THE DAY?: ")
raining = input("IS IT RAINING? (yes/no): ")

weekday = day.lower() == "saturday"  # ✅ Make it lowercase to avoid case mismatch
is_raining = raining.lower() == "yes"

if weekday:
    if not is_raining:
        print("Let's visit Bagalkot😍!")
    else:
        print("It's raining, better stay in 😓")
else:
    print("Let's postpone the visit 🗓️")
    
'''
#O/P:
     
WHAT'S THE DAY?: saturday
IS IT RAINING? (yes/no): no
Let's visit Bagalkot😍!

WHAT'S THE DAY?: saturday
IS IT RAINING? (yes/no): yes
It's raining, better stay in 😓

WHAT'S THE DAY?: monday
IS IT RAINING? (yes/no): no
Let's postpone the visit 🗓️

''' 
                           
