# import nltk
# import spacy
# import numpy as np

# # def deadlines(text):

# #     deadlines_list = ['registration deadline is June 15th', 'registration deadline is May 15th', 'scheduled by December 15th',
# #                       'by the end of the day', 'registration deadline is June 15th', 'submission deadline is September 15th']

# #     sentences = nltk.sent_tokenize(text)

# #     deadline_sentences = []

# #     for sentence in sentences:

# #         for deadline in deadlines_list:
# #             if deadline in sentence:
# #                 deadline_sentences.append(sentence)

# #     print("Deadlines Extracted")
# #     return deadline_sentences
import nltk
import pandas as pd
# from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
# import torch

# def summarization_model(transcript):

#     model_ckpt = "D:/STM/deepblue/server/python/pegasus-samsum-model"
#     tokenizer_ckpt = "D:/STM/deepblue/server/python/tokenizer"

#     tokenizer = AutoTokenizer.from_pretrained(tokenizer_ckpt)
#     model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

#     gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

#     pipe = pipeline("summarization", model=model_pegasus,
#                     tokenizer=tokenizer)

#     result = pipe(transcript, **gen_kwargs)[0]["summary_text"]
#     return result


def deadlines(text):

    deadlines_list = ['registration deadline is June 15th', 'registration deadline is May 15th', 'scheduled by December 15th',
                      'by the end of the day', 'registration deadline is June 15th', 'submission deadline is September 15th', 'until the end of May', 'application deadline for submission']

    sentences = nltk.sent_tokenize(text)

    deadline_sentences = []

    for sentence in sentences:

        for deadline in deadlines_list:
            if deadline in sentence:
                deadline_sentences.append(sentence)

    # results = []

    # for res in deadline_sentences:
    #     res = summarization_model(res)
    #     print(res)
    #     results.append(res)

    df = pd.DataFrame(deadline_sentences, columns=['Deadlines'])

    df.index = range(1, len(df) + 1)
    print("Deadlines Extracted")
    return df
