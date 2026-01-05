# Tools
# PDF Password Protector (protection.py)

This simple Python script allows you to secure any PDF file with a password, making it ideal for protecting sensitive or private documents.

### 📄 Description

The script reads an input PDF, copies all its pages, and saves a new password-protected version. It's useful for automating PDF security in personal, academic, or business environments.

### ⚙️ Requirements

* Python 3.x
* [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the required library with:

```bash
pip install PyPDF2
```

### 🚀 Usage

```bash
python3 script.py <input_pdf> <output_pdf> <password>
```

**Example:**

```bash
python3 script.py myfile.pdf protected_file.pdf mySecret123
```

### 📌 Features

* Adds password protection to existing PDF files.
* Handles common errors like missing files or invalid PDFs.
* Easy to use from the command line.

#QrCodeGen

# QR Code Generator with Center Logo

This Python script generates a QR code and places a logo at its center.
It uses a high error correction level to keep the QR code readable even with the logo overlay.

---

## Features

* Generate a QR code from a URL or text
* Add a centered logo image
* Supports transparent PNG logos
* High error correction (`ERROR_CORRECT_H`)

---

## Requirements

* Python 3.7+
* Libraries:

  * `qrcode`
  * `Pillow`

---

## Installation

```bash
pip install qrcode[pil] pillow
```

---

## Configuration

Edit these variables in the script:

```python
logo_path = "/path/to/logo.png"
qr_data = "https://www.example.com"
qr_output_path = "/path/to/output.png"
```

---

## Usage

Run the script and the QR code image will be saved to the specified output path.

---
#merge_pdf

This Python script merges two PDF files into a single output PDF using **PyPDF2**.

---

## Features

* Merge two PDF files in order
* Simple and lightweight
* Uses `PyPDF2.PdfMerger`

---

## Requirements

* Python 3.7+
* Library:

  * `PyPDF2`

---

## Installation

```bash
pip install PyPDF2
```

---

## Usage

Edit the file names or run the script directly:

```python
unisci_pdf("file1.pdf", "file2.pdf", "merged.pdf")
```

The merged PDF will be saved to the specified output file.



