import datetime

print("PRESCRIPTION\n")
sname=input("ENTER YOUR NAME: ")
age=input("ENTER YOUR AGE : ")
Weight= input("ENTER YOUR WEIGHT: ")
height= input("ENTER YOUR HEIGHT: ")
ill= input("WHAT DO YOU FEEL LIKE? ENTER YOUR AILMENT: ")

def headache1():
    hvar = "\nwhat you can do is : Get enough sleep. The average adult needs seven to eight hours of sleep a night. It's best to go to bed and wake up at the same time every day. Don't skip meals. Eat healthy meals at about the same times daily.\n Avoid food or drinks, such as those containing caffeine, that seem to trigger headaches. Lose weight if you're obese." + "Exercise regularly. Regular aerobic physical activity can improve your physical and mental well-being and reduce stress.\n choose activities you enjoy — such as walking, swimming or cycling. To avoid injury, start slowly." + "Reduce stress. Stress is a common trigger of chronic headaches. Get organized. Simplify your schedule. Plan ahead. Stay positive.\n Try stress-reduction techniques, such as yoga, tai chi or meditation."
    return hvar
    
def cough1():
    cvar="\nwhat you can do is : Incline the head of your bed,It’s easier for irritants to make their way to your throat to trigger coughing when you’re lying down.\n Try propping up some pillows to raise your head. Use a humidifier,Dry, warm air can irritate your throat and airways. Some people also cough when they turn their heater on in the winter. This is due to the release of pollutants that built up in the heating ducts.\n A humidifier that produces a cool mist can help keep the air in your bedroom moist. This can keep your throat feeling better.Try honey,Honey and a hot drink can help loosen mucus in your throat.\n Mix two teaspoons of honey into an caffeine-free tea, such as herbal tea, to drink before bed." 
    return cvar
    
def cold1():
    wvar="\nwhat you can do is : washing your hands with warm water and soap.not sharing towels or household items (like cups) with someone who has a cold.\nnot touching your eyes or nose in case you have come into contact with the virus – it can infect the body this way.staying fit and healthy."
    return wvar
def sorethroat1():
    svar="\nwhat you can do is : Try comforting foods and beverage. Warm liquids — broth, caffeine-free tea or warm water with honey — and cold treats such as ice pops can soothe a sore throat.\n Humidify the air. Use a cool-air humidifier to eliminate dry air that may further irritate a sore throat, being sure to clean the humidifier regularly so it doesn't grow mold or bacteria Or sit for several minutes in a steamy bathroom.\nGargle with saltwater. A saltwater gargle of 1/4 to 1/2 teaspoon (1.25 to 2.50 milliliters) of table salt to 4 to 8 ounces (120 to 240 milliliters) of warm water can help soothe a sore throat."
    return svar

def bodypain1():
    bvar="\nwhat you can do is : resting the area of the body where you're experiencing aches and pains.\n	taking an over-the-counter pain reliever, such as ibuprofen (Advil),applying ice to the affected area to help relieve pain and reduce inflammation"
    return bvar

def diarrhoea1():
    dvar="\nwhat you can do is : Drink only bottled water, even for tooth brushing.,Avoid eating food from street vendors.\nAvoid ice made with tap water.Eat only those fruits or vegetables that are cooked or can be peeled.Be sure that all foods you eat are thoroughly cooked and served steaming hot"
    return dvar

def nausea1():
    nvar="	\nwhat you can do is : Apply a cool compress with  pressure.Stay hydrated ,Opt for chamomile tea  Sit up and avoid crunching the stomach, Open a window or sit in front of a fan"
    return nvar

def redeyes1():
    rvar="\nwhat you can do is : Avoid smoke, pollen, dust, and other triggers,Do not wear contact lenses until the red eye clears.\n,Always clean lenses properly and do not reuse disposable lenses. Wash your hands regularly and avoid touching the eyes, to prevent infection."
    return rvar

def fever1():
    fvar="\nwhat you can do is : Wash your hands often, especially before eating, after using the toilet, and after being around large numbers of people.\nCarry hand sanitizer or antibacterial wipes with you. They can come in handy when you don’t have access to soap and water. Find hand sanitizers and antibacterial wipes online.\nAvoid touching your nose, mouth, or eyes. Doing so makes it easier for viruses and bacteria to enter your body and cause infection."
    return fvar

def check_ill(ill):
    if ill == "headache":
        return headache1()
    elif ill == "cough":
        return cough1()
    elif ill == "cold":
        return cold1()
    elif ill == "sorethroat":
        return sorethroat1()
    elif ill == "bodypain":
        return bodypain1()
    elif ill == "diarrhoea":
        return diarrhoea1()
    elif ill == "nausea":
        return nausea1()
    elif ill == "redeyes":
        return redeyes1()
    else: 
        return fever1()
   
def print_prescription(sname,age,Weight,height,ill,x,symp):
    y=x.strftime("%c")
    diag ="\nName of the patient is " + sname + "\n"+ sname +" is " + age +" years old "+"\n"+ "Weight :"+ Weight+"  height :"+height+"\n"+ sname +" has been diagnosed for "+ill
    return "\nPRESCRIPTION\n\n" + y + "\n" + diag + "\n" +symp 
    
print("The prescription is printed in your folder's text file named 'yourprescription.txt'")   
x=datetime.datetime.now()
symp = check_ill(ill)
L=print_prescription(sname,age,Weight,height,ill,x,symp)
print(L)
file1 = open('C:/Users/sharo/Desktop/python project/testing python/YourPrescription.txt', 'w') 

# Writing a string to file 
file1.write(str(L) )
  

   
