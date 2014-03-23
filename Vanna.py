from sys import argv
script, parm_phrase = argv

import sys
import time
import string
import exceptions

#initialize variables for reading all puzzles
pzl = 0
puzzle = []


 
class Printer():
    "Print things to stdout on one line dynamically"
 
    def __init__(self,data):
 
        text=''.join(data)
        sys.stdout.write("\r\x1b[K"+text.__str__())
        sys.stdout.flush()
        time.sleep(.02)
  
  
        
def evaluate_guess(guess):
	"check the guess for vowels, number of guesses, and add to list of guesses"
	
	if len(guesses)!=0:  #first time through len(guesses) will be 0 and no space is needed
	    guesses_list = guesses + "  "
	    
	guesses_list = guesses + "["+guess+"]"
	
	if guess in list('aeiou'):
		print "Did you pay for that vowel? ;-)"
		
	if len(guesses_list) in range(21,24): 
		# in counting guesses, consider the [] characters
		print "This must be a tough puzzle for you!"
	
	return guesses_list
		


# if no phrase passed in, open the phrases file to get phrases, load puzzle string
if parm_phrase=="":
	try:
		puzzle=[line.strip() for line in open('phrases.txt')]
	except:  # FileNotFoundError
		print
		print "phrases.txt is empty or missing and call parameter is null..."
		print "Vanna has nothing to do!"
		print
		sys.exit()
else:
    puzzle.append(parm_phrase)



while pzl < len(puzzle):  #play the Vanna game for each phrase in puzzle

	# clear the screen and print the welcome
	print chr(27) + "[2J"
	print '\n' * 2
	if pzl == 0: #first puzzle
		print "Welcome to Vanna!"
	else: #a previous puzzle has been solved
		print "Great job solving: " + '\033[1m' + mask + '\033[0m' 
		print
		print "Here is your next Puzzle"
	print '\n' * 3
	print "Guess the letters in the phrase..."
	print '\n' * 2

	
	
	# load puzzle array
	puzzle_array=list(puzzle[pzl])
	
	# initialize variables for this puzzle
	mask=""
	guess = ""
	guesses = ""
	
	# load the mask string
	for letter in list(puzzle[pzl]):
			if letter == " ":
				mask+=" "
			else:
				mask+="X"
			

	# print the mask string in bold            
	print '\033[1m' + mask  + '\033[0m'


	# load the mask array
	mask_array=list(mask)


	#-----------------------------------------------
	# play the game until the mask equals the puzzle
	while puzzle[pzl] != mask:
   
		guess=raw_input("guess a letter (or type exit)> ")
	
		# clear the screen
		print chr(27) + "[2J"
	
	
		guesses=evaluate_guess(guess)

	
		if len(guess)== 1:
		#user keyed in one letter, see if it is in the puzzle
	
			# use the right article for repeating the guess to the screen
			if guess.upper() in list('BUCDGJKPQTVWYZ'):
				print ('Is there a [' + '\033[1m' + "" + guess + '\033[0m' + "" + ']?')
			else:
				print ('Is there an [' + '\033[1m' + "" + guess + '\033[0m' + "" + ']?')
	
	
			#print blank lines and set bold on
			print '\n' * 1 + '\033[1m' 


			#see if the guess is in the puzzle
			for i in range(len(mask_array)):
					if puzzle_array[i] == guess:

						#a good guess was made, spin the letter position for awesomeness
						for spin_letter in list(string.ascii_letters):
							  mask_array[i]=spin_letter
							  Printer(''.join(mask_array[0:i+1]))
   
						#set the mask to show the correct guess
						mask_array[i]=puzzle_array[i]
			
					#bad guess, so print the X
					else:
						Printer(''.join(mask_array[0:i+1]))

				
			#print the last character in the mask
			Printer(''.join(mask_array[0:i+1]))
			mask=(''.join(mask_array[0:i+1]))
		
		else:

		#user keyed in a word or phrase, check for exit request	
			if guess!="exit":
				mask=guess
				print "You guessed the whole phrase with: " + '\033[1m' + mask + '\033[0m'
				print
				print '\033[1m' + (''.join(mask_array)) + '\033[0m'	
			else:
				#user keyed in exit request, exit by solving puzzle in mask
				mask=puzzle[pzl] 

	
		#turn bold off and show guesses made, then go back to WHILE to see if puzzle is solved
		print '\033[0m' + '\n' *2
		print "Guess(es) made= ", guesses
		print
	#-----------------------------------------------------
	

	# clear the screen
	print chr(27) + "[2J"

	print "Phrase: " + '\033[1m' + mask + '\033[0m'
	print
	print "Your Guess(es): " + '\033[1m' + guesses + '\033[0m'	
	print '\n' * 2
	print "Thanks for playing, keep an eye out for the cake!"
	print '\n' * 3
	
	if guess=='exit':  #user requested exit
		pzl=len(puzzle)-1
		
	pzl+=1
        
