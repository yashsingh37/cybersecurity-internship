import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raise error for bad status
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract links
    links = [a['href'] for a in soup.find_all('a', href=True)]
    # Extract forms
    forms = [str(form) for form in soup.find_all('form')]

    # Save to file
    with open("crawl_results.txt", "w", encoding="utf-8") as f:
        f.write(f"🔗 Links found on {url}:\n")
        f.write("\n".join(links))
        f.write("\n\n📝 Forms found:\n")
        f.write("\n".join(forms))

    print(f"✅ Crawl completed. Results saved in crawl_results.txt")

# Example usage
crawl_website("http://example.com")
