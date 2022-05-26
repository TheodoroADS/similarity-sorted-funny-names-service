import jellyfish
import Levenshtein


def levenshteinSim(word1,word2):
    biggestLen = len(word1) if len(word1) >= len(word2) else len(word2)

    return 1 - (Levenshtein.distance(word1,word2)/biggestLen)

def soundSim(word1,word2):
    return levenshteinSim(jellyfish.soundex(word1),jellyfish.soundex(word2))


print(jellyfish.soundex("Mehdi"))
print(jellyfish.soundex("Marius"))

print(Levenshtein.distance(jellyfish.soundex("dtgbnq"), jellyfish.soundex("dftreqw")))