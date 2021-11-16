name = input("Enter your name : ")
pas = int(input("Enter the password : "))
password = 2683

if pas==password:
    print("""
    Hello {}
    
    --------------------------
    1.) Balance enquiry      
    2.) withdrawal
    --------------------------
    """.format(name))

    value = input("Chose any one : ")

    balance = 50000

    if value=="1":
        print("You having balance of {}".format(balance))
    elif value=="2":
        amount = int(input("Enter the amount : "))
        if amount>balance:
            print("The safest balance. your Balance {}".format(balance))
        else:
            total_blance = balance-amount
            print("Take your money of {}".format(amount))
            print("After taking of amount of {} your Total Balance is {}".format(amount,total_blance))

else:
    print("Password is not match")

print("""
-----------------------------
Thanks for using Sairam ATM
-----------------------------
""")