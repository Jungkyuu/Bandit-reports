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

<details>
<summary><b>Level 8 -> Level 9</b></summary>

**Goal**
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**Commands Used**
*  `sort`
*  `uniq`

**Thought Process**
1. Used the `sort` command to order based on alphabet
2. Pass the result of the left side using  `|` to right side and show the result after appling the command of right side
3. Extracted the password by reading the line using `uniq -u`

**Key Concepts**

- `sort`: Orders by alphabet
- `uniq -u`: show only the line that is not duplicated
</details>

<details>
<summary><b>Level 9 -> Level 10</b></summary>

**Goal**
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

**Commands Used**
*  `string`
*  `grep`

**Thought Process**
1. Used the `string` command to exctracted the strings that only human-readable
2. Pass the result of the left side using  `|` to right side and show the result after appling the command of right side
3. Extracted the strings that preceded by several '=' characters using grep

**Key Concepts**

- `string`: show the strings that only human-readable
</details>

<details>
<summary><b>Level 10 -> Level 11</b></summary>

**Goal**
The password for the next level is stored in the file data.txt, which contains base64 encoded data

**Commands Used**
*  `base64`
*  `--decode`

**Thought Process**
1. Identified that the content in `data.txt` is encoded in Base64 format.
2. Used the `base64` command with the `--decode` option to decode the text back into its original human-readable form.
3. Executed `base64 --decode data.txt` to reveal the password directly.

**Key Concepts**
- `base64`: A command used to encode or decode data using the Base64 encoding scheme.
- `--decode`: An option that tells the `base64` command to decode the data rather than encode it.
</details>

<details>
<summary><b>Level 11 -> Level 12</b></summary>

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
</details>


<details>
<summary><b>Level 12 -> Level 13</b></summary>

**Goal**
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

**Commands Used**
- `mktemp -d`, `cp`, `cd`, `mv`
- `xxd`
- `file`
- `gzip`, `bzip2`, `tar`

**Thought Process**
1. Created a temporary working directory in `/tmp` using `mktemp -d` and copied `data.txt` into it from the home directory.
2. Reversed the hexdump back into a binary file using `xxd -r data.txt > data.bin`.
3. Used the `file` command to determine the actual file type of the binary file.
4. Renamed the file with the appropriate extension (`.gz`, `.bz2`, or `.tar`) using the `mv` command so that the decompression tools could recognize it.
5. Decompressed the file using `gzip -d`, `bzip2 -d`, or `tar -xf` based on the file type.
6. Repeated the cycle of `file` -> `mv` -> `decompress` several times until the final uncompressed ASCII text file containing the password was revealed.

**Key Concepts**
- `mktemp -d`: Creates a secure, temporary directory.
- `xxd -r`: Reverses a hexdump, converting hexadecimal text back into binary data.
- `file`: Determines a file's type by examining its content (magic bytes), not just its extension.
- **Compression Tools**: Linux uses various compression formats. `.gz` is extracted with `gzip -d`, `.bz2` with `bzip2 -d`, and `.tar` (an archive) with `tar -xf`.
</details>

