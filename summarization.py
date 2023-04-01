from transformers import pipeline

summarizer = pipeline("summarization")


def summ(transcript):
    res = summarizer(transcript, max_length=120, min_length=30,
                     do_sample=False, truncation=True)
    data = res[0]
    return data["summary_text"]
