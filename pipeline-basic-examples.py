"""
This script demonstrates how to use the pipeline
function to load a pre-trained model and use it to
make predictions.
There are many tipes of pipelines, such as:
- feature-extraction: get the vector representation of a text
- fill-mask: fill in the blanks in a text
- ner: named entity recognition, find entities in a text
- question-answering: answer questions based on a text
- sentiment-analysis: classify the sentiment of a text
- summarization: summarize a text
- text-generation: generate text
- translation: translate text
- zero-shot-classification: classify a text without any training data

You can specify the model to use, or use the default one.

"""
from transformers import pipeline


class PipelineExamples():

    def __init__(self):
        pass

    def sentiment_analysis(self, text: str) -> None:
        """
        Test the sentiment analysis pipeline

        Args:
            text (str): The text to analyze.
        """
        print("\n---------------------------------\n")
        print("Sentiment analysis:\n")
        try:
            sentiment = pipeline("sentiment-analysis",
                                 model="nlptown/bert-base-multilingual-uncased-sentiment")
            out = sentiment(text)
            print(out)
        except Exception as e:
            print("Error: {e}")


    def zero_shot_classification(self, text: str) -> None:
        """
        Test the zero-shot classification pipeline

        Args:
            text (str): The text to analyze.
        """
        print("\n---------------------------------\n")
        print("Zero-shot classification:\n")
        try:
            classifier = pipeline("zero-shot-classification",
                                  model="facebook/bart-large-mnli")
            out = classifier(text)
            print(out)
        except Exception as e:
            print("Error: {e}")


    def text_generation(self, text: str) -> None:
        """
        Test the text generation pipeline
        The generator can take few arguments, such as:
        - max_length: maximum length of the generated text
        - num_return_sequences: number of sequences to generate


        Args:
            text (str): The text to analyze.
        """
        print("\n---------------------------------\n")
        print("Text generation:\n")
        try:
            generator = pipeline("text-generation",
                                 model="gpt2")
            out = generator(text,
                            max_length=50,
                            num_return_sequences=5)

            for i in out:
                print("Generated text:")
                print(i["generated_text"])
                print("\n")

        except Exception as e:
            print("Error: {e}")


if __name__ == "__main__":
    examples = PipelineExamples();

    # A different model is needed for each pipeline
    # taking a lot of memory and time to load them
    # examples.sentiment_analysis("This is a test sentence.")
    # examples.zero_shot_classification("This is a test sentence.")
    examples.text_generation("This is a test sentence.")
