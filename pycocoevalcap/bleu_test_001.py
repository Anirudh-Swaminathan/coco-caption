#from bleu.bleu_scorer import BleuScorer
from bleu.bleu import Bleu
import re

a = dict()
b = dict()

test_cap = "This is a test caption"
ref_cap1 = "This is ref cap 1"
ref_cap2 = "Reference caption 2 right here"

a[1] = []

b[1] = []

#a[1].append(re.sub(r'[^a-zA-Z0-9 ]+', '', test_cap).lower().strip().split())
#b[1].append(re.sub(r'[^a-zA-Z0-9 ]+', '', ref_cap1).lower().strip().split())
#b[1].append(re.sub(r'[^a-zA-Z0-9 ]+', '', ref_cap2).lower().strip().split())
a[1].append(test_cap)
b[1].append(ref_cap1)
b[1].append(ref_cap2)

print(a)
print(b)
print("Printed a and b")

#bleu_scor = BleuScorer(n=4)
#bleu_scor += (a, b)

scorer = Bleu(4)

score, scores = scorer.compute_score(b, a)
print("Score: ")
print(score)
print("Scores: ")
print(scores)

method = ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]
print(method)
print("Loop Bois!")
for sc, scs, m in zip(score, scores, method):
    print(sc)
    print(scs)
    print(m)
    print("{}: {}".format(m, sc))
