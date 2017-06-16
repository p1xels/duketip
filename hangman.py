from numpy import random
import re

DEBUG = False

def filter_string(word,lst):
	# Create a regex that matches every letter not 
	# in lst, and filter the word based on it.
	if len(lst):
		return re.sub(r'[^#'+''.join(lst)+r']', '_', word)
	else:
		return '_' * len(word) # ew
		
def get_hangman(n):
	if n > len(hangmen):
		if DEBUG: print "WARNING: Tried to get %d, but only %d hangmen exist! Defaulting..."
		return hangmen[-1] # print first hangman
	return hangmen[n]

with open('words.txt', 'r') as file:
    words = file.read().splitlines() # set words to list of lines in words.txt

with open('hanged.txt', 'r') as file:
	hangmen = file.read().split('-#SPLIT#-')[::-1] 
	# split hanged.txt by -#SPLIT#-, save to array, reverse array 
	# we reverse the array so it can be accessed by indexing the number of tries left

word = random.choice(words)
if DEBUG:
	print "DEBUG: word is %s!" % word
	print hangmen

ltrs = set(word) 
ltrsknown = set()
tries = 6

print hangmen[-1] # print the first hangman
while ltrs != ltrsknown and not tries == 0:
	print "Word: %s | Tries: %d" % (filter_string(word, ltrsknown), tries)
	i = raw_input('> ').strip()
	if not len(i) or not i.isalpha(): 
		print "Please enter a letter."
		continue
	elif len(i) == 1:
		if i in ltrs and not i in ltrsknown:
			print "Correct!"
			ltrsknown.add(i)
		elif i in ltrsknown:
			print "Already known."
			continue
		else: 
			tries -= 1
			print "Incorrect! Tries: %s" % tries
	else:
		print "Please enter only one letter."
		continue
	print get_hangman(tries)
print

if ltrs == ltrsknown: 
	print "You win!"
else:
	print "You lost."
	print "The word was %s!" % word
