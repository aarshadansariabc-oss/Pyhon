

def format_name(f_name, l_name):
    """Take a first and last name and fort it
    to return the title case version fo the name."""
    if f_name =="" or l_name == "":
        return "you did not provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {
        formated_l_name
    }"
print(format_name("Anjela",""))