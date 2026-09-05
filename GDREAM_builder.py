import os
import shutil
import subprocess
import sys

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------
ROOT = os.path.abspath(os.path.dirname(__file__))
DIST = os.path.join(ROOT, "dist")

# BASIC templates for each machine
BASIC_TEMPLATES = {
    "PET": "pet/GDREAM32K.BAS",
    "C64": "c64/GDREAM_C64.BAS",
    "VIC20": "vic20/GDREAM_VIC20.BAS",
    "PLUS4": "plus4/GDREAM_PLUS4.BAS",
    "C128": "c128/GDREAM_C128.BAS"
}

# Output D64 names
D64_OUTPUTS = {
    "PET": "GDREAM_PET.d64",
    "C64": "GDREAM_C64.d64",
    "VIC20": "GDREAM_VIC20.d64",
    "PLUS4": "GDREAM_PLUS4.d64",
    "C128": "GDREAM_C128.d64"
}

# Linux C/H sources
LINUX_FILES = [
    "linux/gdream.c",
    "linux/gdream.h",
    "linux/Makefile"
]

# ---------------------------------------------------------
# UTILITIES
# ---------------------------------------------------------

def autofill_bas(bas_path, tokens):
    with open(bas_path, "r") as f:
        content = f.read()

    dispatcher = ""
    line = 500
    for token in tokens:
        dispatcher += f'IF C$="{token}" THEN GOSUB {line}\n'
        line += 10

    content = content.replace("REM %%GDREAM_COMMANDS%%", dispatcher)

    with open(bas_path, "w") as f:
        f.write(content)

def ensure(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy(src, dst):
    shutil.copy(src, dst)

def run(cmd):
    subprocess.run(cmd, shell=True)

    def load_tokens():
        token_file = os.path.join(ROOT, "gui/pet_tokens.txt")
        if not os.path.exists(token_file):
            print("No token file found — skipping auto-fill.")
            return []

        systems = ["PET", "C64", "VIC20", "PLUS4", "C128", "B128"]
        system_var = tk.StringVar(value="PET")

        system_menu = tk.OptionMenu(root, system_var, *systems)
        system_menu.pack(pady=5)

        with open(token_file, "r") as f:
            lines = f.readlines()
        tokens = load_tokens()

        for system in BASIC_TEMPLATES.keys():
            generate_bas_for_system(system, tokens)
            build_d64_for_system(system)

        return tokens

    def export_tokens():
        target = system_var.get()
        out_file = f"tokens_{target}.txt"

        with open(out_file, "w") as f:
            for intent, payload, token in tokens:
                f.write(f"{token}:{payload}\n")


def generate_bas_for_system(system, tokens):
    template = BASIC_TEMPLATES[system]
    dst = os.path.join(DIST, os.path.basename(template))

    shutil.copy(os.path.join(ROOT, template), dst)

    dispatcher = ""
    line = 500

    for token in tokens:
        dispatcher += f'IF C$="{token}" THEN GOSUB {line}\n'
        line += 10

    with open(dst, "r") as f:
        content = f.read()

    content = content.replace("REM %%GDREAM_COMMANDS%%", dispatcher)

    with open(dst, "w") as f:
        f.write(content)


def build_d64_for_system(system):
    bas = os.path.join(DIST, os.path.basename(BASIC_TEMPLATES[system]))
    out = os.path.join(DIST, D64_OUTPUTS[system])

    cmd = f'c1541 -format GDREAM,GD d64 "{out}" -write "{bas}" GDREAM'
    run(cmd)


# ---------------------------------------------------------
# PACKAGE BASIC FILES + LINUX SOURCES
# ---------------------------------------------------------
def package_base():
    print("Packaging BASIC templates and Linux sources...")
    ensure(DIST)
def load_tokens()
    tokens = load_tokens()

    for target, bas_path in BASIC_TEMPLATES.items():
        src = os.path.join(ROOT, bas_path)
        dst = os.path.join(DIST, os.path.basename(bas_path))

        shutil.copy(src, dst)
        autofill_bas(dst, tokens)

    # Copy Linux sources
    for lf in LINUX_FILES:
        copy(os.path.join(ROOT, lf),
             os.path.join(DIST, os.path.basename(lf)))

    print("Base packaging complete.")


# ---------------------------------------------------------
# BUILD D64 IMAGES
# ---------------------------------------------------------
def build_d64():
    print("Building D64 images...")

    for target, bas_path in BASIC_TEMPLATES.items():
        out_name = D64_OUTPUTS[target]
        out_path = os.path.join(DIST, out_name)

        bas_full = os.path.join(ROOT, bas_path)

        # Requires user-installed c1541
        cmd = f'c1541 -format GDREAM,GD d64 "{out_path}" -write "{bas_full}" GDREAM'
        print("Running:", cmd)
        run(cmd)

    print("D64 build complete.")

# ---------------------------------------------------------
# BUILD WINDOWS EXE
# ---------------------------------------------------------
def build_windows_exe():
    if not sys.platform.startswith("win"):
        print("Skipping Windows EXE build (not on Windows).")
        return

    print("Building Windows EXE...")

    gui_file = os.path.join(ROOT, "gui/GDREAM_PET_TOKEN_GUI.py")
    cmd = f'pyinstaller --onefile --windowed "{gui_file}"'
    run(cmd)

    exe_src = os.path.join(ROOT, "dist", "GDREAM_PET_TOKEN_GUI.exe")
    exe_dst = os.path.join(DIST, "GDREAM_GUI_win.exe")

    if os.path.exists(exe_src):
        copy(exe_src, exe_dst)
        print("Windows EXE built:", exe_dst)
    else:
        print("Windows EXE build failed or PyInstaller missing.")

# ---------------------------------------------------------
# BUILD LINUX EXECUTABLE
# ---------------------------------------------------------
def build_linux_exe():
    if not sys.platform.startswith("linux"):
        print("Skipping Linux build (not on Linux).")
        return

    print("Building Linux executable...")

    cmd = f'make -C "{os.path.join(ROOT, "linux")}"'
    run(cmd)

    linux_bin = os.path.join(ROOT, "linux/gdream")
    linux_dst = os.path.join(DIST, "GDREAM_GUI_linux")

    if os.path.exists(linux_bin):
        copy(linux_bin, linux_dst)
        print("Linux executable built:", linux_dst)
    else:
        print("Linux build failed or Makefile missing.")

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    print("GDREAM Builder Starting...")

    package_base()
    build_d64()
    build_windows_exe()
    build_linux_exe()

    print("GDREAM Builder Complete.")
    print("Final release is in:", DIST)
