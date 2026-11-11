# Level 4 -> Level 5

**Goal**
The password for the next level is stored in the only human-readable file in the inhere directory. 

**Commands Used**
* `cd`
* `ls -la`
* `file`
* `cat`

**Thought Process**
1. Navigated to the `inhere` directory.
2. Used `file ./*` to identify the file types, since the files contained different types of data.
3. Found the only human-readable file among the unknown data files.
4. Extracted the password using the `cat` command on the identified text file.
