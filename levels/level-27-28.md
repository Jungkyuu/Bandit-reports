# Level 27 -> Level 28

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
