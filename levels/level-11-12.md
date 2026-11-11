# Level 11 -> Level 12

**Goal**
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

**Commands Used**
-  `tr`
-  `cat`

**Thought Process**
1. Identified that the text is encoded using the ROT13 cipher, which shifts letters by 13 positions.
2. Used the `tr` (translate) command to map and replace each letter with the letter 13 positions ahead/behind it in the alphabet.
3. Executed `cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'` to decode the text and reveal the original password.

**Key Concepts**
- `tr`: A command-line utility for translating or deleting characters.
