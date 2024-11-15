"""""from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def web_scraping_veg_fruits(url, vegetable_name=""):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'customers'})
    
    vegetable_details = []
    for row in table.find_all('tr')[1:]:  # skip the header row
        columns = row.find_all(['th', 'td'])
        vegetable_name = columns[0].text.strip()
        unit = columns[1].text.strip()
        market_price = columns[2].text.strip()
        retail_price_range = columns[3].text.strip()
        mall_price_range = columns[4].text.strip()

        vegetable_details.append({
            'name': vegetable_name,
            'unit': unit,
            'marketPrice': market_price,
            'retailPriceRange': retail_price_range,
            'mallPriceRange': mall_price_range
        })

    '''table_rows = soup.select('.Table .Row')
    print(table_rows)
    for row in table_rows:
        columns = row.select('.Cell')
        name = columns[0].text.strip()
        unit = columns[1].text.strip()
        market_price = columns[2].text.strip()
        retail_price_range = columns[3].text.strip()
        mall_price_range = columns[4].text.strip()

        if vegetable_name.lower() in name.lower():
            vegetable_details.append({
                'name': name,
                'unit': unit,
                'marketPrice': market_price,
                'retailPriceRange': retail_price_range,
                'mallPriceRange': mall_price_range
            })'''

    return vegetable_details


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/reqVeg', methods=['GET'])
def reqVeg():
    url = 'https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price'
    vegetable_prices = web_scraping_veg_fruits(url)
    json_vegetable_prices = jsonify(vegetable_prices)
    return json_vegetable_prices


@app.route('/reqFruit', methods=['GET'])
def reqFruit():
    url = 'https://market.todaypricerates.com/Andhra-Pradesh-fruits-price'
    fruits_prices = web_scraping_veg_fruits(url)
    json_fruit_prices = jsonify(fruits_prices)
    return json_fruit_prices


if __name__ == '__main__':
    app.run(debug=True)  """""

'''''

from flask import Flask, jsonify, request, render_template
import pdfplumber
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Function to read and extract text from the PDF
def read_pdf(pdf_path):
    extracted_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text
        return extracted_text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Refined function to find answers from the PDF content
def find_answer_in_pdf(query, pdf_content):
    query_lower = query.lower().strip()
    pdf_content_lower = pdf_content.lower().strip()

    # Improved logic to find partial matches
    if query_lower in pdf_content_lower:
        start_idx = pdf_content_lower.find(query_lower)
        snippet = pdf_content[start_idx:start_idx + 300]  # Return a snippet around the answer
        return snippet
    else:
        # Try a partial match (split the query into words and check each one)
        query_words = query_lower.split()
        for word in query_words:
            if word in pdf_content_lower:
                start_idx = pdf_content_lower.find(word)
                snippet = pdf_content[start_idx:start_idx + 300]
                return snippet
        return "Sorry, no relevant information found in the PDF. Please ask about a judge's name, appointment date, or retirement date."

# API route to handle PDF-related queries
@app.route('/pdf-query', methods=['POST'])
def pdf_query():
    data = request.get_json()
    user_query = data.get('query', '')

    # Path to your PDF (change this to the actual path)
    pdf_path = r"C:\\Users\\krish\\Downloads\\NyayaBot\\supreme_court_judgeslist.pdf"
    
    # Read the PDF and find the answer
    pdf_content = read_pdf(pdf_path)
    if "Error" in pdf_content:
        return jsonify({"answer": pdf_content})

    answer = find_answer_in_pdf(user_query, pdf_content)
    return jsonify({"answer": answer})

# Scraping logic for the Department of Justice data
def web_scraping_doj(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting main content based on the provided HTML structure
    content = []
    
    # Find the div with id='row-content'
    main_content_div = soup.find('div', id='row-content')
    
    # If the main content is not found in the above div, try other approaches
    if not main_content_div:
        main_content_div = soup.find('div', class_='container')  # Update this if necessary

    if main_content_div:
        # Extract all text from the found div
        text = main_content_div.get_text(strip=True, separator='\n')
        if text:
            content.append(text)
    
    return {
        'content': content
    }

# Route for the homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route to get DOJ data
@app.route('/aboutDOJ', methods=['GET'])
def aboutDOJ():
    url = 'https://doj.gov.in/about-department/'
    about_dep = web_scraping_doj(url)
    return jsonify(about_dep)

if __name__ == '__main__':
    app.run(debug=True)
'''''

"""""from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def web_scraping_veg_fruits(url, vegetable_name=""):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'customers'})
    
    vegetable_details = []
    for row in table.find_all('tr')[1:]:  # skip the header row
        columns = row.find_all(['th', 'td'])
        vegetable_name = columns[0].text.strip()
        unit = columns[1].text.strip()
        market_price = columns[2].text.strip()
        retail_price_range = columns[3].text.strip()
        mall_price_range = columns[4].text.strip()

        vegetable_details.append({
            'name': vegetable_name,
            'unit': unit,
            'marketPrice': market_price,
            'retailPriceRange': retail_price_range,
            'mallPriceRange': mall_price_range
        })

    '''table_rows = soup.select('.Table .Row')
    print(table_rows)
    for row in table_rows:
        columns = row.select('.Cell')
        name = columns[0].text.strip()
        unit = columns[1].text.strip()
        market_price = columns[2].text.strip()
        retail_price_range = columns[3].text.strip()
        mall_price_range = columns[4].text.strip()

        if vegetable_name.lower() in name.lower():
            vegetable_details.append({
                'name': name,
                'unit': unit,
                'marketPrice': market_price,
                'retailPriceRange': retail_price_range,
                'mallPriceRange': mall_price_range
            })'''

    return vegetable_details


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/reqVeg', methods=['GET'])
def reqVeg():
    url = 'https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price'
    vegetable_prices = web_scraping_veg_fruits(url)
    json_vegetable_prices = jsonify(vegetable_prices)
    return json_vegetable_prices


@app.route('/reqFruit', methods=['GET'])
def reqFruit():
    url = 'https://market.todaypricerates.com/Andhra-Pradesh-fruits-price'
    fruits_prices = web_scraping_veg_fruits(url)
    json_fruit_prices = jsonify(fruits_prices)
    return json_fruit_prices


if __name__ == '__main__':
    app.run(debug=True)  """""

'''''

from flask import Flask, jsonify, request, render_template
import pdfplumber
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Function to read and extract text from the PDF
def read_pdf(pdf_path):
    extracted_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text
        return extracted_text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Refined function to find answers from the PDF content
def find_answer_in_pdf(query, pdf_content):
    query_lower = query.lower().strip()
    pdf_content_lower = pdf_content.lower().strip()

    # Improved logic to find partial matches
    if query_lower in pdf_content_lower:
        start_idx = pdf_content_lower.find(query_lower)
        snippet = pdf_content[start_idx:start_idx + 300]  # Return a snippet around the answer
        return snippet
    else:
        # Try a partial match (split the query into words and check each one)
        query_words = query_lower.split()
        for word in query_words:
            if word in pdf_content_lower:
                start_idx = pdf_content_lower.find(word)
                snippet = pdf_content[start_idx:start_idx + 300]
                return snippet
        return "Sorry, no relevant information found in the PDF. Please ask about a judge's name, appointment date, or retirement date."

# API route to handle PDF-related queries
@app.route('/pdf-query', methods=['POST'])
def pdf_query():
    data = request.get_json()
    user_query = data.get('query', '')

    # Path to your PDF (change this to the actual path)
    pdf_path = r"C:\\Users\\krish\\Downloads\\NyayaBot\\supreme_court_judgeslist.pdf"
    
    # Read the PDF and find the answer
    pdf_content = read_pdf(pdf_path)
    if "Error" in pdf_content:
        return jsonify({"answer": pdf_content})

    answer = find_answer_in_pdf(user_query, pdf_content)
    return jsonify({"answer": answer})

# Scraping logic for the Department of Justice data
def web_scraping_doj(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting main content based on the provided HTML structure
    content = []
    
    # Find the div with id='row-content'
    main_content_div = soup.find('div', id='row-content')
    
    # If the main content is not found in the above div, try other approaches
    if not main_content_div:
        main_content_div = soup.find('div', class_='container')  # Update this if necessary

    if main_content_div:
        # Extract all text from the found div
        text = main_content_div.get_text(strip=True, separator='\n')
        if text:
            content.append(text)
    
    return {
        'content': content
    }

# Route for the homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route to get DOJ data
@app.route('/aboutDOJ', methods=['GET'])
def aboutDOJ():
    url = 'https://doj.gov.in/about-department/'
    about_dep = web_scraping_doj(url)
    return jsonify(about_dep)

if __name__ == '__main__':
    app.run(debug=True)
'''''

from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_about_dept(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    content = []
    main_content_div = soup.find('div', id='row-content')
    
    if main_content_div:
        text = main_content_div.get_text(strip=True, separator='\n')
        if text:
            content.append(text)
    
    return {'content': content}

def scrape_functions_dept(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    content = []
    main_content_div = soup.find('div', id='row-content')
    
    if main_content_div:
        ordered_list = main_content_div.find('ol')
        if ordered_list:
            list_items = ordered_list.find_all('li')
            for item in list_items:
                content.append(item.get_text(strip=True))
    
    return {'content': content}
def scrape_tele_law(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    content = []
    
    # Find the main content area
    container_div = soup.find('div', class_='container')
    if container_div:
        # Extract text from paragraphs and headers within the main content area
        paragraphs = container_div.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:
                content.append(text)
                
        headers = container_div.find_all(['h1', 'h3'])
        for header in headers:
            text = header.get_text(strip=True)
            if text:
                content.append(text)
    
    return {'content': content}



def scrape_njdg(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    content = []
    
    # Find the container with id='row-content'
    container_div = soup.find('div', class_='container', id='row-content')
    
    if container_div:
        # Extract text from the paragraphs and any other relevant tags
        paragraphs = container_div.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:
                content.append(text)
                
        # Additionally, extract text from any 'h1' tags if they are relevant
        headers = container_div.find_all('h1')
        for header in headers:
            text = header.get_text(strip=True)
            if text:
                content.append(text)
    
    return {'content': content}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutDOJ', methods=['GET'])
def aboutDOJ():
    url = 'https://doj.gov.in/about-department/'
    about_dep = scrape_about_dept(url)
    return jsonify(about_dep)

@app.route('/functions-of-doj', methods=['GET'])
def functions_of_doj():
    url = 'https://doj.gov.in/about-department/function-of-department/'
    functions_dep = scrape_functions_dept(url)
    return jsonify(functions_dep)

@app.route('/tele-law', methods=['GET'])
def tele_law():
    url = 'https://doj.gov.in/tele-law-about/'  # Update the URL as needed
    tele_law_data = scrape_tele_law(url)
    return jsonify(tele_law_data)


@app.route('/njdg', methods=['GET'])
def nydg():
    url = 'https://doj.gov.in/the-national-judicial-data-grid-njdg/'
    nydg_data = scrape_njdg(url)
    return jsonify(nydg_data)

if __name__ == '__main__':
    app.run(debug=True)

















