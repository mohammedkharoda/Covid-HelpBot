
print("Hello, Welcome my name is Enzo")
print("How may I help you Today\n")

# ========> Symptoms
def symptoms():

    count = 0
    print('Do you Have fever ?')
    user = input('Enter 1 to Confirm or press any other key to Denied: ')

    if(user=="1"):
        count = count+1

    print('Do you Have DryCough ?')
    user = input('Enter 2 to Confirm or press any other key to Denied: ')

    if (user == "2"):
        count = count + 1

    print('Do you Have tiredness ?')
    user = input('Enter 3 to Confirm or press any other key to Denied: ')

    if (user == "3"):
        count = count + 1

    if count == 0:
        print('\n Results: ')
        print(' Chances of getting covid +ve is very low')
        print(' Get tested to be Sure')

    if count == 1:
        print('\n Results: ')
        print(' Chances of getting covid +ve is low')

    if count == 2:
        print('\n Results: ')
        print(' Chances of getting covid +ve is very Mild')
        print(' Make sure To have a Checkup!!')

    if count == 3:
        print('\nResults: ')
        print(' Chances of getting covid +ve is very High')
        print(' Have a Check Immediately!!')


# ========> Book Vaccine
def bookVaccine():
    print('To book your vaccine you may visit here: https://www.cowin.gov.in')

# ========> Helpline
def helpline():
    print("""HelpLine Numbers:
         1. Health Ministry: 1075
         2. Child: 1098
         3. Mental Health: 08046110007
         4. Ayush Covid-19 Conuselling: 14443
         5. MyGov Whatsapp Number: 9013151515
         6. MyGov Corona Live HelpDesk: 919013151515
         """)

# ========> Saftey Measure
def  safteyMeasure():
    print("""
    Safety Measure to keep in the mind are:
    1. Face masks and respiratory hygiene
    2. Indoor ventilation and avoiding crowded indoor spaces
    3. Hand-washing and hygiene
    4. Social distancing
    5. Surface cleaning
    """)

# ---------- Excutation Block -------------
while True:
    print("""Please Enter:
        1. To Check for symptoms
        2. To Book Vactination
        3. To get a list of helpline number
        4. To get to know about Safety Measures \n
    """)

    choice = int(input("Enter your choice: "))

    if(choice==1):
        symptoms()
    elif(choice==2):
        bookVaccine()
    elif(choice==3):
        helpline()
    elif(choice==4):
        safteyMeasure()
    else:
        print('Invalid Input!!')

    print("""\n \nTo Start again Enter 1 or Enter any Key To Quit """)

    userChoice = input('Enter the Choice: ')
    if(userChoice!= "1"):
        print('Be safe Wear Mask')
        break