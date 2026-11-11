# Level 22 -> Level 23

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
