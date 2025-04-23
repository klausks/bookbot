def count_words(text):
    return len(text.split())

def count_char_occurrences(text):
    character_occurrences = {}
    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in character_occurrences:
            character_occurrences[lower_case_char] += 1
        else:
            character_occurrences[lower_case_char] = 1
    return character_occurrences

def sorted_char_count(dict):
    char_occurrences = [{"char": char, "num": dict[char]} for char in dict]
    # print(char_occurrences)
    # sort_on = lambda occurence : occurence["num"]
    char_occurrences.sort(reverse=True, key=sort_on)
    return char_occurrences

def sort_on(dict):
    return dict["num"]