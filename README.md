# OverTheWire: Bandit Write-up

My solutions and thought process for the Bandit wargame challenges.

<details>
<summary><b>Level 0 -> Level 1</b></summary>

**Goal**
The password for the next level is stored in a file called readme located in the home directory.

**Commands Used**
* `ls -la`
* `cat`

**Thought Process**
1. Checked the current directory with `ls -la` to locate the target file.
2. Read the file contents using `cat readme` to extract the password.
</details>

<details>
<summary><b>Level 1 -> Level 2</b></summary>

**Goal**
The password for the next level is stored in a file called - located in the home directory.

**Commands Used**
* `ls -la`
* `cat`

**Thought Process**
1. Found the file named `-` in the home directory.
2. Specified the current directory path (`./-`) to read it with `cat`, preventing the terminal from treating `-` as a command option flag.
</details>

<details>
<summary><b>Level 2 -> Level 3</b></summary>

**Goal**
The password for the next level is stored in a file called --spaces in this filename-- located in the home directory.

**Commands Used**
* `ls -la`
* `cat`

**Thought Process**
1. Used `ls -la` to verify the exact name of the target file which contained spaces and started with hyphens.
2. Extracted the password by adding `./` and enclosing the file name in quotes to handle the spaces: `cat "./--spaces in this filename--"`.
</details>

<details>
<summary><b>Level 3 -> Level 4</b></summary>

**Goal**
The password for the next level is stored in a hidden file in the inhere directory.

**Commands Used**
* `cd`
* `ls -la`
* `cat`

**Thought Process**
1. Navigated to the `inhere` directory using `cd`.
2. Used `ls -la` to reveal hidden files and discovered a file named `...Hiding-From-You`.
3. Read the text inside the hidden file with `cat ./...Hiding-From-You`.
</details>

<details>
<summary><b>Level 4 -> Level 5</b></summary>

**Goal**
The password for the next level is stored in the only human-readable file in the inhere directory. 

**Commands Used**
* `cd`
* `ls -la`
* `file`
* `cat`

**Thought Process**
1. Navigated to the `inhere` directory.
2. Used `file ./*` to identify the data types of all files, as they were mixed and visually indistinguishable.
3. Found the only human-readable file among the unknown data files.
4. Extracted the password using the `cat` command on the identified text file.
</details>

<details>
<summary><b>Level 5 -> Level 6</b></summary>

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
2. Used `ls -la` to identify how many files or directory there are in inhere directory.
3. Found the files that are exactly 1033 bytes in size using `find . -type f -size 1033c` among the all files under inhere directory.
4. Extracted the password using the `cat` command on the identified text file.

**Key Concepts**

- `find`: Searches for files and directories.
- `-type f`: Matches regular files.
- `-size 1033c`: Matches files exactly 1033 bytes in size.
</details>

<details>
<summary><b>Level 6 -> Level 7</b></summary>

**Goal**
The password for the next level is stored somewhere on the server and has all of the following properties:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

**Commands Used**
* `find`
* `cat`

**Thought Process**
1. Used the `find` command starting from the root directory (`/`) to search the entire server.
2. Applied specific options to match the properties: `-user bandit7` for the owner, `-group bandit6` for the group, and `-size 33c` for the exact 33-byte size.
3. Added `2>/dev/null` at the end of the command to hide "Permission denied" error messages.
4. Extracted the password by reading the found file path using the `cat` command.
</details>

<details>
<summary><b>Level 7 -> Level 8</b></summary>

**Goal**
The password for the next level is stored in the file data.txt next to the word millionth

**Commands Used**
*  `grep`

**Thought Process**
1. Used the `grep` command to find specific strings in a file
2. Applied specific options to match the properties: `-Eoi` for matching neiboring words, only matching that I target and catches all cases such as lowercase and uppercase.
3. Used the regular expression `"millionth\s+\S+"` to precisely extract the password. `millionth` targets the specific keyword, `\s+` matches one or more spaces, and `\S+` captures the subsequent consecutive non-space characters.
</details>




