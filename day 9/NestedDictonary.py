capitals ={
    "france":"Paris",
    "Germany":"Barlin",
}

#Nesting a list in a Dictionary

travel_log = {
   "India" : {"visited_cities" : ["Delhi","Mumbai","Lucknow"],"total_visits" : 12},
   "Pakistan" : {"visited_cities" : ["Lahore","Karachi","Punjab"],"Total_visits": 12} 
}

#Nesting Dictionary in a List

travel_log = [
    {
        "Country" : "India",
        "Visited_cities":["Delhi","Mumbai","Lucknow"],"Total_citites":12
    },
    {
        "Country" : "Pakistan", 
        "Visited_cites":["Lahore","Karachi","Punjab"],"Total_visits": 12
    }

]