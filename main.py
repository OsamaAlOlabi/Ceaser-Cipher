alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = '''
 ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄ 
█ █   ▐ ▐  ▄▀   ▐ █ █    ▌ █   █   █ ▐  ▄▀   ▐ █    █  ▐ █ █   ▐ 
   ▀▄     █▄▄▄▄▄  ▐ █      ▐  █▀▀█▀    █▄▄▄▄▄  ▐   █        ▀▄   
▀▄   █    █    ▌    █       ▄▀    █    █    ▌     █      ▀▄   █  
 █▀▀▀    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄    ▄▀        █▀▀▀   
 ▐       █    ▐   █     ▐  ▐     ▐    █    ▐   █          ▐      
         ▐        ▐                   ▐        ▐                 
'''
print(logo)
introduction = print("HOW TO USE:\nFirst, you need to choose what you want to do.\nNext, you need to type in your message.\nFinally, you need to specify how many shifts between your letter and the new one.")

def ceasar(direction, text, shift):

    global new_position

    magic_word = ""
    shift %= 25

    if direction == "encode" or "decode":

        for letters in text:
            if letters in alphabet:
                position = alphabet.index((letters))
                if direction == "encode":
                    new_position = position + shift
                elif direction == "decode":
                    new_position = position - shift
                new_letter = alphabet[new_position]
                magic_word += new_letter
            else:
                magic_word += letters
        print("")
        print(f"Your {direction}d message is '{magic_word}'")


while True:
    direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower().lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(direction, text, shift)

    try_again = input("Would you like to try again?: 'Y' or 'N'\n").lower()
    if try_again == "y":
        pass
    elif try_again == "n":
        exit()


