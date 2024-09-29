import httpx
from bs4 import BeautifulSoup
import spacy

# Initialize spaCy NLP model
nlp = spacy.load('en_core_web_sm')

async def fetch_link_preview(url):
    """Fetches the title and description from a given URL using httpx asynchronously."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').get_text() if soup.find('title') else 'No Title'
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No Description'
            return title, description
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {url}: {exc}")
            return 'No Title', 'No Description'
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {url}")
            return 'No Title', 'No Description'


def classify_topic(text):
    """Classifies the topic of a given text (usually title + description)."""
    if not text:
        return ['general']
    
    doc = nlp(text)
    keywords = [chunk.text.strip() for chunk in doc.noun_chunks if chunk.text.strip()]
    
    return keywords if keywords else ['general']