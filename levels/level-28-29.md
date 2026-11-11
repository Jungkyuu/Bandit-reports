# Level 28 -> Level 29

### Goal
There is a git repository at ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `cat`
- `git log`
- `git show`

### Steps

**1. Clone the repository**

First, I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo bandit28-repo
```

**2. Navigate to the repository**

I moved into the cloned repository directory.

```bash
cd bandit28-repo
```

**3. Check the README file**

I opened the README file and noticed that the password was replaced with `xxxxxxxxxx`.

```bash
cat README.md
```

**4. Inspect the Git commit history**

I checked the commit history to see what had changed.

```bash
git log
```

I found three commits:

- `388bcd3` - initial commit of README.md
- `df10da1` - add missing data
- `801b85f` - fix info leak

**5. Check the previous commit**

The latest commit had removed the sensitive information, so I inspected the previous commit.

```bash
git show df10da19c2625f7c59e071e16030bd587d8c409d
```

The previous commit revealed the original README content, including the password for Bandit 29.

### What I Learned

- How to clone a remote Git repository
- How to inspect commit history using `git log`
- How to view previous commits using `git show`
- How deleted or modified information can remain in Git history
- How sensitive information can be exposed through Git repositories

### Key Takeaway

This level showed me that deleting sensitive information from the latest version of a file does not necessarily remove it from the Git repository.

Even if a password is replaced or deleted, it may still be accessible through previous commits. This is an important security risk known as information disclosure.

In real-world development, exposed passwords and API keys should be revoked and replaced, not simply deleted from the latest commit.
