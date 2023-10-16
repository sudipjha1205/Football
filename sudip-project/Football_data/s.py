s = '| index | Rk   | Player  | Nation | Pos  | Squad     | Age  | Born | 90s  | GA   | PKA  | FK   | CK   | OG   | PSxg | PSxgvsSot | PSxgminusGA | PSxgminusGAper90 | LCMp | LAtt | LCmpperc | PAtt | PThr | PLaunedperc | PAvgLen | GKAtt | GKLaunchPerc | GKAvgLen | CrossessFaced | CrossedStopped | StopPrecentage | DefActOutPenalBox | DefActOutPenalBoxPer90 | AverageDistfromPenalBox |'
l = (("".join(s.split("  "))).split("|"))
print("','".join(l))
