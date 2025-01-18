Here's a description you can use for your GitHub repository:

---

## **Zoom Subdomain Archive URL Fetcher**

This Python script retrieves archived URLs for a specified **subdomain** of the **zoom.us** domain from the **Wayback Machine**. It fetches all available archived URLs and **filters** them based on the presence of a `pwd=` parameter in the query string.

### **Features**:
- **Fetch Archived URLs**: Retrieves a list of archived URLs for any subdomain under `zoom.us` (e.g., `test.zoom.us`, `abc.zoom.us`).
- **Filter by `pwd=`**: Filters and displays only those URLs that contain the `pwd=` parameter, which is often used for Zoom meeting links requiring a password.
- **Custom Subdomain Input**: Allows you to input any subdomain to retrieve its archived URLs.
- **Wayback Machine Integration**: Uses the Wayback Machine's **CDX API** to fetch historical snapshots of the specified subdomain.

### **Usage**:
1. Clone this repository.
2. Install the required dependencies with:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python fetch_pwd_urls.py
   ```
4. Enter the desired subdomain when prompted (e.g., `test` for `test.zoom.us`).
5. The script will display all archived URLs containing the `pwd=` parameter.

### **Example**:
If you input the subdomain `abc`, the script will return a list of archived URLs like:
```
https://web.archive.org/web/20230101010101/https://abc.zoom.us/j/1234567890?pwd=abcd1234
```

### **Contributing**:
Feel free to open issues or pull requests if you'd like to contribute to the project. Bug fixes, feature suggestions, or improvements are always welcome!

---

Feel free to modify this description as needed! It covers all the essential aspects of the script and provides a good starting point for your GitHub repository.
