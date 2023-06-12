class hotelBookings:
    booking=[]
    no_of_booking=0

    def AddBooking(self,query1,query2,query3):
        self.booking.append(query1)
        self.booking.append(query2)
        self.booking.append(query3)
        self.no_of_booking +=1
    
    def NoOfBooking(self):
        print(f"Total no of booking in the hotel {self.no_of_booking}")
    
    def Showbooking(self):
        b="".join(self.booking)
        list_string = []
        chunk_list=3
        for i in range(0,len(b),chunk_list):
            list_string.append(b[i:i+chunk_list])
        print(list_string)
        
        # start=0
        # end=len(list_string)
        # for i in range(start,end,3):
        #     x=i
        #     print(x)
        #     print(list_string[x:x+3])


        
        # for index,room in enumerate(self.booking):
        #     print(f"{index+1}.) {room}",end="")
    
    def Check(self):
        if(self.no_of_booking == len(self.booking)):
            print("This Hotel is booked")
        else:
            print("Some rooms on the hotel remains still empty")

Central_Hotel = hotelBookings()

print("---------Welcome To Lords Hotel System---------")
print()
print(" Press 1 for book a room in the hotel \n 2 for number of rooms book in the Lords \n 3 for getting name of person who stay in the hotel \n 4 for exit")
print()

while True:
    choice = int(input("Choose Between 1 2 3 4: "))
    if(choice == 1):
        int1=str(input("You enter only in between + and - and + means booked and - means freed:"))
        int2=str(input("You select the floor of the room 0 to 9:"))
        int3=str(input("You select the room name from A to Z:")).upper()
        int4=int1+int2+int3
        Central_Hotel.AddBooking(int1,int2,int3)
        print(f"{int4} room has been booked")
    

    elif(choice == 2):
        Central_Hotel.NoOfBooking()

    elif(choice == 3):
        Central_Hotel.Showbooking()

    elif(choice == 4):
        break

    else:
        print("Invalid Input")
