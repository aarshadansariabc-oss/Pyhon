alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
def ceaser(dir, code, plain_text):
    final_result = ""
    if dir ==  "decode":
            code *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + code
            final_result += alphabet[new_position]
        else:
             final_result+=letter
    
    print(f"The {dir} text is : {final_result}")

should_continure = True
while should_continure:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    text = input("Enter your message : ").lower()
    shift = int(input("Enter your shift Number : "))

    shift %= 26
    ceaser(dir = direction, plain_text = text, code = shift)
    res = input("Type 'yes' if you want to continue otherwise type 'no' : ").lower()
    if res == 'no':
         should_continure = False
    else : 
         should_continure = True
