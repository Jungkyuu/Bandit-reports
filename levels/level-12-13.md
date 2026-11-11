# Level 12 -> Level 13

**Goal**
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

**Commands Used**
- `mktemp -d`, `cp`, `cd`, `mv`
- `xxd`
- `file`
- `gzip`, `bzip2`, `tar`

**Thought Process**
1. Created a temporary working directory in `/tmp` using `mktemp -d` and copied `data.txt` into it from the home directory.
2. Reversed the hexdump back into a binary file using `xxd -r data.txt > data.bin`.
3. Used the `file` command to determine the actual file type of the binary file.
4. Renamed the file with the appropriate extension (`.gz`, `.bz2`, or `.tar`) using the `mv` command so that the decompression tools could recognize it.
5. Decompressed the file using `gzip -d`, `bzip2 -d`, or `tar -xf` based on the file type.
6. Repeated the cycle of `file` -> `mv` -> `decompress` several times until the final uncompressed ASCII text file containing the password was revealed.

**Key Concepts**
- `mktemp -d`: Creates a secure, temporary directory.
- `xxd -r`: Reverses a hexdump, converting hexadecimal text back into binary data.
- `file`: Determines a file's type by examining its content (magic bytes), not just its extension.
- **Compression Tools**: Linux uses various compression formats. `.gz` is extracted with `gzip -d`, `.bz2` with `bzip2 -d`, and `.tar` (an archive) with `tar -xf`.
