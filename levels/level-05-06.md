# Level 5 -> Level 6

**Goal**
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable 

**Commands Used**
* `cd`
* `ls -la`
* `find`
* `cat`

**Thought Process**
1. Navigated to the `inhere` directory.
2. Used ls -la to check the files and directories inside the inhere directory.
3. Found the files that are exactly 1033 bytes in size using `find . -type f -size 1033c` among the all files under inhere directory.
4. Extracted the password using the `cat` command on the identified text file.

**Key Concepts**

- `find`: Searches for files and directories.
- `-type f`: Matches regular files.
- `-size 1033c`: Matches files exactly 1033 bytes in size.
