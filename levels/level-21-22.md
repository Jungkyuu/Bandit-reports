# Level 21 -> Level 22

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
