c_p=1411
m_a = 3
at = 0

while at < m_a :
    u_inp = int(input("Enter your Pin : "))
    if u_inp == c_p :
        Balance = 50000
        print("WELCOME OUR CANARA BANK ATM")
        print("Insert Your Card")
        while True:
            print("1.balance enquiry")
            print("2.cash withdraw")
            print("3.amount deposit")
            print("4.exit")
            option = int(input("Enter Your Correct Option:"))
            if option == 1:
                print("You're Account have", Balance)
                print("ThankYou For Your Visiting!")
            elif option == 2:
                withdraw_amount = int(input("Enter Your Amount:"))
                if withdraw_amount > Balance:
                    print("Sorry,This amount is not in your account")
                else:
                    print("Processing is Being so wait")
                    print(withdraw_amount, "is successfully withdrawal! So Remove Your Card.")
                    print("Balance is : ", Balance - withdraw_amount)
                    print("Thank You For Your Visiting!")
            elif option == 3:
                ac_no = int(input("Enter Your Account Number:"))
                if ac_no == 9790511802:
                    print("Process Is Being")
                    Amount = int(input("Enter your amount:"))
                    print("Amount Added Your Account Successfully,And Your Balance amount is:", Balance + Amount)
                    print("ThankYou For Your Visiting!")
                elif ac_no != 9790511802:
                    print("You're Account Number Is Wrong")
            elif option == 4:
                exit()
            else:
                print("choose your correction answer.")
    else:
        print("Invalid Pin")
        at += 1
        print(f"Attempts left : {m_a-at}")
        print(f"Attempts left : {m_a-at}")