# Level 6 -> Level 7

**Goal**
The password for the next level is stored somewhere on the server and has all of the following properties:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

**Commands Used**
* `find`
* `cat`

**Thought Process**
1. Used the `find` command starting from the root directory (`/`) to search the entire server.
2. Applied specific options to match the properties: `-user bandit7` for the owner, `-group bandit6` for the group, and `-size 33c` for the exact 33-byte size.
3. Added `2>/dev/null` at the end of the command to hide "Permission denied" error messages.
4. Extracted the password by reading the found file path using the `cat` command.
