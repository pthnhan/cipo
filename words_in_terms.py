import pandas as pd


def get_words(data_folder: str, c: int) -> dict:
    df = pd.read_excel(f"{data_folder}/class{c}.xls", header=0, skiprows=[0])
    df = df[df.Status == 'Active']
    term = df.Term.to_list()
    words_dict = {}
    for t in term:
        words_dict[t] = t.split(" ")
    return words_dict

def count_words(words_dict: dict) -> dict:
    num_of_words = {}
    for term in words_dict:
        for w in words_dict[term]:
            if w not in num_of_words:
                num_of_words[w] = 1
            else:
                num_of_words[w] += 1
    return num_of_words

if __name__ == "__main__":
    REMOVED_WORDS = ['in', 'on', 'at', 'for', 'into', 'upon', 'up', 'from', 'the', 'a', 'an', 'of', 'and', 'or', 'be', 'use']
    words_dict = get_words("data", 1)
    num_of_words = count_words(words_dict)
    for word in REMOVED_WORDS:
        if word in num_of_words:
            del num_of_words[word]
    
    max_count = max(num_of_words, key=num_of_words.get)
    print(max_count, num_of_words[max_count])