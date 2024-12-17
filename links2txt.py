import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links_with_extension(url, extension):
    # Send a GET request to the given URL
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching the page: {response.status_code}")
        return []

    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a', href=True)

    # Filter the links that end with the specified extension
    filtered_links = [link['href'] for link in links if link['href'].endswith(extension)]

    # Make the links complete (absolute URLs) by adding the base URL
    full_links = [urljoin(url, link) for link in filtered_links]

    return full_links

def save_links_to_file(links, filename):
    # Save the found links to a file
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')
    print(f"Links have been saved to {filename}")

def main():
    # Ask the user for a URL and an extension
    url = input("Enter the URL: ")
    extension = input("Enter the extension (e.g., .zip): ")

    # Get the links with the specified extension
    links = get_links_with_extension(url, extension)

    if links:
        # Save the links to output.txt
        save_links_to_file(links, 'output.txt')
    else:
        print(f"No links found with the extension {extension}.")

if __name__ == '__main__':
    main()
