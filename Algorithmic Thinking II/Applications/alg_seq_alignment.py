# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:00:24 2020

@author: logos
"""

"""
Prject 4: computing alignments of sequences
"""

#import random

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Input
        alphabet: a set of characters as strings
        diag_score: score for entries indexed by two same non_dash characters
        off_diag_score: score for entries indexed by two different non-dash characters
        dash_score: score for entries indexed by one or two dashes
    Output
        a scoring matrix: a dictionary of dictionaries, the keys of the main dict.
                          are characters in alphabet and dash (1st index), the keys
                          of the sub-dict. are also from alphabet and dash (2nd index),
                          the values of the sub-dict. are related scores
    """
    chars = set(alphabet)
    chars.add("-")
    matrix = {}
    for char_1 in chars:
        matrix[char_1] = {}
        for char_2 in chars:
            if char_1 == "-" or char_2 == "-":
                matrix[char_1][char_2] = dash_score
            elif char_1 == char_2:
                matrix[char_1][char_2] = diag_score
            else:
                matrix[char_1][char_2] = off_diag_score
    return matrix
    

#alphabet = set("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
#diag_score = 2
#off_diag_score = 1 
#dash_score = 0
#scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
#print "Scoring matrix"
#for key, value in scoring_matrix.items():
#    print key, str(value)

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Input
        seq_x: a string as 1st sequence
        seq_y: a string as 2nd sequence
        scoring_matrix: a dictionary of dictionaries giving scores of matching
        global_flag: a boolean value, if True, compute golbal alignment scores, if False,
                     compute compute local alignment scores (negative scores changed to 0)
    Output
        an alignment matrix: a list of lists, entry value of row i column j is the max
                             score over all possible alignments of sliced seq_x[:i] and
                             sliced seq_y[:j], value of [0][0] is 0
    """
    len_x = len(seq_x)
    len_y = len(seq_y)
    score = scoring_matrix
    matrix = [[None for dummy_col in range(len_y+1)] for dummy_row in range(len_x+1)]
    matrix[0][0] = 0
    if global_flag:
        for idx_i in range(1, len_x+1):
            matrix[idx_i][0] = matrix[idx_i-1][0] + score[seq_x[idx_i-1]]["-"]        
        for idx_j in range(1, len_y+1):
            matrix[0][idx_j] = matrix[0][idx_j-1] + score["-"][seq_y[idx_j-1]]
        for idx_i in range(1, len_x+1):
            for idx_j in range(1, len_y+1):
                matrix[idx_i][idx_j] = max(matrix[idx_i-1][idx_j-1] + score[seq_x[idx_i-1]][seq_y[idx_j-1]],
                                           matrix[idx_i-1][idx_j] + score[seq_x[idx_i-1]]["-"],
                                           matrix[idx_i][idx_j-1] + score["-"][seq_y[idx_j-1]])
    else:
        for idx_i in range(1, len_x+1):
            matrix[idx_i][0] = max(0, matrix[idx_i-1][0] + score[seq_x[idx_i-1]]["-"])        
        for idx_j in range(1, len_y+1):
            matrix[0][idx_j] = max(0, matrix[0][idx_j-1] + score["-"][seq_y[idx_j-1]])
        for idx_i in range(1, len_x+1):
            for idx_j in range(1, len_y+1):
                matrix[idx_i][idx_j] = max(matrix[idx_i-1][idx_j-1] + score[seq_x[idx_i-1]][seq_y[idx_j-1]],
                                           matrix[idx_i-1][idx_j] + score[seq_x[idx_i-1]]["-"],
                                           matrix[idx_i][idx_j-1] + score["-"][seq_y[idx_j-1]], 
                                           0)    
    return matrix

#print "\nAlignment of sequences"
#chars = list(alphabet)
#print "Characters:", chars
#len_x = 2
#seq_x = "".join([random.choice(chars) for _ in range(len_x)])
#seq_x = "firetruck"
#print "Seq_x:", seq_x
#len_y = 3
#seq_y = "".join([random.choice(chars) for _ in range(len_y)])
#seq_y = "freck"
#print "Seq_y:", seq_y


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Input
        seq_x: a string as 1st sequence
        seq_y: a string as 2nd sequence
        scoring_matrix: a dictionary of dictionaries giving scores of matching
        alignment_matrix: a list of lists, entry value of row i column j is the max
                          score over all possible alignments of sliced seq_x[:i] and
                          sliced seq_y[:j]
    Output
        a global alignment: a tuple (score, align_x, align_y), score is the global 
                            alignment score of aligned seq_x as align_x and aligned
                            seq_y as align_y of same length
    """
    idx_i = len(seq_x)
    idx_j = len(seq_y)
    score = scoring_matrix
    align = alignment_matrix
    align_x = ""
    align_y = ""
    
    align_score = alignment_matrix[idx_i][idx_j]
    
    while idx_i != 0 and idx_j != 0:
        if align[idx_i][idx_j] == align[idx_i-1][idx_j-1] + score[seq_x[idx_i-1]][seq_y[idx_j-1]]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_i -= 1
            idx_j -= 1
        elif align[idx_i][idx_j] == align[idx_i-1][idx_j] + score[seq_x[idx_i-1]]["-"]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = "-" + align_y
            idx_i -= 1
        elif align[idx_i][idx_j] == align[idx_i][idx_j-1] + score["-"][seq_y[idx_j-1]]:
            align_x = "-" + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_j -= 1
    
    align_x = seq_x[:idx_i] + "-" * idx_j + align_x 
    align_y = "-" * idx_i + seq_y[:idx_j] +  align_y
    
    return (align_score, align_x, align_y)

#global_flag = True
#if global_flag:
#    print "\n=================="
#    print "Global alignment of " + seq_x + " and " + seq_y
#    print "\nGlobal Alignment matrix"
#    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
#    for row in alignment_matrix:
#        print row
#    global_alignment = compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
#    print "\nGlobal alignment score: ", global_alignment[0]
#    print "Global aligned seq_x: ", global_alignment[1]
#    print "Global aligned seq_y: ", global_alignment[2]


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Input
        seq_x: a string as 1st sequence
        seq_y: a string as 2nd sequence
        scoring_matrix: a dictionary of dictionaries giving scores of matching
        alignment_matrix: a list of lists, entry value of row i column j is the max
                          score over all possible alignments of sliced seq_x[:i] and
                          sliced seq_y[:j]
    Output
        a local alignment: a tuple (score, align_x, align_y), score is the local 
                           alignment score of aligned seq_x as align_x and aligned
                           seq_y as align_y of same length
    """
    len_x = len(seq_x)
    len_y = len(seq_y)
    score = scoring_matrix
    align = alignment_matrix
    align_x = ""
    align_y = ""
    
    align_score = -float("inf")
    idx_i = -1
    idx_j = -1
    for temp_i in range(len_x+1):
        for temp_j in range(len_y+1):
            if align[temp_i][temp_j] > align_score:
                idx_i = temp_i
                idx_j = temp_j
                align_score = align[temp_i][temp_j]
    
    while idx_i != 0 and idx_j != 0:
        if align[idx_i][idx_j] == 0:
            break          
        if align[idx_i][idx_j] == align[idx_i-1][idx_j-1] + score[seq_x[idx_i-1]][seq_y[idx_j-1]]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_i -= 1
            idx_j -= 1
        elif align[idx_i][idx_j] == align[idx_i-1][idx_j] + score[seq_x[idx_i-1]]["-"]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = "-" + align_y
            idx_i -= 1
        elif align[idx_i][idx_j] == align[idx_i][idx_j-1] + score["-"][seq_y[idx_j-1]]:
            align_x = "-" + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_j -= 1

    return (align_score, align_x, align_y)


#global_flag = False
#if not global_flag:
#    print "\n=================="    
#    print "Local alignment of " + seq_x + " and " + seq_y
#    print "\nLocal Alignment matrix"
#    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
#    for row in alignment_matrix:
#        print row
#    local_alignment = compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
#    print "\nLocal alignment score: ", local_alignment[0]
#    print "Local aligned seq_x: ", local_alignment[1]
#    print "Local aligned seq_y: ", local_alignment[2]





