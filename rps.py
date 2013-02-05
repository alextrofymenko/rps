class Player:
	Name = None
	Hand = None

	def __init__(self, name):
		self.Name = name

class Hand: 
	Values = None
	Beats = None
	LosesTo = None

	def __lt__(self, other):
		for hand in self.LosesTo:
			if (isinstance(other, hand)):
				return True

		return False

	def __gt__(self, other):
		for hand in self.Beats:
			if (isinstance(other, hand)):
				return True

		return False

class Rock (Hand): 
	def __init__(self):
		self.Values = [ "r", "rock" ]
		self.Beats = { 
			Scissors: "Rock dulls scissors...", 
			Lizard: "Rock crushes lizard"
		}
		self.LosesTo = [ Paper, Spock ]

class Paper (Hand): 
	def __init__(self):
		self.Values = [ "p", "paper" ]
		self.Beats = [ Rock, Spock ]
		self.LosesTo = [ Scissors, Lizard ]

class Scissors (Hand): 
	def __init__(self):
		self.Values = [ "s", "scissors" ]
		self.Beats = [ Paper, Lizard ]
		self.LosesTo = [ Rock, Spock ]

class Lizard (Hand):
	def __init__(self):
		self.Values = [ "l", "lizard" ]
		self.Beats = [ Paper, Spock ]
		self.LosesTo = [ Rock, Scissors ]

class Spock (Hand):
	def __init__(self):
		self.Values = [ "sp", "spock" ]
		self.Beats = [ Rock, Scissors ]
		self.LosesTo = [ Paper, Lizard ]

hands = [ Rock(), Paper(), Scissors(), Lizard(), Spock() ]

player1 = Player("Player 1")
player2 = Player("Player 2")

def GetPlayerHand(str):
	for hand in hands:
		try:
			hand.Values.index(str)
			return hand
		except ValueError: pass

	return False

def GetInputFor(player):
	input = raw_input(str(player.Name) + "?") # get input
	input = input.lower().strip() # sanitize input

	player.Hand = GetPlayerHand(input)

	if (not player.Hand):
		print "Input invalid, please try again"
		return False

	return True

def RPS():
	while not GetInputFor(player1):
		pass

	while not GetInputFor(player2):
		pass

	if (player1.Hand > player2.Hand):
		print str(player1.Name) + " is the winner!"
	elif (player1.Hand < player2.Hand):
		print str(player2.Name) + " is the winner!"
	else:
		print "It's a draw, let's play again!"
		RPS()

RPS()