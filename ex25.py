def break_words(stuff):
    """This function will break up words for us."""
    words=stuff.split(' ') 
    return words
	
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
	
def print_first_word(words):
    """Prints the first word after popping it off."""
    word=words.pop(0)
    return word
	
def print_last_word(words):
    """Prints the last word after popping it off."""
    word=words.pop(-1)
    return word
	
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words=break_words(sentence)
    return sort_words(words)
	
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)
    return print_first_word(words),print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words=sort_sentence(sentence)
    first=print_first_word(words)
    last=print_last_word(words)
    return first,last

'''#stuff="my name is xyz"
sentence="you can eat an apple!"

words=break_words(stuff)
print "words:%s" %words

sorts=sort_words(words)
print "sorts:%s" %sorts

first_word=print_first_word(words)
print "first_word:%s" %first_word

last_word=print_last_word(words)
print "last_word:%s" %last_word

sorts=sort_sentence(sentence)
print "sort_sentence:%s" %sorts

print "first_and_last:%s %s" %print_first_and_last(sentence)

print "first_and_last_sorted:%s %s" %print_first_and_last_sorted(sentence)
'''