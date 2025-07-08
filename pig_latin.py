def pl_word(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

for one_word in 'computer apple papaya elephant mango'.split():
    print(pl_word(one_word))
    