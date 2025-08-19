import requests

def security_scan(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return

    print(f"🔎 Security Scan for: {url}\n")

    # Check HTTPS
    if url.startswith("https://"):
        print("✅ HTTPS is enabled")
    else:
        print("⚠️ Website is not using HTTPS")

    # Check for important security headers
    required_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Referrer-Policy"
    ]

    for h in required_headers:
        if h in headers:
            print(f"✅ {h}: {headers[h]}")
        else:
            print(f"⚠️ {h} is missing")

# Example usage
security_scan("https://example.com")
