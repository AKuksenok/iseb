# зададим всевозможные символы, которые будут использоваться при генерации сообщений
lettersSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "intelligent information systems."

import random

# генерация начальной популяции
def generateParent(length: int) -> str:
    genesList = list()
    while len(genesList) < length:
        sampleSize = min(length - len(genesList), len(lettersSet))
        genesList.extend(random.sample(lettersSet, sampleSize))
    return "".join(genesList)


# подсчёт фитнес функции5
def fitness(guess) -> int:
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


# мутация новых особей
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(lettersSet, 2)
    if newGene == childGenes[index]:
        childGenes[index] = alternate
    else:
        childGenes[index] = newGene
    return "".join(childGenes)


import datetime

# вывод результатов
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    res = fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, res, str(timeDiff)))


random.seed()
startTime = datetime.datetime.now()
bestParent = generateParent(len(target))
bestFitness = fitness(bestParent)
display(bestParent)

# итерируемся до тех, пор пока не отыщем верное решение

while True:
    child = mutate(bestParent)
    childFitness = fitness(child)

    if childFitness <= bestFitness:
        continue
    display(child)
    if len(bestParent) <= childFitness:
        break
    bestFitness = childFitness
    bestParent = child
