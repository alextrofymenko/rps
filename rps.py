class Player:
	Name = None
	Hand = None

	def __init__(self, name):
		self.Name = name

class Rock: pass
class Paper: pass
class Scissors: pass

hands = {
	"r": Rock(),
	"rock": Rock(),

	"p": Paper(),
	"paper": Paper(),

	"s": Scissors(),
	"scissors": Scissors()
}

player1 = Player("Player 1")
player2 = Player("Player 2")

def GetInputFor(player):
	input = raw_input(str(player.Name) + "?") # get input
	input = input.lower().strip() # sanitize input

	player.Hand = hands.get(input, False)

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

	if (Beats(player1, player2)):
		print str(player1.Name) + " is the winner!"
	elif (Beats(player2, player1)):
		print str(player2.Name) + " is the winner!"
	else:
		print "It's a draw, let's play again!"
		RPS()

RPS()