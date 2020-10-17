# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:58:46 2020

@author: logos
"""

"""
Prject 4: computing alignments of sequences
"""


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
    print(alphabet
    chars = alphabet.add("-")
    print chars
    matrix = {}
    for char_1 in chars:
        matrix[char_1] = {}
        for char_2 in chars:
            if char_1 == "-" or char_2 == "-":
                matrix[char_1][cahr_2] = dash_score
            elif char_1 == char_2:
                matrix[char_1][cahr_2] = diag_score
            else:
                matrix[char_1][cahr_2] = off_diag_score
    return matrix
    
alphabet = set(["A", "C", "G", "T"])
diag_score = 10
off_diag_score = 4 
dash_score = -6
scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
for key, value in scoring_matrix.items():
    print key, str(value)


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
    pass



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
    pass



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
    pass








