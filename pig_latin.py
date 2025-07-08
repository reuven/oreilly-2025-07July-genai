def pl_word(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

for one_word in 'computer apple papaya elephant mango'.split():
    print(pl_word(one_word))

def pl_sentence(sentence):
    output = []

    for one_word in sentence.split():
        output.append(pl_word(one_word))

    return ' '.join(output)

print(pl_sentence('this is a test sentence for my chatbot class'))
