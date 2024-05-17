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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = process_text_body(file_contents)
        count_character_occourance(file_contents)
        
main()