# Spelling Checker

## Description

Spelling Correction is a Python program that takes an input text, corrects the spelling of words, and saves the corrected text to an output file. It uses a word frequency dictionary to suggest the best corrections for misspelled words.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Flow of code](#flowOfCode)

## Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/overlordiam/Spell-checker.git
   cd Spell-checker

## Usage

1. Place the text you want to correct in the `input.txt` file.
2. Run the Python program using the following command:

    ```bash
    python s_checker.py

## Features

- Corrects the spelling of words in the input text using a word frequency dictionary.
- Supports English words with hyphens and apostrophes.

## Flow of code

-	In the main program, the code starts by specifying the paths for the corpus file, input file, and output file.
-	The program builds the word frequency dictionary by calling the build_dictionary function and passing the corpus file path.
-	The input text is read from the input file and stored in the input_text variable.
-	The clean_text function is called to clean the input text and store the result in the cleaned_text variable.
-	The correct_spelling function is called to correct the spelling mistakes in the cleaned text. It also returns the error count and correction count.
-	The corrected text, error count, and correction count are printed to the console.
-	The save_corrected_text function is called to save the corrected text to the output file.
By following these steps, the code reads a corpus file to build a dictionary of words and frequencies. It then reads an input text, corrects the spelling mistakes using the dictionary, saves the corrected text to an output file, and provides a report on the number of errors detected and corrections made.
