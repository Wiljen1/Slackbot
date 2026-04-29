from services.graph import list_files, get_file_content
import os


def get_documents(query):
    folder = os.getenv("ONEDRIVE_FOLDER_PATH")
    files = list_files(folder)

    results = []

    for f in files:
        file_id = f.get("id")
        name = f.get("name")

        content = get_file_content(file_id)

        if query.lower() in content.lower():
            snippet = content[:500]
            results.append(f"{name}: {snippet}")

    return results
