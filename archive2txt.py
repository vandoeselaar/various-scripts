import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_and_save_links(url, root_url, file_extension, visited=None, indent=0, output_file="output.txt"):
    if visited is None:
        visited = set()

    if url in visited:
        return  # Avoid repetitions

    visited.add(url)  # Mark this URL as visited
    print("  " * indent + f"[{url}]")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links on the page
        links = soup.find_all("a", href=True)

        with open(output_file, "a") as f:  # Open output.txt in append mode
            for link in links:
                href = link['href']
                # Create a full URL from the link
                full_url = urljoin(url, href)

                if full_url.startswith(root_url):
                    # Check for file extension and save to output.txt
                    if full_url.endswith(file_extension):
                        print("  " * (indent + 1) + f"File found: {full_url}")
                        f.write(full_url + "\n")

                    # Recursively go to subdirectories
                    if href.endswith("/"):
                        find_and_save_links(full_url, root_url, file_extension, visited, indent + 1, output_file)
    except Exception as e:
        print("  " * indent + f"Error: {e}")

# Base URL and file extension
base_url = "https://archive.org/download/*********/"
file_extension = ".7z"  # Change the extension to the one you're looking for (e.g., ".iso")

# Clear the output file if it exists
with open("output.txt", "w") as f:
    f.write("")  # Empty the file to remove old results

# Start the process
print(f"Searching for '{file_extension}' files in the directory structure:")
find_and_save_links(base_url, base_url, file_extension)
