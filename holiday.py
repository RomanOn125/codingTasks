def get_plane():
 while True:
  print(f"Please check the list of available flights: {city_flight}")
  entered_city = input("Enter your destination: ").lower()
  if entered_city in city_flight and entered_city != "kyiv":
   return entered_city
  elif entered_city == "kyiv":
   print("Sorry, this destination is not available at the moment. There's war in Ukraine")
  else:
   print("Invalid entry")
  

def get_car():
 while True:
  print(f"Please check the list of cars available to rent: {cars}")
  entered_car = input("Choose your car: ").lower()
  if entered_car in cars:
   return entered_car
  else:
   print("Invalid entry")


def num_hotel_nights():
  while True:
    try:
     num_h = int(input(("How many nights would you like to spend in this city? ")))
     if num_h in range (1, 61):
      return num_h
     else:
      print("Invalid entry, maximum stay 60 nights")
    except ValueError:
      print("Enter a valid number")


def num_car_rent_days():
  while True:
    try:
     num_c = int(input(("For how many days would you like to rent a car? ")))
     if num_c in range (1, 31):
      return num_c
     else:
      print("Invalid entry, maximum rent 30 days")
    except ValueError:
      print("Enter a valid number")


def hotel_cost(num_nights):
  while True:
   print(f"Please select hotel from the list: {hotels}")
   entered_hotel = input("What hotel would you like to stay in: ").lower()
   if entered_hotel in hotels:
    total_hotel_cost = hotel_price[entered_hotel]*num_nights 
    print(f"Total cost for this hotel is {total_hotel_cost:.2f} usd")
    return total_hotel_cost
   else:
    print("Invalid entry")


def plane_cost(city):
   total_plane_cost = plane_price[city]
   print(f"Flight cost for this desination is {total_plane_cost:.2f} usd")
   return total_plane_cost


def car_cost(new_car):
   total_car_cost = car_price[new_car]*num_car_rent_days()
   print(f"Rent cost for this car is {total_car_cost:.2f} usd")
   return total_car_cost


def holiday_cost():
 total_holiday_cost = plane_cost(get_plane()) + hotel_cost(num_hotel_nights()) + car_cost(get_car())
 print(f"Total cost for your holiday is {total_holiday_cost:.2f} usd")


city_flight = [
    "toronto",
    "new york",
    "kyiv",
    "barcelona",
    "london",
    "singapore"
]

plane_price = {
    "toronto": 1500,
    "new york": 1800,
    "kyiv": 395,
    "barcelona": 795,
    "london": 850,
    "singapore": 3500
}

hotels = [
    "premier inn",
    "hilton",
    "holiday inn",
    "grand hotel",
    "plaza hotel",
    "travelodge"
]

hotel_price = {
    "premier inn": 150,
    "hilton": 350,
    "holiday inn": 175,
    "grand hotel": 400,
    "plaza hotel": 450,
    "travelodge": 195
}

cars = [
    "nissan micra",
    "toyota aygo",
    "shkoda fabia",
    "vw passat",
    "nissan xtrail",
    "ford kuga"
]

car_price = {
    "nissan micra": 75,
    "toyota aygo": 95,
    "shkoda fabia": 85,
    "vw passat": 120,
    "nissan xtrail": 150,
    "ford kuga": 210
}

if __name__ == "__main__":
 holiday_cost()
