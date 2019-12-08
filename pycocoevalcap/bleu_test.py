from bleu.bleu_scorer import BleuScorer

a = dict()
b = dict()

a["image_id"] = 1
a["id"] = 1
a["caption"] = "This is a test sentence that I'm using"

b["image_id"] = 1
b["id"] = 1
b["caption"] = "This is a reference sentence that is being referred to"

bleu_scor = BleuScorer(n=2)
bleu_scor += (a["caption"], b["caption"])
 
score, scores = bleu_scor.compute_score(option = 'closest',verbose = 1)
print("Score",score)
print("Scores",scores)

