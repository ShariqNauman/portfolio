from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

template = (
    """
    You are tasked with extracting specific information from the following text content: {dom_content}. 
    Please follow these instructions carefully:

    1. Extract Information: Extract the information that matches the provided description: {parse_description}.
    2. Mixed Format: Your response can include both text and tables as needed.
    3. Table Format: When presenting lists or tabular data, use Markdown tables with | characters. Include a header row and a separator row.
    4. Text Formatting: Use Markdown formatting for text sections to improve readability (e.g., headers, bold, italic).
    5. No Extra Content: Do not include any additional explanations or comments outside of the extracted information.
    6. Empty Response: If no information matches the description, return an empty string ('').
    """
)

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def parse_chunk(chunk, parse_description):
    try:
        return chain.invoke({"dom_content": chunk, "parse_description": parse_description})
    except Exception as e:
        logger.error(f"Error parsing chunk: {e}")
        return ""

def parse_with_ollama(dom_chunks, parse_description):
    parsed_results = []
    total_chunks = len(dom_chunks)

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_chunk = {executor.submit(parse_chunk, chunk, parse_description): i 
                           for i, chunk in enumerate(dom_chunks, start=1)}
        
        for future in as_completed(future_to_chunk):
            chunk_index = future_to_chunk[future]
            try:
                result = future.result()
                parsed_results.append(result)
                logger.info(f"Parsed batch: {chunk_index} of {total_chunks}")
            except Exception as e:
                logger.error(f"Error processing chunk {chunk_index}: {e}")

    return "\n".join(parsed_results)