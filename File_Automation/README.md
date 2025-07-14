# 🗂️ File Automation Tool (Python + Watchdog)

This project automates the organization of downloaded files by **monitoring a folder in real-time** and **moving files to specific directories based on their extensions**.

---

## ⚙️ How It Works

- Monitors a source folder (e.g., `Downloads`) using the `watchdog` library.
- When a new file is created, it checks the file's extension and moves it to the appropriate destination folder.
- Uses a `mapping.json` configuration file to define where each file type should be moved.

---


## 🧩 Template Configuration (`mapping.json`)

The `mapping.json` file contains:

- `watch_folder`: the folder to monitor
- `mappings`: the destination folder for each file extension

Example:

```json
{
  "watch_folder": "D:\\Downloads",
  "mappings": {
    ".torrent": "D:\\Rar\\Torrent",
    ".png": "D:\\Wallpapers",
    ".jpg": "D:\\Wallpapers",
    ".rar": "D:\\Rar",
    ".zip": "D:\\Rar",
    ".exe": "D:\\Setups",
    "default": "D:\\Rar"
  }
}
```
---
## 🚀 How to Use

1. **Run the executable:**  
   Navigate to `Executable/dist/FileSorter.exe` and launch the application.

2. **Configure the JSON file:**  
   - Either rename `mapping_template.json` to `mapping.json`, or  
   - Create your own `mapping.json` file using the provided format.

3. **(Optional) Add the EXE to startup:**  
   To enable the automation on every boot, add `FileSorter.exe` to Windows startup.

4. **(Alternative) Run the Python script directly:**  
   - Make sure Python is installed.  
   - Install dependencies with `pip install watchdog`.  
   - Run `file_sorter.py`.
"""