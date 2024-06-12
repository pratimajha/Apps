def count_duplicate(input_string):

    letter_count = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
        if char in letter_count:
            letter_count[char]+=1
        else:
            letter_count[char] = 1
    
    duplicate_letters = {}

    # for char,count in letter_count.items():
    #     if count>=1:
    #         duplicate_letters.extend({char:count})
    
    #dict comprehension
    duplicate_letters = {char:count for char,count in letter_count.items() if count>=1}

    for char,count in duplicate_letters.items():
        print(f"{char}{count}", end="")

count_duplicate("Hello World!")

        
