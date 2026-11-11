# Level 17 -> Level 18

### Goal

The password for the next level is stored in one of two files: `passwords.old` and `passwords.new`.

The files are almost identical, but one line has been changed. I needed to find that line to get the next password.

### Commands Used
- `diff`

### Thought Process

1. I started by comparing the two files using `diff`.
2. I ran:

   ```bash
   diff passwords.new passwords.old
   ```

3. The command showed that line 42 was different between the two files.
4. I checked the output and identified the changed line in `passwords.new`.
5. That line contained the password for the next level.

### Key Concepts

- **diff:** Compares two files and displays their differences.
- **File comparison:** Helps identify changes between files without reading everything manually.
- **Output symbols:** `<` and `>` indicate which file each changed line belongs to.

### Troubleshooting & Lessons Learned

At first, I had to understand what the `diff` output meant.

The output showed `42c42`, which means line 42 in the first file differs from line 42 in the second file.

I also learned that the order of filenames matters when interpreting the output.

### What I Learned

I learned how to use `diff` to compare files and find a specific change.

This was a useful way to find information without manually checking every line.
