import sys
#
if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())
#
targetToon = Target.PromptTarget('Who do you want to follow')
toon = Mobiles.FindBySerial( targetToon )
while True:
    #Follow script by matsamilla
    if Player.DistanceTo( toon ) >= 1:
        toonPosition = toon.Position
        toonCoords = PathFinding.Route()
        toonCoords.MaxRetry = 5
        toonCoords.StopIfStuck = False
        toonCoords.X = toonPosition.X
        toonCoords.Y = toonPosition.Y - 1
        PathFinding.Go( toonCoords )
    Journal.Clear()
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(100, True)
    Target.TargetExecute(toon)
    if Journal.Search("fail to tame"):
        Journal.Clear()
        Player.UseSkill("Animal Taming")
        Target.WaitForTarget(100, True)
        Target.TargetExecute(toon)
    if Journal.Search("seems to accept you as master"):
        sys.exit()