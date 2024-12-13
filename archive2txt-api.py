import requests

def fetch_files_from_archive(base_url, file_extension, output_file="output.txt"):
    identifier = base_url.split("/")[-1]  # Haal de ID van de collectie uit de URL
    api_url = f"https://archive.org/metadata/{identifier}"  # Metadata API
    
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    
    with open(output_file, "w") as f:
        for file in data.get("files", []):
            if file.get("name", "").endswith(file_extension):
                file_url = f"https://archive.org/download/{identifier}/{file['name']}"
                print(f"Found: {file_url}")
                f.write(file_url + "\n")

# Gebruik de functie
base_url = "https://archive.org/download/***"
file_extension = ".7z"
output_file = "output.txt"
fetch_files_from_archive(base_url, file_extension, output_file)
