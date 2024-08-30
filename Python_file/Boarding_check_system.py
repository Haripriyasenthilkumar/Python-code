def ticket_checkup(ticket):
    valid_ticket=["TICKET11","TICKET14","TICKET13","TICKET12"]
    if ticket in valid_ticket:
        print("Step 1:\tTICKET_CHECKUP - Yes, your ticket is valid")
        return True
    else:
        print("Step 1:\tTICKET_CHECKUP - sorry your ticket is invalid")
        return False
def covid_checkup(result):
    if result=="negative":
        print("Step 2:\tCOVID_CHECKUP - Result neagtive ")
        return True
    elif result=="positive":
        print("Step 2:\tCOVID_CHECKUP - Not Allowed")
        return False
def immigration_checkup(immigration):
    if immigration=="clear":
        print("Step 3:\tIMMIGRATION_CHECKUP - clear ")
        return True
    elif immigration=="not clear":
        print("Step 3:\tIMMIGRATION_CHECKUP - not clear")
        return False
def bag_checkup(weight):
    if (weight<=20):
        print("Step 4:\tBAG_CHECKUP - Your bag weight is less than 20Kg ")
        return True
    elif (weight>20):
        print("Step:4\tBAG_CHECKUP - Your bag weight is more than 20Kg. So, you have to pay an extra charge for your bag")
        return True
def boarding_checkup(board_no):
    board_pass=["BP2001","BP2002","BP2003","BP2004"]
    if board_no in board_pass:
        print("Step 5:\tBOARDPASS_CHECKUP - board passing clear")
        return True
    else:
        print("Step 5:\tBOARDPASS_CHECKUP - board pass not clear")
        return False
def main():
    print("\t\tWElCOME TO AIRLINE")
    print("___________________________________________")
    ticket=input("\nEnter your ticket no:")
    result=input("\nEnter the covid result [Negative/Positive]:")
    immigration=input("\nEnter the immigration status [Clear/Not clear]:")
    weight=int(input("\nEnter your bag weight:"))
    board_no=input("\nEnter the board no:")
    print("\n\n")
    if  ticket_checkup(ticket) and covid_checkup(result) and immigration_checkup(immigration) and bag_checkup(weight) and boarding_checkup(board_no):
        print("\nHappy Journey...Now your are allowed to travel...Welcome")
    else:
        print("sorry! your are eligible to travel try next time")
main()
       