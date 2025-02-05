import string

sentence = "Rotates a log file by renaming it to log_file.old and creating a new empty log file."
#sentence = "this isaa logg file offf four lett errr word."
# 1. Length of the sentence (excluding punctuation):
sentence_without_punct = sentence.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
sentence_length = len(sentence_without_punct)
print(f"Length of the sentence (excluding punctuation): {sentence_length}")

# 2. Word count and specific length counts:
words = sentence_without_punct.split()  # Split into words
word_counts = {}

for word in words:
    word_len = len(word)
    word_counts[word_len] = word_counts.get(word_len, 0) + 1

print(f"Word counts by length: {word_counts}")


# Example of accessing specific lengths:
five_letter_words = word_counts.get(4, 0) # Get count of 4 letter words, default 0 if not found
three_letter_words = word_counts.get(3, 0) # Get count of 3 letter words, default 0 if not found
print(f"Number of 5-letter words: {five_letter_words}")
print(f"Number of 3-letter words: {three_letter_words}")



import string

sentence = "Rotates a a a a a a a a a a a log file by renaming it to log_file.old and creating a new empty log file. file file file"

# Remove punctuation and split into words:
words = sentence.translate(str.maketrans('', '', string.punctuation)).split()

word_length_counts = {}

for word in words:
    length = len(word)
    if length in word_length_counts:
        count, _ = word_length_counts[length]  # Unpack the tuple (we don't need the old word)
        word_length_counts[length] = (count + 1, word) # Update with new count and word
    else:
        word_length_counts[length] = (1, word)  # Initialize with count 1 and the word

print(word_length_counts)

# Example of accessing the count and word for length 3:
if 3 in word_length_counts:
    count, word = word_length_counts[3]
    print(f"Length 3: Count = {count}, Example word = '{word}'")

# Example of accessing the count and word for length 5:
if 5 in word_length_counts:
    count, word = word_length_counts[5]
    print(f"Length 5: Count = {count}, Example word = '{word}'")

# Example of accessing the count and word for length 7:
if 7 in word_length_counts:
    count, word = word_length_counts[7]
    print(f"Length 7: Count = {count}, Example word = '{word}'")


tup = 'Hello'
print(len(tup))
tup = 'Hello',
print(len(tup))