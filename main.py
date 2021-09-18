from random import randint

def generateList(filename):
    lst = []
    clnlst = []
    with open(filename) as file:
        for line in file:
            lst.append(line)
    for elems in lst:

        clnlst.append(elems.strip())
    return clnlst



def main():

    adjectives = generateList("adjectives")
    names = generateList("Names")
    past_tense_verbs = generateList("pasttenseverbs")
    nouns = generateList("nouns")

    randpsttense = past_tense_verbs[randint(0,len(past_tense_verbs)-1)].split(" ")
    randpsttense = randpsttense[randint(0,len(randpsttense)-1)]


    print(

        adjectives[randint(0,len(adjectives)-1)],
        names[randint(0,len(names)-1)],
        randpsttense,
        nouns[randint(0,len(nouns)-1)]
    )
    

main()
