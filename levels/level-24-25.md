# Level 24 -> Level 25

### Goal

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time.

### Commands Used

- `nano`
- `seq`
- `for`
- `echo`
- `nc` (Netcat)
- `chmod`
- `cat`

### Thought Process

1. I first connected to the daemon using Netcat:

   ```bash
   nc localhost 30002
   ```

2. I learned that I needed to provide the Bandit 24 password along with a 4-digit PIN.

3. Since I didn't know the PIN, I decided to automate the process with a Bash script instead of trying every combination manually.

4. I created a script:

   ```bash
   nano /tmp/brute.sh
   ```

5. I wrote the following code:

   ```bash
   #!/bin/bash

   PASS="BANDIT24_PASSWORD"

   for i in $(seq -w 0 9999); do
       echo "$PASS $i"
   done | nc -w 1 localhost 30002 > /tmp/results.txt
   ```

6. The `seq -w 0 9999` command generates PIN combinations from `0000` to `9999`.

7. The `for` loop sends the Bandit 24 password and each PIN to the daemon through Netcat.

8. I used output redirection (`>`) to save the server's responses in `/tmp/results.txt`.

9. After running the script, I checked the results:

   ```bash
   cat /tmp/results.txt
   ```

10. The output contained the response from the server, including the password for the next level.

### Key Concepts

- **Brute Force:** Trying all possible combinations until the correct one is found.
- **Bash Loop:** Using a `for` loop to repeat commands automatically.
- **seq -w:** Generates a sequence of numbers while keeping leading zeros.
- **Netcat (nc):** Used to communicate with a service through a network connection.
- **Output Redirection (`>`):** Saves command output to a file.
- **Automation:** Using a script to perform repetitive tasks without manual input.

### Troubleshooting & Lessons Learned

At first, I tried connecting to the daemon manually, but I couldn't retrieve the password because I didn't know the correct PIN.

Instead of guessing manually, I used a Bash script to test all 10,000 combinations.

One important detail was using `seq -w` to keep the PINs in a four-digit format, including leading zeros.

I also learned that I could save the server's response to a file and check it afterward instead of watching all the output directly in the terminal.

### What I Learned

This challenge helped me understand how brute-force attacks work at a basic level.

I also got more comfortable writing Bash scripts, using loops, and working with Netcat.

Most importantly, I learned how a simple script can automate a task that would take a long time to complete manually.
