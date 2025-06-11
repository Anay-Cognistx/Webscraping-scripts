from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import os
import re



scraper_utils_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "square-ds", "resources", "scraper", "utils")
)
sys.path.insert(0, scraper_utils_dir)

from scraper_utils import save_url_as_txt, save_text_to_file


#Basic setup 
chrome_options = Options()
chrome_options.add_argument("--headless=new") #disables gui, unnecessary
chrome_options.add_argument("--no-sandbox") #bypasses security
driver = webdriver.Chrome(options=chrome_options) #launches chrome to driver

url = "https://flypittsburgh.com/pittsburgh-international-airport/parking/#parking-options"
driver.get(url)

#Using existing implementation

save_url_as_txt(url, output_dir="output")



time.sleep(3) # Not sure if htis is right, just looking at example


#use readibility.js here, basically executes js script
driver.execute_script("""
    if (!window.readabilityScriptInjected) {
        window.readabilityScriptInjected = true;
        let script = document.createElement('script');
        script.src = 'https://unpkg.com/@mozilla/readability@0.4.4/Readability.js';
        script.type = 'text/javascript';
        document.head.appendChild(script);
    }
""")


time.sleep(3) # Again, not sure if this is needed

#Actual script
article = driver.execute_script("""
    const article = new Readability(document).parse();
    return article ? article.textContent : "No readable content found.";
""")

def clean_lines(text: str) -> str:
    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(cleaned_lines)

article = clean_lines(article)

save_text_to_file(article, "readibility", output_dir="output")

driver.quit()
