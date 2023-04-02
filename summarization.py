from transformers import pipeline

summarizer = pipeline("summarization")


def summ(transcript):
    res = summarizer(transcript, max_length=1000, min_length=150,
                     do_sample=False)
    data = res[0]
    return data["summary_text"]
