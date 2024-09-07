Principal=int(input("Enter the principal amount: "))
Time=int(input("Enter the time: "))
Rate=int(input("Enter the rate: "))
Amount=Principal*(1+Rate/100)**Time
CompoundInterest=round((Amount-Principal),2)
print(f"Compound Interest of {Principal},{Time},{Rate} is {CompoundInterest}.")