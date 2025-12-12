program_dictonary = {"Bug":"Zero divison error,","division":"This is division function"}

#Retreving items for dictonary
print(program_dictonary["Bug"])

#Adding new items to dictonary
program_dictonary["Loop"] = "Doing something Again and Again"



#Creating an Empity Dictonary
empty_dictonary = {}

#Wipe and existing dictionary
# program_dictonary = {}

# print(program_dictonary)

#Edit an item in a dictionary

program_dictonary["Bug"] = "No Error"
print(program_dictonary["Bug"])

#Loop through Dictonary

for keys in program_dictonary:
    print(keys)
    print(program_dictonary[keys])

