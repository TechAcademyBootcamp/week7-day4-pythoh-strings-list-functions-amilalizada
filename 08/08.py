words =['Azerbaycan','Turkiye','Rusiya','Iran','Gurcustan']
def longestone(words):
    longest_string=max(words, key=len)
    return len(longest_string)
print(longestone(words))

