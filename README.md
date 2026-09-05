The previous readme text is irrelevant, I have updated everything.

It is finally done. the python file is up. just run the command line and use the following:

python GDREAM_builder.py --system PET --commands "MOVEUSIN,GRAPHIC,CHARDEF"

this was a MASSIVE undertaking and a month of progress is finished

I will NOT be updating this

good luck and have fun.

Here's the updated README:

GDREAM — Universal Commodore Command System
One command language. Any Commodore machine. One click to build a disk image.
GDREAM is a modern toolchain for classic Commodore computers.
It lets you define high‑level commands once, then automatically generates:

PET BASIC runtimes

C64 BASIC runtimes

VIC‑20 BASIC runtimes

Plus/4 BASIC runtimes

C128 BASIC runtimes

B128 BASIC runtimes

…and builds matching D64 disk images for each system.

GDREAM is designed to be simple, powerful, and universal — a single command language that works across the entire Commodore ecosystem.

✨ Features
Universal Command Adder
Define commands in plain language:

Code
MOVEUSIN:ACCEPTS X AND Y POSITION
GRAPHIC:PICK FROM HIRES OR LORES
CHARDEF:CREATE A CHARACTER USING A DRAW TOOL
GDREAM automatically:

Converts them into PET‑safe tokens

Generates BASIC dispatchers

Injects them into system templates

Builds runnable BASIC programs

Produces D64 disk images

You never touch BASIC.
You never edit templates.
You only add commands.

Cross‑Commodore Support
GDREAM supports:

PET

C64

VIC‑20

Plus/4

C128

B128

Each system gets its own auto‑generated BASIC runtime and disk image.

GUI Front‑End
The GDREAM GUI lets you:

Add commands

Select a target system

Choose an output folder

Build a disk image with one click

The GUI funnels all commands directly into the builder.

Builder Script
GDREAM_builder.py is the heart of GDREAM.

It:

Accepts commands from the GUI

Generates BASIC runtimes

Injects dispatchers

Builds D64 images

Writes everything into the user‑selected folder

The user’s only job is to pick a folder and click “Make Disk Image.”

Linux C/H Source Version
A native Linux CLI version is included:

gdream.c

gdream.h

Makefile

This provides a lightweight, terminal‑friendly alternative to the GUI.

📦 Installation
Windows
Install Python 3.10+

Install PyInstaller:

Code
pip install pyinstaller
Build the GUI executable:

Code
pyinstaller --onefile --windowed GDREAM_PET_TOKEN_GUI.py
Run the builder through the GUI.

Linux
Install GCC

Build the CLI version:

Code
make -C linux
Run the builder directly:

Code
python3 GDREAM_builder.py --system PET --commands "MOVEUSIN,GRAPHIC" --folder "/path/to/output"
🛠 Usage
1. Run the GUI
Select a system

Add commands

Choose an output folder

Click Make Disk Image

The GUI calls the builder automatically.

2. Builder Output
The builder writes into the chosen folder:

GDREAM_SYSTEM.BAS

GDREAM_SYSTEM.d64

Example:

Code
GDREAM_PET.BAS
GDREAM_PET.d64
3. Load the D64 in your emulator
Use your own installation of:

xpet

x64

xvic

xplus4

x128

GDREAM does not include emulator binaries.

📁 Output Structure
Code
/chosen/folder/
  GDREAM_PET.BAS
  GDREAM_PET.d64
  GDREAM_C64.BAS
  GDREAM_C64.d64
  GDREAM_VIC20.BAS
  GDREAM_VIC20.d64
  GDREAM_PLUS4.BAS
  GDREAM_PLUS4.d64
  GDREAM_C128.BAS
  GDREAM_C128.d64
  GDREAM_B128.BAS
  GDREAM_B128.d64
Only the systems you build will appear.

📜 License
GDREAM is released under the MIT License.
You are free to modify, distribute, and build upon this project.

💬 Credits
GDREAM was created as a modern, universal command system for retro computing enthusiasts who want a single language that works across the entire Commodore family.

 
