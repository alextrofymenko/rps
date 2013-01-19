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
		self.Beats = [ Scissors ]
		self.LosesTo = [ Paper ]

class Paper (Hand): 
	def __init__(self):
		self.Values = [ "p", "paper" ]
		self.Beats = [ Rock ]
		self.LosesTo = [ Scissors ]

class Scissors (Hand): 
	def __init__(self):
		self.Values = [ "s", "scissors" ]
		self.Beats = [ Paper ]
		self.LosesTo = [ Rock ]

hands = [ Rock(), Paper(), Scissors() ]

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

def Beats(player1, player2):
	if (isinstance(player1.Hand, Rock) and isinstance(player2.Hand, Scissors) or
	isinstance(player1.Hand, Paper) and isinstance(player2.Hand, Rock) or
	isinstance(player1.Hand, Scissors) and isinstance(player2.Hand, Paper)):
		return True
	else:
		return False

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