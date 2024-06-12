def count_duplicate_letters(input_string):
    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate over each character in the input string
    for char in input_string:
        # If the character is a letter, convert it to lowercase (for case insensitivity)
        if char.isalpha():
            char = char.lower()
            # If the character is already in the dictionary, increment its count
            if char in letter_count:
                letter_count[char] += 1
            else:
                # Otherwise, add the character to the dictionary with a count of 1
                letter_count[char] = 1
    
    # Create a dictionary to store only the duplicate letters
    duplicate_letters = {char: count for char, count in letter_count.items() if count >= 1}
    
    # Output the count of each duplicate letter
    for char, count in duplicate_letters.items():
        print(f"{char}{count}", end="")

count_duplicate_letters("Hello")