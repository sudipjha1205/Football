from django.contrib import admin
from AppTwo.models import Top5LeagueAttack,Top5LeagueDefense,Top5LeagueGoalie
from AppTwo.models import BundesligaAttackers,BundesligaDefenders,BundesligaGoalie,BundesligaGoalieAdv,BundesligaTeamAttack,BundesligaTeamDefense,BundesligaTeamKeeper

admin.site.register(Top5LeagueAttack)
admin.site.register(Top5LeagueDefense)
admin.site.register(Top5LeagueGoalie)
admin.site.register(BundesligaAttackers)
admin.site.register(BundesligaDefenders)
admin.site.register(BundesligaGoalie)
admin.site.register(BundesligaGoalieAdv)
admin.site.register(BundesligaTeamAttack)
admin.site.register(BundesligaTeamDefense)
admin.site.register(BundesligaTeamKeeper)
