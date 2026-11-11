# Level 7 -> Level 8

**Goal**
The password for the next level is stored in the file data.txt next to the word millionth

**Commands Used**
*  `grep`

**Thought Process**
1. Used the `grep` command to find specific strings in a file
2. Used the `-Eoi` options to match the target keyword, display only the matching text, and ignore case differences.
3. Used the regular expression `"millionth\s+\S+"` to find the word `millionth` and the non-space characters immediately following it.
