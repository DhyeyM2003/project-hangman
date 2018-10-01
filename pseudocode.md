# Hangman (Pseudocode)

```
Generate a word

loop while word not done and player not dead:
  Display letters in the word as underscore 
  Display the platform
  Ask player for a letter
  Check if the letter is found in the word
    If the letter is in the word, display the letter
      Add letter to string of correct guesses
    If the letter is not in the word, display a (new) part of the body and the letter in a separate list
      Add letter to string of incorrect guesses

if lettes all guessed:
  player wins
else:
  they lose

```
