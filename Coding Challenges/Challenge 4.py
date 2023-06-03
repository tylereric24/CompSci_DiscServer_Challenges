def main():
    print_banner()
    input_string = input("What sentence would you like to check? ")
    print(f"The longest word is {sentence_splitter(input_string)}")

def print_banner():
    print("""
    ________             ___.         .__                    _________              __                               _________ .__                   __                 
    /  _____/______   ____\_ |__  __ __|  |   ____   ____    /   _____/ ____   _____/  |_  ____   ____   ____  ____   \_   ___ \|  |__   ____   ____ |  | __ ___________ 
    /   \  __\_  __ \_/ __ \| __ \|  |  \  |  /  _ \ /    \   \_____  \_/ __ \ /    \   __\/ __ \ /    \_/ ___\/ __ \  /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
    \    \_\  \  | \/\  ___/| \_\ \  |  /  |_(  <_> )   |  \  /        \  ___/|   |  \  | \  ___/|   |  \  \__\  ___/  \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
    \______  /__|    \___  >___  /____/|____/\____/|___|  / /_______  /\___  >___|  /__|  \___  >___|  /\___  >___  >  \______  /___|  /\___  >\___  >__|_ \\___  >__|   
            \/            \/    \/                       \/          \/     \/     \/          \/     \/     \/    \/          \/     \/     \/     \/     \/    \/       
    """)
    print()

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
        
if __name__ == '__main__':
    main()
