def get_word_count(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count
def get_character_counts(text):
    lower_case_text = text.lower()
    char_counts = {}
    for char in lower_case_text:
        char_counts.setdefault(char, 0)
        char_counts[char] += 1
    return char_counts
def get_sorted_dicts(dict):
    dict_list = []
    def sort_on(input):
        return input["num"] 
    for char in dict:
        char_dict = {"char": char, "num": dict[char]}
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
        
    

