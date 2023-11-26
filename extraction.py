import requests
from bs4 import BeautifulSoup

# Replace 'url_to_scrape' with the URL of the site you want to scrape
url_to_scrape = "https://www.forebet.com/en/predictions-tips-burnley-west-ham-1920239"
# Send an HTTP GET request to the URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url_to_scrape, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <div> elements with class "st_rescnt"
    st_rescnt_divs = soup.find_all('div', class_='st_rescnt')

    # Initialize a list to store the extracted <span> elements
    extracted_spans = []

    # Iterate through the <div> elements and extract <span> elements with class "st_res lscrsp"
    for div in st_rescnt_divs:
        spans = div.find_all('span', class_='st_res lscrsp')
        extracted_spans.extend(spans)

    # Create or open a text file for writing
    with open('manliv_data.txt', 'w', encoding='utf-8') as file:
        # Write the text content of the extracted <span> elements to the file
        for span in extracted_spans:
            file.write(span.text + '\n')

    print("Data extracted and saved to 'manliv.txt' successfully!")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
