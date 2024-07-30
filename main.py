def main():
    book_path = "books/frankentstein.txt"
    text = get_book_text(book_path)
    print(get_words_in_book(book_path))
    # print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_in_book(path):
   text = get_book_text(path)
   words = text.split()
   words = len(words)
   return words
main()