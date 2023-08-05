import re

def clean_text(text):
    """
    Clean the input text by removing non-alphabetical characters except hyphens and apostrophes,
    and convert the text to lowercase.
    """
    cleaned_text = re.sub(r'[^a-zA-Z\'\- ]', '', text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text

def build_dictionary(corpus_file):
    """
    Build a word frequency dictionary from the given corpus file.
    """
    word_freq = {}
    with open(corpus_file, 'r') as file:
        corpus = file.read()
        cleaned_corpus = clean_text(corpus)
        words = cleaned_corpus.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def deletion(word):
    """
    Generate all possible words by deleting one character from the given word.
    """
    return [word[:i] + word[i+1:] for i in range(len(word))]

def replacement(word):
    """
    Generate all possible words by replacing one character of the given word with each alphabet letter.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [word[:i] + c + word[i+1:] for i in range(len(word)) for c in alphabet]

def transposition(word):
    """
    Generate all possible words by transposing adjacent characters in the given word.
    """
    return [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word)-1)]

def insertion(word):
    """
    Generate all possible words by inserting each alphabet letter at every position in the given word.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [word[:i] + c + word[i:] for i in range(len(word)+1) for c in alphabet]

def find_best_suggestion(word, word_freq):
    """
    Find the best suggestion for the misspelled word from the generated suggestions.
    The best suggestion is the word with the highest frequency in the dictionary.
    """
    suggestions = deletion(word) + replacement(word) + transposition(word) + insertion(word)
    suggestions = [s for s in suggestions if s in word_freq]
    if suggestions:
        best_suggestion = max(suggestions, key=lambda x: (word_freq[x], x))
        return best_suggestion
    else:
        return None

def correct_spelling(text, word_freq):
    """
    Correct the spelling of the words in the input text using the word frequency dictionary.
    Return the corrected text, number of errors detected, and number of corrections made.
    """
    corrected_text = ''
    error_count = 0
    correction_count = 0
    words = text.split()
    for word in words:
        if word in word_freq:
            corrected_text += word + ' '
        else:
            best_suggestion = find_best_suggestion(word, word_freq)
            if best_suggestion:
                corrected_text += best_suggestion + ' '
                correction_count += 1
            else:
                corrected_text += word + ' '
            error_count += 1
    return corrected_text.strip(), error_count, correction_count

def save_corrected_text(text, output_file):
    """
    Save the corrected text to the output file.
    """
    with open(output_file, 'w') as file:
        file.write(text)

# Main program
corpus_file = 'corpus_b73bb2ea634cf11c51a00b669f12f95b.txt'
input_file = 'input.txt'
output_file = 'output.txt'

# Step 1: Build dictionary from the corpus file
word_freq = build_dictionary(corpus_file)

# Step 2: Read input text
with open(input_file, 'r') as file:
    input_text = file.read()

# Step 3: Clean input text
cleaned_text = clean_text(input_text)

# Step 4: Correct spelling and get error and correction counts
corrected_text, error_count, correction_count = correct_spelling(cleaned_text, word_freq)

# Step 5: Save corrected text to output file
save_corrected_text(corrected_text, output_file)

# Print report
print("Number of errors detected:", error_count)
print("Number of corrections made:", correction_count)
