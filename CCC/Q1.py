"""
One of the rides at the funfair is a roller coaster which has one train with a number of cars. 
Each car holds the same number of people.

Your job is to determine whether or not you will be on the next train ride, assuming that every 
car is fully occupied for every ride.

Input Specification
The first line of input contains a positive integer N, representing your place in line.

*** N - input - My place in queue/line ***

The second line contains a positive integer C, representing the number of cars the train has.
*** C - input - Number of Cars ***

The third line contains a positive integer P, representing the number of people a single car holds.
*** P - input - People per car ***

Output Specification
Output either yes or no, indicating whether or not you will be on the next train ride.

Sample Input 1
N - 14 (queue number)
C - 3 (Number of cars)
P - 2 (Passenger per car)

Output for Sample Input 1
no - (yes or no output)
"""

# Read inputs
N = int(input("Your position in queue: "))
C = int(input("Number of cars: "))
P = int(input("People per car: "))

# Calculate total capacity of the train
capacity = C * P

# Check if you are within the first 'capacity' people
if N <= capacity:
    print("Yes. You may enjoy the ride!")
else:
    print("No. The ride is full. You'll have to wait!")

answer = N // capacity
if (answer == 0):
    print ("I can get on this ride.")
else:
    print ("I'll have to wait for {}th/rd train.".format(answer+1))
