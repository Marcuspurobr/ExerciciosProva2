def RSPLSp2(j1,j2):
    if j1==j2: 
        return 0 #empate
    if (j1=='R' and (j2=='L' or j2=='S')) or (j1=='L' and (j2=='Sp' or j2=='P')) or (j1=='Sp' and (j2=='R' or j2=='S')) or (j1=='S' and (j2=='P' or j2=='L')) or (j1=='P' and (j2=='R' or j2=='Sp')):
        return 1 #j1 ganha
    return 2 #j2 ganha
def RSPLSP3(j1,j2,j3):
    if RSPLSp2(j1,j2)==RSPLSp2(j2,j3)==RSPLSp2(j3,j1) or (RSPLSp2(j1,j2)==0 and RSPLSp2(j2,j3)==1) or (RSPLSp2(j2,j3)==0 and RSPLSp2(j2,j3)==1) or (RSPLSp2(j1,j3)==0 and RSPLSp2(j1,j2)==1): 
        return 0 #empate
    if RSPLSp2(j1,j2)==1 and RSPLSp2(j2,j3)==0:
        return 1 #j1 ganha
    if RSPLSp2(j2,j1)==1 and RSPLSp2(j1,j3)==0:
        return 2 #j2 ganha
    return 3 #j3 ganha
jogo1=RSPLSP3('P','S','P')
jogo2=RSPLSP3('S','L','Sp')
print(jogo1)
print(jogo2)