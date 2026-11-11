# Level 23 -> Level 24

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
