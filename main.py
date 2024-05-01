def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    occurance_rate = get_word_occurance(text)

    sorted_words = get_sorted_words(occurance_rate)
    printchars(sorted_words)
    print("--- End Report ---")


def printchars(list):
    for c in list:
        print(f"The '{c["char"]}' was found {c["num"]} times")
    return None


def get_sorted_words(dict):
    unsorted_list = []
    for k in dict:
        tempdict = {}
        if k.isalpha() == True:
            tempdict["char"] = k
            tempdict["num"] = dict[k]
            unsorted_list.append(tempdict)
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

def sort_on(dict):
    return(dict["num"])

    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_occurance(text):
    letters = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

main()
