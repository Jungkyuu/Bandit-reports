# Level 26 -> Level 27

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
