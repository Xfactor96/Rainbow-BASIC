import tkinter as tk
from tkinter import messagebox

MAX_BYTES = 32 * 1024
tokens = []
current_size = 0

def pet_token(intent):
    t = intent.upper()
    safe = ""
    for ch in t:
        if ch.isalnum():
            safe += ch
    return safe[:8]

def estimate(intent, payload, token):
    return len(intent) + len(payload) + len(token) + 4

def add_command():
    global current_size

    raw = entry.get().strip()
    if ":" not in raw:
        messagebox.showerror("Error", "Use INTENT:EXPLANATION format.")
        return

    intent, payload = raw.split(":", 1)
    intent = intent.strip()
    payload = payload.strip()

    if not intent:
        messagebox.showerror("Error", "Intent cannot be empty.")
        return

    token = pet_token(intent)
    size = estimate(intent, payload, token)

    if current_size + size > MAX_BYTES:
        messagebox.showwarning("Limit", "32K limit reached.")
        return

    tokens.append((intent, payload, token))
    current_size += size

    listbox.insert(tk.END, f"{token} : {payload}")
    entry.delete(0, tk.END)

def export_tokens():
    if not tokens:
        messagebox.showinfo("Export", "No tokens to export.")
        return

    with open("pet_tokens.txt", "w") as f:
        for intent, payload, token in tokens:
            f.write(f"{token}:{payload}\n")

    messagebox.showinfo("Export", "Saved to pet_tokens.txt")

root = tk.Tk()
root.title("GDREAM PET Command Tokenizer")
root.geometry("480x360")

label = tk.Label(root, text="Enter command (INTENT:EXPLANATION):")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

add_btn = tk.Button(root, text="ADD COMMAND", command=add_command)
add_btn.pack(pady=5)

list_label = tk.Label(root, text="PET Tokens:")
list_label.pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=5)

export_btn = tk.Button(root, text="EXPORT TOKENS", command=export_tokens)
export_btn.pack(pady=10)

root.mainloop()
