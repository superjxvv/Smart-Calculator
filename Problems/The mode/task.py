from collections import Counter
data = input().split()
freq_counter = Counter(data)
print(freq_counter.most_common(1)[0][0])
