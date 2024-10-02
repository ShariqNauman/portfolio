import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def scrape_website(website):
    logger.info('Connecting to Scraping Browser...')
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(website)
        logger.info('Connected! Navigating...')
        logger.info('Navigated! Scraping page content...')
        html = driver.page_source
        time.sleep(10)
        return html
    except Exception as e:
        logger.error(f"Error scraping website: {e}")
        return None

def extract_body_content(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]

