#Ex:01

"""
wanted output: "SANGAMESH meets RANI and their age difference is 2"

"""
boy_name = input("BOY'S NAME: ")
girl_name = input("GIRL'S NAME:")
boy_age = int(input("BOY'S AGE: "))
girl_age = int(input("GIRL'S AGE: "))

age_diff = (boy_age - girl_age)

#use abs(absolute) to get absolute value by converting negative outputs as positive outputs

print(boy_name+ " meets " +girl_name + " and their age difference is " + str(age_diff))

"""

#O/P:
    
BOY'S NAME: KING
GIRL'S NAME:QUEEN
BOY'S AGE: 28
GIRL'S AGE: 26
KING meets QUEEN and their age difference is 2

"""



#Ex:02

"""
wanted output: "RAM and RAJ are the two brothers and they are studying in the class 10 and 12 respectively. Their age difference is 2",

"""

yb_name = input("YOUNGER BROTHER: ") 
eb_name = input("ELDER BROTHER: ")

age_of_yb = int(input("AGE OF YOUNGER BROTHER: "))

age_of_eb = int(input("AGE OF ELDER BROTHER: "))

age_diff = abs(age_of_yb - age_of_eb)

class_of_yb = int(input("CLASS OF YOUNGER BROTHER: "))

class_of_eb = int(input("CLASS OF ELDER BROTHER: "))

print(yb_name + " and " + eb_name + " are the two brothers and they are studying in class " + str(class_of_yb) + " and " + str(class_of_eb) + " respectively.Their age difference is " + str(age_diff))

"""

#O/P:
     
YOUNGER BROTHER: RAM
ELDER BROTHER: RAJ
AGE OF YOUNGER BROTHER: 18
AGE OF ELDER BROTHER: 20
CLASS OF YOUNGER BROTHER: 10
CLASS OF ELDER BROTHER: 12
RAM and RAJ are the two brothers and they are studying in class 10 and 12 respectively.Their age difference is 2

"""

#Ex:03

"""
wanted output: "Meera and Reema are sisters. Meera is 5 years elder than Reema. They are currently pursuing B.Sc and M.Sc respectively from Bangalore University and Delhi University."

younger sis = Reema
elder sis = meera

"""

name_of_ys = input("NAME OF THE YOUNGER SISTER: ")
name_of_es = input("NAME OF THE ELDER SISTER: ")

age_of_reema = int(input("AGE OF THE YOUNGER SISTER: "))
age_of_meera = age_of_reema + 5
 

reema_pursuing = input("Reema is studying: ")
university_1 = input("From University: ")

meera_pursuing = input("meera is studying: ")
university_2 = input("From University: ")

print(name_of_ys + " and " + name_of_es + " are sisters. " + name_of_es + " is 5 years elder than " + name_of_ys + ". " + " They are currently pursuing " + reema_pursuing + " and " + meera_pursuing + " respectively. " + " from " + university_1 + " and " + university_2 + " respectively." )


"""

#O/P: 

NAME OF THE YOUNGER SISTER: Reema
NAME OF THE ELDER SISTER: Meera
AGE OF THE YOUNGER SISTER: 20
Reema is studying: B.Sc
From University: Bengaluru University
meera is studying: M.Sc
From University: Delhi University
Reema and Meera are sisters. Meera is 5 years elder than Reema.  They are currently pursuing B.Sc and M.Sc respectively.  from Bengaluru University and Delhi University respectively.

"""


#Ex:04

"""
wanted output:"Arjun and Akash play football and cricket respectively. Arjun scored 3 goals more than Akash scored runs. If Akash scored 40 runs, their total score is 83."

"""

player_1 = input("NAME OF THE 1st PLAYER: ")
player_2 = input("NAME OF THE 2nd PLAYER: ")

game_1 = input("THE GAME PLAYED BY ARJUN: ")
game_2 = input("THE GAME PLAYED BY AKASH: ")

akash_score = 40 

arjun_score = akash_score + 3

total_score = akash_score + arjun_score 

print(player_1 + " and " + player_2 + " play " + game_1 + " and " + game_2 + " respectively." + player_1 + " scored 3 goals more than " + player_2 + " scored runs. " + " if " + player_2 + " scored " + str(akash_score) + " runs "+ ", " + " Their total score is " + str(total_score))

"""

#O/P: 

NAME OF THE 1st PLAYER: Arjun
NAME OF THE 2nd PLAYER: Akash
THE GAME PLAYED BY ARJUN: Football
THE GAME PLAYED BY AKASH: Cricket

Arjun and Akash play Football and Cricket respectively.Arjun scored 3 goals more than Akash scored runs.  if Akash scored 40 runs ,  Their total score is 83

"""
