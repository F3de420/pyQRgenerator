"""
Script Name: pyQRgenerator
Author: f3de420
Version: 0.1
Date: 02.19.2024
Sources: https://github.com/F3de420/pyQRgenerator
"""

import argparse
import qrcode
import os
from PIL import Image

def print_script_info():
    """
    Prints the docstring at the beginning of this script.
    """
    print(__doc__)

def create_qr_code(data, size, logo_path, qr_path):
    """
    Creates a QR code with the provided data.

    Parameters:
    data (str): The data to be encoded in the QR code.
    size (str): The size of the QR code ("1" for small, "2" for medium, "3" for large).
    logo_path (str): The full path of the logo file.
    qr_path (str): The path where to save the QR code file.

    Returns:
    None
    """
    try:
        # Create the QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size={"1": 5, "2": 10, "3": 15}.get(size, 10), border=4)
        qr.add_data(data)
        qr.make(fit=True)

        # Create the QR code image
        img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # If a logo path was provided, load the logo and paste it into the QR code
        if logo_path is not None:
            logo = Image.open(logo_path)
            # Resize the logo to a fifth of the QR code size
            logo_size = (img_qr.size[0] // 5,) * 2
            logo = logo.resize(logo_size)
            logo_pos = ((img_qr.size[0] - logo.size[0]) // 2,) * 2

            # Create a white box in the middle of the QR code for the logo
            white_box_size = (img_qr.size[0] // 4,) * 2
            white_box = Image.new('RGB', white_box_size, 'white')
            box_pos = ((img_qr.size[0] - white_box.size[0]) // 2,) * 2
            img_qr.paste(white_box, box_pos)

            # Paste the logo at the center of the QR code
            img_qr.paste(logo, logo_pos)

        # Save the QR code in high quality
        img_qr.save(qr_path, "PNG", quality=100)
        print(f"QR code successfully created! You can find the file here: {os.path.abspath(qr_path)}")
    except FileNotFoundError:
        print("The logo file was not found. Please check the file path and try again.")
    except IOError:
        print("An error occurred in reading or writing the file. Please check the file paths and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def create_qr_code_interactive():
    """
    Interactive version of the create_qr_code function that asks the user for input.
    """
    data = input("Enter the data to be encoded in the QR code: ")
    size = input("Enter the size of the QR code (1: Small, 2: Medium, 3: Large): ")
    logo_path = input("Enter the full path of the logo file (including the file name and extension): ")
    qr_path = input("Enter the name of the QR code file (without extension): ") + ".png"
    create_qr_code(data, size, logo_path, qr_path)

def main():
    """
    Main function that parses command line arguments and calls the function to create the QR code.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Create a QR code with optional logo.")

    # Add the arguments
    parser.add_argument("-i", "--interactive", action='store_true', help="Run the script in interactive mode.")
    parser.add_argument("-d", "--data", help="The data to be encoded in the QR code.")
    parser.add_argument("-s", "--size", choices=["1", "2", "3"], help="The size of the QR code (1: Small, 2: Medium, 3: Large).")
    parser.add_argument("-l", "--logo", help="The full path of the logo file (including the file name and extension).")
    parser.add_argument("-o", "--output", help="The name of the QR code file (without extension).")

    # Parse the arguments
    args = parser.parse_args()

    # If the interactive argument was provided, run the interactive version
    if args.interactive:
        print_script_info()
        create_qr_code_interactive()
    # If other arguments were provided, use them to create the QR code
    elif args.data and args.size and args.output:
        create_qr_code(args.data, args.size, args.logo, args.output + ".png")
    else:
        # If no arguments were provided, print an error message and the help text
        print("Error: No arguments provided.")
        parser.print_help()

if __name__ == "__main__":
    main()
    input("Press any key to exit...")
