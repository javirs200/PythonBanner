from characters import custom_characters

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print_custom_word(alphabet)
    print()
    print_custom_word("goodjob")
    
def print_custom_word(word:str):
    word = word.upper()
    for row in range(5):
        for char in word:
            print(custom_characters[char][row], end=" ")
        print()
    
if __name__ == "__main__":
    main()