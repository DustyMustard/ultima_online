import math
from System.Collections.Generic import List

# Calculates distance between player and given coords
def distance(x1,y1):
    x2 = Player.Position.X
    y2 = Player.Position.Y
    return math.floor(math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)))
    
# Tries PathFindTo on exact coords and 1 square around to find a route
def pathfindNear(x, y, z, isItem):
    startX = Player.Position.X
    startY = Player.Position.Y
   
    for dx in [0, -1, 1]:
        for dy in [0, -1, 1]:
            # If it's an item, ignores the exact given coords and search 1 square around
            if (isItem and (dx == 0 and dy == 0)): continue
            # Just a debug code to see which path is choosed, you can safely comment out...
            Misc.SendMessage(str(dx) + ' ' + str(dy))
            Player.PathFindTo(x + dx, y + dy, z)
            # This pause added to wait PathFindTo calculate its route and check moving is started
            # Because PathFindTo runs async and returns nothing
            # You need to increase wait if you see many paths on previous SendMessage line
            Misc.Pause(100)
            if(startX != Player.Position.X or startY != Player.Position.Y): break
            
        if(startX != Player.Position.X or startY != Player.Position.Y): break
    
    # You can comment out these lines if you don't want to pause script till arrive to position
    while distance(x, y) > 1: Misc.Pause(100)
            
def pathfindToNearestItem(filter):
    item = Items.Select(Items.ApplyFilter(filter), 'Nearest')
    if item is None: return False
    Items.Message(item, 53, 'Come to me!')
    pathfindNear(item.Position.X, item.Position.Y, item.Position.Z, True)

def pathfindToNearestMobile(filter):
    mobile = Mobiles.Select(Mobiles.ApplyFilter(filter), 'Nearest')
    if mobile is None: return False
    Mobiles.Message(mobile, 53, 'Come to me!')
    pathfindNear(mobile.Position.X, mobile.Position.Y, mobile.Position.Z, False)
    
def pathfindToCoords(x, y, z):
    pathfindNear(x, y, z, False)
    
def test():
    itemFilter = Items.Filter()
    itemFilter.RangeMax = 24
    itemFilter.OnGround = True
    itemFilter.Enabled = True
    itemFilter.Movable = False
    itemFilter.Graphics = List[int]((0x0EDC, 0x0EDC))

    mobileFilter = Mobiles.Filter()
    mobileFilter.RangeMax = 24

    pathfindToNearestMobile(mobileFilter)
    Misc.Pause(1000)
    pathfindToNearestItem(itemFilter)
    Misc.Pause(1000)
    pathfindToCoords(Player.Position.X - 5, Player.Position.Y - 5, 0)
    
test()