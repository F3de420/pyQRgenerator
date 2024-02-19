[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# pyQRgenerator

## Table of Contents
1. [Overview](overview)
2. [Requirements](requirements)
3. [Installation](installation)
4. [Usage](usage)
5. [Examples](examples)
6. [License](license)

## Overview <a name="overview"></a>
`pyQRgenerator` is a Python script that generates QR codes with optional logos. It can be run in interactive mode or with command line arguments. This script is perfect for generating custom QR codes for your business or personal use.

## Requirements <a name="requirements"></a>
- Python 3.9 or higher
- `qrcode` Python library
- `PIL` Python library

## Installation <a name="installation"></a>
To install the necessary libraries, you can use pip:

```bash
pip install qrcode pillow
```

## Usage <a name="usage"></a>
You can run the script in two ways:

1. **Interactive mode**: The script will prompt you to enter the data, size of the QR code, path of the logo file, and the output file name.

```bash
python3 pyQRgenerator.py --interactive
```

2. **Command line arguments**: You can provide the data, size, logo path, and output file name as command line arguments.

```bash
python3 pyQRgenerator.py --data "Your data" --size "2" --logo "/path/to/logo.png" --output "output_file_name"
```

## Examples <a name="examples"></a>
Here are some examples of how to use the script:

- **Interactive mode**:

```bash
python3 pyQRgenerator.py --interactive
```
Enter the data to be encoded in the QR code: ```bash Your data '''
Enter the size of the QR code (1: Small, 2: Medium, 3: Large): ```bash 2 '''
Enter the full path of the logo file (including the file name and extension): ```bash /path/to/logo.png '''
Enter the name of the QR code file (without extension): ```bash output_file_name ```
```

- **Command line arguments**:

```bash
python3 pyQRgenerator.py --data "Your data" --size "2" --logo "/path/to/logo.png" --output "output_file_name"
```

## License <a name="license"></a>
This project is licensed under the terms of the MIT license.
