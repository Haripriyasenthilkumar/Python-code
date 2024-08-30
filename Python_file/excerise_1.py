print("\t\t\t_____________VASU CINEMA_________")
print("********************************************************************************************************")
print("The running movies in our thetre\n\tPREMALU \n\tGHILLI \n\tMANJUMMEL BOYS\n\n")
select_movie=input("\tHELLO...WELCOME TO VASU CINEMA\nEnter the movie you want to watch:")
movie=["premalu","ghilli","manjummel boys"]
if select_movie in movie:
    print(f"\n{select_movie} movie is available")
    movie_date=input(f"\nEnter the date [dd/mm/yyyy]:")
    movie_time=input("\n\tWhich timing you want\nmorning show\nafternoon show\nnight show\t:")
    ticket=int(input(f"\nHow many tickets you want for {select_movie} movie: "))
    print("*****************************************************")
    print("\t\tAVAILABLE CLASS")
    print("\n\tFisrt class  = ₹150\n\tSecond class = ₹130\n\tThird class  =  ₹120 ")
    print("\nIf you want \nFirst class tickets then select '1'\nSecond class tickets then select '2'\nThird class tickets then select '3'\n")
    select_class=input("\nEnter the class:")
    ticket_types=["1","2","3"]
    if (select_class=="1"):
           amt=ticket*150
           print("\nYou have to pay ₹",amt)
    elif (select_class=="2"):
          amt=ticket*130
          print("\nYou have to pay ₹",amt)
    elif (select_class=="3"):
          amt=ticket*120
          print("\nYou have to pay ₹",amt)
    else:
        print("Please select the available classes")
    print("\t\t_____________VASU CINEMA_________")
    print(f"\nMovie:\t\t{select_movie} \nDate:\t\t{movie_date}\nTimimg:\t\t{movie_time}\nClass:\t\t{select_class}\nNo.of tickets:\t{ticket}\nAmount:\t\t{amt}")
    print("\n\n\t\t*******THANKYOU******")

else:
    print(f"Sorry...{select_movie} movie is not available")
