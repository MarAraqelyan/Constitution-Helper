import sys
import spacy

nlp = spacy.load("en_core_web_lg")

def readFile() -> str:
    """
        Reads the entire file and returns it as a string.
    """
    try:
        with open("Constitution.txt", encoding="utf-8") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    except Exception as e:
        print("Error while reading the file: {e}")
        sys.exit(1)


def readConstitution() -> tuple:
    """
        Gets the command and search text from the command-line.
    """
    try:
        return sys.argv[1], sys.argv[2]
    except IndexError:
        print("Not enough arguments")
        sys.exit(1)


def checkCommand(command: str) -> None:
    """
        Check if the command is right, otherwise raise an Error.
    """
    if command.lower() != "find":
        raise Exception("Wrong input command")


def splitIntoSentences(text: str) -> list:
    """
        Splits the given text into sentences.
    """
    text = text.replace('\n', ".")
    sentences = text.split(".")
    return sentences

def findSimilarities(sentences: list, input_text: str) -> dict:
    """
        Finds similar or the exact words in the search text and file sentences.
    """
    word_count = {}
    input_text = input_text.split(" ")

    """
        Split the sentence into list of words.
    """
    for sentence in sentences:
        new_sentence = list(filter(None, sentence.replace('\n', " ").split(" ")))
        count = 0

        """
            Find similar words and add the filtered sentence to the dictionary.
        """
        for word in new_sentence:
            for input_word in input_text:
                if nlp.vocab[input_word.lower()].has_vector and nlp.vocab[word.lower()].has_vector:
                    if nlp.vocab[input_word.lower()].similarity(nlp.vocab[word.lower()]) >= 0.7:
                        count += 1
        if count:
            word_count[sentence] = count
    return word_count


def enumerateSentences(filtered_sentences: dict) -> None:
    """
        Prints the sorted sentences numbered.
    """
    for index, sentence in enumerate(sorted(filtered_sentences.items(), key=lambda item: item[1], reverse = True), start=1):
        print(index, sentence[0])
        print()


def similarSentence(filtered_sentences: dict, input_text: str) -> str:
    """
        Finds the sentence that is the most similar to the search text.
    """
    most_similar = ""
    percent = 0

    for sentence in filtered_sentences:
        if nlp(sentence.lower()).has_vector and nlp(input_text.lower()).has_vector:
            similarity = nlp(sentence.lower()).similarity(nlp(input_text.lower()))
            if similarity >= percent:
                most_similar = sentence
                percent = similarity

    return most_similar


if __name__ == "__main__":
    command, input_text = readConstitution()

    text = readFile()

    sentences = splitIntoSentences(text)

    filtered_sentences = findSimilarities(sentences, input_text)

    enumerateSentences(filtered_sentences)

    print("Similar sentence:\n",similarSentence(filtered_sentences, input_text))
