def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    number_of_words = get_number_of_words(text)
    print(f"{number_of_words} words were found in the document")
    characters = get_number_of_characters_repetitions(text)
    for char in characters:
        print(f"The '{char}' character was found {characters[char]} times.")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def to_lowercase(text):
    return text.lower()

def get_number_of_characters(text):
    return len(text)

def get_number_of_characters_repetitions(text):
    text = to_lowercase(text)
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
            
        else:
            characters[char] = 1
    return characters

def get_number_of_words(text):
    words = text.split()
    return len(words)
    
main()