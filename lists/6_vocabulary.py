# You've been given a list of vocabulary words grouped into sub-lists, by 
# meaning. This is a two-dimensional list or a nested list. Write some code 
# that iterates through and prints all the words, one per line.

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

for vocab_list in vocabulary:
    for vocab in vocab_list:
        print(vocab)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# fatigued
# drained
# excited
# eager
# enthused
# animated

# Nested comprehension practice
flattened_vocabulary_list = [vocab for vocab_list in vocabulary
                              for vocab in vocab_list]

for vocab in flattened_vocabulary_list:
    print(vocab)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# fatigued
# drained
# excited
# eager
# enthused
# animated
