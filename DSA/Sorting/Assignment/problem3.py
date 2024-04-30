def top_k_frequent_words(words, k):
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the words based on their counts and lexicographical order
    sorted_words = sorted(word_counts.keys(), key=word_counts.get, reverse=True)
    sorted_words.sort()  # Sort lexicographically

    # Return the top k frequent words
    return sorted_words[:k]

# Example usage:
words = ['priya', 'bhatia', 'akshay', 'arpit', 'priya', 'arpit']
k = 3
result = top_k_frequent_words(words, k)
print(result)