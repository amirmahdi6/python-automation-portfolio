
import requests
import bs4
import time
from urllib.parse import urljoin, urlparse

url = 'https://automatetheboringstuff.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (link checker script)'
}

res = requests.get(url, headers=headers, timeout=10)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('a')

seen = set()

for link in link_elems:
    href = link.get('href')

    if not href:
        continue

    # Convert relative URLs to absolute URLs.
    full_url = urljoin(url, href)

    # Only check HTTP and HTTPS links.
    parsed = urlparse(full_url)
    if parsed.scheme not in ('http', 'https'):
        continue

    # Skip duplicate URLs.
    if full_url in seen:
        continue

    seen.add(full_url)

    try:
        # HEAD is lighter than GET.
        link_res = requests.head(
            full_url,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )

        # Some servers don't support HEAD correctly.
        if link_res.status_code in (405, 403):
            link_res = requests.get(
                full_url,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )

        if link_res.status_code >= 400:
            print(f'Broken ({link_res.status_code}): {full_url}')
        else:
            print(f'OK ({link_res.status_code}): {full_url}')

    except requests.RequestException as e:
        print(f'Could not access: {full_url} — {e}')

    # Avoid sending requests too quickly.
    time.sleep(0.5)
