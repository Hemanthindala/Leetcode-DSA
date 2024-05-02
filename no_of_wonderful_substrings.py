
# Method -1 : O(n2) ---- Gives time limit exceeded
def wonderfulSubstrings(self, word):
    n = len(word)
    arr = []
    for i in range(n):
        stri = ""
        for j in range(i, n):
            stri = stri + word[j]
            arr.append(stri)
    counter = 0
    for element in arr:
        dict = {}
        n = len(element)
        for i in range(n):
            if element[i] not in dict:
                dict[element[i]] = 1
            else:
                dict[element[i]] += 1
        count = 0
        for i in dict:
            if dict[i] % 2 != 0:
                count = count + 1
        if count <= 1:
            counter = counter + 1

    return counter


#Method-2:
