def main():
    book_path = "books/frankentstein.txt"
    text = get_book_text(book_path)
    # # print(get_words_in_book(book_path))
    # # print(text)
    # print(count_characters(book_path))
    Print_A_Report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_in_book(path):
   text = get_book_text(path)
   words = text.split()
   words = len(words)
   return words

def count_characters(path):
    letters ="" 
    text = get_book_text(path).lower()
    # store will eventually be the dictionary that contains the return value
    store = {} 
    # makes a string that contains all of the unqiue strings
    for x in range(0,len(text)):
        if text[x] not in letters:
            letters+=text[x]
    letters = list(letters)
    for x in letters:
        lettercount = text.count(x)
        store[x] = lettercount
    return store
def Print_A_Report(path):
    print(f"--- Begin report of {path} ---")
    print(f"{get_words_in_book(path)} words found in the document\n")
    dictionary = count_characters(path)
    for char ,count in dictionary.items():
        print(f"The '{char}' character was found {count} times")


main()