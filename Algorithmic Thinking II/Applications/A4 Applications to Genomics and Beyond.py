# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:58:23 2020

@author: logos
"""

"""
Provide code and solution for Application 4
"""

import math
import random
import urllib
import matplotlib.pyplot as plt
import alg_seq_alignment as aln
import time


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib.request.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeys = ykeys.decode("utf-8")
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        line = line.decode("utf-8")
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict

# =============================================================================
# scoring_matrix = read_scoring_matrix(PAM50_URL)
# for key, value in scoring_matrix.items():
#     print(key, str(value))
# =============================================================================


def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib.request.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.decode("utf-8")
    protein_seq = protein_seq.rstrip()
    return protein_seq

# =============================================================================
# print(read_protein(HUMAN_EYELESS_URL))
# =============================================================================

def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib.request.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    words = words.decode("utf-8")
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print("Loaded a dictionary with", len(word_list), "words")
    return word_list

# =============================================================================
# print(read_words(WORD_LIST_URL))
# =============================================================================

def compare_seqs(seq_x, seq_y):
    """
    Return the percentage of agreeing characters in two sequences
    """
    assert len(seq_x) == len(seq_y)
    length = len(seq_x)
    count = 0
    for i in range(length):
        if seq_x[i] == seq_y[i]:
            count += 1
    return length, count / length

#%% question 1

def question_1():
    """
    run question 1
    """
    human_seq = read_protein(HUMAN_EYELESS_URL)
    fly_seq = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    global_flag = False
    alignment_matrix = aln.compute_alignment_matrix(human_seq, fly_seq, scoring_matrix, global_flag)
    local_alignment = aln.compute_local_alignment(human_seq, fly_seq, scoring_matrix, alignment_matrix)
    print("Comparing human and fly")
    print(local_alignment)
    print(compare_seqs(local_alignment[1], local_alignment[2]))

# =============================================================================
# question_1()
# =============================================================================

#%% question 2

LOCAL_HUMAN = 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ'
LOCAL_FLY = 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ'


def question_2():
    """
    run question 2
    """
    local_human = LOCAL_HUMAN.replace("-", "")
    print("Local human:\n", local_human)
    local_fly = LOCAL_FLY.replace("-", "")
    print("\nLocal fly:\n", local_fly)
    pax = read_protein(CONSENSUS_PAX_URL)
    print("\nPAX domain:\n", pax)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    global_flag = True
    alignment_human = aln.compute_alignment_matrix(local_human, pax, scoring_matrix, global_flag)
    alignment_fly = aln.compute_alignment_matrix(local_fly, pax, scoring_matrix, global_flag)
    human_pax = aln.compute_global_alignment(local_human, pax, scoring_matrix, alignment_human)
    print("\nComparing huamn and PAX")
    print(human_pax)
    print(compare_seqs(human_pax[1], human_pax[2]))
    fly_pax = aln.compute_global_alignment(local_fly, pax, scoring_matrix, alignment_fly)
    print("\nComparing fly and PAX")    
    print(fly_pax)
    print(compare_seqs(fly_pax[1], fly_pax[2]))    
    
    
# =============================================================================
# question_2()
# =============================================================================


#%% question 3

# =============================================================================
# print((math.factorial(133)) / (math.factorial(93)*math.factorial(40)*(23**133)))
# =============================================================================


#%% question 4

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    return a dictinary, the key is the score of each trial, 
    the value is the number of trials of that score
    """
    distribution = {}
    for i in range(num_trials):
        copy_y = list(seq_y)        
        random.shuffle(copy_y)
        rand_y = "".join(copy_y)
        global_flag = False
        align = aln.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, global_flag)

        score = -float("inf")        
        len_x = len(seq_x)
        len_y = len(seq_y)

        for temp_i in range(len_x+1):
            for temp_j in range(len_y+1):
                if align[temp_i][temp_j] > score:

                    score = align[temp_i][temp_j]

        if score in distribution:
            distribution[score] += 1
        else:
            distribution[score] = 1
    return distribution

def question_4():
    """
    run question 4
    """
    human_seq = read_protein(HUMAN_EYELESS_URL)
    fly_seq = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    num_trials = 1000
    distribution = generate_null_distribution(human_seq, fly_seq, scoring_matrix, num_trials)
    print(distribution)
    x, y = [], []
    for score, num in distribution.items():
        x.append(score)
        y.append(num/num_trials)
    plt.figure("question 4")
    plt.clf()
    plt.bar(x, y)
    plt.title("Alignment score distribution")
    plt.xlabel("Score of optimal local alignment")
    plt.ylabel("Fraction of total trials")
    plt.tight_layout()
    plt.show()
    
    
# =============================================================================
# question_4() 
# =============================================================================


#%% question 5

DIST = {47: 62, 49: 81, 59: 24, 53: 59, 45: 61, 60: 22, 65: 9, 52: 60, 54: 39, 39: 1, 51: 63, 56: 41, 46: 62, 42: 26, 48: 59, 73: 2, 62: 11, 58: 28, 41: 13, 64: 10, 70: 2, 55: 35, 43: 25, 40: 4, 44: 42, 50: 61, 61: 21, 63: 13, 67: 4, 57: 34, 66: 5, 71: 2, 76: 2, 85: 1, 75: 3, 80: 1, 77: 1, 69: 5, 68: 3, 84: 1, 78: 1, 79: 1}
    
def question_5():
    """
    run question 5
    """
    num_trials = 0
    sum_score = 0
    for score, num in DIST.items():
        num_trials += num
        sum_score += score * num
    mean_score = sum_score / num_trials
    
    sqr_sum = 0
    for score, num in DIST.items():
        sqr_sum += num * (score - mean_score)**2
    s_dev = math.sqrt(sqr_sum / num_trials)
    
    human_fly = 875
    z_score = (human_fly - mean_score) / s_dev
    
    print(mean_score, s_dev, z_score)
    
# =============================================================================
# question_5()
# =============================================================================


#%% question 8



def edit_distance(word_1, word_2, scoring_matrix):
    """
    return the edit distance between word_1 and word_2
    """
    global_flag = True
    alignment_matrix = aln.compute_alignment_matrix(word_1, word_2, scoring_matrix, global_flag)
    alignment = aln.compute_global_alignment(word_1, word_2, scoring_matrix, alignment_matrix)
    return len(word_1) + len(word_2) - alignment[0]

# =============================================================================
# print(edit_distance("ad", "abcf"))
# =============================================================================

def check_spelling(checked_word, dist, word_list, scoring_matrix):
    """
    return set of all words in word_list that are within the edit distance (dist)
    of the given checked_word 
    """
    ans = set()
    for word in word_list:
        if edit_distance(checked_word, word, scoring_matrix) <= dist:
            ans.add(word)
    return ans


def question_8():
    """
    run quesiton 8
    """
    alphabet = set("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
    diag_score = 2
    off_diag_score = 1
    dash_score = 0
    scoring_matrix = aln.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    
    word_list = set(read_words(WORD_LIST_URL))
    start = time.time()
    ans_1 = check_spelling("humble", 1, word_list, scoring_matrix)
    ans_2 = check_spelling("firefly", 2, word_list, scoring_matrix)
    stop = time.time()
    check_time = stop - start
    print("Word list 1 - humble:")
    print(ans_1)
    print("\nWord list 2 - firefly:")
    print(ans_2)
    print("\nChecking time is " + str(check_time))

# =============================================================================
# question_8()
# =============================================================================


#%% question 9

def edit_distance_2(word_1, word_2):
    """
    return the edit distance between word_1 and word_2
    """
    dist = 0
    words = [word_1, word_2]
    words.sort(key=lambda word: len(word))
    short, long = words[0], words[1]
    while short:
        char = short[0]
        idx = long.find(char)
        if idx != -1 and idx + len(short) <= len(long):
                dist += idx
                short = short[1:]
                long = long[idx+1:]
        else:
            dist += 1
            short = short[1:]
            long = long[1:]
    if long:
        dist += len(long)
    return dist


word_1, word_2 = "ab", "cba"
alphabet = set("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
diag_score = 2
off_diag_score = 1
dash_score = 0
scoring_matrix = aln.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
print(edit_distance(word_1, word_2, scoring_matrix))
print(edit_distance_2(word_1, word_2))

def check_spelling_2(checked_word, dist, word_list):
    """
    return set of all words in word_list that are within the edit distance (dist)
    of the given checked_word 
    """
    ans = set()
    for word in word_list:
        if edit_distance_2(checked_word, word) <= dist:
            ans.add(word)
    return ans


def question_9():
    """
    run quesiton 9
    """
# =============================================================================
#     alphabet = set("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
#     diag_score = 2
#     off_diag_score = 1
#     dash_score = 0
#     scoring_matrix = aln.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
# =============================================================================
    
    word_list = set(read_words(WORD_LIST_URL))
    start = time.time()
    ans_1 = check_spelling_2("humble", 1, word_list)
    ans_2 = check_spelling_2("firefly", 2, word_list)
    stop = time.time()
    check_time = stop - start
    print("Word list 1 - humble:")
    print(ans_1)
    print("\nWord list 2 - firefly:")
    print(ans_2)
    print("\nChecking time is " + str(check_time))

# =============================================================================
# print("Run question 8")
# question_8()
# 
# print("\nRun question 9")
# question_9()
# =============================================================================
