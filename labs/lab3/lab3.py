"""
Briana Addison
Lab 3
lab3.py
Traffic
Problem: This code solves the problem of analyzing traffic patterns by using nested loops
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    surveyed_roads = eval(input("How many roads were surveyed?"))
    total_vehicles = 0
    for m in range(surveyed_roads):
        average_per_road = 0
        print("How many days was road",m + 1, "surveyed?")
        days_surveyed = eval(input())
        for i in range(days_surveyed):
           print("How many cars traveled on day", i + 1, "?")
           cars_traveled = eval(input())
           average_per_road = cars_traveled + average_per_road
        print("Road", i + 1, "average vehicles per day:",average_per_road/days_surveyed )
        total_vehicles = average_per_road + total_vehicles
    print("Total number of vehicles traveled on all roads:", total_vehicles)
    print("Average number of vehicles per road:", round(total_vehicles/surveyed_roads, 2))








