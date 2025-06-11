<h1>Webscraping Alternatives for RAG LLM</h1>

<h2>Current Implementation</h2>
- Takes screenshots of webpage
- Uses OCR (Optical character recognition) on PDFs

However, for dropdown elements and others, this method can yield inconsistent results.

<h2>New Implementation</h2>
- Leverages Firefox browser's accessibility mode through a js library called "readibility"
- Extracts text from the accessibility mode in a cleaner and summarized format
- Overall simpler and less computationally expensive


Comparison on URL: https://flypittsburgh.com/pittsburgh-international-airport/parking/#parking-options
