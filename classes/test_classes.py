import unittest
from card_definitions import Card
from player_definitions import Player

class TestClasses(unittest.TestCase):

    def test_valid_roll_dice(self):
        roll = Player('Kamelia',15,12,[5,2,2],1,True,15,9,True )
        self.assertEqual(roll.roll_dice,True)
    
    def test_move_player(self,nb):
        movep = Player('Kamelia',4,2,[7,12,12],8,True,9,7,True)
        self.assertEquals(movep.move_player,True)
    
    def test_bankrupt_player(self): 
        bnkplayer = Player('Kamelia',5,2,[25,82,2],10,True,5,8,False )
        self.assertEquals(bnkplayer.bankrupt_player,True)

    def test_mortgage(self):
        mortg = Card('Chance','orange', 128, 200000,10000,20,19,"Kamelia",True)
        self.assertEquals(mortg.mortgage, True)

    def test_sell(self):
        sells = Card('Prison','vert', 1, 30,30000,2,1,"Kamelia",False)
        self.assertEquals(sells.sell, True)

    if __name__ == "__main__":
        unittest.main()
