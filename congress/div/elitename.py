import random, sys

digrams=  "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"

LONGISHPROB= .25 # shorter values give shorter names
ROMANPROB= .01   # for names like Lave IX
DOUBLEPROB= .02  # for names like Solela Onriat
SMALLPLANETPROB= .5
POPMEAN= 300000000
POPSTDEV= 70000000


RomanNumerals= [ "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
          "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVIII", "XIX"]


def makeonename():
    name = ""
    min= 3
    while (min>0 or random.random()<LONGISHPROB):
        r= 2*(random.randrange(len(digrams))/2)
        name+= digrams[r:r+2].rstrip(".")
        min-= 1
        
    return name.capitalize()




def makename():
    name= makeonename()
    if random.random() < ROMANPROB:
        name+= " " + random.choice(RomanNumerals)
    elif random.random() < DOUBLEPROB:
        name+= " "+makeonename()
    return name


i= 0
while i < int(sys.argv[1]):
    seen= {}
    name= makename()
    if len(name) <= 2 or name in seen: continue
    seen[name]= 1
    print makename()
    pop= random.gauss(POPMEAN, POPSTDEV)
    if pop<0: pop= -pop
    if random.random() < SMALLPLANETPROB: pop/= 10
    if random.random() < SMALLPLANETPROB: pop/= 10
    print int(pop)
    i+= 1
