import random

def get_words_from_file():
    with open("sowpods.txt", "r") as f:
        words = [word.replace("\n", "") for word in f.readlines()]
    return words

def get_random_sentence(length):
    words = get_words_from_file()
    sentence = random.choices(words, k=length)
    return ", ".join([word.lower() for word in sentence])

def ask_user():
    while True:
        l = input("Length of the sentence (int between 2 and 20): ")
        if not l.isdigit():
            print("Input needs to be a digit")
            continue
        l = int(l)
        if l < 2 or l > 20:
            print("input needs to be between 2 and 20")
            continue
        else:
            break
    return l

def main():
    print("...Explanatory message...")
    length = ask_user()
    print(get_random_sentence(length))

if __name__ == '__main__':
    main()