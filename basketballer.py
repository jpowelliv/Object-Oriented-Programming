#Joseph E. Powell IV
#CIS 225-01
#Basketball Game
#9th November 2018

class Game:
	#Info
	def __init__(self, squad, city, state):
		self.squad = squad
		self.city = city
		self.state = state
	
	def getSquad(self):
		return self.squad
		
	def getCity(self):
		return self.city
		
	def getState(self):
		return self.state
		
	#str
	def __str__(self):
		return self.squad+","+self.city+","+str(self.getState())
		
	#main
def main():
	game = []
	input_stream = open("basketball.txt",'r')
	line = input_stream.readline()
	
	#loop
	while line:
		columns = line.split(',')
		squad = columns[0]
		city = columns[1]
		state = columns[2]
		basketball = Game(sqaud, city, state)
		games.append(basketball)
		line = input_stream.readline()
		
	for game in games:
		print(game)

main()
	