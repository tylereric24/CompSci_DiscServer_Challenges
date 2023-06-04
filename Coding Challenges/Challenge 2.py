#Converts user input to and from morse code

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u","v","w","x","y","z"]
morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.", "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def encrypt():
    user_input = input("What would you like to encrypt?\n").lower()
    output = ""
    for x in user_input:
        if x in letters:
            output += morsecode[letters.index(x)]
            output += " "
        elif x == " ":
            output += " "
    print(output)

def decrypt():
    user_input = input("What would you like to decrypt?\n").lower()
    output = ""
    for x in user_input:
        if x in morsecode:
            output += letters[morsecode.index(x)]
        elif x == " ":
            output += " "
    print(output)

def main():
    user_input = input("Would you like to encrypt or decrypt?\n").lower()
    if user_input == "encrypt":
        encrypt()
    elif user_input == "decrypt":
        decrypt()
    else:
        print("Invalid input")
        main()

main()


