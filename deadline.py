import nltk
import spacy
import numpy as np


ner_model = spacy.load(
    "C:/Users/Shetty/Documents/Experiments/ner_model_deadlines-20230402T130211Z-001/ner_model_deadlines")


def get_deadlines(transcript):
    # text = """
    # Welcome everyone to the Parent-Teacher Meeting. We'll start with a brief introduction from each of you.
    # Hello, I'm Mrs. Smith, John's mother.
    # Good afternoon, I'm Mr. Lee, Emily's father.
    # Namaste, I'm Mrs. Gupta, Ankit's mother.
    # Hello, I'm Mr. Patel, Riya's father.
    # Thank you, everyone. Now, let's start with the feedback. The feedback form for this meeting should be submitted by all the students before the end of the meeting. Mrs. Smith, would you like to start?
    # Yes, thank you. John Cena has been struggling with Math, and I was wondering if there are any extra classes or resources available to help him.
    # Certainly, we have after-school tutoring every Wednesday. I can also provide some extra practice problems if needed.
    # Thank you, that would be helpful.
    # An important thing to note that the musical performance on September 25th at 7 PM at the church is a fundraiser for a local charity. It's a great cause and the music is always beautiful. Mr. Lee, do you have any concerns?
    # Yes, Emily has been feeling overwhelmed with the workload. Is there any way to reduce the number of assignments or projects
    # I can definitely understand how that can be stressful. Perhaps we can adjust the due dates or provide some extra time in class for the projects.
    # """
    deadlines = []

    sent_text = nltk.sent_tokenize(transcript)

    for sentence in sent_text:
        # print(f"Sentence: {sentence}")
        doc = ner_model(sentence)
        # print(f"Doc: {doc}")
        for ent in doc.ents:
            if ent.label_ == 'Deadline':
                deadlines.append(sentence)
    return deadlines[0]
