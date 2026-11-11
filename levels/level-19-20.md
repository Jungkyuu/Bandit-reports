# Level 19 -> Level 20

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
