def CompoundInterest(Principal,Time,Rate):
    Amount=Principal * (pow((1+Rate/100),Time))
    CompoundInterest=round((Amount-Principal),2)
    print("Compound Interest is: ",CompoundInterest)
Principal=int(input("Enter the principal amount: "))
Time=int(input("Enter the time: "))
Rate=int(input("Enter the rate: "))
CompoundInterest(Principal,Time,Rate)