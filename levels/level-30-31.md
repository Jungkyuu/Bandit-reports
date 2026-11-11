# Level 30 -> Level 31

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
