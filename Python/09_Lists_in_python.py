#. Lists in python:
 
       
#(1). Accessing List elements:-

#Ex:01

fruits = ["apple", "banana", "cherry", "grapes"]

print(fruits[0])
#O/P: apple

print(fruits[3])
#O/P: grapes 

print(fruits[2])
#O/P: cherry


#Ex:02

my_list = [100, "ram", 108, "success", 55]

print(my_list[2])
#O/P: 108

print(my_list[3])
#O/P: success


#Ex:03

list_of_items = ["book", "pen", "pencil", "fan", "phone"]

print(list_of_items[2])
#O/P: pencil

print(list_of_items[4])
#O/P: phone


#We can also use -ve indexing:

#Ex:04

names = ["sangamesh", "ram", "raj"]

print(names[-1])
#O/P: raj

print(names[-3])
#O/P: sangamesh



#(2). Modifying List elements:-

#(★). Changing the specific element:    

#Ex:01

fruits = ["apple", "banana", "cherry", "grapes"]

fruits[1] = "orange"
print(fruits)
#O/P: ['apple', 'orange', 'cherry', 'grapes']


#Ex:02
my_lists =["AIDS", "AIML", "CSE", "BCI"]
my_lists[3] = "CIVIL"
print(my_lists)
#O/P: ['AIDS', 'AIML', 'CSE', 'CIVIL']

my_lists[-2] = "IAS"
print(my_lists)
#O/P: ['AIDS', 'AIML', 'IAS', 'CIVIL']



#(★). Adding the elements:
    
#(a). append() :-

fruits = ["apple", "banana", "cherry", "grapes"]

#Ex:01

fruits.append("lemon")
print(fruits)
#O/P: ['apple', 'banana', 'cherry', 'grapes', 'lemon']

#Ex:02

fruits.append("watermelon")
print(fruits)  
#O/P: ['apple', 'banana', 'cherry', 'grapes', 'lemon', 'watermelon']


#(b). insert() :-

fruits = ["apple", "banana", "cherry", "grapes"]

#Ex:01

fruits.insert(1,"watermelon")
print(fruits)
#O/P: ['apple', 'watermelon', 'banana', 'cherry', 'grapes']

#Ex:02

fruits.insert(4,"kiwi")
print(fruits)
#O/P: ['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'grapes']


#(★). Removing elements:
    
#(a). remove()

fruits = ["apple", "banana", "cherry", "watermelon", "grapes"]

#Ex:01

fruits.remove("watermelon")
print(fruits)
#O/P: ['apple', 'banana', 'cherry', 'grapes']

#Ex:02

fruits.remove("apple")
print(fruits)
#O/P:['banana', 'cherry', 'grapes']



#(b). pop()

fruits = ["apple", "banana", "cherry", "grapes"]

#Ex:01

fruits.pop(1)
print(fruits)
#O/P:['apple', 'cherry', 'grapes']

#Ex:02

fruits.pop(-2)
print(fruits)
#O/P: ['apple', 'grapes']



#(c). clear()

#Ex:01

fruits = ["apple", "banana", "cherry", "grapes"]
fruits.clear()
print(fruits)
#O/P: []



#(3). Slicing Lists:-

#Ex:01

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[ : ])
#O/P: [1,2,3,4,5,6,7,8,9,10]

print(numbers[2: :2])
#O/P: [3,5,7]

print(numbers[1: :2])
#O/P: [2,4,6,8,10]



#(4).List functions and methods:-

#(★). Common functions:
   
#(a). len(lists):-

#Ex:01

fruits = ["apple", "banana", "cherry", "grapes"]
print(len(fruits))
#O/P: 4

#Ex:02

my_list = [99, "master", 30, "evolve", 100, 1947, "Jai Hind"]
print(len(my_list))
#O/P: 7


#(b). sorted(list):-returns a new sorted list (original stays same).

#Ex:01

designation = ["chief", "prime", "governor"]

print(sorted(designation))
#O/P:['chief', 'governor', 'prime']

print(designation)
#O/P:['chief', 'prime', 'governor']


#(c). sum(list):-

#Ex:01

only_num = [11,22,33,44,55,66]
print(sum(only_num))
#O/P: 231

#Ex:02

just_num = [45,99,100,6789]
print(sum(just_num))
#O/P: 7033



#(★). Common methods:
    
#(a). index(element):-

#Ex:01

fruits = ["apple", "banana", "grapes", "orange"]

print(fruits.index("banana"))
#O/P: 1
print(fruits.index("orange"))
#O/P: 3
print(fruits.index("grapes"))
#O/P: 2



#(b). count(element):-

#Ex:01

numbers = [1,2,4,10,1,1,3,88,99, 100,10,100,10,10,10]

print(numbers.count(1))
#O/P: 3
print(numbers.count(10))
#O/P: 5
print(numbers.count(100))
#O/P:2

#(c). reverse():-

#Ex:01

fruits = ["apple", "banana", "cherry", "grapes"]
fruits.reverse()
print(fruits)
#O/P: ['grapes', 'cherry', 'banana', 'apple']


#Ex:02

my_lists = [99, "pen", "books", 143, 999]
my_lists.reverse()
print(my_lists)

#O/P:[999, 143, 'books', 'pen', 99]


#(d). sort():sorts the original list in-place.

#Ex:01

num = [12,99,2,102,-2,444]
num.sort()
print(num)
#O/P: [-2, 2, 12, 99, 102, 444]

#Ex:02

frnds_weight = [2.1, 3.4, 6.1, 5.9, 4.4]
frnds_weight.sort()
print(frnds_weight)
#O/P: [2.1, 3.4, 4.4, 5.9, 6.1]


#(5).Nested lists:
    
matrix = [[1,2,3], [4,5,6], [7,8,9]]

'''
↪️THE ABOVE MATRIX IS SHOWN LIKE THIS AND GIVES ROWS AND COLUMNS:
              
               0 1 2
               | | |
matrix =   0—[[1,2,3],
           1—[4,5,6],
           2—[7,8,9]]


'''

print(matrix) 
#O/P: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])
#O/P: [1,2,3] ¡e., The first index always represents the "ROW" and 2nd is "COLUMN".

print(matrix[0][0])
#O/P: 1

print(matrix[2][2])
#O/P: 9

print(matrix[1])
#O/P: [4,5,6]

  


   

