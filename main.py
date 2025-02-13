def count_characters(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():    
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def print_report(text, char_counts):
    word_count = len(text.split())    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    char_counts = count_characters(file_contents)  
    print_report(file_contents, char_counts)      

main()
