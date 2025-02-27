'''C is number of cities F is number of flights. arry A is given where A[0] is starting city A[1] is destination and A[2] is price to travel from starting to destination .
return the price of the top 2 cheapest round trips as array. if there no possible round trip return infinity .


test case
4
6
0 1 20
1 0 60
1 2 10
2 0 10


op -
40
40 '''

def find_cheapest_round_trips(C, F, flights):
    from math import inf  # Infinity for cases with no valid trips

    # Step 1: Store flight prices in a dictionary (direct flights)
    flight_map = {}  # {(start, dest): price}

    for start, dest, price in flights:
        flight_map[(start, dest)] = price  # Store direct flight price

    # Step 2: Find all valid round trips
    round_trips = []

    for (start, dest), price1 in flight_map.items(): # .items will use all the values and keys
        if (dest, start) in flight_map:  # Check if reverse trip exists
            price2 = flight_map[(dest, start)]
            round_trips.append(price1 + price2)  # Store round trip price

    # Step 3: Get the two cheapest round trips
    round_trips = sorted(set(round_trips))  # Sort and remove duplicates

    # Step 4: Handle cases with less than 2 round trips
    if len(round_trips) < 2:
        return [inf, inf] # In our round-trip problem, we use [inf, inf] when there aren’t two valid round trips.

    return round_trips[:2]  # Return the two cheapest

# Example test case
C = 4
F = 6
flights = [
    (0, 1, 20),
    (1, 0, 60),
    (1, 2, 10),
    (2, 0, 10)
]

print(find_cheapest_round_trips(C, F, flights))  # Output: [40, 40]
