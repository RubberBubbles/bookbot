
#my first attempt
#def main():
#    with open("books/frankenstein.txt") as f:
#        file_contents = f.read()
#        print(f)

#main()

def main():
    book_path = "books/frankenstein.txt"

    print(f"\n--- Begin report of {book_path} ---")

    text = get_book_text(book_path)

    num_words = count_words(text) 
    print(f"\nthe book file contains {num_words} words")
    dict_of_chars = get_chars_dict(text)
    print("\n")
    #print(dict_of_chars)

   # new_list_of_dict = convert_dict(dict_of_chars)
    
    new_sorted_list = chars_dict_to_sorted_list(dict_of_chars)

    #
    for item in new_sorted_list:
        if item["char"].isalpha():
            print(f"Character {item["char"]} was found {item["num"]} times")

    print("\n --- End of Report ---")


######################## funcs below ##################

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(input_string):
    word_count = 0
    list_of_words = []

    list_of_words = input_string.split()
    for word in list_of_words:
        word_count += 1
    return word_count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_criteria(d):
    return d["num"]

#def convert_dict(dictionary):
#  return [{key: value} for key, value in dictionary.items()]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_criteria)
    return sorted_list



############################# main ########################

main()