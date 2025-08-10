
import unicodedata
import numpy as np

# Define alphabet (a-z + space)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '


def clean_text(text):
    """Remove accents, lowercase, keep only letters and space"""
    # Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Keep only alphabet chars
    return ''.join(c for c in text.lower() if c in ALPHABET)

def get_bigram_matrix(text):
    """Create 27x27 transition frequency matrix"""
    cleaned = clean_text(text)
    matrix = np.zeros((27, 27))
    
    # Count letter transitions
    for i in range(len(cleaned) - 1):
        idx1 = ALPHABET.index(cleaned[i])
        idx2 = ALPHABET.index(cleaned[i + 1])
        matrix[idx1, idx2] += 1
    
    # Normalize to probabilities
    for i in range(27):
        row_sum = matrix[i].sum()
        if row_sum > 0:
            matrix[i] = matrix[i] / row_sum
    
    return matrix

def get_profiles(data_train):
    profiles={}
    for key in data_train:
        profiles[key]=get_bigram_matrix(data_train[key])
    return profiles

def detect_language(text, profiles):
    """Compare input text to language matrices"""
    input_matrix = get_bigram_matrix(text)
    distances = {}
    
    # Calculate distances
    for i in profiles:
        distances[i]=np.sum(np.abs(input_matrix-profiles[i]))

    
    return min(distances,key=distances.get)