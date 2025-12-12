Country = input("Enter your Country name : ")
Total_visits = int(input("Enter Number of cities"))
list_of_ciies = eval(input("Enter your city list"))

travel_log = [
    {
        "Country" : "India",
        "Visited_cities":["Delhi","Mumbai","Lucknow"],"Total_visits":12
    },
    {
        "Country" : "Pakistan", 
        "Visited_cities":["Lahore","Karachi","Punjab"],"Total_visits": 12
    }

]


def add_new_country(names,times_visited,cities_visited):
    new_country = {}
    new_country["Country"] = names
    new_country["Total_visits"] = times_visited
    new_country["Visited_cities"] = cities_visited
    travel_log.append(new_country)



add_new_country(Country,Total_visits,list_of_ciies)

print(f"I've been to {travel_log[2]['Country']} {travel_log[2]["Total_visits"]}")

print(f"My favorites city way {travel_log[2]['Visited_cities'][0]}")