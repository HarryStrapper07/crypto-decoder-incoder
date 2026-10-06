# crypto – Encoder / Decoder Toolkit

A simple command-line **encoding and decoding toolkit** written in Python.  
crypto is useful for learning, CTFs, cybersecurity labs, and quick text encoding/decoding tasks.

## Features

### Decoder
- Base64
- Base32
- Hex
- Binary
- ASCII
- URL Encoding
- Reverse
- Caesar Cipher (shows all 25 shifts)
- Morse Code

### Encoder
- Base64
- Base32
- Hex
- Binary
- ASCII
- URL Encoding
- Reverse
- Caesar Cipher
- Morse Code

### Other Features
- Encoding type identification
- Auto decoder
- Colorful terminal interface
- Interactive menu

## Requirements

- Python 3.x
- No external Python packages are required.

The tool uses only Python standard-library modules:
- `base64`
- `urllib.parse`

## Installation

Clone the repository:

```bash
git clone https://github.com/HarryStrapper07/<YOUR-REPO>.git
cd <YOUR-REPO>
```

No `pip install` is required.

## Usage

Run the tool with:

```bash
python crypto.py
```

On some Linux systems:

```bash
python3 crypto.py
```

## Menu

```text
1. Identify Encoding
2. Single Decoder
3. Auto Decoder
4. Encoder
0. Exit
```

### Identify Encoding

Attempts to identify possible encoding types from the supplied input.

### Single Decoder

Select a specific decoder and provide the encoded text.

### Auto Decoder

Attempts multiple decoding methods automatically and repeatedly processes the result when another layer can be decoded.

### Encoder

Select an encoding method and enter plain text to encode.

## Example

Input:

```text
SGVsbG8=
```

Using Base64 decoder produces:

```text
Hello
```

## Project Structure

```text
.
├── crypto.py
├── README.md
└── requirements.txt
```

## Disclaimer

This tool is intended for **educational purposes, CTFs, cybersecurity labs, and authorized testing**.

Do not use it to access, modify, or decode data without proper authorization.

## Author

**Harry_Strapper**

GitHub: `@HarryStrapper07`
