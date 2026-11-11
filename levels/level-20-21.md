# Level 20 -> Level 21

### Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

### Commands Used

- `ls -l`
- `cat`
- `nc`
- `./suconnect`

### Thought Process

1. I started by checking the files in the home directory:

   ```bash
   ls -l
   ```

2. I found a binary called `suconnect`.

3. I checked the current level's password:

   ```bash
   cat /etc/bandit_pass/bandit20
   ```

4. Since the program connects to a port on localhost, I needed to create a local listener using Netcat.

5. I opened a terminal and started listening on port 1234:

   ```bash
   nc -l -p 1234
   ```

6. In another SSH session, I ran the setuid binary and specified the same port:

   ```bash
   ./suconnect 1234
   ```

7. I went back to the first terminal and entered the `bandit20` password.

8. The program checked the password and sent the next level's password through the connection.

### Key Concepts

- **Netcat (nc):** A tool used to create network connections and send or receive data.
- **localhost:** Refers to the current machine.
- **TCP port:** Identifies a communication endpoint used by applications.
- **setuid:** Allows a program to run with the privileges of its file owner.
- **TCP connection:** Allows two programs to exchange data over a network connection.

### Troubleshooting & Lessons Learned

The important part was keeping the Netcat listener running while executing `suconnect` from another terminal.

Both programs needed to use the same port number. If the port numbers did not match, they would not be able to communicate.

### What I Learned

I learned how to use Netcat to listen for incoming connections and how two programs can exchange data through a local TCP connection.

This level also helped me understand how setuid binaries can interact with network services.
