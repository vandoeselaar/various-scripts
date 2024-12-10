import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_and_save_links(url, root_url, file_extension, visited=None, indent=0, output_file="output.txt"):
    if visited is None:
        visited = set()

    if url in visited:
        return  # Vermijd herhalingen

    visited.add(url)  # Markeer deze URL als bezocht
    print("  " * indent + f"[{url}]")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Controleer of de aanvraag succesvol was
        soup = BeautifulSoup(response.text, "html.parser")

        # Alle links op de pagina vinden
        links = soup.find_all("a", href=True)

        with open(output_file, "a") as f:  # Open output.txt in append-modus
            for link in links:
                href = link['href']
                # Maak een volledige URL van de link
                full_url = urljoin(url, href)

                if full_url.startswith(root_url):
                    # Controleer op bestandsextensie en sla op in output.txt
                    if full_url.endswith(file_extension):
                        print("  " * (indent + 1) + f"Bestand gevonden: {full_url}")
                        f.write(full_url + "\n")

                    # Recursief doorgaan naar subdirectories
                    if href.endswith("/"):
                        find_and_save_links(full_url, root_url, file_extension, visited, indent + 1, output_file)
    except Exception as e:
        print("  " * indent + f"Fout: {e}")

# Basis-URL en bestandsextensie
base_url = "https://archive.org/download/*********/"
file_extension = ".7z"  # Pas de extensie aan naar wat je zoekt (bijvoorbeeld ".iso")

# Outputbestand wissen als het al bestaat
with open("output.txt", "w") as f:
    f.write("")  # Leeg bestand om oude resultaten te verwijderen

# Start het proces
print(f"Zoeken naar '{file_extension}' bestanden in de directorystructuur:")
find_and_save_links(base_url, base_url, file_extension)
