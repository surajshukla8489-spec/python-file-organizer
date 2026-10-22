# 🗂️ Python File Organizer

A simple and efficient Python automation tool that organizes cluttered directories by automatically moving files into category-based folders according to their file extensions.

## 📌 Project Overview

The **Python File Organizer** helps users keep their directories clean and organized. It scans files in a selected directory, identifies their extensions, creates appropriate category folders, and moves files to their respective locations.

The project also includes duplicate filename protection, exception handling, logging, and an execution summary.

## ✨ Features

- **Automatic File Organization:** Sorts files based on their extensions.
- **Category-Based Folders:** Creates folders such as Documents, Images, Videos, Archives, Code, and Others.
- **Duplicate Filename Protection:** Renames duplicate files instead of overwriting existing files.
- **Exception Handling:** Handles permission and file operation errors.
- **Logging:** Records file operations and errors in `organizer.log`.
- **Execution Summary:** Displays the number of successfully moved files, skipped files, and errors.
- **User-Defined Directory:** Allows users to enter the directory they want to organize.

## 🛠️ Technologies Used

- Python 3
- `os`
- `shutil`
- `pathlib`
- `logging`

## 📁 Project Structure

```text
file_organizer/
│
├── organizer.py
├── README.md
└── organizer.log
```

`organizer.log` is generated when the script records its operations.

## 📂 File Categories

| File Extensions | Destination Folder |
|---|---|
| `.pdf`, `.docx`, `.txt`, `.xlsx