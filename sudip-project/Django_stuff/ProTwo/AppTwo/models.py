# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Top5LeagueAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.FloatField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Top_5_league_attack'


class Top5LeagueDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Top_5_league_defense'


class Top5LeagueGoalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(blank=True, null=True)
    number_90s = models.FloatField(blank=True, null=True)
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(blank=True, null=True)
    saves = models.BigIntegerField(blank=True, null=True)
    saveperc = models.FloatField(blank=True, null=True)
    w = models.BigIntegerField(blank=True, null=True)
    d = models.BigIntegerField(blank=True, null=True)
    l = models.BigIntegerField(blank=True, null=True)
    cs = models.BigIntegerField(blank=True, null=True)
    csperc = models.FloatField(blank=True, null=True)
    pkatt = models.BigIntegerField(blank=True, null=True)
    pka = models.BigIntegerField(blank=True, null=True)
    pksv = models.BigIntegerField(blank=True, null=True)
    pkm = models.BigIntegerField(blank=True, null=True)
    savepercpenalty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Top_5_league_goalie'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BundesligaAttackers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxg_xag = models.FloatField(db_column='npxG+xAG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bundesliga_attackers'


class BundesligaDefenders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_defenders'


class BundesligaGoalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.BigIntegerField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.FloatField(db_column='SavePerc', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.BigIntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.BigIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.FloatField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.BigIntegerField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.BigIntegerField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.
    savepercpenalty = models.FloatField(db_column='SavepercPenalty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_goalie'


class BundesligaGoalieAdv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    fk = models.BigIntegerField(db_column='FK', blank=True, null=True)  # Field name made lowercase.
    ck = models.BigIntegerField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    og = models.BigIntegerField(db_column='OG', blank=True, null=True)  # Field name made lowercase.
    psxg = models.FloatField(db_column='PSxg', blank=True, null=True)  # Field name made lowercase.
    psxgvssot = models.FloatField(db_column='PSxgvsSot', blank=True, null=True)  # Field name made lowercase.
    psxgminusga = models.FloatField(db_column='PSxgminusGA', blank=True, null=True)  # Field name made lowercase.
    psxgminusgaper90 = models.FloatField(db_column='PSxgminusGAper90', blank=True, null=True)  # Field name made lowercase.
    lcmp = models.BigIntegerField(db_column='LCMp', blank=True, null=True)  # Field name made lowercase.
    latt = models.BigIntegerField(db_column='LAtt', blank=True, null=True)  # Field name made lowercase.
    lcmpperc = models.FloatField(db_column='LCmpperc', blank=True, null=True)  # Field name made lowercase.
    patt = models.BigIntegerField(db_column='PAtt', blank=True, null=True)  # Field name made lowercase.
    pthr = models.BigIntegerField(db_column='PThr', blank=True, null=True)  # Field name made lowercase.
    plaunedperc = models.FloatField(db_column='PLaunedperc', blank=True, null=True)  # Field name made lowercase.
    pavglen = models.FloatField(db_column='PAvgLen', blank=True, null=True)  # Field name made lowercase.
    gkatt = models.BigIntegerField(db_column='GKAtt', blank=True, null=True)  # Field name made lowercase.
    gklaunchperc = models.FloatField(db_column='GKLaunchPerc', blank=True, null=True)  # Field name made lowercase.
    gkavglen = models.FloatField(db_column='GKAvgLen', blank=True, null=True)  # Field name made lowercase.
    crossessfaced = models.BigIntegerField(db_column='CrossessFaced', blank=True, null=True)  # Field name made lowercase.
    crossedstopped = models.BigIntegerField(db_column='CrossedStopped', blank=True, null=True)  # Field name made lowercase.
    stopprecentage = models.FloatField(db_column='StopPrecentage', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalbox = models.BigIntegerField(db_column='DefActOutPenalBox', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalboxper90 = models.FloatField(db_column='DefActOutPenalBoxPer90', blank=True, null=True)  # Field name made lowercase.
    averagedistfrompenalbox = models.FloatField(db_column='AverageDistfromPenalBox', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_goalie_adv'


class BundesligaTeamAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    poss = models.TextField(db_column='Poss', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.TextField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.TextField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.TextField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.TextField(blank=True, null=True)
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.TextField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.TextField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.TextField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.TextField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.TextField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.TextField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.TextField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    gaminuspk = models.TextField(db_column='GAminusPK', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.TextField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.TextField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.TextField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.TextField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.TextField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_team_attack'


class BundesligaTeamDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.TextField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.TextField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.TextField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.TextField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.TextField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    att = models.TextField(db_column='Att', blank=True, null=True)  # Field name made lowercase.
    tklperc = models.TextField(db_column='Tklperc', blank=True, null=True)  # Field name made lowercase.
    lost = models.TextField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.TextField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    sh = models.TextField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.TextField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    tklint = models.TextField(db_column='TklInt', blank=True, null=True)  # Field name made lowercase.
    clr = models.TextField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.TextField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_team_defense'


class BundesligaTeamKeeper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.TextField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.TextField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.TextField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.TextField(db_column='Saveperc', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.TextField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.TextField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.TextField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.TextField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bundesliga_team_keeper'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GcaData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.FloatField(blank=True, null=True)
    sca = models.BigIntegerField(blank=True, null=True)
    scaperninety = models.FloatField(blank=True, null=True)
    live_pass_sca = models.BigIntegerField(blank=True, null=True)
    dead_pass_sca = models.BigIntegerField(blank=True, null=True)
    take_on_sca = models.BigIntegerField(blank=True, null=True)
    shot_sca = models.BigIntegerField(blank=True, null=True)
    fouls_sca = models.BigIntegerField(blank=True, null=True)
    def_action_sca = models.BigIntegerField(blank=True, null=True)
    gca = models.BigIntegerField(blank=True, null=True)
    gcaperninety = models.FloatField(blank=True, null=True)
    live_pass_gca = models.BigIntegerField(blank=True, null=True)
    dead_pass_gca = models.BigIntegerField(blank=True, null=True)
    take_on_gca = models.BigIntegerField(blank=True, null=True)
    shot_gca = models.BigIntegerField(blank=True, null=True)
    fouls_gca = models.BigIntegerField(blank=True, null=True)
    def_action_gca = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gca_data'


class LaLigaAttackers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxg_xag = models.FloatField(db_column='npxG+xAG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'la_liga_attackers'


class LaLigaDefenders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_defenders'


class LaLigaGoalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.BigIntegerField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.FloatField(db_column='SavePerc', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.BigIntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.BigIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.FloatField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.BigIntegerField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.BigIntegerField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.
    savepercpenalty = models.FloatField(db_column='SavepercPenalty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_goalie'


class LaLigaGoalieAdv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    fk = models.BigIntegerField(db_column='FK', blank=True, null=True)  # Field name made lowercase.
    ck = models.BigIntegerField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    og = models.BigIntegerField(db_column='OG', blank=True, null=True)  # Field name made lowercase.
    psxg = models.FloatField(db_column='PSxg', blank=True, null=True)  # Field name made lowercase.
    psxgvssot = models.FloatField(db_column='PSxgvsSot', blank=True, null=True)  # Field name made lowercase.
    psxgminusga = models.FloatField(db_column='PSxgminusGA', blank=True, null=True)  # Field name made lowercase.
    psxgminusgaper90 = models.FloatField(db_column='PSxgminusGAper90', blank=True, null=True)  # Field name made lowercase.
    lcmp = models.BigIntegerField(db_column='LCMp', blank=True, null=True)  # Field name made lowercase.
    latt = models.BigIntegerField(db_column='LAtt', blank=True, null=True)  # Field name made lowercase.
    lcmpperc = models.FloatField(db_column='LCmpperc', blank=True, null=True)  # Field name made lowercase.
    patt = models.BigIntegerField(db_column='PAtt', blank=True, null=True)  # Field name made lowercase.
    pthr = models.BigIntegerField(db_column='PThr', blank=True, null=True)  # Field name made lowercase.
    plaunedperc = models.FloatField(db_column='PLaunedperc', blank=True, null=True)  # Field name made lowercase.
    pavglen = models.FloatField(db_column='PAvgLen', blank=True, null=True)  # Field name made lowercase.
    gkatt = models.BigIntegerField(db_column='GKAtt', blank=True, null=True)  # Field name made lowercase.
    gklaunchperc = models.FloatField(db_column='GKLaunchPerc', blank=True, null=True)  # Field name made lowercase.
    gkavglen = models.FloatField(db_column='GKAvgLen', blank=True, null=True)  # Field name made lowercase.
    crossessfaced = models.BigIntegerField(db_column='CrossessFaced', blank=True, null=True)  # Field name made lowercase.
    crossedstopped = models.BigIntegerField(db_column='CrossedStopped', blank=True, null=True)  # Field name made lowercase.
    stopprecentage = models.FloatField(db_column='StopPrecentage', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalbox = models.BigIntegerField(db_column='DefActOutPenalBox', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalboxper90 = models.FloatField(db_column='DefActOutPenalBoxPer90', blank=True, null=True)  # Field name made lowercase.
    averagedistfrompenalbox = models.FloatField(db_column='AverageDistfromPenalBox', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_goalie_adv'


class LaLigaTeamAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    poss = models.TextField(db_column='Poss', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.TextField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.TextField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.TextField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.TextField(blank=True, null=True)
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.TextField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.TextField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.TextField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.TextField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.TextField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.TextField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.TextField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    gaminuspk = models.TextField(db_column='GAminusPK', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.TextField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.TextField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.TextField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.TextField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.TextField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_team_attack'


class LaLigaTeamDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.TextField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.TextField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.TextField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.TextField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.TextField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    att = models.TextField(db_column='Att', blank=True, null=True)  # Field name made lowercase.
    tklperc = models.TextField(db_column='Tklperc', blank=True, null=True)  # Field name made lowercase.
    lost = models.TextField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.TextField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    sh = models.TextField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.TextField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    tklint = models.TextField(db_column='TklInt', blank=True, null=True)  # Field name made lowercase.
    clr = models.TextField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.TextField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_team_defense'


class LaLigaTeamKeeper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.TextField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.TextField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.TextField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.TextField(db_column='Saveperc', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.TextField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.TextField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.TextField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.TextField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'la_liga_team_keeper'


class Ligue1Attackers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxg_xag = models.FloatField(db_column='npxG+xAG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ligue_1_attackers'


class Ligue1Defenders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_defenders'


class Ligue1Goalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.BigIntegerField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.FloatField(db_column='SavePerc', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.BigIntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.BigIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.FloatField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.BigIntegerField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.BigIntegerField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.
    savepercpenalty = models.FloatField(db_column='SavepercPenalty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_goalie'


class Ligue1GoalieAdv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    fk = models.BigIntegerField(db_column='FK', blank=True, null=True)  # Field name made lowercase.
    ck = models.BigIntegerField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    og = models.BigIntegerField(db_column='OG', blank=True, null=True)  # Field name made lowercase.
    psxg = models.FloatField(db_column='PSxg', blank=True, null=True)  # Field name made lowercase.
    psxgvssot = models.FloatField(db_column='PSxgvsSot', blank=True, null=True)  # Field name made lowercase.
    psxgminusga = models.FloatField(db_column='PSxgminusGA', blank=True, null=True)  # Field name made lowercase.
    psxgminusgaper90 = models.FloatField(db_column='PSxgminusGAper90', blank=True, null=True)  # Field name made lowercase.
    lcmp = models.BigIntegerField(db_column='LCMp', blank=True, null=True)  # Field name made lowercase.
    latt = models.BigIntegerField(db_column='LAtt', blank=True, null=True)  # Field name made lowercase.
    lcmpperc = models.FloatField(db_column='LCmpperc', blank=True, null=True)  # Field name made lowercase.
    patt = models.BigIntegerField(db_column='PAtt', blank=True, null=True)  # Field name made lowercase.
    pthr = models.BigIntegerField(db_column='PThr', blank=True, null=True)  # Field name made lowercase.
    plaunedperc = models.FloatField(db_column='PLaunedperc', blank=True, null=True)  # Field name made lowercase.
    pavglen = models.FloatField(db_column='PAvgLen', blank=True, null=True)  # Field name made lowercase.
    gkatt = models.BigIntegerField(db_column='GKAtt', blank=True, null=True)  # Field name made lowercase.
    gklaunchperc = models.FloatField(db_column='GKLaunchPerc', blank=True, null=True)  # Field name made lowercase.
    gkavglen = models.FloatField(db_column='GKAvgLen', blank=True, null=True)  # Field name made lowercase.
    crossessfaced = models.BigIntegerField(db_column='CrossessFaced', blank=True, null=True)  # Field name made lowercase.
    crossedstopped = models.BigIntegerField(db_column='CrossedStopped', blank=True, null=True)  # Field name made lowercase.
    stopprecentage = models.FloatField(db_column='StopPrecentage', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalbox = models.BigIntegerField(db_column='DefActOutPenalBox', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalboxper90 = models.FloatField(db_column='DefActOutPenalBoxPer90', blank=True, null=True)  # Field name made lowercase.
    averagedistfrompenalbox = models.FloatField(db_column='AverageDistfromPenalBox', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_goalie_adv'


class Ligue1TeamAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    poss = models.TextField(db_column='Poss', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.TextField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.TextField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.TextField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.TextField(blank=True, null=True)
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.TextField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.TextField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.TextField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.TextField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.TextField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.TextField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.TextField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    gaminuspk = models.TextField(db_column='GAminusPK', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.TextField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.TextField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.TextField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.TextField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.TextField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_team_attack'


class Ligue1TeamDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.TextField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.TextField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.TextField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.TextField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.TextField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    att = models.TextField(db_column='Att', blank=True, null=True)  # Field name made lowercase.
    tklperc = models.TextField(db_column='Tklperc', blank=True, null=True)  # Field name made lowercase.
    lost = models.TextField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.TextField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    sh = models.TextField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.TextField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    tklint = models.TextField(db_column='TklInt', blank=True, null=True)  # Field name made lowercase.
    clr = models.TextField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.TextField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_team_defense'


class Ligue1TeamKeeper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.TextField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.TextField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.TextField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.TextField(db_column='Saveperc', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.TextField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.TextField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.TextField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.TextField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligue_1_team_keeper'


class MiscData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.FloatField(blank=True, null=True)
    yellow_card = models.BigIntegerField(blank=True, null=True)
    red_card = models.BigIntegerField(blank=True, null=True)
    second_yellow_card = models.BigIntegerField(blank=True, null=True)
    fouls_committed = models.BigIntegerField(blank=True, null=True)
    fouls_drawn = models.BigIntegerField(blank=True, null=True)
    offsides = models.BigIntegerField(blank=True, null=True)
    crosses = models.BigIntegerField(blank=True, null=True)
    interception = models.BigIntegerField(blank=True, null=True)
    tackle_won = models.BigIntegerField(blank=True, null=True)
    penalty_won = models.BigIntegerField(blank=True, null=True)
    penalty_conceded = models.BigIntegerField(blank=True, null=True)
    own_goals = models.BigIntegerField(blank=True, null=True)
    recoveries = models.BigIntegerField(blank=True, null=True)
    aerial_duels_won = models.BigIntegerField(blank=True, null=True)
    aerial_duels_lost = models.BigIntegerField(blank=True, null=True)
    aerial_duels_won_perc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'misc_data'


class PassTypeData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.FloatField(blank=True, null=True)
    total_pass_attempted = models.BigIntegerField(blank=True, null=True)
    live_pass = models.BigIntegerField(blank=True, null=True)
    dead_pass = models.BigIntegerField(blank=True, null=True)
    free_kick = models.BigIntegerField(blank=True, null=True)
    through_balls = models.BigIntegerField(blank=True, null=True)
    switches = models.BigIntegerField(blank=True, null=True)
    crosses = models.BigIntegerField(blank=True, null=True)
    throw_ins = models.BigIntegerField(blank=True, null=True)
    corner_kicks = models.BigIntegerField(blank=True, null=True)
    corner_ins = models.BigIntegerField(blank=True, null=True)
    corner_out = models.BigIntegerField(blank=True, null=True)
    straight_corner = models.BigIntegerField(blank=True, null=True)
    passess_completed = models.BigIntegerField(blank=True, null=True)
    offside_passess = models.BigIntegerField(blank=True, null=True)
    passess_blocked = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pass_type_data'


class PassingData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.FloatField(blank=True, null=True)
    total_pass_completed = models.BigIntegerField(blank=True, null=True)
    total_pass_attempted = models.BigIntegerField(blank=True, null=True)
    total_pass_completed_perc = models.FloatField(blank=True, null=True)
    total_distance = models.BigIntegerField(blank=True, null=True)
    total_progressive_dist = models.BigIntegerField(blank=True, null=True)
    short_pass_completed = models.BigIntegerField(blank=True, null=True)
    short_pass_attempted = models.BigIntegerField(blank=True, null=True)
    short_pass_completed_perc = models.FloatField(blank=True, null=True)
    medium_pass_completed = models.BigIntegerField(blank=True, null=True)
    medium_pass_attempted = models.BigIntegerField(blank=True, null=True)
    medium_pass_completed_perc = models.FloatField(blank=True, null=True)
    long_pass_completed = models.BigIntegerField(blank=True, null=True)
    long_pass_attempted = models.BigIntegerField(blank=True, null=True)
    long_pass_completed_perc = models.FloatField(blank=True, null=True)
    assists = models.BigIntegerField(blank=True, null=True)
    xag = models.FloatField(blank=True, null=True)
    xa = models.FloatField(blank=True, null=True)
    assistminusxag = models.FloatField(blank=True, null=True)
    key_passes = models.BigIntegerField(blank=True, null=True)
    passes_in_final_third = models.BigIntegerField(blank=True, null=True)
    passes_into_penalty_area = models.BigIntegerField(blank=True, null=True)
    crosses_into_penalty_area = models.BigIntegerField(blank=True, null=True)
    progressive_passes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passing_data'


class PossessionData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.FloatField(blank=True, null=True)
    touches = models.BigIntegerField(blank=True, null=True)
    touches_in_def_penalty_area = models.BigIntegerField(blank=True, null=True)
    touches_in_def_3rd = models.BigIntegerField(blank=True, null=True)
    touches_in_mid_3rd = models.BigIntegerField(blank=True, null=True)
    touches_in_att_3rd = models.BigIntegerField(blank=True, null=True)
    touches_in_att_penalty_area = models.BigIntegerField(blank=True, null=True)
    live_ball_touches = models.BigIntegerField(blank=True, null=True)
    take_ons_attempted = models.BigIntegerField(blank=True, null=True)
    take_ons_succeeded = models.BigIntegerField(blank=True, null=True)
    take_ons_success_perc = models.FloatField(blank=True, null=True)
    tackled_during_take_on = models.BigIntegerField(blank=True, null=True)
    perc_time_tackled_during_take_on = models.FloatField(blank=True, null=True)
    carries = models.BigIntegerField(blank=True, null=True)
    total_carry_dist = models.BigIntegerField(blank=True, null=True)
    progressive_dist = models.BigIntegerField(blank=True, null=True)
    progressive_carries = models.BigIntegerField(blank=True, null=True)
    carries_in_final_3rd = models.BigIntegerField(blank=True, null=True)
    carries_in_penalty_area = models.BigIntegerField(blank=True, null=True)
    miscontrols = models.BigIntegerField(blank=True, null=True)
    dispossessed = models.BigIntegerField(blank=True, null=True)
    passess_received = models.BigIntegerField(blank=True, null=True)
    progressive_passess_received = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'possession_data'


class PremierLeagueAttackers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxg_xag = models.FloatField(db_column='npxG+xAG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'premier_league_attackers'


class PremierLeagueDefenders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_defenders'


class PremierLeagueGoalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.BigIntegerField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.FloatField(db_column='SavePerc', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.BigIntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.BigIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.FloatField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.BigIntegerField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.BigIntegerField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.
    savepercpenalty = models.FloatField(db_column='SavepercPenalty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_goalie'


class PremierLeagueGoalieAdv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    fk = models.BigIntegerField(db_column='FK', blank=True, null=True)  # Field name made lowercase.
    ck = models.BigIntegerField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    og = models.BigIntegerField(db_column='OG', blank=True, null=True)  # Field name made lowercase.
    psxg = models.FloatField(db_column='PSxg', blank=True, null=True)  # Field name made lowercase.
    psxgvssot = models.FloatField(db_column='PSxgvsSot', blank=True, null=True)  # Field name made lowercase.
    psxgminusga = models.FloatField(db_column='PSxgminusGA', blank=True, null=True)  # Field name made lowercase.
    psxgminusgaper90 = models.FloatField(db_column='PSxgminusGAper90', blank=True, null=True)  # Field name made lowercase.
    lcmp = models.BigIntegerField(db_column='LCMp', blank=True, null=True)  # Field name made lowercase.
    latt = models.BigIntegerField(db_column='LAtt', blank=True, null=True)  # Field name made lowercase.
    lcmpperc = models.FloatField(db_column='LCmpperc', blank=True, null=True)  # Field name made lowercase.
    patt = models.BigIntegerField(db_column='PAtt', blank=True, null=True)  # Field name made lowercase.
    pthr = models.BigIntegerField(db_column='PThr', blank=True, null=True)  # Field name made lowercase.
    plaunedperc = models.FloatField(db_column='PLaunedperc', blank=True, null=True)  # Field name made lowercase.
    pavglen = models.FloatField(db_column='PAvgLen', blank=True, null=True)  # Field name made lowercase.
    gkatt = models.BigIntegerField(db_column='GKAtt', blank=True, null=True)  # Field name made lowercase.
    gklaunchperc = models.FloatField(db_column='GKLaunchPerc', blank=True, null=True)  # Field name made lowercase.
    gkavglen = models.FloatField(db_column='GKAvgLen', blank=True, null=True)  # Field name made lowercase.
    crossessfaced = models.BigIntegerField(db_column='CrossessFaced', blank=True, null=True)  # Field name made lowercase.
    crossedstopped = models.BigIntegerField(db_column='CrossedStopped', blank=True, null=True)  # Field name made lowercase.
    stopprecentage = models.FloatField(db_column='StopPrecentage', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalbox = models.BigIntegerField(db_column='DefActOutPenalBox', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalboxper90 = models.FloatField(db_column='DefActOutPenalBoxPer90', blank=True, null=True)  # Field name made lowercase.
    averagedistfrompenalbox = models.FloatField(db_column='AverageDistfromPenalBox', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_goalie_adv'


class PremierLeagueTeamAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    poss = models.TextField(db_column='Poss', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.TextField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.TextField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.TextField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.TextField(blank=True, null=True)
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.TextField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.TextField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.TextField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.TextField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.TextField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.TextField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.TextField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    gaminuspk = models.TextField(db_column='GAminusPK', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.TextField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.TextField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.TextField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.TextField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.TextField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_team_attack'


class PremierLeagueTeamDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.TextField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.TextField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.TextField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.TextField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.TextField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    att = models.TextField(db_column='Att', blank=True, null=True)  # Field name made lowercase.
    tklperc = models.TextField(db_column='Tklperc', blank=True, null=True)  # Field name made lowercase.
    lost = models.TextField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.TextField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    sh = models.TextField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.TextField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    tklint = models.TextField(db_column='TklInt', blank=True, null=True)  # Field name made lowercase.
    clr = models.TextField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.TextField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_team_defense'


class PremierLeagueTeamKeeper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.TextField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.TextField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.TextField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.TextField(db_column='Saveperc', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.TextField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.TextField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.TextField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.TextField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premier_league_team_keeper'


class SerieAAttackers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.BigIntegerField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.BigIntegerField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.BigIntegerField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.BigIntegerField(blank=True, null=True)
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.BigIntegerField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.BigIntegerField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.BigIntegerField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.BigIntegerField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    prgr = models.BigIntegerField(db_column='PrgR', blank=True, null=True)  # Field name made lowercase.
    glsp90 = models.FloatField(db_column='Glsp90', blank=True, null=True)  # Field name made lowercase.
    astp90 = models.FloatField(db_column='Astp90', blank=True, null=True)  # Field name made lowercase.
    gap90 = models.FloatField(db_column='GAp90', blank=True, null=True)  # Field name made lowercase.
    gminuspkp90 = models.FloatField(db_column='GminusPKp90', blank=True, null=True)  # Field name made lowercase.
    gaminuspkp90 = models.FloatField(db_column='GAminusPKp90', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.FloatField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.FloatField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.FloatField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.FloatField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.FloatField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxg_xag = models.FloatField(db_column='npxG+xAG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'serie_a_attackers'


class SerieADefenders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.BigIntegerField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.BigIntegerField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.BigIntegerField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.BigIntegerField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.BigIntegerField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    tkl_drib = models.BigIntegerField(db_column='Tkl_Drib', blank=True, null=True)  # Field name made lowercase.
    att_drib = models.BigIntegerField(db_column='Att_Drib', blank=True, null=True)  # Field name made lowercase.
    tkl_per = models.FloatField(db_column='Tkl_Per', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.BigIntegerField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    shot = models.BigIntegerField(blank=True, null=True)
    pass_field = models.BigIntegerField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.BigIntegerField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    intplustkl = models.BigIntegerField(db_column='IntplusTkl', blank=True, null=True)  # Field name made lowercase.
    clr = models.BigIntegerField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.BigIntegerField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_defenders'


class SerieAGoalie(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    mp = models.BigIntegerField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.BigIntegerField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.BigIntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.FloatField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.BigIntegerField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.BigIntegerField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.FloatField(db_column='SavePerc', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.BigIntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.BigIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.FloatField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.BigIntegerField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.BigIntegerField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.BigIntegerField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.
    savepercpenalty = models.FloatField(db_column='SavepercPenalty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_goalie'


class SerieAGoalieAdv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rk = models.BigIntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    nation = models.TextField(db_column='Nation', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    born = models.BigIntegerField(db_column='Born', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.FloatField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.BigIntegerField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    pka = models.BigIntegerField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    fk = models.BigIntegerField(db_column='FK', blank=True, null=True)  # Field name made lowercase.
    ck = models.BigIntegerField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    og = models.BigIntegerField(db_column='OG', blank=True, null=True)  # Field name made lowercase.
    psxg = models.FloatField(db_column='PSxg', blank=True, null=True)  # Field name made lowercase.
    psxgvssot = models.FloatField(db_column='PSxgvsSot', blank=True, null=True)  # Field name made lowercase.
    psxgminusga = models.FloatField(db_column='PSxgminusGA', blank=True, null=True)  # Field name made lowercase.
    psxgminusgaper90 = models.FloatField(db_column='PSxgminusGAper90', blank=True, null=True)  # Field name made lowercase.
    lcmp = models.BigIntegerField(db_column='LCMp', blank=True, null=True)  # Field name made lowercase.
    latt = models.BigIntegerField(db_column='LAtt', blank=True, null=True)  # Field name made lowercase.
    lcmpperc = models.FloatField(db_column='LCmpperc', blank=True, null=True)  # Field name made lowercase.
    patt = models.BigIntegerField(db_column='PAtt', blank=True, null=True)  # Field name made lowercase.
    pthr = models.BigIntegerField(db_column='PThr', blank=True, null=True)  # Field name made lowercase.
    plaunedperc = models.FloatField(db_column='PLaunedperc', blank=True, null=True)  # Field name made lowercase.
    pavglen = models.FloatField(db_column='PAvgLen', blank=True, null=True)  # Field name made lowercase.
    gkatt = models.BigIntegerField(db_column='GKAtt', blank=True, null=True)  # Field name made lowercase.
    gklaunchperc = models.FloatField(db_column='GKLaunchPerc', blank=True, null=True)  # Field name made lowercase.
    gkavglen = models.FloatField(db_column='GKAvgLen', blank=True, null=True)  # Field name made lowercase.
    crossessfaced = models.BigIntegerField(db_column='CrossessFaced', blank=True, null=True)  # Field name made lowercase.
    crossedstopped = models.BigIntegerField(db_column='CrossedStopped', blank=True, null=True)  # Field name made lowercase.
    stopprecentage = models.FloatField(db_column='StopPrecentage', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalbox = models.BigIntegerField(db_column='DefActOutPenalBox', blank=True, null=True)  # Field name made lowercase.
    defactoutpenalboxper90 = models.FloatField(db_column='DefActOutPenalBoxPer90', blank=True, null=True)  # Field name made lowercase.
    averagedistfrompenalbox = models.FloatField(db_column='AverageDistfromPenalBox', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_goalie_adv'


class SerieATeamAttack(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    poss = models.TextField(db_column='Poss', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    gls = models.TextField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.TextField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    gminuspk = models.TextField(db_column='GminusPK', blank=True, null=True)  # Field name made lowercase.
    penaltykick = models.TextField(blank=True, null=True)
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    crdy = models.TextField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.TextField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    xg = models.TextField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.TextField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.TextField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    npxgxag = models.TextField(db_column='npxGxAG', blank=True, null=True)  # Field name made lowercase.
    prgc = models.TextField(db_column='PrgC', blank=True, null=True)  # Field name made lowercase.
    prgp = models.TextField(db_column='PrgP', blank=True, null=True)  # Field name made lowercase.
    gaminuspk = models.TextField(db_column='GAminusPK', blank=True, null=True)  # Field name made lowercase.
    xgp90 = models.TextField(db_column='xGp90', blank=True, null=True)  # Field name made lowercase.
    xagp90 = models.TextField(db_column='xAGp90', blank=True, null=True)  # Field name made lowercase.
    xgxagp90 = models.TextField(db_column='xGxAGp90', blank=True, null=True)  # Field name made lowercase.
    npxgp90 = models.TextField(db_column='npxGp90', blank=True, null=True)  # Field name made lowercase.
    npxgxagp90 = models.TextField(db_column='npxGxAGp90', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_team_attack'


class SerieATeamDefense(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tkl = models.TextField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    tklw = models.TextField(db_column='TklW', blank=True, null=True)  # Field name made lowercase.
    def_3rd = models.TextField(db_column='Def_3rd', blank=True, null=True)  # Field name made lowercase.
    mid_3rd = models.TextField(db_column='Mid_3rd', blank=True, null=True)  # Field name made lowercase.
    att_3rd = models.TextField(db_column='Att_3rd', blank=True, null=True)  # Field name made lowercase.
    att = models.TextField(db_column='Att', blank=True, null=True)  # Field name made lowercase.
    tklperc = models.TextField(db_column='Tklperc', blank=True, null=True)  # Field name made lowercase.
    lost = models.TextField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    blocks = models.TextField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    sh = models.TextField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='Pass', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    int = models.TextField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    tklint = models.TextField(db_column='TklInt', blank=True, null=True)  # Field name made lowercase.
    clr = models.TextField(db_column='Clr', blank=True, null=True)  # Field name made lowercase.
    err = models.TextField(db_column='Err', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_team_defense'


class SerieATeamKeeper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    squad = models.TextField(db_column='Squad', blank=True, null=True)  # Field name made lowercase.
    pl = models.TextField(db_column='Pl', blank=True, null=True)  # Field name made lowercase.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    starts = models.TextField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    number_90s = models.TextField(db_column='90s', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ga = models.TextField(db_column='GA', blank=True, null=True)  # Field name made lowercase.
    ga90 = models.TextField(db_column='GA90', blank=True, null=True)  # Field name made lowercase.
    sota = models.TextField(db_column='SoTA', blank=True, null=True)  # Field name made lowercase.
    saves = models.TextField(db_column='Saves', blank=True, null=True)  # Field name made lowercase.
    saveperc = models.TextField(db_column='Saveperc', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    csperc = models.TextField(db_column='CSperc', blank=True, null=True)  # Field name made lowercase.
    pkatt = models.TextField(db_column='PKatt', blank=True, null=True)  # Field name made lowercase.
    pka = models.TextField(db_column='PKA', blank=True, null=True)  # Field name made lowercase.
    pksv = models.TextField(db_column='PKsv', blank=True, null=True)  # Field name made lowercase.
    pkm = models.TextField(db_column='PKm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_a_team_keeper'


class ShootingData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    squad = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    born = models.BigIntegerField(blank=True, null=True)
    ninety_minutes = models.TextField(blank=True, null=True)
    gls = models.BigIntegerField(blank=True, null=True)
    total_shot = models.BigIntegerField(blank=True, null=True)
    total_shot_on_target = models.BigIntegerField(blank=True, null=True)
    shot_on_target_perc = models.TextField(blank=True, null=True)
    shot_on_target_per90 = models.TextField(blank=True, null=True)
    goal_per_shot = models.TextField(blank=True, null=True)
    goal_per_shot_on_target = models.TextField(blank=True, null=True)
    avg_shot_distance = models.TextField(blank=True, null=True)
    shots_from_free_kick = models.BigIntegerField(blank=True, null=True)
    penalty_kick = models.BigIntegerField(blank=True, null=True)
    penalty_kick_attempted = models.BigIntegerField(blank=True, null=True)
    xg = models.TextField(blank=True, null=True)
    npxg = models.TextField(blank=True, null=True)
    npxgpershot = models.TextField(blank=True, null=True)
    goalminusxg = models.TextField(blank=True, null=True)
    npgoalminusxg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shooting_data'
