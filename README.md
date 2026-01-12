# Text Shadow – Secure Message Hiding & Key Management

**Text Shadow** is a web-based application built with **Django** that allows users to securely hide messages within cover text and generate cryptographic keys. It combines **encryption**, **steganography-inspired techniques**, and a clean, responsive UI for an easy and secure experience.

---

## Features

### Key Generation
- Generate cryptographic keys with optional seeding.  
- Copy keys to clipboard instantly.

### Message Hiding
- Hide a secret message inside a cover message.  
- Use a key to secure the hidden message.  
- View and copy the combined hidden message via a modal interface.

### Message Extraction
- Extract hidden messages from previously combined messages using the correct key.

### Responsive UI
- Sidebar navigation with hamburger menu for small screens.  
- Dark mode-friendly design with modals for key/message display.

### Security
- Uses cryptography-backed key handling and JSON-based form submissions.  
- CSRF protection for all forms.

---

## Tech Stack
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Cryptography:** Python’s `cryptography` library (Fernet)

---

## Why Use Text Shadow
- Easily secure sensitive messages without complex software.  
- Simple interface that works on both desktop and mobile.  
- Explore practical encryption and key management techniques.

---

## Usage
1. Generate a key via the **Generate Key** page.  
2. Use the key to hide a secret message in a cover text on the **Hide Message** page.  
3. Extract the hidden message using the key on the **Extract Message** page.
