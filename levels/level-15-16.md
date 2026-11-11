# Level 15 -> Level 16

**Goal**

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

**Commands Used**

- `cat`
- `openssl s_client`

**Thought Process**

1. Retrieved the current level's password by reading the password file:

   ```bash
   cat /etc/bandit_pass/bandit15
   ```

2. Connected to port `30001` on the local machine using OpenSSL with SSL/TLS encryption:

   ```bash
   openssl s_client -connect localhost:30001
   ```

3. After establishing the connection, the terminal displayed information about the SSL/TLS connection. I pasted the `bandit15` password into the terminal and pressed Enter.

4. The server checked the submitted password and returned the password for Level 16.

**Key Concepts**

- **OpenSSL (`s_client`):** A command-line tool used to establish SSL/TLS connections and communicate with secure services. In this level, I used it to connect to port `30001`.
- **SSL/TLS:** Protocols used to encrypt communication between a client and a server. They help protect data while it is being transmitted.
- **Localhost:** Refers to the machine you are currently using. The address `127.0.0.1` can also be used to connect to the same machine.
- **Ports:** A port identifies a specific service running on a machine. In this challenge, port `30001` was used for the password-checking service.

**Troubleshooting & Lessons Learned**

- **SSL/TLS Connection:** Unlike the previous level, using Netcat alone was not sufficient because the service required an encrypted connection.
- **Understanding OpenSSL:** I learned that `openssl s_client` can be used to connect to services that require SSL/TLS encryption.
- **Terminal Messages:** OpenSSL may display connection information or messages such as `DONE` or `RENEGOTIATING`. These messages do not necessarily mean the connection failed.

**What I Learned**

This level helped me understand the difference between a regular network connection and an encrypted SSL/TLS connection. I also learned how to use OpenSSL to communicate securely with a service running on a specific port.
