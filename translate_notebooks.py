import nbformat
import os
import requests
import json
import time  # For rate limiting
import logging  # For logging errors and debugging
from ratelimit import limits, sleep_and_retry  # For rate limiting

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Qwen API Configuration ---
QWEN_API_ENDPOINT = "YOUR_QWEN_API_ENDPOINT"  # Replace with the actual endpoint
QWEN_API_RATE_LIMIT_CALLS = 10  # Example: 10 calls
QWEN_API_RATE_LIMIT_PERIOD = 60  # Example: 60 seconds

@sleep_and_retry
@limits(calls=QWEN_API_RATE_LIMIT_CALLS, period=QWEN_API_RATE_LIMIT_PERIOD)
def translate_text(text, api_key):
    """Translates text using the Qwen API with rate limiting and error handling."""
    if not text:
        return ""  # Handle empty text gracefully

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "text": text,
            "target_language": "zh"  # Chinese
        }

        response = requests.post(QWEN_API_ENDPOINT, headers=headers, data=json.dumps(data), timeout=10)  # Add timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        result = response.json()

        if "translated_text" in result:
            return result["translated_text"]
        else:
            logging.warning(f"Translation API response missing 'translated_text': {result}")
            return text  # Return original text if translation fails

    except requests.exceptions.RequestException as e:
        logging.error(f"Error during translation: {e}")
        return text  # Return original text on error
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON response: {e}")
        return text
    except Exception as e:
        logging.exception(f"Unexpected error during translation: {e}") # Log full exception
        return text

def translate_notebook(notebook_path, api_key, output_folder):
    """Translates the text content of a Jupyter Notebook and saves it to a new file in the output folder, preserving the folder structure."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            try:
                nb = nbformat.read(f, as_version=4)
            except nbformat.reader.NotJSONError as e:
                logging.error(f"Error reading notebook {notebook_path}: Invalid JSON format. Skipping.")
                return
            except Exception as e:
                logging.error(f"Error reading notebook {notebook_path}: {e}. Skipping.")
                return

        for cell in nb.cells:
            if cell.cell_type == 'markdown':  # Only translate markdown cells
                try:
                    cell.source = translate_text(cell.source, api_key)
                except Exception as e:
                    logging.error(f"Error translating cell in {notebook_path}: {e}")
                    # Consider whether to continue translating other cells or skip the notebook

        # Create the output path, preserving the folder structure
        relative_path = os.path.relpath(notebook_path, ".")  # Path relative to the root
        translated_path = os.path.join(output_folder, relative_path)
        translated_dir = os.path.dirname(translated_path)  # Directory of the translated file

        # Create the directory if it doesn't exist
        try:
            os.makedirs(translated_dir, exist_ok=True)
        except OSError as e:
            logging.error(f"Error creating directory {translated_dir}: {e}")
            return

        # Write the translated notebook
        try:
            with open(translated_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            logging.info(f"Translated: {notebook_path} -> {translated_path}")
        except Exception as e:
            logging.error(f"Error writing translated notebook to {translated_path}: {e}")


    except FileNotFoundError:
        logging.error(f"File not found: {notebook_path}")
    except Exception as e:
        logging.exception(f"Unexpected error processing {notebook_path}: {e}") # Log full exception


if __name__ == "__main__":
    api_key = os.environ.get("QWEN_API_KEY")
    if not api_key:
        logging.error("Error: QWEN_API_KEY not found in environment variables.")
        exit(1)

    output_folder = "translated_notebooks"  # Define the output folder name

    # Find all .ipynb files in the repository
    notebook_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_files.append(os.path.join(root, file))

    if not notebook_files:
        logging.info("No notebook files found.")
        exit(0)

    for notebook_file in notebook_files:
        translate_notebook(notebook_file, api_key, output_folder)

    logging.info("Translation process completed.")