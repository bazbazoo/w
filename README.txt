=== ROUGH DRAFT ===

=
w
=

w provides a very simple web server that:
* can query and modify the filesystem;
* execute CGI executables.

Usage
=====

% bin/w -h
usage: w [-h] [--ip IP] [--port PORT] [--debug] [ROOT]

positional arguments:
  ROOT

optional arguments:
  -h, --help            show this help message and exit
  --ip IP, -a IP
  --port PORT, -p PORT
  --debug, -d

Examples
========

Serve data under a directory:
-----------------------------

% bin/w dirname

All operations on the directory are governed by the file system permissions.
If an executable is inside the directory, when queried it will be executed.

Serve as a pipe to a CGI script:
--------------------------------

% bin/w executable

POST/PUT/GET data will be delivered to executable via stdin.
stdout will be returned to user.
stderr will be printed in the console.