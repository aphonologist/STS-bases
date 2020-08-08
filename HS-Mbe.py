# Andrew Lamont
# November 2019

class Candidate:
	def __init__(self, segs = '', sylls = [], feet = [], lexc = ''):
		# string of characters
		self.segments = list(segs)
		# list of ints: # of segs per syllable
		self.syllables = sylls
		# list of ints: # of segs per foot
		self.feet = feet
		self.lexical_class = lexc
		self.operation = ''

	def __str__(self):
		sylls = ' '.join(self.syllables)
		segs = ' '.join(self.segments)
		return sylls + '\n' + segs

	def __eq__(self, other):
		return self.segments == other.segments and self.syllables == other.syllables and self.feet == other.feet and self.lexical_class == other.lexical_class

	def __len__(self):
		return len(self.segments)

	def copy(self):
		return Candidate(self.segments, self.syllables[:], self.feet[:], self.lexical_class)

def Gen(input):
	cset = []
	# add fully faithful candidate
	cset.append([input.copy(), []])

	# add candidates derived by copying segments
	for i in range(len(input)):
		pass

	return cset

# Class I
grow =   Candidate('bu',   '()', [(0,1)], lexc = 'I', root = True)
dig =    Candidate('kab',  '( )', lexc = 'I', root = True)
drive =  Candidate('wel',  '( )', lexc = 'I', root = True)
cook =   Candidate('lam',  '( )', lexc = 'I', root = True)
send =   Candidate('tuOm', '(  )', lexc = 'I', root = True)
cut =    Candidate('SIEb', '(  )', lexc = 'I', root = True)
refuse = Candidate('tuEn', '(  )', lexc = 'I', root = True)
beold =  Candidate('ruEn', '(  )', lexc = 'I')
print(grow)
print(dig)
print(drive)
print(cook)
print(send)
print(cut)
print(refuse)
print(beold)

# Class II
pull =     Candidate('-ru',    [(1,2)], lexc = 'II')
goout =    Candidate('-jubo',  [(1,2),(2,3)], lexc = 'II')
descend =  Candidate('-soro',  [(1,2),(2,3)], lexc = 'II')
blow =     Candidate('-fuel',  [(1,4)], lexc = 'II')
teach =    Candidate('-taN',   [(1,3)], lexc = 'II')
collide =  Candidate('-Geno',  [(1,2), (3,4)], lexc = 'II')
forget =   Candidate('-jiOnI', [(1,3), (4,5)], lexc = 'II')
behigher = Candidate('-DuON',  [(1,4)], lexc = 'II')

