import requests

def fetch_archived_urls(subdomain):
    domain = "zoom.us"  # Constant domain
    full_url = f"{subdomain}.{domain}"  # Construct the full URL (subdomain.zoom.us)

    # Wayback Machine CDX API URL
    cdx_api_url = "https://web.archive.org/cdx/search/cdx"
    
    # Query parameters
    params = {
        "url": f"{full_url}/*",  # Use wildcard to get all URLs under the subdomain
        "output": "json",        # Format the response as JSON
        "limit": "10000"         # Limit the number of results (optional)
    }

    # Send the request to the Wayback Machine API
    response = requests.get(cdx_api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Check if there are any results
        if len(data) > 1:
            # Skip the header row (first element)
            archived_urls = data[1:]

            # Filter and display URLs containing 'pwd='
            print(f"Archived URLs for {full_url} containing 'pwd=':\n")
            for entry in archived_urls:
                timestamp = entry[1]  # Timestamp of the snapshot
                url = entry[2]        # URL of the snapshot
                if 'pwd=' in url:     # Check if 'pwd=' exists in the URL
                    print(f"{url} (Captured on: {timestamp})")
        else:
            print(f"No archived versions found for {full_url}.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Get user input for the subdomain
subdomain = input("Enter the subdomain (e.g., 'test' for test.zoom.us): ")

# Fetch and display the list of archived URLs containing 'pwd=' for the given subdomain
fetch_archived_urls(subdomain)
