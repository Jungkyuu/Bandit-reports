# Level 2 -> Level 3

**Goal**
The password for the next level is stored in a file called --spaces in this filename-- located in the home directory.

**Commands Used**
* `ls -la`
* `cat`

**Thought Process**
1. Used `ls -la` to verify the exact name of the target file which contained spaces and started with hyphens.
2. Extracted the password by adding `./` and enclosing the file name in quotes to handle the spaces: `cat "./--spaces in this filename--"`.
