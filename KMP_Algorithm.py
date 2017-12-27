# KMP (Knuth Morris Pratt) Algorithm for pattern matching

def patternArray(arr):
    pArr = [0 for x in range(len(arr))]
    i = 1
    j = 0
    while i < len(arr):
        if arr[i] == arr[j]:
            j += 1
            pArr[i] = j
            i += 1
        else:
            if j!=0:
                j = pArr[j-1]
            else:
                pArr[i]= 0
                i+=1
    return pArr

def kmp_algo(text, pattern):
    match = patternArray(pattern)


text = "abcabceabcabc"
pattern = "abcab"

kmp_algo(text, pattern)