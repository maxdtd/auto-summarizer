"""
    Produce EXTRACTIVE summarization of the source text.
    Selects top n sentences and concatenates them for summary.

    Summary method 1: https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65

"""
import nltk
import sys
import argparse

def create_word_freq_table(text):

    stopwords = set(nltk.corpus.stopwords.words("english"))
    words = nltk.tokenize.word_tokenize(text)
    porter_stemmer = nltk.stem.PorterStemmer()

    frequency_table = dict()
    for word in words:
        word = porter_stemmer.stem(word)
        if word in stopwords:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1
    return frequency_table

def calc_sentence_score(sentences, frequency_table):
    sentence_score = dict()
    
    for sentence in sentences:
        sentence_word_count = len(nltk.tokenize.word_tokenize(sentence))
        for value in frequency_table:
            if value in sentence.lower():
                if sentence[:10] in sentence_score:
                    sentence_score[sentence[:10]] += frequency_table[value] 
                else: 
                    sentence_score[sentence[:10]] = frequency_table[value]
        sentence_score[sentence[:10]] = sentence_score[sentence[:10]] // sentence_word_count

    return sentence_score

def calculate_avg_score(sentence_score):
    
    sum = 0
    for key in sentence_score:
        sum += sentence_score[key]  

    average = int(sum / len(sentence_score))

    return average

def summarize(sentences, sentence_score, threshold):
    sent_count = 0
    summary = ""

    for sentence in sentences:
        if sentence[:10] in sentence_score and sentence_score[sentence[:10]] > threshold:
            summary += " " + sentence
            sent_count += 1

    return summary

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Extractive summarization for .txt files")
    parser.add_argument("txt_file", type=str, help="text file for summarization")
    parser.add_argument("threshold", type=float, help="threshold for summary")
    args = parser.parse_args()

    IN_FILE = args.txt_file

    text = ""
    with open(IN_FILE,"r") as read_file:
        text = read_file.read()
    factor = args.threshold
    frequency_table = create_word_freq_table(text)
    sentences = nltk.tokenize.sent_tokenize(text)
    sentence_scores = calc_sentence_score(sentences, frequency_table)
    threshold = calculate_avg_score(sentence_scores)
    summary = summarize(sentences, sentence_scores, factor * threshold)

    print(summary)


                    