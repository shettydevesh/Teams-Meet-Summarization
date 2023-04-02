import spacy
import nltk

ner_model = spacy.load(
    "C:/Users/Shetty/Documents/Experiments/ner_model_events-20230402T145156Z-001/ner_model_events")


def get_events(transcript):
    events = []

    sent_text = nltk.sent_tokenize(transcript)

    for sentence in sent_text:
        sentence = sentence.replace("\n\n", "")
        doc = ner_model(sentence)
        for ent in doc.ents:
            if ent.label_ == 'Event':
                events.append(sentence)
    return events[1]
