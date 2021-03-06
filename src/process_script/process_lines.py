from src.params import *
from src.utils import *
logger = get_logger(__name__)


def clean_line(line):
    """
    Apply basic cleaning steps to a line

    Args:
        line (str): string to be cleaned

    Returns:

    """
    line = re.sub(r"[\[].*?[\]]", "", line)
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.strip()
    return line


def tokenize_line(line):
    """
    Transform a string to a list of words

    Args:
        line (str):

    Returns:

    """
    tokens = line.split(' ')
    return tokens


def remove_stopwords(tokens, stop_words=STOPWORDS):
    """
    Remove stopwords from a list of tokens

    Args:
        tokens (list): input list of words
        stop_words (list): list of words to remove

    Returns:

    """
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens


def process_lines(input_df):
    """
    Takes in Dataframe script and process "line" column which
    contains the text of each lines
    - Clean the text (column clean_line)
    - Tokenize it (tokenized_line)
    - Get non stop words (tokenized_non_stop)

    Args:
        input_df (pd.DataFrame): raw dataset containing one line per row
    """
    logger.info("Processing lines")
    input_df['clean_line'] = input_df['line_text'].apply(clean_line)
    input_df['tokenized_line'] = input_df['clean_line'].apply(tokenize_line)
    input_df['tokenized_non_stop'] = input_df['tokenized_line'].apply(
        remove_stopwords)
    return input_df
