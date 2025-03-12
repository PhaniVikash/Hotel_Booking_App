import pandas as pd

df = pd.read_csv("hotels.csv",dtype=str)
df_cards = pd.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv",dtype=str)

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
class Spa(Hotel):
    def book_spa_pacakage(self):
        pass

class ReservationTicket:
    def __init__(self,customer_name,hotel_obj):
        self.customer_name=customer_name
        self.hotel=hotel_obj

        pass
    def generate(self):
        content=(f"""
            Your reservation is confirmed \n
            Your Name : {self.customer_name}\n
            Hotel Id : {self.hotel.hotel_id}\n
            Hotel Name : {self.hotel.name}\n
            City : {self.hotel.city}         
            """)
        return content

class CreditCard:

    def __init__(self,number):
        self.number =number

    def validate(self,expiration,cvc,holder):
        card_data  = {"number":self.number,"expiration":expiration,"cvc":cvc,"holder":holder}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCards(CreditCard):

    def authenticate(self,given_pass):
        password = df_security.loc[df_security["number"]==self.number,"password"].squeeze()
        if password==given_pass:
            return True



class SpaTicket:
    def __init__(self,customer_name,hotel_obj):
        self.customer_name=customer_name
        self.hotel=hotel_obj

    def generate(self):
        content = (f"""
                    Thanks for Booking SPA Service\n
                    Here are Your details : \n
                    Your Name : {self.customer_name}\n
                    Hotel Id : {self.hotel.hotel_id}\n
                    Hotel Name : {self.hotel.name}\n
                    City : {self.hotel.city} 
                    Spa service : YES        
                    """)
        return content


print(df)

h_id = input("Enter the Hotel ID : ")
hotel = Spa(hotel_id=h_id)


if hotel.available():
    credit_card = SecureCards(number="1234")

    if credit_card.validate(expiration="12/26",cvc="123",holder="JOHN SMITH"):
        passw= input("Enter password  : ")
        if credit_card.authenticate(given_pass=passw):
            hotel.book()
            name= input("Enter your Name  :  ")
            reservation_ticket=ReservationTicket(customer_name=name,hotel_obj=hotel)
            print(reservation_ticket.generate())
            spa=input("Do you want to Book a SPA service ?  : ")
            if spa =="yes":
                hotel.book_spa_pacakage()
                spa_ticket=SpaTicket(customer_name=name,hotel_obj=hotel)
                print(spa_ticket.generate())

            else:
                pass
        else:
            print("Authentication Failed ")

    else:
        print("There is a problem with payment")
else:
    print("Hotel is not available for booking !!")

