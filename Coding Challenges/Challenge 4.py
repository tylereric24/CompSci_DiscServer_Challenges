print(""" 
 ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||G |||r |||e |||b |||u |||l |||o |||n |||       |||S |||e |||n |||t |||e |||n |||c |||e |||       |||C |||h |||e |||c |||k |||e |||r ||
||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
""")


input_string = input("What sentence would you like to check? ")


def sentence_splitter(input_string):
    split_string = input_string.split(" ")
    print(split_string)
    current_longest = ''
    for word in split_string:
        if len(word) > len(current_longest):
            current_longest = word
    return current_longest
        




print(f"The longest word is {sentence_splitter(input_string)}")
