import urllib.request
import tkinter as tk
from tkinter import filedialog, messagebox
import random

# Function to download the audio file from a given URL
def download_audio(url, output_file):
    urllib.request.urlretrieve(url, output_file)

# Function to handle the "Download" button click event
def download_button_click():
    audio_url = url_entry.get()
    if not audio_url:
        messagebox.showwarning("Warning", "Please enter a valid URL")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if not output_file:
        return

    # Download the audio file
    messagebox.showinfo("Info", "Downloading audio...")
    try:
        download_audio(audio_url, output_file)
        messagebox.showinfo("Info", "Audio downloaded.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading the audio:\n{str(e)}")

# Function to change the background color
def change_background_color():
    current_color = window.cget("bg")
    new_color = random.choice(colors)
    while new_color == current_color:
        new_color = random.choice(colors)
    window.configure(bg=new_color)
    window.after(5000, change_background_color)

# Define a list of colors
colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff", "#ffa500", "#800080", "#008000", "#ff69b4", "#800000", "#00bfff"]

# Create the main window
window = tk.Tk()
window.title("Audio Downloader")
window.geometry("500x600")

# Create the URL entry label and text box
url_label = tk.Label(window, text="Audio URL:", font=("Arial", 12))
url_label.pack(pady=10)

url_entry = tk.Entry(window, width=50, font=("Arial", 12))
url_entry.pack()

# Create the "Download" button
download_button = tk.Button(window, text="Download", command=download_button_click, font=("Arial", 12), bg="#4caf50", fg="white", relief="raised")
download_button.pack(pady=20)

# Start changing the background color
window.after(5000, change_background_color)

# Run the Tkinter event loop
window.mainloop()
