def main():
    text = input("Please enter a string of text")
    print("Input text:", text)

    # I converted the entire text to lowercase to ensure consistent counting
    normalized_text = text.lower()
    print("Normalized text:", normalized_text)

    words = normalized_text.split()
    print("List of words:", words)

    word_count = {}
    for word in words:
        if word in word_count:      # Check if the word is already a key in our dictionary
            word_count[word] += 1   # If yes, increment its count by 1
        else:                       # If not, add the word to the dictionary with a starting count of 1
            word_count[word] = 1

    print("Word count dictionary:", word_count)

    items = list(word_count.items())

    items.sort(key=lambda x: x[1], reverse=True)
    print("Sorted items:", items)

    print("\nWord Frequency Results:")  # Print results header
    for word, count in items:
        # Format and print each word and its count
        print(f"{word}:{count}")


main()
