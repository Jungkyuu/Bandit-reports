# Level 29 -> Level 30

### Goal
There is a git repository at ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `ls`
- `cat`
- `git show`
- `git branch -a`

### Steps

**1. Clone the repository**

I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo bandit29-repo
```

**2. Navigate to the repository**

```bash
cd bandit29-repo
```

**3. Check the README file**

I listed the files and opened the README.

```bash
ls
cat README.md
```

The README contained the username `bandit30`, but the password was replaced with:

```text
<no passwords in production!>
```

**4. Inspect the latest commit**

I used `git show` to check the latest commit and noticed that the username had been changed from `bandit29` to `bandit30`.

```bash
git show
```

**5. Check available branches**

Since the password was not available in the master branch, I checked all available branches.

```bash
git branch -a
```

I found three branches:

- `master`
- `origin/dev`
- `origin/sploits-dev`

**6. Inspect the dev branch**

I checked the contents of the `dev` branch using:

```bash
git show origin/dev
```

This revealed the password for Bandit 30.

### What I Learned

- How Git branches work
- How to list local and remote branches using `git branch -a`
- How to inspect a remote branch using `git show`
- How different branches can contain different versions of files
- How sensitive information can be hidden in a different branch

### Key Takeaway

This level showed me that checking only the master branch is not always enough. Other branches may contain important information that is not available in the main version of the repository.

Understanding Git branches is useful not only for development but also for security investigations.
