
import os
import shutil
import logging
from pathlib import Path

# Logging configuration
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File extension mapping
EXTENSION_MAP = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".svg": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".jsx": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".json": "Code",
    ".sql": "Code",
}


def get_unique_path(destination):
    """Generate a unique filename if a duplicate exists."""
    destination = Path(destination)

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )
        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_directory(source_directory):
    source = Path(source_directory).expanduser().resolve()

    if not source.is_dir():
        print("Error: Directory does not exist.")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0

    print(f"\nOrganizing directory: {source}\n")

    try:
        # Inspect entries in the source directory
        with os.scandir(source) as entries:
            for entry in entries:

                # Process files only, not subdirectories
                if not entry.is_file(follow_symlinks=False):
                    continue

                file_path = Path(entry.path)

                # Determine category from file extension
                extension = file_path.suffix.lower()
                category = EXTENSION_MAP.get(
                    extension, "Others"
                )

                destination_folder = source / category

                try:
                    # Create category folder if needed
                    destination_folder.mkdir(
                        parents=True, exist_ok=True
                    )

                    # Prevent moving a file onto itself
                    if file_path.parent == destination_folder:
                        skipped_count += 1
                        continue

                    destination = get_unique_path(
                        destination_folder / file_path.name
                    )

                    shutil.move(
                        str(file_path),
                        str(destination)
                    )

                    moved_count += 1
                    logging.info(
                        "Moved %s -> %s",
                        file_path,
                        destination
                    )

                    print(
                        f"[MOVED] {file_path.name} "
                        f"-> {category}/{destination.name}"
                    )

                except PermissionError as error:
                    error_count += 1
                    logging.error(
                        "Permission denied for %s: %s",
                        file_path, error
                    )
                    print(f"[PERMISSION DENIED] {file_path.name}")

                except OSError as error:
                    error_count += 1
                    logging.error(
                        "Could not move %s: %s",
                        file_path, error
                    )
                    print(f"[ERROR] {file_path.name}: {error}")

    except PermissionError as error:
        error_count += 1
        logging.error("Cannot access directory %s: %s", source, error)
        print(f"Cannot access directory: {error}")

    # Execution summary
    print("\n" + "=" * 40)
    print("       ORGANIZATION SUMMARY")
    print("=" * 40)
    print(f"Files moved successfully : {moved_count}")
    print(f"Files skipped            : {skipped_count}")
    print(f"Errors                   : {error_count}")
    print(f"Log file                 : organizer.log")
    print("=" * 40)


if __name__ == "__main__":
    folder = input(
        "Enter directory path to organize: "
    ).strip().strip('"')

    organize_directory(folder)
