# Write the single line of code using and and not that sets a variable
# book_flight to True if (flight_cost is under the MAX_PRICE) AND (the
# destination is NOT "Asia").

flightCost = int(input("Enter the flight cost: "))
maxprice = 100000
destinantion_to_arrive_at = str(input("Enter your destination: "))
destination = "asia"
book_flight = ((flightCost<maxprice) and (destinantion_to_arrive_at!=destination))
print(book_flight)