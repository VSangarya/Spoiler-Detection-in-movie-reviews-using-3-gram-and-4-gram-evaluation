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
    if(i==1):
      if(mp>0.1 and mp1>0.05):
          return('Review for movie 1 contains spoilers')
      else:
          return('Review for movie 1  doesnt contain spoilers')
    if (i == 2):
        if (mp>0.1 and mp1>0.05):
            return ('Review for movie 2 contains spoilers')
        else:
            return ('Review for movie 2 doesnt contain spoilers')
    if (i == 3):
        if (mp>0.1 and mp1>0.05):
            return ('Review for movie 3 contains spoilers')
        else:
            return ('Review for movie 3 doesnt contain spoilers')

def resultshort(i, mp,mp1):
    if(i==1):
      if((mp>0.05) and (mp1>0.01)):
          return('Review for movie 1 is small, it contains spoilers')
      else:
          return('Review for movie 1 is small, it may not contain spoilers')
    if (i == 2):
        if (mp>0.05 and mp1>0.01):
            return ('Review for movie 2 is small, it contains spoilers')
        else:
            return ('Review for movie 2 is small, it may not contain spoilers')
    if (i == 3):
        if (mp>0.05 and mp1>0.01):
            return ('Review for movie 3 is small, it contains spoilers')
        else:
            return ('Review for movie 3 is small, it may contain spoilers')


