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
3. Found the only ASCII text file among the unknown data files.
4. Extracted the password using the `cat` command on the identified text file.
</details>