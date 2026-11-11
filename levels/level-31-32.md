# Level 31 -> Level 32

### Goal
There is a git repository at ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Commands Used

- `git clone`
- `cd`
- `cat`
- `echo`
- `git add -f`
- `git commit`
- `git push`
- `GIT_SSH_COMMAND`

### Steps

**1. Clone the repository**

I cloned the remote Git repository from my Mac using SSH on port 2220.

```bash
GIT_SSH_COMMAND="ssh -p 2220" git clone ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo bandit31-repo
```

**2. Navigate to the repository**

```bash
cd bandit31-repo
```

**3. Read the instructions**

I checked the README file to understand the requirements.

```bash
cat README.md
```

The instructions required me to create:

- File name: `key.txt`
- Content: `May I come in?`
- Branch: `master`

**4. Create the required file**

I created `key.txt` with the required content.

```bash
echo "May I come in?" > key.txt
```

**5. Add the file to Git**

Since the `.txt` file was ignored by Git, I used the `-f` option to force-add it.

```bash
git add -f key.txt
```

**6. Commit the changes**

```bash
git commit -m "Add key.txt"
```

**7. Push to the remote repository**

My first push attempt failed because Git tried to connect using SSH port 22 instead of port 2220.

I fixed this by specifying the correct SSH port:

```bash
GIT_SSH_COMMAND="ssh -p 2220" git push origin master
```

The remote server validated the file and returned the password for Bandit 32.

### What I Learned

- How to create files using `echo`
- How `.gitignore` affects Git tracking
- How to force-add ignored files using `git add -f`
- How to commit and push changes to a remote repository
- How to specify an SSH port using `GIT_SSH_COMMAND`
- How Git pre-receive hooks can validate pushed files

### Key Takeaway

This level introduced me to pushing files to a remote Git repository and understanding how server-side Git hooks work.

I also learned that a failed push does not always mean the task failed. In this challenge, the server validated my file, displayed the next password, and then intentionally rejected the push.
