from words_in_terms import get_words, count_words

DATAFOLDER = "/home/nhan/Desktop/other/cipo/data"
threshold = 10

term_9 = get_words(DATAFOLDER, 9)
term_36 = get_words(DATAFOLDER, 36)
num_of_word_class_9 = count_words(term_9)
num_of_word_class_36 = count_words(term_36)
# max_count = max(num_of_word_class_9, key=num_of_word_class_9.get)
print(num_of_word_class_36['financial'])

# count = 0
# for term in term_9:
#     for word in term_9[term]:
#         if num_of_word_class_9[word] <= threshold and word in num_of_word_class_36:
#             print(term, '-', word, num_of_word_class_9[word])
#             count += 1
# print(count)