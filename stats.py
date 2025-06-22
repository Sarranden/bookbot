def text_to_words(book):
    num_words = 0
    for i in book.split(maxsplit=-1):
        num_words += 1
    return num_words

def count_characters(text):
    char_count= {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] = char_count[lower_char] + 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_dic(dic):
    sorted_dic = []
    for char_key, num_value in dic.items():
        sorted_dictionary = {
            "char": char_key,
            "num": num_value
        }
        sorted_dic.append(sorted_dictionary)
    def sorted_dictionary_num(sorted_dictionary):
        return sorted_dictionary["num"]
    sorted_dic.sort(reverse=True, key=sorted_dictionary_num)
    return sorted_dic