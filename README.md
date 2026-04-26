# Client-Server-Intro-Project
This is a very simple program that uses Python's socket library to create a connection between a client and a server. It uses TCP for the server to get a message from a client, then the server sends back a message to the client.

Resources Used:
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
https://realpython.com/python-sockets/

Purpose:
The main purpose was to learn how communication between a client and a server works. There are several steps that are needed to setup a socket for a server and client, and those steps are different. This was a quick project, but one that really helped me understand network communication.

Technologies used:
Python
Python sockets library

Setup:
1. Open 2 separate terminals
2. Run python3 server.py
3. Run python3 client.py

Key features/functionality:
Uses the Python sockets library to create a connection between a client and a server. The client sends the message "Hello server, please write back!", but this can be whatever you want. Then, the server hears this, and sends back the clients message as well as the IP address and port it came from.

Role/Contribution:
All code was made by me, referencing from the defined resources above.

Screenshots:
<img width="854" height="47" alt="Screenshot 2026-04-26 134424" src="https://github.com/user-attachments/assets/13603c85-5b96-4f6e-8fd5-939dae86cc8d" />
<img width="621" height="46" alt="Screenshot 2026-04-26 134513" src="https://github.com/user-attachments/assets/decaff97-bf13-446d-ba5a-60027188da6f" />

Reflection/Challenges:
Overall, this project was easy to implement, but was more about learning the steps of client-server communication. The resources were very helpful and taught me the functions I needed to use in the socket library. I plan on making this project more in-depth, where you can send multiple messages, and possibly do multithreading so multiple clients can talk to the server.
