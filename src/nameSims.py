import Levenshtein
import jellyfish

print(Levenshtein.distance('Mike Hawk','Mike'))

def levenshteinSim(word1,word2):
    biggestLen = len(word1) if len(word1) >= len(word2) else len(word2)

    return 1 - (Levenshtein.distance(word1,word2)/biggestLen)

def phoneticSym(word1,word2, phoneticTranscriber):
    return levenshteinSim(phoneticTranscriber(word1),phoneticTranscriber(word2))

def soundexSim(word1,word2):
    return phoneticSym(word1,word2,jellyfish.soundex)


def metaphoneSim(word1,word2):
    return phoneticSym(word1,word2,jellyfish.metaphone)

def mrcSim(word1,word2):
    return phoneticSym(word1,word2, jellyfish.jellyfish.match_rating_codex)

def nysiisSym(word1,word2):
    return phoneticSym(word1,word2, jellyfish.nysiis)

def closestName(inputName,nameSet, similarityFunc):
    if len(nameSet) == 0 : return "There are no names available :("
    bestScore = 0
    bestWord = "Not found"
    for name in nameSet:
        sim = similarityFunc(inputName, name)
        if sim > bestScore:
            bestScore = sim
            bestWord = name
    return bestWord

