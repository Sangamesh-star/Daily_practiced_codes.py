#SETS IN PYTHON:-

'''
Syntax:
    my_set = {element1, element2, element3, element4}
    
'''

#(★). Creation of an empty set:
   
empty_set = set()
print(empty_set)
#O/P: set()


#(1).Set Operations:
    
#(a). Union: (|): Combines and deletes repeated elements.

#Ex:01

set_1 = {1,2,3,4}
set_2 = {4,5,6,7}

union_set = set_1 | set_2
print(union_set)
#O/P: {1, 2, 3, 4, 5, 6, 7}


#Ex:02

my_set = {"computer"}
My_set = {"science"}

whole_set = my_set | My_set
print(whole_set)
#O/P: {'science', 'computer'}


    
#(b). Intersection (&):
 
#Ex:01

set_1 = {1,2,3,4}
set_2 = {4,5,6,7}

whole_set = set_1 & set_2
print(whole_set)
#O/P: {4}


#Ex:02

name = {"sangamesh", "ram","ravan", "raj"}
Name = {"sangamesh", "ravi", "anand","raj"}

Names = name & Name
print(Names)
#O/P: {'raj', 'sangamesh'}


#(c). Difference (-):
    
#Ex:01

set_1 = {1,2,3,4,10,20}
set_2 = {1,2,3,99,100,87}
difference_set = set_1 - set_2

print(difference_set)
#O/P: {10, 4, 20}

#Ex:02

names_1 = {"sangamesh", "raj", "ram"}
names_2 = {"raj", "prem", "anand","naveen"}

difference_set = names_1 - names_2

print(difference_set)
#O/P: {'sangamesh', 'ram'}

 

#(d).Symmetric Difference (^): gives what is not in both.
    
#Ex:01

set_1 = {1,2,3,4}
set_2 = {4,5,6,7}
sym_dif_set = set_1 ^set_2 
print(sym_dif_set) 
#O/P: {1, 2, 3, 5, 6, 7} 


#(2).Set Methods:
    
#(a).add():
    
#Ex:01

fruits = {"apple", "banana", "cherry", "grapes"}
fruits.add("mango")

print(fruits)
#O/P: {'banana', 'cherry', 'apple', 'mango', 'grapes'}


#Ex:02

names = {"sangamesh", "Vivek"}
names.add("akshay")

print(names)
#O/P: {'akshay', 'Vivek', 'sangamesh'}


#(b).remove():gives an error if the item is not in the set.

#Ex:01

fruits = {"apple", "mango", "grapes"}

fruits.remove("grapes")
print(fruits)        
#O/P: {'apple', 'mamgo'}

'''
fruits.remove("cherry")
print(fruits)
#O/P key error occurs ❌
'''


#Ex:02

names = {"vishal", "ram", "chandan", "surya"}
names.remove("vishal")

print(names)
#O/P: {'surya', 'ram', 'chandan'}


#(c). discard():doesn't give an error if the item is not in the set.

#Ex:01

fruits = {"apple", "mango", "grapes"}
fruits.discard("cherry")
print(fruits)
#O/P: {'grapes', 'apple', 'mango'} No error✅

#Ex:02

my_set = {100, "pencil", "books", 200}
my_set.discard("pen")
print(my_set)
#O/P: {200, 100, 'pencil', 'books'} No error✅


#(d). pop():
    
#Ex:01

items = {"powder", "comb", "coconut oil",}
items.pop()
print(items)
#O/P: {'coconut oil', 'comb'}

#Ex:02

my_set = {"bags","clothes", "power bank"}
my_set.pop()
print(my_set)
#O/P: {'power bank', 'clothes'}



#(e). clear():
    
#Ex:01

fruits = {"apple", "water melon", "grapes", "orange", "mango"}

fruits.clear()

print(fruits)
#O/P: set()

print(fruits.clear())
#O/P: None

