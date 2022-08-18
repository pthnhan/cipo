import Levenshtein

# print(Levenshtein.jaro_winkler("house", "home"))

str1 = "you guys were absolutely amazing tonight, a..."
str2 = "ly amazin"

def find_match(str1,str2):
    min_similarity = .75
    output = []
    results = [[Levenshtein.jaro_winkler(x,y) for x in str1.split()] for y in str2.split()]
    for x in results:
        if max(x) >= min_similarity:
            output.append(str1.split()[x.index(max(x))])
    return output

print(find_match(str2, str1))