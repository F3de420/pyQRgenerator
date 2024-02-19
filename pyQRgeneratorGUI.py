import tkinter as tk
from tkinter import filedialog, messagebox, IntVar, Checkbutton, ttk
from PIL import Image
from pyQRgenerator import create_qr_code

def browse_file():
    """Open a file dialog and return the selected file's path."""
    filename = filedialog.askopenfilename()
    return filename

def save_file():
    """Open a save file dialog and return the selected file's path."""
    filename = filedialog.asksaveasfilename(defaultextension=".png")
    return filename

def toggle_logo_button(var, logo_button):
    """
    Enable or disable the logo button based on the state of the checkbutton.
    
    Parameters:
    var: tkinter variable associated with the checkbutton.
    logo_button: The button to be enabled or disabled.
    """
    if var.get():
        logo_button.config(state="normal")
    else:
        logo_button.config(state="disabled")

def generate_qr(data, size, var, logo_path, qr_path):
    """
    Generate a QR code with the given parameters and display a success message.
    
    Parameters:
    data: The data to be encoded in the QR code.
    size: The size of the QR code.
    var: tkinter variable associated with the checkbutton.
    logo_path: The path of the logo file.
    qr_path: The path where the QR code will be saved.
    """
    if not var.get():
        logo_path = None
    create_qr_code(data, str(size), logo_path, qr_path)
    messagebox.showinfo("Success", f"QR code successfully created! You can find the file here: {qr_path}")
    Image.open(qr_path).show()

def create_gui():
    """Create the GUI for the QR code generator."""
    window = tk.Tk()
    window.title("pyQRgenerator GUI")
    window.resizable(0, 0)  # Prevent the user from resizing the window
    style = ttk.Style(window)
    style.theme_use("clam")

    frame = ttk.Frame(window)
    frame.pack(padx=20, pady=20)

    # Create and place the widgets
    data_label = ttk.Label(frame, text="Data:")
    data_entry = ttk.Entry(frame, width=50)  # Set the width of the text input widget

    size_label = ttk.Label(frame, text="Size:")
    size_var = IntVar()
    size_small = ttk.Radiobutton(frame, text="Small", variable=size_var, value=1)
    size_medium = ttk.Radiobutton(frame, text="Medium", variable=size_var, value=2)
    size_large = ttk.Radiobutton(frame, text="Large", variable=size_var, value=3)

    logo_label = ttk.Label(frame, text="Logo file:")
    var = tk.IntVar()
    logo_check = ttk.Checkbutton(frame, text="Add logo", variable=var, command=lambda: toggle_logo_button(var, logo_button))
    logo_button = ttk.Button(frame, text="Browse", command=lambda: logo_button.config(text=browse_file()), state="disabled")

    output_label = ttk.Label(frame, text="Output file name:")
    output_button = ttk.Button(frame, text="Save As", command=lambda: output_button.config(text=save_file()))
    generate_button = ttk.Button(frame, text="Generate QR Code", command=lambda: generate_qr(data_entry.get(), size_var.get(), var, logo_button.cget('text'), output_button.cget('text')))
    exit_button = ttk.Button(frame, text="Exit", command=window.quit)

    # Use grid layout to place the widgets on the same row
    data_label.grid(row=0, column=0, pady=10, sticky='E')
    data_entry.grid(row=0, column=1, columnspan=2, pady=10, sticky='W')  # Center the text input widget
    size_label.grid(row=1, column=0, pady=10, sticky='E')
    size_small.grid(row=1, column=1, pady=10, padx=(5, 0), sticky='E')  # Reduce the space to the right of the "Small" button
    size_medium.grid(row=1, column=2, pady=10, padx=5)  # Reduce the space to the left of the "Medium" button and to the right of the "Large" button
    size_large.grid(row=1, column=3, pady=10, sticky='W')
    logo_label.grid(row=2, column=0, pady=10, sticky='E')
    logo_check.grid(row=2, column=1, pady=10, sticky='E')
    logo_button.grid(row=3, column=1, pady=10, sticky='E')  # Move the button to the row below
    output_label.grid(row=4, column=0, pady=5, sticky='E')  # Reduce the space above the "Save As" button
    output_button.grid(row=4, column=1, pady=5, sticky='E')  # Align the "Save As" button with the other buttons
    generate_button.grid(row=5, column=0, columnspan=4, pady=10)
    exit_button.grid(row=6, column=0, columnspan=4, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
