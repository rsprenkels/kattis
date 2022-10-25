num_words = int(input())
word_list = []
for _ in range(num_words):
    word_list.append(input())
for index in range(0, num_words, 2):
    print(word_list[index])