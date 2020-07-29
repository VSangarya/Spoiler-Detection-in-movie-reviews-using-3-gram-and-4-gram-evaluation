def copy(i):
    if (i == 1):
        with open('a4/a3.txt') as f:
            with open("a4/a1.txt", "w") as f1:
                for line in f:
                    f1.write(line)
    if (i == 2):
        with open('a4/a4.txt') as f:
            with open("a4/a1.txt", "w") as f1:
                for line in f:
                    f1.write(line)
    if (i == 3):
        with open('a4/a5.txt') as f:
            with open("a4/a1.txt", "w") as f1:
                for line in f:
                    f1.write(line)

def result(i, mp,mp1):
    if((i==1 or 2 or 3)):
      if(mp>0.1 and mp1>0.05):
          return('Review for movie contains spoilers')
      else:
          return('Review for movie doesnt contain spoilers')
    else:
       return('The reference synopsis for this movie hasnt been updated yet')

def resultshort(i, mp,mp1):
    if((i==1 or 2 or 3)):
      if(mp>0.1 and mp1>0.05):
          return('Review for movie is small, it may contains spoilers')
      else:
          return('Review for movie is small, it may not contain spoilers')
    else:
       return('The reference synopsis for this movie hasnt been updated yet')

