# Imports
from os import path
import argparse
import string
import jiwer

# Jaccard Similarity of two strings
def jaccard_similarity(doc1, doc2):
    intersection = set(doc1).intersection(set(doc2))
    union = set(doc1).union(set(doc2))
    return len(intersection)/len(union)

# Parsing
parser = argparse.ArgumentParser(description="Compare manual and T2S transcript")
parser.add_argument("t2s", type=str, help="T2S transcript")
parser.add_argument("hw", type=str, help="Handwritten transcript")
args = parser.parse_args()

# Path declaration
TRANSCRIPT_T2S_PATH = args.t2s
TRANSCRIPT_MANUAL = args.hw

# Translation table for removing punctuation
translation_table = str.maketrans("","",string.punctuation)

# Read file contents and remove punctuation
with open(TRANSCRIPT_T2S_PATH) as read_file:
    t2s_content = read_file.read()

t2s_content = t2s_content.translate(translation_table)

with open(TRANSCRIPT_MANUAL) as read_file:
    manual_content = read_file.read()

manual_content = manual_content.translate(translation_table)

# Compute Jaccard Similarity
print(f"Jaccard: {jaccard_similarity(TRANSCRIPT_T2S_PATH, TRANSCRIPT_MANUAL)}")
print(f"\nWER:     {jiwer.wer(manual_content, t2s_content)}")
