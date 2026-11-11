# Level 14 -> Level 15

**Goal**
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

### Commands Used

- `cat`
- `nc` (Netcat)

### Thought Process

1. Retrieved the current level's password by reading the password file:

   ```bash
   cat /etc/bandit_pass/bandit14
   ```

2. Connected to port `30000` on the local machine using Netcat:

   ```bash
   nc localhost 30000
   ```

3. After connecting, the terminal did not display any message or prompt. I pasted the `bandit14` password into the terminal and pressed Enter.

4. The server checked the password and returned the password for Level 15.

### Key Concepts

- **Netcat (`nc`):** A command-line tool used to establish network connections and send or receive data. In this level, I used it to communicate with a service listening on TCP port `30000`.
- **Localhost:** Refers to the machine you are currently using. The address `127.0.0.1` can also be used to connect to the same machine.
- **Ports:** A port identifies a specific service running on a machine. In this challenge, port `30000` was used to communicate with the password-checking service.

### Troubleshooting & Lessons Learned

- **No Output After Connecting:** When I ran `nc localhost 30000`, the terminal appeared blank. At first, it was not obvious whether the connection had worked. However, Netcat was waiting for input, so I entered the password and pressed Enter.
- **Understanding Netcat:** I learned that Netcat does not always display a prompt or welcome message. Sometimes, I need to send data directly through the terminal after establishing a connection.

### What I Learned

This level helped me understand how to use Netcat to communicate with a service through a specific port. I also learned that a successful network connection does not always display a message, and that I can send input directly through the terminal.
