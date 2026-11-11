# Level 13 -> Level 14

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
