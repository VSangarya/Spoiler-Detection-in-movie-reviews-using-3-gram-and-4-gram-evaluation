def copy(i):
        ai=i+2
        with open('a4/a'+str(ai)+'.txt') as f:
            with open("a4/a1.txt", "w") as f1:
                for line in f:
                    f1.write(line)

def result(i, mp,mp1):
    if(0<i<4)):
      if(mp>0.1 and mp1>0.05):
          return('Review for movie contains spoilers')
      else:
          return('Review for movie doesnt contain spoilers')
    else:
       return('The reference synopsis for this movie hasnt been updated yet')

def resultshort(i, mp,mp1):
    if(0<i<4):
      if(mp>0.1 and mp1>0.05):
          return('Review for movie is small, it may contains spoilers')
      else:
          return('Review for movie is small, it may not contain spoilers')
    else:
       return('The reference synopsis for this movie hasnt been updated yet')

