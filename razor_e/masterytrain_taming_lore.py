def medcheck():
    Spells.CastMastery("Combat Training")
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(0x59CE04C)
    Player.UseSkill("Animal Lore")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x59CE04C)
    Gumps.WaitForGump(475, 10000)
    Gumps.SendAction(475, 0)
    Misc.Pause(1500)
    if Player.Mana < 24:
        if Timer.Check('med') == False:
            Player.UseSkill('Meditation')
            Misc.Pause(500)
            Timer.Create('med', 1000)
            if Player.BuffsExist('Meditation'):
                while Player.Mana != Player.ManaMax:
                    Misc.Pause(200)

while True:
    medcheck()