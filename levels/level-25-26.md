# Level 25 -> Level 26

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
