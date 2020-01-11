healPot = 0x0F0C
curePot = 0x0F07
apple = 0x2FD8
healHits = 90

while True:

    if Player.Hits <= healHits and not Player.IsGhost and Player.Visible and not Player.Poisoned and not Player.BuffsExist('Mortal Strike'):
        Spells.CastChivalry("Close Wounds")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)
    
    elif Player.Poisoned and not Player.BuffsExist('Mortal Strike'):
        Spells.CastChivalry("Cleanse By Fire")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)

    elif Player.BuffsExist('Mortal Strike'):
        Spells.CastChivalry("Remove Curse")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)

    elif Player.BuffsExist('Curse'):
        Spells.CastChivalry("Remove Curse")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)
        
    elif Player.BuffsExist('Strangle'):
        Spells.CastChivalry("Remove Curse")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)
        
    elif Player.BuffsExist('Corpse Skin'):
        Spells.CastChivalry("Remove Curse")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)
    
    elif Player.BuffsExist('Bload Oath (curse)'):
        Spells.CastChivalry("Remove Curse")
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(400)

    else:
        Misc.Pause(400)
        

