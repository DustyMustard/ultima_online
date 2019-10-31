g = Player.Serial #keeps your character invisible

while True:
    if Player.Visible == True:
        Spells.CastMagery("Invisibility")
    Target.WaitForTarget(1000, False)
    if Target.HasTarget():
        Target.TargetExecute(g)
        Misc.Pause(2500)