
from google.cloud import language_v1
import streamlit as st
import pandas as pd

def analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()
    try:
     if text_content is None:
        text_content = 'I am so happy and joyful.'
    except NameError:
        text_content = 'I am not so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    return response

# response = analyze_sentiment("pretty good service today.")
# print(response)
st.write('Inspects the given text and identifies the prevailing emotional opinion within the text, especially to determine a writer\'s attitude as positive, negative, or neutral.')
st.write('The scoring range is defined as:')


st.write(pd.DataFrame({
    'Opinion Type': ['Clearly Positive*', 'Clearly Negative', 'Neutral*', 'Mixed*'],
    'Score': [0.8, -0.6,  0.1, 0.0],
     'Magnitude': [3.0, 4.0,0.0,4.0],
}))
st.title('Sentiment analysis')


text_to_analysis = st.text_input('Enter your text here')


if st.button('Get the Score'):
    generated_text = analyze_sentiment(text_to_analysis)
    st.write(generated_text)