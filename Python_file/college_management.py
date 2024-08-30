print("\t\tSASTRA DEEMED TO BE UNIVERSITY")
print("**************************************************************")
print("\tAVAILABLE COURSE IN SASTRA\nBsc cs\nBCA\nBcom\nBsc maths\n")
select_course=input("Select your favourite course:")
available_course=["Bsc cs","BCA","Bcom","Bsc maths"]
if (select_course in available_course):
    print(f"Yes...{select_course} is available ")
    if (select_course=="Bsc cs"):
        print(f"\n\tDETAIL FOR {select_course}\nTution fees:\t₹18000\nLab fees:\t₹800\nLibrary fees:\t₹700\npaper fees:\t₹200\nSport fees:₹300\nTOTAL: ₹20000")
        score=int(input("\nEnter your +2 mark here:"))
        if(score>=400):
            print(f"\n\tcongratulation!!! Your are eligible for {select_course}")
            print("Here fill your personal details")
            name,phno,address=input("ENter your name:"),int(input("Enter your phno:")),input("Enter your address:")
            print("**************************************************************")
            print("\n\t\tWELCOME TO SASTRA ")
            print(f"Student name:\t{name}\nphone number:\t{phno}\naddress:\t{address}\nCourse:\t\t{select_course}\nfees:\t\t₹20000")
        else:
            print(f"Sorry...your are not eligible for {select_course}")
    if (select_course=="BCA"):
        print(f"\n\tDETAIL FOR {select_course}\nTution fees:\t₹18000\nLab fees:\t₹800\nLibrary fees:\t₹700\npaper fees:\t₹200\nSport fees:₹300\nTOTAL: ₹20000")
        score=int(input("\nEnter your +2 mark here:"))
        if(score>=450):
            print(f"\n\tcongratulation!!! Your are eligible for {select_course}")
            print("Here fill your personal details")
            name,phno,address=input("ENter your name:"),int(input("Enter your phno:")),input("Enter your address:")
            print("**************************************************************")
            print("\n\t\tWELCOME TO SASTRA ")
            print(f"Student name:\t{name}\nphone number:\t{phno}\naddress:\t{address}\nCourse:\t\t{select_course}\nfees:\t\t₹20000")
        else:
            print(f"Sorry...your are not eligible for {select_course}")
    if (select_course=="Bcom"):
        print(f"\n\tDETAIL FOR {select_course}\nTution fees:\t₹28000\n\nLibrary fees:\t₹700\npaper fees:\t₹200\nSport fees:₹300\nTOTAL: ₹30000")
        score=int(input("\nEnter your +2 mark here:"))
        if(score>=400):
            print(f"\n\tcongratulation!!! Your are eligible for {select_course}")
            print("Here fill your personal details")
            name,phno,address=input("ENter your name:"),int(input("Enter your phno:")),input("Enter your address:")
            print("**************************************************************")
            print("\n\t\tWELCOME TO SASTRA ")
            print(f"Student name:\t{name}\nphone number:\t{phno}\naddress:\t{address}\nCourse:\t\t{select_course}\nfees:\t\t₹30000")
        else:
            print(f"Sorry...your are not eligible for {select_course}")
    if (select_course=="Bsc maths"):
        print(f"\n\tDETAIL FOR {select_course}\nTution fees:\t₹18000\nLab fees:\t₹800\nLibrary fees:\t₹700\npaper fees:\t₹200\nSport fees:₹300\nTOTAL: ₹20000")
        score=int(input("\nEnter your +2 mark here:"))
        if(score>=400):
            print(f"\n\tcongratulation!!! Your are eligible for {select_course}")
            print("Here fill your personal details")
            name,phno,address=input("ENter your name:"),int(input("Enter your phno:")),input("Enter your address:")
            print("**************************************************************")
            print("\n\t\tWELCOME TO SASTRA ")
            print(f"Student name:\t{name}\nphone number:\t{phno}\naddress:\t{address}\nCourse:\t\t{select_course}\nfees:\t\t₹20000")
        else:
            print(f"Sorry...your are not eligible for {select_course}")
else:
    print(f"Sorry...{select_course} is not available")
