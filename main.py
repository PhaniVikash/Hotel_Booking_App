import pandas as pd

class Hotel():
    def __init__(self,id):
        pass
    def book(self):
        pass
    def available(self):
        return True

class ReservationTicket():
    def __init__(self,customer_name,hotel_obj):
        pass
    def generate(self):
        print(f"Your reservation is confirmed ")

df = pd.read_csv("hotels.csv")

print(df)

id = int(input("Enter the Hotel ID : "))
hotel = Hotel(id=id)

if hotel.available():
    hotel.book()
    name= input("Enter your Name  :  ")
    age = int(input("Enter your age "))
    reservation_ticket=ReservationTicket(customer_name=name,hotel_obj=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free ")

