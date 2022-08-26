##########################################################################
#    Computer Project #3
#    Algorithm
#        Prompt to ask the student their level.
#        Based on level, ask for other information like which college.
#        Ask for the number of credits.
#        Calculate tution with all the information/
#        Ask the user if they want to continue.  
##########################################################################

#Creating variables with None value for now.
level, college, CoE_admitted, madison = None, None, None ,None

#Welcome message.
print("2021 MSU Undergraduate Tuition Calculator.\n")

#answer if the user wants to continue, "yes" now.
ans = "yes"

#loop to make sure user wants to continue.
while ans.lower() == "yes":
    
    level = input("Enter Level as freshman, sophomore, junior, senior: ")
    level = level.lower()
    #loop to make sure user enters level correctly.   
    while level != "freshman" and level != "sophomore" and level != "junior"\
         and level != "senior":
        print("Invalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ")
    level = level.lower()
    
    if level == "junior" or level == "senior":
        #asks to enter college.
        college = \
input("Enter college as business, engineering, health, sciences, or none: ")
        college = college.lower()

    if level == "freshman" or level == "sophomore":
        #asks if user is admitted to College of Engineering or not.
        CoE_admitted = \
            input("Are you admitted to the College of Engineering (yes/no): ")
        CoE_admitted = CoE_admitted.lower()

    if college != "business" and college != "engineering" and \
        college != "health" and college != "sciences":
        #asks if user is in James Madison College or not.
        madison = input("Are you in the James Madison College (yes/no): ")
        madison = madison.lower()

    #prompt to enter number of credits.
    credits = (input("Credits: "))
    #loop to make sure user enters credits correctly.
    while (credits.isdigit() == False) or (int(credits) <= 0):
        print("Invalid input. Try again.")
        credits = (input("Credits: "))
    credits = int(credits)

    #calculation of resident fees.
    if level == "freshman":
        if 1 <= credits <= 11:
            resident_total = 482*credits
        elif 12 <= credits <= 18:
            resident_total = 7230
        else:
            resident_total = 7230 + (credits-18)*482

    if level == "sophomore":
        if 1 <= credits <= 11:
            resident_total = 494*credits
        elif 12 <= credits <= 18:
            resident_total = 7410
        else:
            resident_total = 7410 + (credits-18)*494

    if level == "junior" or level == "senior":
        if college == "business" or college == "engineering":
            if 1 <= credits <= 11:
                resident_total = 573*credits
            elif 12 <= credits <= 18:
                resident_total = 8595
            else:
                resident_total = 8595 + (credits-18)*573
        else:
            if 1 <= credits <= 11:
                resident_total = 555*credits
            elif 12 <= credits <= 18:
                resident_total = 8325
            else:
                resident_total = 8325 + (credits-18)*555

    #calculation of special fees.
    special_fees = 0                         
    if credits <= 4:
        if college == "business" and (level == "junior" or level == "senior"):
            special_fees = 113
        elif CoE_admitted == "yes":
            special_fees = 402
        elif (college == "health" or college == "sciences") and \
            (level == "junior" or level == "senior"):
            special_fees = 50

    else: 
        if college == "business" and (level == "junior" or level == "senior"):
            special_fees = 226
        elif CoE_admitted == "yes" or (college == "engineering" and \
            (level == "junior" or level == "senior")):
            special_fees = 670
        elif (college == "health" or college == "sciences") and \
            (level == "junior" or level == "senior"):
            special_fees = 100

    #calculation of student-voted taxes.
    asmsu_tax = 21
    FM_tax = 3
    statenews_tax, jmc_tax = 0,0
    if credits >= 6:
        statenews_tax = 5
    if madison == "yes":
        jmc_tax = 7.50

    #adding all taxes to get total tax.
    total_tax = asmsu_tax + FM_tax + statenews_tax + jmc_tax

    #calculating tution by adding all 3 values.
    tution = resident_total + special_fees + total_tax

    #print statement.
    print("Tuition is ${:,.2f}.".format(tution))

    #prompt to ask the user if they still want to continue.
    ans = input("Do you want to do another calculation (yes/no): ")
