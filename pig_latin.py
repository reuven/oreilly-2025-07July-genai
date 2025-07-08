def pl_word(word):
    """
    Translates a single word into Pig Latin.
    
    Args:
        word (str): A lowercase English word without punctuation or spaces.
        
    Returns:
        str: The word translated into Pig Latin. If the word starts with a vowel,
             'way' is appended. If it starts with a consonant, the first letter
             is moved to the end and 'ay' is appended.
    """
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

for one_word in 'computer apple papaya elephant mango'.split():
    print(pl_word(one_word))

def pl_sentence(sentence):
    """
    Translates an entire sentence into Pig Latin.
    
    Args:
        sentence (str): A sentence containing words separated by spaces.
        
    Returns:
        str: The sentence with each word translated into Pig Latin,
             maintaining the original word order and spacing.
    """
    output = []
    for one_word in sentence.split():
        output.append(pl_word(one_word))
    return ' '.join(output)

print(pl_sentence('this is a test sentence for my chatbot class'))
