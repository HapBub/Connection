# Connection

Two small Python scripts that act as a TCP client: they connect to a server, send a simple HTTP request, and save the response to a file.

## Scripts

- **`connection.py`** connects to `127.0.0.1:7777`, requests `/connect.html`, and writes the response to `response.html`.
- **`advancedconnection.py`** does the same, but names the output file with the current date and four random letters (for example `01_06_2023_abcd.log`), so earlier responses aren't overwritten.

## Usage

Start a server on the target port first, for example:

    python3 -m http.server 7777

Then run a script:

    python3 connection.py
    python3 advancedconnection.py

## Notes

- Personal learning project from 2023 (sockets and file handling).
- The host and port are set at the top of each script. Change them to connect elsewhere.
- Only the first 4096 bytes of the response are read and saved.
