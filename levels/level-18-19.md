# Level 18 -> Level 19

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
