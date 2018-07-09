n = int(input())

uniq_words = []
word_counts = {}
for _ in range(n):
    word = input().strip()
    if word not in word_counts:
        word_counts[word] = 0
        uniq_words.append(word)
    word_counts[word] += 1

print(len(uniq_words))
print(' '.join(str(word_counts[word]) for word in uniq_words))