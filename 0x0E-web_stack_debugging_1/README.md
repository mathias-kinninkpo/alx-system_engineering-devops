0x0E. Web stack debugging #1
DevOps
SysAdmin
Scripting
Debugging


Concepts
For this project, we expect you to look at these concepts:

Network basics
Web stack debugging




Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
All your Bash script files must be executable
Your Bash scripts must pass Shellcheck without any error
Your Bash scripts must run without error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
You are not allowed to use wget







Tasks 0. required Nginx loves port 80 Score: 0% (checks passed: 0%)
Find out what is preventing the Nginx installation in your Ubuntu container from listening on port 80 using your debugging abilities. Install any tool you require, launch and terminate as many containers as necessary, and work through the problem however you see fit. Then, create a Bash script to automate your fix using the fewest possible instructions.

Requirements:

All of the server's active IPv4 addresses must be listening on port 80 for Nginx to be functioning.
Create a Bash script that sets up a server according to the specifications above.

1. Make it sweet and short 

Using what you did for task #0, make your fix short and sweet.

Requirements:

Your Bash script must be 5 lines long or less
There must be a new line at the end of the file
You must respect usual Bash script requirements
You cannot use ;
You cannot use &&
You cannot use wget
You cannot execute your previous answer file (Do not include the name of the previous script in this one)
service (init) must say that nginx is not running ← for real
