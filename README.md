# Spell-checker
The code begins by defining several functions that will be used throughout the program.
1.	The clean_text function takes a text input and removes all non-alphabetical characters except hyphens and apostrophes. It also converts the text to lowercase for consistency.
2.	The build_dictionary function reads the corpus file and builds a dictionary of words and their frequencies. It uses the clean_text function to clean the text before processing it. Each word encountered in the corpus is added to the dictionary with its frequency.
3.	The deletion, replacement, transposition, and insertion functions handle the four types of spelling mistakes described in the problem statement. They generate candidate words based on the given word by deleting, replacing, transposing, or inserting characters.
4.	The find_best_suggestion function takes a misspelled word and the word frequency dictionary. It generates candidate words using the four types of mistakes and selects the most likely suggestion from the dictionary. If multiple suggestions have the same frequency, it picks the one that occurs first in lexicographical order.
5.	The correct_spelling function takes the input text and the word frequency dictionary. It splits the text into individual words and checks each word for misspelling. If a word is in the dictionary, it is considered correct and added to the corrected text. If not, the function tries to find the best suggestion using the find_best_suggestion function. The corrected text, as well as the counts of errors and corrections, are returned.
6.	The save_corrected_text function takes the corrected text and saves it to the specified output file.

•	In the main program, the code starts by specifying the paths for the corpus file, input file, and output file.
•	The program builds the word frequency dictionary by calling the build_dictionary function and passing the corpus file path.
•	The input text is read from the input file and stored in the input_text variable.
•	The clean_text function is called to clean the input text and store the result in the cleaned_text variable.
•	The correct_spelling function is called to correct the spelling mistakes in the cleaned text. It also returns the error count and correction count.
•	The corrected text, error count, and correction count are printed to the console.
•	The save_corrected_text function is called to save the corrected text to the output file.
By following these steps, the code reads a corpus file to build a dictionary of words and frequencies. It then reads an input text, corrects the spelling mistakes using the dictionary, saves the corrected text to an output file, and provides a report on the number of errors detected and corrections made.
