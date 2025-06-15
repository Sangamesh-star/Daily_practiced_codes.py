#Dictionaries in Python:-

'''
syntax :
    my_dict = {
       "key 1" : "value 1",
       "key 2" : "value 2",
       "key 3" : "value 3"
    }
    
'''

#(1).Accessing dictionary elements:
    
#Ex:01

karnataka_foods = {
    "Bengaluru" : "Mudde",
    "Mysuru"    : "Mysore Pak",
    "Mangaluru" : "Fish"
}

print(karnataka_foods["Bengaluru"])
#O/P: Mudde

print(karnataka_foods["Mysuru"])
#O/P: Mysore Pak

print(karnataka_foods["Mangaluru"])
#O/P: Fish 


#Ex:02

my_dict = {
    "Teachers"    : "Teach",
    "Polices"     : "Law and order",
    "Politicians" : "Rule",
    "Doctors"     : "Health"
}

print(my_dict["Doctors"])
#O/P: Health
print(my_dict["Polices"])
#O/P: Law and order
print(my_dict["Teachers"])
#O/P: Teach
print (my_dict["Politicians"])
#O/P: Rule

#NOTE: We can also use "get()". Bcz-It doesn't throw any error if the keys are not in the dict.

#Ex:03

karnataka_cities = {
    "Bagalkot"  : "ಕೋಟೆಗಳ ನಾಡು",
    "ilkal"     : "ಸೀರೆಗಳ ನಾಡು",
    "Davanageri": "ಬೆಣ್ಣೆನಗರಿ",
    "Dharwad"   : "ಪೇಡಾ ನಗರಿ"
}

print(karnataka_cities.get("Bagalkot"))
#O/P: ಕೋಟೆಗಳ ನಾಡು
print(karnataka_cities.get("Davanageri"))
#O/P: ಬೆಣ್ಣೆನಗರಿ
print(karnataka_cities.get("Dharwad"))
#O/P: ಪೇಡಾ ನಗರಿ

print(karnataka_cities.get("Shivamogga"))
#O/P: None

print(karnataka_cities. get("Ramanagar", "Not found"))
#O/P: Not found


#(2).Adding dictionary elements:

#Ex:01 

Courses = {
    "Engineering" : "Computer science",
    "Medical"     : "MBBS",
    "Degree"      : "B.Sc or BA",
}

Courses["Allied Sc."] = "B.V.V.S"

print(Courses)
#O/P: {'Engineering': 'Computer science', 'Medical': 'MBBS', 'Degree': 'B.Sc or BA', 'Allied Sc.': 'B.V.V.S'}


#Ex:02

karnataka_foods = {
    "Bengaluru" : "Mudde",
    "Mangaluru" : "Fish",
    "Mysuru"    : "Mysore Pak"
}

karnataka_foods["Bagalkot"] = "Roti"
print(karnataka_foods)
#O/P: {'Bengaluru': 'Mudde', 'Mangaluru': 'Fish', 'Mysuru': 'Mysore Pak', 'Bagalkot': 'Roti'}



#(3).Updating dictionary elements:
    

mobile_brands = {
    "India"       : "Lava",
    "China"       : "Oppo",
    "USA"         : "Apple",
    "South Korea" : "MI"
}

mobile_brands["South Korea"] = "Samsung"

print(mobile_brands)
#O/P: {'India': 'Lava', 'China': 'Oppo', 'USA': 'America', 'South Korea': 'Samsung'}



#(4).Removing elements from a  dictionary:  
   
   
#(a). pop()  

#Ex:01

karnataka_foods = {
    "Bengaluru" : "Mudde",
    "Mysuru"    : "Mysore Pak",
    "Bagalkot"  : "Roti",
    "Mangaluru" : "Fish"
}

karnataka_foods.pop("Mysuru")
print(karnataka_foods)
#O/P: {'Bengaluru': 'Mudde', 'Bagalkot': 'Roti', 'Mangaluru': 'Fish'}

karnataka_foods.pop("Ilkal", "Hungund")
print(karnataka_foods)
#O/P: {'Bengaluru': 'Mudde', 'Bagalkot': 'Roti', 'Mangaluru': 'Fish'}

#NOTE: "Hungund" here is a default value — so pop() doesn’t crash when "Ilkal" is not in the dictionary.


#Ex:02

My_dict = {
    "Bags"     : "Books",
    "Books"    : "Writings",
    "writings" : "Feelings"
}

My_dict.pop("Bags")
print(My_dict)
#O/P: {'Books': 'Writings', 'writings': 'Feelings'}



#(b).Del()

#Ex:01

karnataka_cities = {
    "Bagalkot"  : "ಕೋಟೆಗಳ ನಾಡು",
    "ilkal"     : "ಸೀರೆಗಳ ನಾಡು",
    "Davanageri": "ಬೆಣ್ಣೆನಗರಿ",
    "Dharwad"   : "ಪೇಡಾ ನಗರಿ"
}


del karnataka_cities["Davanageri"]

print(karnataka_cities)
#O/P: {'Bagalkot': 'ಕೋಟೆಗಳ ನಾಡು', 'ilkal': 'ಸೀರೆಗಳ ನಾಡು', 'Dharwad': 'ಪೇಡಾ ನಗರಿ'}

#NOTES: del does not support default values — so you can't avoid an error by giving a default like you can with pop().


#Ex:01

karnataka_cities = {
    "Bagalkot"  : "ಕೋಟೆಗಳ ನಾಡು",
    "ilkal"     : "ಸೀರೆಗಳ ನಾಡು",
    "Davanageri": "ಬೆಣ್ಣೆನಗರಿ",
    "Dharwad"   : "ಪೇಡಾ ನಗರಿ"
}

print(karnataka_cities)

#O/P: {'Bagalkot': 'ಕೋಟೆಗಳ ನಾಡು', 'ilkal': 'ಸೀರೆಗಳ ನಾಡು', 'Davanageri': 'ಬೆಣ್ಣೆನಗರಿ', 'Dharwad': 'ಪೇಡಾ ನಗರಿ'} Key not found!

# Trying to delete a key that does NOT exist

try:
    del karnataka_cities["Hubli"]
except KeyError:
    print("Key not found!")
  
# Display dictionary after attempted deletion
print("\nAfter deletion attempt:")
print(karnataka_cities)

        
#O/P: {'Bagalkot': 'ಕೋಟೆಗಳ ನಾಡು', 'ilkal': 'ಸೀರೆಗಳ ನಾಡು', 'Davanageri': 'ಬೆಣ್ಣೆನಗರಿ', 'Dharwad': 'ಪೇಡಾ ನಗರಿ'}  
