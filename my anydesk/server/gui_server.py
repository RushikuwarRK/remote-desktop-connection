import tkinter as tk
from tkinter import messagebox
import threading
import screen_share_server  # Import the server code

def start_sharing():
    try:
        # Run the screen sharing server in a separate thread
        thread = threading.Thread(target=screen_share_server.run_server)
        thread.daemon = True
        thread.start()
        messagebox.showinfo("Screen Sharing", "Screen sharing started!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start screen sharing: {e}")

def stop_sharing():
    # Logic to stop screen sharing (add flag or close socket)
    messagebox.showinfo("Screen Sharing", "Screen sharing stopped!")

# GUI setup
app = tk.Tk()
app.title("Screen Share Application")

start_btn = tk.Button(app, text="Start Sharing", command=start_sharing)
start_btn.pack(pady=10)

stop_btn = tk.Button(app, text="Stop Sharing", command=stop_sharing)
stop_btn.pack(pady=10)

app.mainloop()
