name = "Sangamesh"
height = 5.8
weight = 51
is_student = True 

print(type(name))
#o/p:<class 'str'>

print(type(height))
#o/p:<class 'float'>

print(type(weight))
#o/p:<class 'int'>

print(type(is_student))
#o/p:<class 'bool'>


#(1)int to float:

#Ex:01
weight = 51
weight_float = float(weight)
print(weight_float)
#O/P:51.0

#Ex:02
available_seats = 18
available_seats_float = float(available_seats)
print(available_seats_float)
#O/P:18.0


#(2)float to int:

#Ex:01
height = 5.8
height_int = int(height)
print(height_int)
#O/P:5

#Ex:02
The_refractive_index_of_water = 1.33
The_refractive_index_of_water_int= int(The_refractive_index_of_water)
print(The_refractive_index_of_water_int)
#O/P:1


#(3)string to boolean:

#For non empty strings:'True'

#Ex:01
name = "sangamesh"
name_bool = bool(name)
print(name_bool)
#O/P:True

#Ex:02
Name = " " #space left b/w 2 quotes
Name_bool = bool(Name)
print(Name_bool)
#O/P:True


#For empty strings:'False'

#Ex:01
_name = ""   #No space left 
_name_bool = bool(_name)
print(_name_bool)
#O/P:False


#Boolean to string :

#Ex:01
is_student = True
is_student_str = str(is_student)
print(is_student_str)
#o/p:True » "True"  (string)

#Ex:02
is_business_man = False
is_business_man_str = str(is_business_man)
print(is_business_man_str)
#o/p:False » "False"  (string)


