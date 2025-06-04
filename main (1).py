bal=10000
while(bal>=0):
    wd=int(input("enter the money: "))
    bal=bal-wd
    print("available balance={bal}")
    if(bal<0):
        print("insufficient funds")