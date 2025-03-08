def word_count(string_of_words):
    words = len(string_of_words.split())
    return words

def character_count(string_of_words):
    lowercase_string = string_of_words.lower()
    characters = {}

    for char in lowercase_string:
        characters[char] = characters.get(char, 0) + 1

    return characters

def format_display(characters_to_format):
    formatted_characters = []
    for char, count  in characters_to_format.items():
        # Skip non alpha-numeric
        if char.isalpha():
            # Create a dictionary for this character and its count
            char_dict = {"char" : char, "count": count}
            formatted_characters.append(char_dict)

        # Define sorting function
        def sort_by(dict):
            return dict["count"]
        
        # Sort by count in descending order
        formatted_characters.sort(reverse=True, key=sort_by)
        

    return formatted_characters