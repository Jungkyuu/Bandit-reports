# Level 32 -> Level 33

## Goal
Escape from the Uppercase Shell and retrieve the password for the next level.

## Commands Used
- `$0`
- `ls`
- `whoami`
- `cat`

## Thought Process

1. After logging in as bandit32, I was placed in a restricted shell called the Uppercase Shell.
2. Commands such as `whoami` and `ls` were automatically converted to uppercase, causing permission errors.
3. I entered `$0` to escape the restricted shell and start a normal shell.
4. The prompt changed from `>>` to `$`, indicating that I had successfully escaped.
5. I verified that normal commands worked by running `ls`.

## Key Takeaway

- Linux commands are case-sensitive.
- The Uppercase Shell converts user input into uppercase commands.
- `$0` can be used to start a new shell and escape this restricted environment.

## What I Learned

This level taught me how shell behavior can affect command execution and how shell variables can be used to escape a restricted environment.
