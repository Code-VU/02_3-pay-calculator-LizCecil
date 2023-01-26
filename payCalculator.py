def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    total_hours = input("Enter Hours:")
    hourlyrate = input("enter rate:")
    totalpay = int(total_hours) * int(hourlyrate) 
    print(totalpay) 

    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
