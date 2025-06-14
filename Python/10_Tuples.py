#Tuples:(Immutable❌)
 
#(1).Accessing the tuple elements:-

#Ex:01
      
fruits = ("apple", "banana", "cherry")

print(fruits[1])
#O/P: banana
print(fruits[-1])
#O/P: cherry


#Ex:02

Name = ("sangamesh", "ram", "Shiva", "krish")

print(Name[2])
#O/P: Shiva
print(Name[-2])
#O/P: Shiva
print(Name[-4])
#O/P: sangamesh



#(2).Slicing tuples:-

#Ex:01

my_tuple = ("banana", 100, "apple",30,  "orange", 890)

print(my_tuple[ : ])
#O/P:('banana', 100, 'apple', 30,'orange', 890)
print(my_tuple[1: :2])
#O/P:(100, 30, 890)
print(my_tuple[0: :2])
#O/P:('banana', 'apple', 'orange')
print(my_tuple[0:5:3])
#O/P:('banana', 30)


#(3).Tuple operations:-

#(a). Tuple concatenation:
    
#Ex:01

first_name = ("sangamesh")
last_name = ("kuri")

name = first_name + " M " + last_name
print(name)
#O/P: sangamesh M kuri


#Ex:02

num_1 = (10,20,30,40,50)
num_2 = (60,70,80,90,100)

numbers = num_1 + num_2
print(numbers)
#O/P: (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)



#(b). Tuple Repeatation:
    
#Ex:01

greeting_tuple = ("Hi there!\n")
print(greeting_tuple*5)
'''
#O/P: 
Hi there!
Hi there!
Hi there!
Hi there!
Hi there!
'''

#Ex:02

welcome_tuple = ("Are U Ready!\n")
print(welcome_tuple*3)
'''
#O/P:
Are U Ready!
Are U Ready!
Are U Ready!
'''

#Ex:03

welcome_tuple = ("Are U Ready\t")*3
print(welcome_tuple)
#O/P: Are U Ready     Are U Ready     Are U Ready


#(c). Checking memberships:
    
#Ex:01
    
my_tuple = ("sangamesh", 100, 999, "mobile")

print("mobile" in my_tuple)
#O/P: True
print(100 not in my_tuple)
#O/P: False
print(99 in my_tuple)
#O/P: False
print("pen" not in my_tuple)
#O/P: True


#(4).Tuple Methods:-

#(a). count():

#Ex:01

random_tuple = ("pen", 1000, 99, 1000, 1000, 8900, "phone", "pen", "books", "pen", "pen")

print(random_tuple.count("pen"))
#O/P: 4
print(random_tuple.count(1000))
#O/P: 3
print(random_tuple.count("phone"))
#O/P: 1


#(b). Index():

#Ex:01
    
fruits_tuple = ("apple", "orange", "mango", "cherry")

print(fruits_tuple.index("cherry"))
#O/P: 3
print(fruits_tuple.index("mango"))
#O/P: 2
