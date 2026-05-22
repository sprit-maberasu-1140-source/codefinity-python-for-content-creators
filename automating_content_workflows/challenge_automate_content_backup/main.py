def simulate_backup(content_structure, source_path, backup_path):
    for name, value in content_structure.items():
        current_source = f"{source_path}/{name}"
        current_backup = f"{backup_path}/{name}"
        if isinstance(value, dict):
            print(f"Would create directory: {current_backup}")
            # TODO: Recursively call simulate_backup for subdirectories
            simulate_backup(value,current_source,current_backup)
        else:
            action = f"Would copy file: {current_source} to {current_backup}"
            print(action)

# Sample hardcoded content folder structure
content_folder = {
    "images": {
        "photo1.jpg": None,
        "photo2.png": None,
        "subfolder": {
            "photo3.gif": None
        }
    },
    "videos": {
        "video1.mp4": None
    },
    "docs": {
        "script.txt": None
    }
}

simulate_backup(content_folder, "/content", "/backup")
