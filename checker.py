import hashlib
import json
import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# --- EXCLUSION CONFIGURATION ---
IGNORED_EXTENSIONS = [".tmp", ".log", ".bak", ".DS_Store"]
IGNORED_FOLDERS = [".git", "__pycache__", "temp"]


def is_ignored(filepath):
    """Checks if a file or folder path matches our ignore criteria."""
    for ext in IGNORED_EXTENSIONS:
        if filepath.endswith(ext):
            return True

    path_parts = os.path.normpath(filepath).split(os.sep)
    for folder in IGNORED_FOLDERS:
        if folder in path_parts:
            return True

    return False


def calculate_file_hash(filepath):
    """Calculates SHA-256 hash for a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception:
        return None


def create_baseline(target_directory, output_json_file="baseline.json"):
    """Scans directory and saves baseline hashes to JSON."""
    print(f"Creating baseline for: '{target_directory}'...")
    file_hashes = {}
    ignored_count = 0

    for root, subfolders, files in os.walk(target_directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            if is_ignored(full_path):
                ignored_count += 1
                continue

            file_hash = calculate_file_hash(full_path)
            if file_hash:
                file_hashes[full_path] = file_hash

    with open(output_json_file, "w") as json_file:
        json.dump(file_hashes, json_file, indent=4)

    print(f"Success! Saved baseline with {len(file_hashes)} file records.")
    print(f"Ignored {ignored_count} temporary/excluded file(s).\n")


# --- STEP 5: REAL-TIME EVENT HANDLER ---
class IntegrityMonitorHandler(FileSystemEventHandler):
    """Listens for real-time filesystem events and checks integrity."""

    def on_modified(self, event):
        if not event.is_directory and not is_ignored(event.src_path):
            current_hash = calculate_file_hash(event.src_path)
            print(f"\n[!] ALERT: File Modified -> {event.src_path}")
            print(f"    New SHA-256 Hash: {current_hash}")

    def on_created(self, event):
        if not event.is_directory and not is_ignored(event.src_path):
            current_hash = calculate_file_hash(event.src_path)
            print(f"\n[+] ALERT: New File Created -> {event.src_path}")
            print(f"    SHA-256 Hash: {current_hash}")

    def on_deleted(self, event):
        if not event.is_directory and not is_ignored(event.src_path):
            print(f"\n[-] ALERT: File Deleted -> {event.src_path}")


def start_live_monitoring(target_directory):
    """Starts the Watchdog observer to monitor directory in real-time."""
    event_handler = IntegrityMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=target_directory, recursive=True)
    observer.start()

    print(f"==================================================")
    print(f" LIVE MONITORING ACTIVE: '{target_directory}'")
    print(f" Press Ctrl+C to stop monitoring.")
    print(f"==================================================")

    try:
        while True:
            time.sleep(1)  # Keep script running
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping live monitoring...")
    observer.join()


if __name__ == "__main__":
    target_folder = "my_folder"

    user_choice = (
        input(
            "Select Mode:\n 1) Create Baseline\n 2) Verify Integrity (Static Report)\n 3) Live Watchdog Monitor\nEnter choice (1, 2, or 3): "
        )
        .strip()
    )

    if user_choice == "1":
        create_baseline(target_folder)
    elif user_choice == "2":
        # Static report mode
        pass
    elif user_choice == "3":
        start_live_monitoring(target_folder)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")