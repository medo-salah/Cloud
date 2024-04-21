from collections import Counter
import logging

def load_stopwords(filepath="stopwords.txt"):
  """
  Loads stop words from a text file.

  Args:
      filepath (str, optional): The path to the text file containing stop words (one per line). Defaults to "stopwords.txt" (assuming the file is in the same directory).

  Returns:
      set: A set of stop words.
  """
  stopwords = set()
  try:
    with open(filepath, 'r') as f:
      for line in f:
        stopwords.add(line.strip())
  except FileNotFoundError:
    logging.warning(f"Stop word file not found: {filepath}")
  return stopwords

def remove_stopwords(text, stopwords):
  """
  Removes stop words from a given text.

  Args:
      text (str): The text to process.
      stopwords (set): A set of stop words to remove.

  Returns:
      str: The processed text with stop words removed.
  """
  words = text.lower().split()  # Convert to lowercase and split into words
  filtered_words = [word for word in words if word not in stopwords]
  return " ".join(filtered_words)  # Join the filtered words back into text

def process_paragraphs(filename):
  """
  Reads paragraphs from a file, removes stop words, and counts word frequencies.

  Args:
      filename (str): The path to the text file containing paragraphs.

  Returns:
      None
  """
  logging.basicConfig(level=logging.INFO)
  try:
    with open(filename, 'r') as f:
      text = f.read()
  except FileNotFoundError:
    logging.error(f"File not found: {filename}")
    return

  stopwords = load_stopwords()  # Use default filepath (assuming in the same directory)
  processed_text = remove_stopwords(text, stopwords)

  word_counts = Counter(processed_text.split())
  logging.info("Word Frequency Count:")
  for word, count in word_counts.items():
    logging.info(f"{word}: {count}")

# Update the file path to match your specific location (optional)
filename = "D:/Visual_StudioCode/Cloud_Assignment/random_paragraphs.txt"

if __name__ == "__main__":
  process_paragraphs(filename)
