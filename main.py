import pandas as pd


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        self.name=df.loc[df["id"]==self.hotel_id,"name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"]="no"
        df.to_csv("hotels.csv",index=False)


    def available(self):
        availablity= df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        try:
            if availablity == "yes":
                return True
            else:
                return False
        except ValueError:
            print("Invalid Hotel ID !!")

class ReservationTicket:
    def __init__(self,customer_name,hotel_obj):
        self.customer_name=customer_name
        self.hotel=hotel_obj
        pass
    def generate(self):
        content=(f"""
            Your reservation is confirmed \n
            Your Name : {self.customer_name}\n
            Hotel Name : {self.hotel.name}\n
            City : {self.hotel.city}""")
        return content
df = pd.read_csv("hotels.csv")

print(df)

h_id = int(input("Enter the Hotel ID : "))
hotel = Hotel(hotel_id=h_id)

if hotel.available():
    hotel.book()
    name= input("Enter your Name  :  ")
    reservation_ticket=ReservationTicket(customer_name=name,hotel_obj=hotel)
    print(reservation_ticket.generate())
else:
    pass

