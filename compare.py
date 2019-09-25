# Imports
from os import path
import string

# Jaccard Similarity of two strings
def jaccard_similarity(doc1, doc2):
    intersection = set(doc1).intersection(set(doc2))
    union = set(doc1).union(set(doc2))
    return len(intersection)/len(union)

# Path declaration
TRANSCRIPT_T2S_PATH = ""
TRANSCRIPT_MANUAL = ""

# Read file contents and remove punctuation
with open(TRANSCRIPT_T2S_PATH) as read_file:
    t2s_content = read_file.read()

t2s_content = t2s_content.translate(None, string.punctuation)

with open(TRANSCRIPT_MANUAL) as read_file:
    manual_content = read_file.read()

manual_content = manual_content.translate(None, string.punctuation)

# Compute Jaccard Similarity
print(jaccard_similarity(TRANSCRIPT_T2S_PATH, TRANSCRIPT_MANUAL))

"""
TODO:
    - open both manual and api transcript
    - compare word lists 
    - give comparasion score for evaluation
    - USE JACCARD SIMILARITY, EXPLAIN WHY -> Measure accuracy "intersection over union"
"""