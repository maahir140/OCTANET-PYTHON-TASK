#                  ATM  Console-Bassed
# 
#                      A         TTTTTTTTTTTTT    MM        MM
#                     A A              T          M  M     M M
#                    A   A             T          M   M   M  M
#                   A     A            T          M    MMM   M
#                  AAAAAAAAA           T          M          M
#                 A         A          T          M          M
#                A           A         T          M          M




import time

print("Plese insert your Debit Card------")

time.sleep(5)

print("Please Enter ATM Pin")
password = 12345678
userpassword = int(input())

balance = 10000

transaction_history = []

if password == userpassword:
    while True:

        print("""
           1 = Check Balance
           2 = Withdraw
           3 = Deposit
           4 = Transfer
           5 = Transactions History
           6 = Quit 
          """
          )

        try:
            option = int(input("Please Enter Your Option "))
        except:
            print("Please Enter Valid Option!!!")

        if option == 1:
          print(balance)
          break

        if option == 2:
          bal = int(input("Enter amount "))
          if bal > balance :
             print("Your have not sufficent amoun.")
             break
          else:
              balance -= bal
              transaction_history.append(f"Debited: Rs{bal:.2f}")
              print("Rs. ", bal, " is debited from........account!")
              print("Total amount ", balance)

        if option == 3:
          bal2 = int(input("Enter amount "))
          balance += bal2
          transaction_history.append(f"Credited: Rs{bal2:.2f}")
          print("Rs. ", bal2,"credite from........account!")
          print("Total amount ", balance)

        if option == 4:
          acc = int(input("Enter account name "))
          ifce = input("Enter IFSC code ")
          bal3 = int(input("Enter amount ")) 
          if bal3 > balance:
             print("You have not sufficent amount for transfer. If try to send amount then your account are goes in negative And more imformation please visit your bank")
             break
          else:
           balance -= bal3
           transaction_history.append(f"Transfer: Rs{bal3:.2f}")
           print("Rs. ", bal3," has sccuessfully transfer from the",acc)
           print("Total balance ", balance)
          
        if option == 5:
           for transaction in transaction_history:
            print(transaction)
           break
           
        if option == 6:
          break
else:
    print("Wrong! pin please try again!!")


print("Thank For Using All INDIA ATM")
print("Government Of India ")
