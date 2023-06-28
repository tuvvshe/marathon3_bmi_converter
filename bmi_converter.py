Height = float(input("ENTER YOUR HEIGHT IN CENTIMETERS: "))
Weight = float(input("ENTER YOU WEIGHT IN KG: "))
Height = Height/100
BMI = Weight/(Height*Height)
print("YOUR BODY MASS INDEX IS: ", BMI)
if(BMI>0):
    if(BMI<=16):
        print("YOU ARE UNDERWEIGHT")
    elif(BMI<=25):
        print("YOU ARE HEALTY")
    elif(BMI<=30):
        print("YOU ARE FAT ASS")
    else:
        print("YOU ARE SEVERELY FAT ASS. GO AND DO SOME GYM")
else:
    ("ENTER VALID DETAILS DONT CHEAT!!!!!")
