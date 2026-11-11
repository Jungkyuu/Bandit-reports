# OverTheWire: Bandit Write-up


## About This Project

This repository documents my progress through the OverTheWire Bandit wargame, from Level 0 to Level 33.

Through these challenges, I practiced Linux command-line operations, file permissions, SSH, networking, shell scripting, cron jobs, and Git.

Each write-up includes the commands I used, my thought process, troubleshooting steps, and key concepts I learned.

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
2. Used `file ./*` to identify the file types, since the files contained different types of data.
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
2. Used ls -la to check the files and directories inside the inhere directory.
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
2. Used the `-Eoi` options to match the target keyword, display only the matching text, and ignore case differences.
3. Used the regular expression `"millionth\s+\S+"` to find the word `millionth` and the non-space characters immediately following it.
</details>

<details>
<summary><b>Level 8 -> Level 9</b></summary>

**Goal**
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**Commands Used**
*  `sort`
*  `uniq`

**Thought Process**
1. Used `sort` to arrange the lines in lexicographical order.
2. Used a pipe (`|`) to pass the sorted output to `uniq -u`.
3. Used `uniq -u` to display the line that appears only once.

**Key Concepts**

- `sort`: Sorts lines in lexicographical order.
- `uniq -u`: Displays lines that occur only once.
</details>

<details>
<summary><b>Level 9 -> Level 10</b></summary>

**Goal**
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

**Commands Used**
*  `strings`
*  `grep`

**Thought Process**
1. Used the `strings` command to extract readable text from the binary file.
2. Used a pipe (`|`) to pass the output to `grep`.
3. Used `grep` to find strings preceded by several `=` characters.

**Key Concepts**

- `strings`: Extracts readable text strings from binary files.
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

<details>
<summary><b>Level 13 -> Level 14</b></summary>

**Goal**
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.
If you need help with this level: a hint file can be found in the home directory.
Make sure to read the error messages as they are informative.

**Commands Used**
- `ls`, `cat`
- `exit`
- `scp`
- `chmod`
- `ssh -i`

### Thought Process

1. Used `ls` to check the files in the home directory and found `sshkey.private`.
2. Tried to connect to `bandit14` directly from the server using the private key:

   ```bash
   ssh -i sshkey.private bandit14@localhost -p 2220
   ```

   However, the connection was blocked because the server does not allow localhost connections for this challenge.

3. Exited the SSH session using `exit` to return to my local macOS terminal.
4. Downloaded the private key to my local machine using `scp`:

   ```bash
   scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private key14
   ```

   This was easier than manually copying the key because it preserved the original file.

5. Changed the file permissions so that only the owner could access the key:

   ```bash
   chmod 600 key14
   ```

6. Used the downloaded key to connect to `bandit14`:

   ```bash
   ssh -i key14 bandit14@bandit.labs.overthewire.org -p 2220
   ```

7. After logging in successfully, retrieved the password from the required file:

   ```bash
   cat /etc/bandit_pass/bandit14
   ```

### Key Concepts

- **SSH Key Authentication:** Used `ssh -i` to log in with a private key instead of a password.
- **SCP (Secure Copy):** Used `scp` to download the private key from the remote server to my local machine. The command needs to be run from the local terminal.
- **File Permissions:** Used `chmod 600` to restrict access to the private key. SSH may reject a private key if other users have permission to read it.
- **SSH Key Handling:** Learned that keeping the original key file intact helps avoid formatting issues when transferring or saving private keys.

### Troubleshooting & Lessons Learned

- **Invalid Format:** Initially tried copying and pasting the private key manually, but SSH returned an `invalid format` error. I switched to `scp` to download the original file instead.
- **Permission Denied:** Initially ran `scp` while still connected to the remote server. This caused the command to run from the wrong machine. After using `exit`, I ran it from my local terminal and the transfer worked.
- **Permission Issues:** Even after downloading the key correctly, SSH requires appropriate file permissions. Running `chmod 600 key14` resolved this issue.

### What I Learned

This level helped me understand how SSH private key authentication works and how to transfer files between a remote server and my local machine. I also learned the importance of file permissions and how to troubleshoot common SSH connection errors.
</details>

<details>
<summary><b>Level 14 -> Level 15</b></summary>

**Goal**
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

### Commands Used

- `cat`
- `nc` (Netcat)

### Thought Process

1. Retrieved the current level's password by reading the password file:

   ```bash
   cat /etc/bandit_pass/bandit14
   ```

2. Connected to port `30000` on the local machine using Netcat:

   ```bash
   nc localhost 30000
   ```

3. After connecting, the terminal did not display any message or prompt. I pasted the `bandit14` password into the terminal and pressed Enter.

4. The server checked the password and returned the password for Level 15.

### Key Concepts

- **Netcat (`nc`):** A command-line tool used to establish network connections and send or receive data. In this level, I used it to communicate with a service listening on TCP port `30000`.
- **Localhost:** Refers to the machine you are currently using. The address `127.0.0.1` can also be used to connect to the same machine.
- **Ports:** A port identifies a specific service running on a machine. In this challenge, port `30000` was used to communicate with the password-checking service.

### Troubleshooting & Lessons Learned

- **No Output After Connecting:** When I ran `nc localhost 30000`, the terminal appeared blank. At first, it was not obvious whether the connection had worked. However, Netcat was waiting for input, so I entered the password and pressed Enter.
- **Understanding Netcat:** I learned that Netcat does not always display a prompt or welcome message. Sometimes, I need to send data directly through the terminal after establishing a connection.

### What I Learned

This level helped me understand how to use Netcat to communicate with a service through a specific port. I also learned that a successful network connection does not always display a message, and that I can send input directly through the terminal.
</details>


<details>
<summary><b>Level 15 -> Level 16</b></summary>

**Goal**

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

**Commands Used**

- `cat`
- `openssl s_client`

**Thought Process**

1. Retrieved the current level's password by reading the password file:

   ```bash
   cat /etc/bandit_pass/bandit15
   ```

2. Connected to port `30001` on the local machine using OpenSSL with SSL/TLS encryption:

   ```bash
   openssl s_client -connect localhost:30001
   ```

3. After establishing the connection, the terminal displayed information about the SSL/TLS connection. I pasted the `bandit15` password into the terminal and pressed Enter.

4. The server checked the submitted password and returned the password for Level 16.

**Key Concepts**

- **OpenSSL (`s_client`):** A command-line tool used to establish SSL/TLS connections and communicate with secure services. In this level, I used it to connect to port `30001`.
- **SSL/TLS:** Protocols used to encrypt communication between a client and a server. They help protect data while it is being transmitted.
- **Localhost:** Refers to the machine you are currently using. The address `127.0.0.1` can also be used to connect to the same machine.
- **Ports:** A port identifies a specific service running on a machine. In this challenge, port `30001` was used for the password-checking service.

**Troubleshooting & Lessons Learned**

- **SSL/TLS Connection:** Unlike the previous level, using Netcat alone was not sufficient because the service required an encrypted connection.
- **Understanding OpenSSL:** I learned that `openssl s_client` can be used to connect to services that require SSL/TLS encryption.
- **Terminal Messages:** OpenSSL may display connection information or messages such as `DONE` or `RENEGOTIATING`. These messages do not necessarily mean the connection failed.

**What I Learned**

This level helped me understand the difference between a regular network connection and an encrypted SSL/TLS connection. I also learned how to use OpenSSL to communicate securely with a service running on a specific port.

</details>

<details>
<summary><b>Level 16 -> Level 17</b></summary>

### Goal

The credentials for the next level can be retrieved by submitting the current level's password to a port on localhost in the range 31000 to 32000.

I needed to identify the open ports, determine which services used SSL/TLS, and find the service that returned the credentials for the next level.

### Commands Used

- `cat`
- `nmap`
- `openssl s_client`
- `nano`
- `chmod`
- `scp`
- `ssh`

### Thought Process

1. First, I checked the current level's password:

   ```bash
   cat /etc/bandit_pass/bandit16
   ```

2. I used Nmap to scan ports `31000` to `32000` on localhost:

   ```bash
   nmap -sV -p 31000-32000 localhost
   ```

3. Nmap found five open ports:

   - `31046` - echo
   - `31518` - ssl/echo
   - `31691` - echo
   - `31790` - ssl/unknown
   - `31960` - echo

4. I identified that ports `31518` and `31790` supported SSL/TLS. However, port `31518` was an echo service, meaning it would simply return the data I sent.

5. I decided to test port `31790` because it used SSL/TLS and was identified as an unknown service:

   ```bash
   openssl s_client -connect localhost:31790
   ```

6. At first, I kept seeing messages such as `KEYUPDATE`. After checking the available options, I tried again with `-quiet`:

   ```bash
   openssl s_client -quiet -connect localhost:31790
   ```

7. I submitted the current Bandit 16 password. The server returned an SSH private key for Bandit 17.

8. I saved the private key in a file on the remote server:

   ```bash
   nano /tmp/bandit17.key
   ```

9. I changed the file permissions so that only the owner could read and write it:

   ```bash
   chmod 600 /tmp/bandit17.key
   ```

10. I tried to connect to Bandit 17 from inside the server, but the localhost SSH connection was blocked.

11. I exited the remote SSH session and returned to my Mac terminal. I then transferred the private key from the remote server to my local machine using SCP:

    ```bash
    scp -P 2220 bandit16@bandit.labs.overthewire.org:/tmp/bandit17.key ~/bandit17.key
    ```

12. On my Mac, I restricted the permissions of the downloaded key:

    ```bash
    chmod 600 ~/bandit17.key
    ```

13. Finally, I used the private key to connect to Bandit 17:

    ```bash
    ssh -i ~/bandit17.key bandit17@bandit.labs.overthewire.org -p 2220
    ```

### Key Concepts

- **Nmap:** Used to scan ports and identify the services running on them.
- **Port Scanning:** Helps identify which network ports are open and accepting connections.
- **SSL/TLS:** Provides encrypted communication between a client and a server.
- **OpenSSL (`s_client`):** Used to establish an SSL/TLS connection and interact with the service.
- **Echo Service:** Returns the data sent by the client instead of providing new credentials.
- **SSH Private Key:** Used for authentication when connecting to Bandit 17.
- **SCP (Secure Copy):** Used to transfer the private key from the remote server to my local Mac.
- **File Permissions:** Used `chmod 600` to restrict access to the private key.

### Troubleshooting & Lessons Learned

- **Identifying the Correct Port:** Not every open port provided the required credentials. I had to distinguish between regular echo services and the service that returned the SSH private key.
- **KEYUPDATE Messages:** I initially wasn't sure what the `KEYUPDATE` messages meant. Using the `-quiet` option made it easier to interact with the service.
- **Localhost Connection:** My attempt to connect to Bandit 17 from inside the server did not work because localhost SSH connections were blocked. I had to transfer the private key to my own computer and connect from there.
- **SSH Key Permissions:** I learned that SSH requires appropriate private key permissions. Using `chmod 600` prevents other users from reading the key.

### What I Learned

This level helped me practice port scanning with Nmap and identify services that use SSL/TLS.

I also learned how to use OpenSSL to interact with an encrypted service, how to transfer SSH private keys using SCP, and why proper file permissions are important for SSH authentication.

</details>


<details>
<summary><b>Level 17 -> Level 18</b></summary>

### Goal

The password for the next level is stored in one of two files: `passwords.old` and `passwords.new`.

The files are almost identical, but one line has been changed. I needed to find that line to get the next password.

### Commands Used
- `diff`

### Thought Process

1. I started by comparing the two files using `diff`.
2. I ran:

   ```bash
   diff passwords.new passwords.old
   ```

3. The command showed that line 42 was different between the two files.
4. I checked the output and identified the changed line in `passwords.new`.
5. That line contained the password for the next level.

### Key Concepts

- **diff:** Compares two files and displays their differences.
- **File comparison:** Helps identify changes between files without reading everything manually.
- **Output symbols:** `<` and `>` indicate which file each changed line belongs to.

### Troubleshooting & Lessons Learned

At first, I had to understand what the `diff` output meant.

The output showed `42c42`, which means line 42 in the first file differs from line 42 in the second file.

I also learned that the order of filenames matters when interpreting the output.

### What I Learned

I learned how to use `diff` to compare files and find a specific change.

This was a useful way to find information without manually checking every line.

</details>

<details>
<summary><b>Level 18 -> Level 19</b></summary>

### Goal

The password for the next level is stored in a file called `readme` in the home directory.

However, someone modified `.bashrc` to automatically log me out whenever I connect through SSH.

### Commands Used

- `ssh`
- `cat`

### Thought Process

1. I connected to Bandit 18 using SSH:

   ```bash
   ssh bandit18@bandit.labs.overthewire.org -p 2220
   ```

2. After entering the password, I saw the welcome message, but the connection immediately closed with:

   ```text
   Byebye!
   ```

3. I realized that the problem was not my password. The modified `.bashrc` was logging me out as soon as I logged in.

4. Instead of opening an interactive shell, I used SSH to execute a command directly on the remote server:

   ```bash
   ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
   ```

5. This command should display the contents of `readme` without starting an interactive shell.

### Key Concepts

- **SSH:** Allows me to connect to a remote server securely.
- **Remote command execution:** SSH can execute a command directly without opening an interactive shell.
- **.bashrc:** A configuration file that runs when Bash starts an interactive non-login shell in the usual configuration.

### Troubleshooting & Lessons Learned

My first attempt to connect through SSH failed because the session closed immediately.

Instead of repeatedly trying to log in, I changed my approach and passed the command directly to SSH.

### What I Learned

I learned that SSH is not only used to open a remote terminal. It can also execute commands directly on another machine.

This was especially useful when an interactive login was not possible.

</details>

<details>
<summary><b>Level 19 -> Level 20</b></summary>

### Goal

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary
`/etc/bandit_pass/bandit20`

### Commands Used

- `ls -l`
- `./bandit20-do`
- `whoami`
- `cat`

### Thought Process

1. I started by checking the files in the home directory.
2. I found a binary called `bandit20-do`.
3. I ran it without any arguments to see how it worked:

   ```bash
   ./bandit20-do
   ```

4. It displayed a message explaining that I could run a command as another user.

5. The example showed how to use the binary:

   ```bash
   ./bandit20-do whoami
   ```

6. I understood that I could use this binary to run commands with the permissions of another user.

7. I then used it to read the password file for Bandit 20:

   ```bash
   ./bandit20-do cat /etc/bandit_pass/bandit20
   ```

### Key Concepts

- **setuid:** A Linux permission feature that allows a program to run with the privileges of its file owner.
- **whoami:** Displays the username of the current process.
- **cat:** Reads and displays the contents of a file.
- **File permissions:** Control what users can do with files and executable programs.

### Troubleshooting & Lessons Learned

At first, I wasn't sure what the binary was supposed to do.

Running it without arguments helped me understand its usage. The message explained that I could pass a command to execute as another user.

### What I Learned

I learned how setuid works and how it can allow a program to run with the permissions of its owner.

I also learned that checking a program's usage before running it can make it easier to understand what it does.

</details>

<details>
<summary><b>Level 20 -> Level 21</b></summary>

### Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

### Commands Used

- `ls -l`
- `cat`
- `nc`
- `./suconnect`

### Thought Process

1. I started by checking the files in the home directory:

   ```bash
   ls -l
   ```

2. I found a binary called `suconnect`.

3. I checked the current level's password:

   ```bash
   cat /etc/bandit_pass/bandit20
   ```

4. Since the program connects to a port on localhost, I needed to create a local listener using Netcat.

5. I opened a terminal and started listening on port 1234:

   ```bash
   nc -l -p 1234
   ```

6. In another SSH session, I ran the setuid binary and specified the same port:

   ```bash
   ./suconnect 1234
   ```

7. I went back to the first terminal and entered the `bandit20` password.

8. The program checked the password and sent the next level's password through the connection.

### Key Concepts

- **Netcat (nc):** A tool used to create network connections and send or receive data.
- **localhost:** Refers to the current machine.
- **TCP port:** Identifies a communication endpoint used by applications.
- **setuid:** Allows a program to run with the privileges of its file owner.
- **TCP connection:** Allows two programs to exchange data over a network connection.

### Troubleshooting & Lessons Learned

The important part was keeping the Netcat listener running while executing `suconnect` from another terminal.

Both programs needed to use the same port number. If the port numbers did not match, they would not be able to communicate.

### What I Learned

I learned how to use Netcat to listen for incoming connections and how two programs can exchange data through a local TCP connection.

This level also helped me understand how setuid binaries can interact with network services.

</details>

<details>
<summary><b>Level 21 -> Level 22</b></summary>

### Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

### Commands Used

- `ls -la`
- `cat`
- `chmod`
- `ls -l`

### Thought Process

1. I started by checking the cron configuration directory:

   ```bash
   ls -la /etc/cron.d/
   ```

2. I found a configuration file called `cronjob_bandit22` and checked its contents:

   ```bash
   cat /etc/cron.d/cronjob_bandit22
   ```

3. The configuration showed that a shell script was being executed automatically.

4. I opened the script to see what it was doing:

   ```bash
   cat /usr/bin/cronjob_bandit22.sh
   ```

5. The script contained two important commands:

   ```bash
   chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

   cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```

6. I understood that the script was changing the file permissions and then copying the Bandit 22 password into a file under `/tmp/`.

7. I tried running the commands myself, but both attempts failed with permission errors.

8. This happened because I was logged in as `bandit21`, while the cron job was running with a different user's permissions.

9. After the cron job executed, I checked the output file:

   ```bash
   cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```

### Key Concepts

- **cron:** A time-based job scheduler that automatically runs commands at specified intervals.
- **/etc/cron.d/:** A directory containing system-wide cron job configurations.
- **chmod:** Changes file permissions.
- **cat:** Reads and displays file contents.
- **Redirection (`>`):** Sends command output into a file.
- **File Permissions:** Determine who can read, write, or execute a file.

### What I Learned

I learned how cron jobs can run commands automatically with different user permissions.

I also learned how to inspect cron configurations and understand why manually executing a script may produce permission errors.

</details>

<details>
<summary><b>Level 22 -> Level 23</b></summary>

### Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

### Commands Used

- `ls -la`
- `cat`
- `whoami`
- `echo`
- `md5sum`
- `cut`

### Thought Process

1. I started by checking the cron configuration directory:

   ```bash
   ls -la /etc/cron.d/
   ```

2. I found the configuration file for Bandit 23 and checked its contents:

   ```bash
   cat /etc/cron.d/cronjob_bandit23
   ```

3. The configuration showed that a shell script was running automatically.

4. I opened the script to understand what it was doing:

   ```bash
   cat /usr/bin/cronjob_bandit23.sh
   ```

5. I noticed that the script used `whoami` to get the username of the user running the script.

6. It then used `echo`, `md5sum`, and `cut` to generate a filename based on that username.

7. The important part was that the cron job runs as `bandit23`, not my current user, `bandit22`.

8. I used the same command with `bandit23` to calculate the filename:

   ```bash
   echo I am user bandit23 | md5sum | cut -d ' ' -f 1
   ```

9. The script uses that generated filename to store the password in `/tmp/`.

10. I could then use `cat` with the generated filename to read the password file.

### Key Concepts

- **cron:** A time-based scheduler that automatically runs commands.
- **whoami:** Displays the username of the current user.
- **md5sum:** Generates an MD5 hash from input data.
- **cut:** Extracts specific parts of text.
- **Command substitution (`$()`):** Runs a command and stores its output in a variable.
- **Pipes (`|`):** Pass the output of one command to another.
- **Redirection (`>`):** Writes command output into a file.

### Troubleshooting & Lessons Learned

One important detail was the difference between my current user and the user running the cron job.

I was logged in as `bandit22`, but the script was executed as `bandit23`.

Using the wrong username would generate a different hash and point to the wrong file.

### What I Learned

I learned how multiple Linux commands can be combined using pipes and command substitution.

I also learned that reading a shell script carefully can reveal how a program works and where it stores information.

</details>


<details>
<summary><b>Level 23 -> Level 24</b></summary>

### Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

### Commands Used

- `ls -la`
- `cat`
- `nano`
- `chmod`
- `cp`
- `cd`

### Thought Process

1. I started by checking the cron configuration directory:

   ```bash
   ls -la /etc/cron.d/
   ```

2. I found the configuration for Bandit 24 and checked the script being executed:

   ```bash
   cat /usr/bin/cronjob_bandit24.sh
   ```

3. I noticed that the script changes into this directory:

   ```bash
   /var/spool/bandit24/foo
   ```

4. The script checks the owner of each file and only executes files owned by `bandit23`.

5. I tried listing the contents of the directory, but received a `Permission denied` error.

6. I then created my own shell script using `nano`:

   ```bash
   nano /tmp/getpassword.sh
   ```

7. I added the following commands to the script:

   ```bash
   #!/bin/bash

   cat /etc/bandit_pass/bandit24 > /tmp/bandit24_password
   chmod 644 /tmp/bandit24_password
   ```

8. The script reads the Bandit 24 password and saves it to a file in `/tmp/`. I also changed the output file permissions so that I could read it afterward.

9. I gave my script execution permission:

   ```bash
   chmod +x /tmp/getpassword.sh
   ```

10. I copied it into the cron job directory:

    ```bash
    cp /tmp/getpassword.sh /var/spool/bandit24/foo/
    ```

11. The cron job automatically executed my script and deleted it afterward.

12. Finally, I read the output file to retrieve the next level's password:

    ```bash
    cat /tmp/bandit24_password
    ```

### Key Concepts

- **Shell Script:** A file containing multiple commands that can be executed together.
- **Shebang (`#!/bin/bash`):** Specifies the interpreter used to run the script.
- **chmod +x:** Gives a file execution permission.
- **cp:** Copies files from one location to another.
- **cron:** Automatically executes commands at scheduled intervals.
- **File ownership:** Determines which user owns a file.
- **File permissions:** Control whether users can read, write, or execute files.

### Troubleshooting & Lessons Learned

When I tried to list the contents of `/var/spool/bandit24/foo`, I received a `Permission denied` error.

I also learned that being able to work with a directory does not necessarily mean I can list its contents.

Another important detail was that the cron job only executes scripts owned by `bandit23`. I had to make sure my script was copied with the correct ownership.

### What I Learned

This was my first time writing a shell script for an automated task.

I learned how to create a script, give it execution permission, and use a cron job to run it automatically.

I also got a better understanding of Linux file ownership, permissions, and basic automation.

</details>

<details>
<summary><b>Level 24 -> Level 25</b></summary>

### Goal

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time.

### Commands Used

- `nano`
- `seq`
- `for`
- `echo`
- `nc` (Netcat)
- `chmod`
- `cat`

### Thought Process

1. I first connected to the daemon using Netcat:

   ```bash
   nc localhost 30002
   ```

2. I learned that I needed to provide the Bandit 24 password along with a 4-digit PIN.

3. Since I didn't know the PIN, I decided to automate the process with a Bash script instead of trying every combination manually.

4. I created a script:

   ```bash
   nano /tmp/brute.sh
   ```

5. I wrote the following code:

   ```bash
   #!/bin/bash

   PASS="BANDIT24_PASSWORD"

   for i in $(seq -w 0 9999); do
       echo "$PASS $i"
   done | nc -w 1 localhost 30002 > /tmp/results.txt
   ```

6. The `seq -w 0 9999` command generates PIN combinations from `0000` to `9999`.

7. The `for` loop sends the Bandit 24 password and each PIN to the daemon through Netcat.

8. I used output redirection (`>`) to save the server's responses in `/tmp/results.txt`.

9. After running the script, I checked the results:

   ```bash
   cat /tmp/results.txt
   ```

10. The output contained the response from the server, including the password for the next level.

### Key Concepts

- **Brute Force:** Trying all possible combinations until the correct one is found.
- **Bash Loop:** Using a `for` loop to repeat commands automatically.
- **seq -w:** Generates a sequence of numbers while keeping leading zeros.
- **Netcat (nc):** Used to communicate with a service through a network connection.
- **Output Redirection (`>`):** Saves command output to a file.
- **Automation:** Using a script to perform repetitive tasks without manual input.

### Troubleshooting & Lessons Learned

At first, I tried connecting to the daemon manually, but I couldn't retrieve the password because I didn't know the correct PIN.

Instead of guessing manually, I used a Bash script to test all 10,000 combinations.

One important detail was using `seq -w` to keep the PINs in a four-digit format, including leading zeros.

I also learned that I could save the server's response to a file and check it afterward instead of watching all the output directly in the terminal.

### What I Learned

This challenge helped me understand how brute-force attacks work at a basic level.

I also got more comfortable writing Bash scripts, using loops, and working with Netcat.

Most importantly, I learned how a simple script can automate a task that would take a long time to complete manually.

</details>

<details>
<summary><b>Level 25 -> Level 26</b></summary>

### Goal

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

### Commands Used

- `ls -la`
- `cat`
- `grep`
- `stty`
- `ssh`
- `more`
- `vim`
- `:set shell=/bin/bash`
- `:shell`

### Thought Process

1. I started by checking the files in the Bandit 25 home directory:

   ```bash
   ls -la
   ```

2. I found the SSH private key for Bandit 26 and used it to connect:

   ```bash
   ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
   ```

3. The connection closed immediately after displaying the welcome message. I suspected that the problem was related to Bandit 26's default shell.

4. I checked the user's shell configuration:

   ```bash
   cat /etc/passwd | grep bandit26
   ```

5. I found that Bandit 26 uses `/usr/bin/showtext` instead of `/bin/bash`.

6. I checked the contents of the program:

   ```bash
   cat /usr/bin/showtext
   ```

   It contained:

   ```bash
   #!/bin/sh

   export TERM=linux

   exec more ~/text.txt

   exit 0
   ```

7. I realized that the program uses `more` to display a text file. The terminal size affects whether `more` exits immediately or stays open.

8. I returned to my Mac terminal and reduced the terminal dimensions:

   ```bash
   stty rows 5 cols 20
   ```

9. I connected to Bandit 26 again using the SSH private key:

   ```bash
   ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
   ```

10. This time, the `more` interface stayed open instead of closing immediately.

11. I pressed `v` to open the Vim editor from the `more` interface.

12. Inside Vim, I changed the shell to Bash:

   ```vim
   :set shell=/bin/bash
   ```

13. Then I executed the shell:

   ```vim
   :shell
   ```

14. This allowed me to escape the restricted environment and access a Bash shell.

15. Finally, I retrieved the Bandit 26 password:

   ```bash
   cat /etc/bandit_pass/bandit26
   ```

### Key Concepts

- **SSH Private Key:** A private key used for authentication when connecting to an SSH server.
- **/etc/passwd:** Stores user account information, including each user's default shell.
- **Custom Shell:** A program configured to run instead of a standard shell such as Bash.
- **Terminal Size (`stty`):** Controls terminal settings, including the number of rows and columns.
- **more:** A command-line utility that displays text one page at a time.
- **Vim:** A terminal-based text editor that can also execute shell commands.
- **Shell Escape:** Using an available program to access a different shell from a restricted environment.

### Troubleshooting & Lessons Learned

At first, my SSH connection closed immediately after displaying the welcome message.

After checking `/etc/passwd`, I discovered that Bandit 26 uses a custom shell called `showtext`.

I then checked the script and found that it runs `more` to display a text file.

The important part was reducing the terminal size. This prevented `more` from exiting immediately and allowed me to access its interface.

From there, I used `v` to open Vim and executed Bash through Vim's shell command.

### What I Learned

This challenge helped me understand how Linux users can be assigned different default shells.

I also learned that terminal settings can affect how command-line programs behave.

Most importantly, I learned that programs like `more` and Vim can provide a way to escape a restricted shell environment.

</details>

<details>
<summary><b>Level 26 -> Level 27</b></summary>

### Goal
The goal is to retrieve the password for Bandit 27. The Bandit 26 account uses a restricted shell that runs the `more` command instead of a normal Bash shell.

### Steps

**1. Connect to Bandit 26 using the SSH private key**

First, I changed my terminal size on my Mac to make the `more` command display its prompt.

```bash
stty rows 5 cols 20
```

Then I connected using the private key:

```bash
ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
```

**2. Escape from the restricted shell**

The login started the `more` command because the account uses `/usr/bin/showtext` as its shell.

When the `--More--` prompt appeared, I pressed:

```text
v
```

This opened Vim.

Inside Vim, I changed the shell to Bash and started a shell:

```vim
:set shell=/bin/bash
:shell
```

**3. Find the Bandit 27 password**

After escaping to Bash, I checked the files in the home directory:

```bash
ls -la
```

I used the `bandit27-do` program to read the Bandit 27 password file:

```bash
./bandit27-do cat /etc/bandit_pass/bandit27
```

### What I Learned

- SSH authentication using a private key
- How terminal dimensions can affect command behavior
- How the `more` command works
- Using Vim to escape from a restricted shell
- Changing the shell from Vim
- Understanding setuid programs and privilege escalation

### Key Takeaway

This level showed me that a restricted shell does not always prevent access to other commands. Understanding how programs interact with the terminal can reveal ways to escape a limited environment.

</details>


<details>

<summary><b>Level 27 -> Level 28</b></summary>

### Goal
There is a git repository at ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.



### Commands Used

- `git --version`
- `git clone`
- `cd`
- `ls -la`
- `cat`

### Steps

**1. Check if Git is installed**

First, I checked whether Git was installed on my Mac.

```bash
git --version
```

**2. Clone the repository**

I cloned the remote Git repository using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo
```

When prompted, I entered the Bandit 27 password.

**3. Navigate to the repository**

After cloning the repository, I moved into the `repo` directory.

```bash
cd repo
```

**4. Read the README file**

I checked the repository contents and opened the README file.

```bash
ls -la
cat README
```

The README file contained the password for the next level.

### What I Learned

- How to clone a remote Git repository using SSH
- How to use Git from a local machine
- How to navigate a cloned repository
- How to read files inside a Git repository

### Key Takeaway

This level introduced me to cloning and inspecting a remote Git repository. I also learned how Git can be used to access files stored on a remote server.

</details>

<details>
<summary><b>Level 28 -> Level 29</b></summary>

### Goal
There is a git repository at ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `cat`
- `git log`
- `git show`

### Steps

**1. Clone the repository**

First, I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo bandit28-repo
```

**2. Navigate to the repository**

I moved into the cloned repository directory.

```bash
cd bandit28-repo
```

**3. Check the README file**

I opened the README file and noticed that the password was replaced with `xxxxxxxxxx`.

```bash
cat README.md
```

**4. Inspect the Git commit history**

I checked the commit history to see what had changed.

```bash
git log
```

I found three commits:

- `388bcd3` - initial commit of README.md
- `df10da1` - add missing data
- `801b85f` - fix info leak

**5. Check the previous commit**

The latest commit had removed the sensitive information, so I inspected the previous commit.

```bash
git show df10da19c2625f7c59e071e16030bd587d8c409d
```

The previous commit revealed the original README content, including the password for Bandit 29.

### What I Learned

- How to clone a remote Git repository
- How to inspect commit history using `git log`
- How to view previous commits using `git show`
- How deleted or modified information can remain in Git history
- How sensitive information can be exposed through Git repositories

### Key Takeaway

This level showed me that deleting sensitive information from the latest version of a file does not necessarily remove it from the Git repository.

Even if a password is replaced or deleted, it may still be accessible through previous commits. This is an important security risk known as information disclosure.

In real-world development, exposed passwords and API keys should be revoked and replaced, not simply deleted from the latest commit.
</details>

<details>
<summary><b>Level 29 -> Level 30</b></summary>

### Goal
There is a git repository at ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `ls`
- `cat`
- `git show`
- `git branch -a`

### Steps

**1. Clone the repository**

I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo bandit29-repo
```

**2. Navigate to the repository**

```bash
cd bandit29-repo
```

**3. Check the README file**

I listed the files and opened the README.

```bash
ls
cat README.md
```

The README contained the username `bandit30`, but the password was replaced with:

```text
<no passwords in production!>
```

**4. Inspect the latest commit**

I used `git show` to check the latest commit and noticed that the username had been changed from `bandit29` to `bandit30`.

```bash
git show
```

**5. Check available branches**

Since the password was not available in the master branch, I checked all available branches.

```bash
git branch -a
```

I found three branches:

- `master`
- `origin/dev`
- `origin/sploits-dev`

**6. Inspect the dev branch**

I checked the contents of the `dev` branch using:

```bash
git show origin/dev
```

This revealed the password for Bandit 30.

### What I Learned

- How Git branches work
- How to list local and remote branches using `git branch -a`
- How to inspect a remote branch using `git show`
- How different branches can contain different versions of files
- How sensitive information can be hidden in a different branch

### Key Takeaway

This level showed me that checking only the master branch is not always enough. Other branches may contain important information that is not available in the main version of the repository.

Understanding Git branches is useful not only for development but also for security investigations.
</details>

<details>
<summary><b>Level 30 -> Level 31</b></summary>

### Goal
There is a git repository at ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `cat`
- `ls -la`
- `git tag`
- `git show`

### Steps

**1. Clone the repository**

I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo bandit30-repo
```

**2. Navigate to the repository**

```bash
cd bandit30-repo
```

**3. Check the README file**

I opened the README file and found that it contained a message saying:

```text
just an empty file... muahaha
```

I also checked the directory contents, including hidden files.

```bash
cat README.md
ls -la
```

**4. Check Git tags**

Since the README did not contain any useful information, I checked the repository's tags.

```bash
git tag
```

**5. Inspect the tag**

I used `git show` to inspect the tag and found the password for Bandit 31.

```bash
git show <tag-name>
```

### What I Learned

- How to clone a remote Git repository
- How to identify hidden directories using `ls -la`
- What the `.git` directory stores
- How Git tags work
- How to inspect tags using `git show`

### Key Takeaway

This level showed me that useful information is not always stored in the latest README file. Git tags can also reference commits containing important information.

I learned to check Git tags when investigating a repository, rather than focusing only on the current files.
</details>

<details>
<summary><b>Level 31 -> Level 32</b></summary>

### Goal
There is a git repository at ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `cat`
- `echo`
- `git add -f`
- `git commit`
- `git push`
- `GIT_SSH_COMMAND`

### Steps

**1. Clone the repository**

I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo bandit31-repo
```

**2. Navigate to the repository**

```bash
cd bandit31-repo
```

**3. Read the instructions**

I checked the README file to understand the requirements.

```bash
cat README.md
```

The instructions required me to create:

- File name: `key.txt`
- Content: `May I come in?`
- Branch: `master`

**4. Create the required file**

I created `key.txt` with the required content.

```bash
echo "May I come in?" > key.txt
```

**5. Add the file to Git**

Since the `.txt` file was ignored by Git, I used the `-f` option to force-add it.

```bash
git add -f key.txt
```

**6. Commit the changes**

```bash
git commit -m "Add key.txt"
```

**7. Push to the remote repository**

My first push attempt failed because Git tried to connect using SSH port 22 instead of port 2220.

I fixed this by specifying the correct SSH port:

```bash
GIT_SSH_COMMAND="ssh -p 2220" git push origin master
```

The remote server validated the file and returned the password for Bandit 32.

### What I Learned

- How to create files using `echo`
- How `.gitignore` affects Git tracking
- How to force-add ignored files using `git add -f`
- How to commit and push changes to a remote repository
- How to specify an SSH port using `GIT_SSH_COMMAND`
- How Git pre-receive hooks can validate pushed files

### Key Takeaway

This level introduced me to pushing files to a remote Git repository and understanding how server-side Git hooks work.

I also learned that a failed push does not always mean the task failed. In this challenge, the server validated my file, displayed the next password, and then intentionally rejected the push.
</details>

<details>
<summary><b>Level 32 -> Level 33</b></summary>

## Goal
Escape from the Uppercase Shell and retrieve the password for the next level.

## Commands Used
- `$0`
- `ls`
- `whoami`
- `cat`

## Thought Process

1. After logging in as bandit32, I was placed in a restricted shell called the Uppercase Shell.
2. Commands such as `whoami` and `ls` were automatically converted to uppercase, causing permission errors.
3. I entered `$0` to escape the restricted shell and start a normal shell.
4. The prompt changed from `>>` to `$`, indicating that I had successfully escaped.
5. I verified that normal commands worked by running `ls`.

## Key Takeaway

- Linux commands are case-sensitive.
- The Uppercase Shell converts user input into uppercase commands.
- `$0` can be used to start a new shell and escape this restricted environment.

## What I Learned

This level taught me how shell behavior can affect command execution and how shell variables can be used to escape a restricted environment.
</details>

