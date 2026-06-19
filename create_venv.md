# _BC_scrape_dawg_5000 🐶

This project is a web scraping utility built with Python and Playwright, following the freeCodeCamp "follow along" series. It demonstrates how to capture screenshots of websites using both synchronous and asynchronous methods across different browser engines (Chromium, Firefox, and WebKit).

## 🚀 Getting Started

To get this project running on your local machine, follow these steps:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. You can check this by running:
```bash
python3 --version
```

### 2. Set Up a Virtual Environment
It is best practice to use a virtual environment to keep dependencies organized.
```bash
# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
Playwright requires specific browser binaries to run. Install them with:
```bash
playwright install
```

---

## 🛠 How to Run

Once everything is set up, you can run the main script:
```bash
python main.py
```

This will:
1. Run a **synchronous** loop to take screenshots using Chromium, Firefox, and WebKit.
2. Run an **asynchronous** loop to do the same.
3. Save the screenshots in the project folder as `example-sync-[browser].png` and `example-async-[browser].png`.

---

## 📝 Changes & Improvements Made

If you are following along, here is a summary of the fixes and improvements recently applied to the code:

### 1. Resolved `ModuleNotFoundError`
The initial issue was that `playwright` wasn't recognized. This was fixed by:
- Creating a virtual environment (`.venv`).
- Installing the `playwright` package via `pip`.
- Installing the actual browser engines via `playwright install`.

### 2. Code Refactoring (Clean Code)
The script was reorganized to follow Python best practices:
- **Organized Imports:** Grouped all imports at the top of the file.
- **Function Wrapping:** Logic was moved into `run_sync()` and `run_async()` functions instead of running in the global scope.
- **Entry Point:** Added `if __name__ == "__main__":` to ensure the script only runs when executed directly.
- **Environment Variables:** Added `load_dotenv()` support to allow future configuration via a `.env` file.

### 3. Sync vs. Async Comparison
The code now clearly distinguishes between:
- **Synchronous (`run_sync`)**: Runs one task at a time. Easier to read for beginners.
- **Asynchronous (`run_async`)**: Uses `async`/`await` for better performance when handling multiple tasks simultaneously.

---

## 💡 Pro Tips for Beginners

### Using PyCharm
If you are using PyCharm, make sure it is using your virtual environment. This is likely why you might see "outdated" packages or missing ones:
1. Go to **Settings** (or **Settings...** on macOS).
2. Navigate to **Project: _BC_scrape_dawg_5000** > **Python Interpreter**.
3. Click **Add Interpreter** > **Add Local Interpreter...**.
4. Select **Existing** and point it to `./.venv/bin/python` (inside your project folder).

---

## 🔄 Keeping Everything Up to Date

To check for newer versions of your installed packages and update them, use these commands in your terminal (make sure your `.venv` is activated):

### 1. Check for Outdated Packages
```bash
pip list --outdated
```

### 2. Update All Packages to Latest
You can update everything in your `requirements.txt` at once:
```bash
pip install -U -r requirements.txt
```

### 3. Update a Specific Package
```bash
pip install --upgrade [package-name]
# Example: pip install --upgrade playwright
```

### 4. Update Playwright Browsers
Occasionally, Playwright updates its browser engines. Run this after updating the `playwright` package:
```bash
playwright install
```

### Web Scraping Ethics
- Always check a website's `robots.txt` before scraping.
- Don't spam requests; be respectful to the server's resources.

Happy Scraping! 🕸️
