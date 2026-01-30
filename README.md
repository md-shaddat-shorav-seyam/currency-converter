# currency-converter

# Graphical Currency Converter (Python)

## Overview

This project is a **graphical currency converter application** built using **Python** and **Tkinter**. It allows users to convert an amount from one currency to another using **real-time exchange rates** fetched from an online API.

The application is simple, beginner-friendly, and suitable for learning:

* Python GUI programming
* API integration
* Basic error handling

---

## Features

* Graphical User Interface (GUI)
* Real-time currency conversion
* Supports all major international currencies (USD, EUR, BDT, etc.)
* Input validation and error messages
* Lightweight and easy to run

---

## Technologies Used

* **Python 3**
* **Tkinter** (built-in GUI library)
* **Requests** (for HTTP API calls)

---

## Requirements

Make sure Python 3 is installed on your system.

Install the required dependency:

```bash
pip install requests
```

---

## How It Works

1. The user enters:

   * Amount to convert
   * Source currency code (e.g., USD)
   * Target currency code (e.g., BDT)
2. When the **Convert** button is clicked:

   * The app sends a request to the exchange rate API
   * Fetches the latest exchange rates
   * Calculates the converted value
   * Displays the result in the GUI

---

## API Used

The application uses the following public API:

```
https://api.exchangerate-api.com/v4/latest/{BASE_CURRENCY}
```

### Example Response

```json
{
  "base": "USD",
  "rates": {
    "EUR": 0.92,
    "BDT": 109.65
  }
}
```

---

## File Structure

```
currency_converter.py
```

---

## Main Components

### 1. GUI Window

* Created using `tk.Tk()`
* Fixed size window
* Title: **Currency Converter**

### 2. Input Fields

* Amount input (`Entry` widget)
* From currency code input
* To currency code input

### 3. Convert Button

* Triggers the currency conversion process

### 4. Result Label

* Displays the converted amount

---

## Error Handling

The application handles common errors such as:

* Empty amount field
* Invalid number input
* Invalid currency codes
* Network or API errors

Error messages are shown using pop-up dialogs.

---

## Usage Instructions

1. Run the program:

   ```bash
   python currency_converter.py
   ```
2. Enter the amount
3. Enter the source currency code (e.g., USD)
4. Enter the target currency code (e.g., EUR)
5. Click **Convert**
6. View the result

---

## Example

**Input:**

* Amount: 10
* From: USD
* To: BDT

**Output:**

```
10 USD = 1096.50 BDT
```

---

## Limitations

* Requires an active internet connection
* Currency codes must be entered manually
* UI is basic (Tkinter default style)

---

## Future Improvements

* Dropdown menu for currency selection
* Dark mode UI
* Save conversion history
* Desktop executable (.exe)
* Modern UI using PyQt or CustomTkinter

---

## License

This project is open-source and free to use for learning and personal projects.

---

## Author

Developed using Python for educational purposes.
