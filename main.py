def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = count_letters(text)
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    present_outcomes(sorted_letter_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letter_dict = {}
    text = text.lower()
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def present_outcomes(letter_count: dict):
    for letter, count in letter_count:
        print(f"The '{letter}' was found {count} times")

main()
