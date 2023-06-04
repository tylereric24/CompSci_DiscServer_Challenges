
def main():
    print_banner()
    input_string = input("What sentence would you like to check? ")
    print(f"The longest word is \"{sentence_splitter(input_string)}\"")

def print_banner():
    banner = r"""\
   ______          __                        _____            __                          ________              __            
  / ____/_______  / /_  ____  ___  ____     / ___/___  ____  / /____  ____  ________     / ____/ /_  ___  _____/ /_____  _____
 / / __/ ___/ _ \/ __ \/ __ \/ _ \/ __ \    \__ \/ _ \/ __ \/ __/ _ \/ __ \/ ___/ _ \   / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
/ /_/ / /  /  __/ /_/ / / / /  __/ / / /   ___/ /  __/ / / / /_/  __/ / / / /__/  __/  / /___/ / / /  __/ /__/ ,< /  __/ /    
\____/_/   \___/_.___/_/ /_/\___/_/ /_/   /____/\___/_/ /_/\__/\___/_/ /_/\___/\___/   \____/_/ /_/\___/\___/_/|_|\___/_/     """

    print(banner)

def sentence_splitter(input_string): 
    split_string = input_string.split(" ")
    ##print(split_string)
    current_longest = ''
    for word in split_string:
        if len(word) > len(current_longest):
            current_longest = word
    return current_longest

def test_sentence_splitter():
    longest = sentence_splitter("I can't believe the Celtics choked.")
    assert longest == "believe"
    longest = sentence_splitter("Code forever.")
    assert longest == "forever."
    longest = sentence_splitter("Boss used TrenGPT for the last challenge!")
    assert longest == "challenge!"

def test_print_banner():
    print_banner()
    pass
        
if __name__ == '__main__':
    main()
