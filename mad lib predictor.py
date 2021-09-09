from hobbiess import yourHobbies, person, yourReligion, quotes
import random
print("This program takes basic information about you and tells you something about you")
 #get data from user
age="0"
 #validate data
while age!=int(age):
    try:
        age=int(input("please enter your age: "))
        if age>25:
            virgin= input("are you a virgin? ")
            while virgin!="yes" and virgin!="no" and virgin!="Yes" and virgin!="No":
                print("please enter yes or no")
                virgin= input("again, are you a virgin? ")
            bank="0"
            while bank!=int(bank):
                try:
                    bank=int(input("So how much do you have in your bank account right now? "))
                except:
                    print("please enter a valid amount")
    except ValueError:
        print("please enter a valid age") 
     

name=input("please enter your first name: ")
sex=input("please enter your gender: ")
while sex!="male" and sex!="female" and sex!="Male" and sex!="Female":
        print("please enter male or female")
        sex=input("please enter your gender: ")
 
firstChild=input("are you the first child. Please enter yes or no: ")
while firstChild!="yes" and firstChild!="no" and firstChild!="Yes" and firstChild!="No":
    print("please enter yes or no")
    firstChild=input("are you the first child, yes or no: ")
country=input("where did you grow up? ")
if country=="Nigeria" or country=="nigeria":
    if sex=="male" or sex=="Male":
        print("my brother you dey try o")
    else:
        print("my sister you dey try o")
music=input("do you like music? Answer yes or no")
while music!="yes" and music!="no" and music!="Yes" and music!="No":
    print("please enter yes or no")
    music=input("please tell us if you like music? ")
print(yourHobbies[1]["answer"])
print(yourHobbies[2]["answer"]) 
print(yourHobbies[3]["answer"]) 
print(yourHobbies[4]["answer"]) 
print(yourHobbies[5]["answer"]) 
print(yourHobbies[6]["answer"])
def check_ans():
    num=1
    while num<=6:
        if yourHobbies[num]['answer'].lower() == hobbies.lower():
            return True
        else:
            num+=1
            
hobbies= input("what are your hobbies, select one from above? ")
check_ans()
while check_ans()!= True:
    print(yourHobbies[1]["answer"])
    print(yourHobbies[2]["answer"]) 
    print(yourHobbies[3]["answer"]) 
    print(yourHobbies[4]["answer"]) 
    print(yourHobbies[5]["answer"]) 
    print(yourHobbies[6]["answer"])
    hobbies= input("please enter a valid hobby, select from above? ")
    check_ans()

mondays= input("do you like mondays? ")
while mondays!="yes" and mondays!="no" and mondays!="Yes" and mondays!="No":
    print("please enter yes or no")
    music=input("again, you like mondays? ")
happy= input("what makes you happy really? ")
masturbate= input("do you masturbate? ")
while masturbate!="yes" and masturbate!="no" and masturbate!="Yes" and masturbate!="No":
    print("please enter yes or no")
    masturbate= input("do you masturbate? ")
if age>20:
    sexfrequency=input("when last did you have sex? ")
print(religion[0])
print(religion[1]) 
print(religion[2]) 
print(religion[3]) 
print(religion[4])
def check_religion():
    num=1
    while num<=5:
        if yourReligion[num].lower() == religion.lower():
            return True
        else:
            num+=1

religion=input("how religious are you? choose one from above ")
check_religion()
while check_religion()!= True:
    print(religion[0])
    print(religion[1]) 
    print(religion[2]) 
    print(religion[3]) 
    print(religion[4])
    religion=input("Please enter a valid answer on your religion from the list above ")
    check_religion()
afterdeath= input("do uou believe in life after death? ")
while afterdeath.lower()!="yes".lower() and afterdeath.lower()!="no".lower():
    print("please enter yes or no")
    afterdeath= input("do uou believe in life after death? ")
misogyny= input("what's your take on misogyny? ")
biggest_money=0
while biggest_money!=int(biggest_money):
    try:
        biggest_money= int(input("what's the largest money you have ever earned? "))
    
    except ValueError:
        print("please enter a valid amount")

destiny= input("do you belive in destiny? ")
while destiny.lower()!="yes".lower() and destiny.lower()!="no".lower():
    print("please enter yes or no")
    destiny= input("do you belive in destiny? ")
if age>25:
    societyclass= input("what class do you believe you fall into in the society? ")
    study= input("what did you study in school?")
    occupation=input("what is your occupation? ")
if sex=="female" or sex=="Female":
    boys= input("are you good with boys? ")
    while boys.lower()!="yes".lower() and boys.lower()!="no".lower():
        print("please enter yes or no")
        boys= input("are you good with boys? ")
if sex=="male" or sex=="male":
    girls= input("are you good with girls? ")
    while girls.lower()!="yes".lower() and girls.lower()!="no".lower():
        print("please enter yes or no")
        girls= input("are you good with girls? ")
inclination= input("conservative or free spirit? ")
while inclination.lower()!="conservative".lower() and inclination.lower()!="free spirit".lower():
        print("please enter conservative or free spirit")
        inclination= input("conservative or free spirit? ")
momdad= input("if there was a fire and you could only choose one person between your dad and mom, who would it be? ")
while momdad.lower()!="mom".lower() and momdad.lower()!="dad".lower():
        print("please enter mom or dad ")
        momdad=input("dad or mom, who would it be? ")
heartbreak=input("have you ever been heart broken? ")
while heartbreak.lower()!="yes".lower() and heartbreak.lower()!="no".lower():
        print("please enter yes or no")
        heartbreak=input("have you ever been heart broken? ")
dice=""
while dice!=int(dice):
    try:
        dice=int(input("pick a number from 1 to 9"))
        
    except ValueError:
        print("please enter a valid number") 


print("So here's what we know about you")
print("you are "+age" years old")
print("your first anme is "+name)
print("you are "+sex)
if age>25:
    if virgin.lower()=="yes".lower():
        print("you are a virgin ")
    else:
        print("you don fuck before ")
    if country.lower=="nigeria".lower():
        print("you have #"+bank+"in your bank account")
        if bank<3000000:
            print("you are poor ")
    else:
        print("you have $"+bank+"in your bank account")
     
if firstChild=="yes" or firstChild=="Yes":
    print("you are the first child ")
else:
     print("you are not the first child ")
 print("you grew up in "+country)
if music=="yes" or music=="Yes":
    print("you love music! ")
else:
     print("you don't like music ")
print("your favorite hooby is "+hobbies)
if mondays=="yes" or mondays=="Yes":
    print("you are a monday person ")
else:
     print("you don't like mondays "+name)
print("you explained this is what you happy: "+happy)
if masturbate.lower()=="yes".lower():
    print("you masturbate lol eww ")
else:
     print("you don't masturbate ")
if age>20:
    print("About your sexfrequency you said: "+sexfrequency)
if religion!=yourReligion[4]:
print(" you said you are "+religion)
if destiny.lower()=="yes".lower():
    print("you believe in destiny ")
else:
     print("you don't believe in destiny ")
if age>25:
    print("You fall into the "+society+"class of society")
    print("You studied: "+study)
    print("your occupation is: "+occupation)

if sex=="female" or sex=="Female"::
    print("regarding the opposite sex, you said "+girls)
else:
    print("regarding the opposite sex, you said "+boys)

print("your are a: "+inclination)
print("your occupation is: "+occupation)
print("you would save your: "+momdad+"if there was a fire")
if heartbreak.lower()=="yes".lower():
    print("you have been heart broken before")
else:
    print("heart break don't got nothing on you ")




 #we analyze based on data given above
 if age > 25 and music.lower()=="yes".lower() and virgin.lower()=="yes".lower():
    print(person["music"])
    print("Here's a quote to help:\n ",random.choice(quotes))
if firstChild.lower()=="yes".lower() and mondays.lower()=="yes".lower():
    print(person["firstchild"])
    print("Here's a quote to help:\n ",random.choice(quotes))
if masturbate.lower()=="yes".lower() or hobbies==yourHobbies[1]["answer"] and age<25 or religion==yourReligion[0] or afterdeath.lower()=="yes".lower():
    print(person["world"])
    print("Here's a quote to help:\n ",random.choice(quotes))