# Level 10 -> Level 11

**Goal**
The password for the next level is stored in the file data.txt, which contains base64 encoded data

**Commands Used**
*  `base64`
*  `--decode`

**Thought Process**
1. Identified that the content in `data.txt` is encoded in Base64 format.
2. Used the `base64` command with the `--decode` option to decode the text back into its original human-readable form.
3. Executed `base64 --decode data.txt` to reveal the password directly.

**Key Concepts**
- `base64`: A command used to encode or decode data using the Base64 encoding scheme.
- `--decode`: An option that tells the `base64` command to decode the data rather than encode it.
