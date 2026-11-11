# Level 16 -> Level 17

### Goal

The credentials for the next level can be retrieved by submitting the current level's password to a port on localhost in the range 31000 to 32000.

I needed to identify the open ports, determine which services used SSL/TLS, and find the service that returned the credentials for the next level.

### Commands Used

- `cat`
- `nmap`
- `openssl s_client`
- `nano`
- `chmod`
- `scp`
- `ssh`

### Thought Process

1. First, I checked the current level's password:

   ```bash
   cat /etc/bandit_pass/bandit16
   ```

2. I used Nmap to scan ports `31000` to `32000` on localhost:

   ```bash
   nmap -sV -p 31000-32000 localhost
   ```

3. Nmap found five open ports:

   - `31046` - echo
   - `31518` - ssl/echo
   - `31691` - echo
   - `31790` - ssl/unknown
   - `31960` - echo

4. I identified that ports `31518` and `31790` supported SSL/TLS. However, port `31518` was an echo service, meaning it would simply return the data I sent.

5. I decided to test port `31790` because it used SSL/TLS and was identified as an unknown service:

   ```bash
   openssl s_client -connect localhost:31790
   ```

6. At first, I kept seeing messages such as `KEYUPDATE`. After checking the available options, I tried again with `-quiet`:

   ```bash
   openssl s_client -quiet -connect localhost:31790
   ```

7. I submitted the current Bandit 16 password. The server returned an SSH private key for Bandit 17.

8. I saved the private key in a file on the remote server:

   ```bash
   nano /tmp/bandit17.key
   ```

9. I changed the file permissions so that only the owner could read and write it:

   ```bash
   chmod 600 /tmp/bandit17.key
   ```

10. I tried to connect to Bandit 17 from inside the server, but the localhost SSH connection was blocked.

11. I exited the remote SSH session and returned to my Mac terminal. I then transferred the private key from the remote server to my local machine using SCP:

    ```bash
    scp -P 2220 bandit16@bandit.labs.overthewire.org:/tmp/bandit17.key ~/bandit17.key
    ```

12. On my Mac, I restricted the permissions of the downloaded key:

    ```bash
    chmod 600 ~/bandit17.key
    ```

13. Finally, I used the private key to connect to Bandit 17:

    ```bash
    ssh -i ~/bandit17.key bandit17@bandit.labs.overthewire.org -p 2220
    ```

### Key Concepts

- **Nmap:** Used to scan ports and identify the services running on them.
- **Port Scanning:** Helps identify which network ports are open and accepting connections.
- **SSL/TLS:** Provides encrypted communication between a client and a server.
- **OpenSSL (`s_client`):** Used to establish an SSL/TLS connection and interact with the service.
- **Echo Service:** Returns the data sent by the client instead of providing new credentials.
- **SSH Private Key:** Used for authentication when connecting to Bandit 17.
- **SCP (Secure Copy):** Used to transfer the private key from the remote server to my local Mac.
- **File Permissions:** Used `chmod 600` to restrict access to the private key.

### Troubleshooting & Lessons Learned

- **Identifying the Correct Port:** Not every open port provided the required credentials. I had to distinguish between regular echo services and the service that returned the SSH private key.
- **KEYUPDATE Messages:** I initially wasn't sure what the `KEYUPDATE` messages meant. Using the `-quiet` option made it easier to interact with the service.
- **Localhost Connection:** My attempt to connect to Bandit 17 from inside the server did not work because localhost SSH connections were blocked. I had to transfer the private key to my own computer and connect from there.
- **SSH Key Permissions:** I learned that SSH requires appropriate private key permissions. Using `chmod 600` prevents other users from reading the key.

### What I Learned

This level helped me practice port scanning with Nmap and identify services that use SSL/TLS.

I also learned how to use OpenSSL to interact with an encrypted service, how to transfer SSH private keys using SCP, and why proper file permissions are important for SSH authentication.
