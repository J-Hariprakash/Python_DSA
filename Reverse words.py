def reverseWords(s):
    words = s.split()
    rev = " ".join(reversed(words))
    return rev
s = input("Enter a Sentence: \n")
result = reverseWords(s)
print(result)
