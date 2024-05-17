import re

def count_character_occourance(text):
    character_dict = {}
    
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict
        
def process_text_body(text):
    return re.sub(r'[^a-zA-Z]', '', text.lower())

def dict_to_list(characters_dict):
    character_list = []
    
    for key in characters_dict:
        character_list.append({ "character": key, "occurance": characters_dict[key] })
    
    return character_list

def sort_on(dict):
    return dict["occurance"]

def get_text_body(file):
    with open(file) as f:
        file_contents = f.read()
        file_contents = process_text_body(file_contents)
        
        return file_contents

def count_text_words(file):    
    with open(file) as f:
        file_contents = f.read()
        
        return len(file_contents.strip().split(" "))
def main():
    file = "books/frankenstein.txt"
    file_contents = get_text_body(file)
        
    characters_by_occurance = count_character_occourance(file_contents)
    character_list = dict_to_list(characters_by_occurance)
    character_list.sort(reverse=True, key=sort_on)
    word_count = count_text_words(file)
    
    print("--- Begin report of books/frankenstein.txt --")
    print(f"{word_count} words found in the document")
    print("")
    
    for char in character_list:
        print(f"The '{char["character"]}' character was found {char["occurance"]} times")
    
    print("--- End report ---")
main()