# This script will run UNTIL you stop it. If you hotkey it, think of it as an on/off switch.
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

#Pet list you can add to it by putting the mobileID number in the list. 
petList = [
# PetList
 0x03A5A5DB, # Meta Dragon
]


petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 15
petfilter.IsHuman = False
petfilter.IsGhost = False
petfilter.Serials = List[int] (petList)

while Player.IsGhost == False: 
    
    petList = Mobiles.ApplyFilter(petfilter)   
    for g in petList:
        g = Mobiles.Select(petList, 'Weakest')
        
        #bandage        
        #check health level if in range one of guilded meta pet heals with bandages.          
        if g.Hits < 23:
                if Target.HasTarget( ) == False:
                    Spells.CastMagery('Greater Heal')
                    Target.WaitForTarget(5000, True)
                    Target.TargetExecute(g)
                    Misc.Pause (500)
                    Journal.Clear()
                    break
        
        if Journal.Search("too far away"):
            Journal.Clear()
        elif Journal.Search("stay close enough"):
            Player.HeadMessage(95, "You moved")
            Journal.Clear()
    Misc.Pause(50)
Target.ClearLastandQueue()
Target.Cancel() 
