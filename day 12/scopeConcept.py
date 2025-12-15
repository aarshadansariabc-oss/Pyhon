
###################Scope##################
boys = 2
def increase_boys():
    boys = 5
    print(f"Boys in funciton : {boys}")

increase_boys()
print(f"Boys outside of fucntion : {boys}")


#####################Local Scope#############

def total_teacher():
    teacher = 5
    print(f"Tearch is {teacher}")

total_teacher()
# print(teacher)  getting error we cannot acess this due to teacher variable declared within a funciton 

###################MOdify Global scope #############

enemies = 3

def increase_enimies():
   return enemies+1

enemies = increase_enimies()
print(f"Enemies are : {enemies}")

PI = 3.14159
