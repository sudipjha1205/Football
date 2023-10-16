from rest_framework import serializers
from .models import Top5LeagueAttack,Top5LeagueDefense,Top5LeagueGoalie
from .models import BundesligaAttackers,BundesligaDefenders,BundesligaGoalie,BundesligaGoalieAdv,BundesligaTeamAttack,BundesligaTeamDefense,BundesligaTeamKeeper



#### TOP 5 LEAGUE ######
class Top5leagueattackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top5LeagueAttack
        fields = ('index','player','nation','pos','squad','age','born','mp','starts','min','gls','ast','ga','gminuspk','penaltykick','pkatt','crdy','crdr','xg','npxg','xag','npxgxag','prgc','prgp','prgr','glsp90','astp90','gap90','gminuspkp90','gaminuspkp90','xgp90','xagp90','xgxagp90','npxgp90','npxgxagp90')

class Top5leaguedefenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top5LeagueDefense
        fields = ('index','player','nation','pos','squad','age','born','number_90s','tkl','tklw','def_3rd','mid_3rd','att_3rd','tkl_drib','att_drib','tkl_per','lost','blocks','shot','pass_field','int','intplustkl','clr','err')

class Top5leaguegoalieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top5LeagueGoalie
        fields = ('index','player','nation','pos','squad','age','born','mp','starts','min','number_90s','ga','ga90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty')


######## BUNDESLIGA  ###########

class BundesligaAttackersSerializer(serializers.ModelSerializer):

    class Meta:
        model = BundesligaAttackers
        fields = ('index','player','nation','pos','squad','age','born','mp','starts','min','gls','ast','ga','gminuspk','penaltykick','pkatt','crdy','crdr','xg','npxg','xag','npxgxag','prgc','prgp','prgr','glsp90','astp90','gap90','gminuspkp90','gaminuspkp90','xgp90','xagp90','xgxagp90','npxgp90','npxgxagp90')

class BundesligaDefendersSerializer(serializers.ModelSerializer):

    class Meta:
        model = BundesligaDefenders
        fields = ('index','player','nation','pos','squad','age','born','number_90s','tkl','tklw','def_3rd','mid_3rd','att_3rd','tkl_drib','att_drib','tkl_per','lost','blocks','shot','pass_field','int','intplustkl','clr','err')

class BundesligaGoalieSerializer(serializers.ModelSerializer):

    class Meta:
        model = BundesligaGoalie
        fields = ('index','player','nation','pos','squad','age','born','mp','starts','min','number_90s','ga','ga90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty')

class BundesligaGoalieAdvSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BundesligaGoalieAdv
        fields = ('index',  'player', 'nation', 'pos', 'squad', 'age', 'born', 'number_90s', 'ga', 'pka', 'fk', 'ck', 'og', 'psxg', 'psxgvssot', 'psxgminusga', 'psxgminusgaper90', 'lcmp', 'latt', 'lcmpperc', 'patt', 'pthr', 'plaunedperc', 'pavglen', 'gkatt', 'gklaunchperc', 'gkavglen', 'crossessfaced', 'crossedstopped', 'stopprecentage', 'defactoutpenalbox', 'defactoutpenalboxper90', 'averagedistfrompenalbox')

class BundesligaTeamAttackSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = BundesligaTeamAttack
        fields = ('index', 'squad', 'pl', 'age', 'poss', 'mp', 'starts', 'min', 'number_90s', 'gls', 'ast', 'ga', 'gminuspk', 'penaltykick', 'pkatt', 'crdy', 'crdr', 'xg', 'npxg', 'xag', 'npxgxag', 'prgc', 'prgp', 'gaminuspk', 'xgp90', 'xagp90', 'xgxagp90', 'npxgp90', 'npxgxagp90')

class BundesligaTeamDefenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = BundesligaTeamDefense
        fields = ('index', 'squad', 'pl', 'number_90s', 'tkl', 'tklw', 'def_3rd', 'mid_3rd', 'att_3rd', 'att', 'tklperc', 'lost', 'blocks', 'sh', 'pass_field', 'int', 'tklint', 'clr', 'err')

class BundesligaTeamKeeperSerializer(serializers.ModelSerializer):

    class Meta:
        model = BundesligaTeamKeeper
        fields = ('index', 'squad', 'pl', 'mp', 'starts', 'min', 'number_90s', 'ga', 'ga90', 'sota', 'saves', 'saveperc', 'w', 'd', 'l', 'cs', 'csperc', 'pkatt', 'pka', 'pksv', 'pkm')
