def organize_files_by_type(file_list):
    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "videos": [".mp4", ".mov", ".avi", ".mkv"],
        "documents": [".pdf", ".docx", ".txt", ".xlsx"]
    }
    folders_created = set()
    for file in file_list:
        file_lower = file.lower()
        moved = False
        for folder, extensions in file_types.items():
            if any(file_lower.endswith(ext) for ext in extensions):
                if folder not in folders_created:
                    print(f"Simulating: Creating folder '{folder}'")
                    folders_created.add(folder)
                print(f"Simulating: Moving '{file}' to '{folder}/'")
                moved = True
                break
        if not moved:
            if "others" not in folders_created:
                print("Simulating: Creating folder 'others'")
                folders_created.add("others")
            print(f"Simulating: Moving '{file}' to 'others/'")

files = [
    "summer_vacation.jpg",
    "project_proposal.pdf",
    "family_video.mp4",
    "notes.txt",
    "logo.png",
    "meeting_recording.mov",
    "budget.xlsx",
    "unknown_file.xyz"
]

organize_files_by_type(files)
