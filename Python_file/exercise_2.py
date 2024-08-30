def main():
    print("\t******JUICE CORNER*****")
    print("___________________________________________________")
    print("Available juices\n1.apple > ₹50\n2.orange . ₹30\n3.lemon > ₹20")
    juice_list=["apple","orange","lemon"]
    juice=input("enter the juice name you like to drink : ")
    if juice in juice_list:
        print(f"YES...{juice} juice is available")
        try:
            count=int(input(f"How many {juice} juice you want :  "))
            if juice=="apple":
                a_price=count*50
                print("price:",a_price)
                next=int(input("if you want to continue your order then select 1\n if no then select 2 : "))
                if next==1:
                    main()
                else:
                    print("thankyou for your order please wait ")
            elif juice=="orange":
                o_price=count*30
                print("price:",o_price)
                next=int(input("if you want to continue your order then select 1\n if no then select 2 : "))
                if next==1:
                    main()
                else:
                    print("thankyou for your order please wait ")
            elif juice=="lemon":
                l_price=count*20
                print("price:",l_price)
                next=int(input("if you want to continue your order then select 1\n if no then select 2 : "))
                if next==1:
                    main()
                else:
                    print("thankyou for your order please wait ")
        except:
            print("Please type type number only")
            main()
    else:
        print(f"Sorry...{juice} juice is not available ")
main()
    


