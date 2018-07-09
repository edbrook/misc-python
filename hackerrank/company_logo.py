from collections import Counter

top_letters = Counter(input()).most_common()
top_letters.sort(key=lambda n: (-n[1], n[0]))
print('\n'.join('{} {}'.format(*x) for x in top_letters[:3]))