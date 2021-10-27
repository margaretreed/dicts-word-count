"""Count words in file."""


# put your code here.


def count_words(file):
    word_counts = {}
    text_file = open(file)

    for line in text_file:
        line = line.rstrip()
        words = line.split(' ')

        for word in words:
            word = word.lower()
            word = word.strip(",?!:';.()")
            word_counts[word] = word_counts.get(word, 0) + 1
            # if word not in word_counts:
            #     word_counts[word] = 1

            # else:
            #     word_counts[word] = words_counts[word] + 1

    
    print(word_counts)
    return word_counts

count_words("twain.txt")
