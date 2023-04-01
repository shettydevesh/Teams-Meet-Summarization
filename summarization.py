from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch


def summarization_model(transcript):

    model_ckpt = "D:/STM/deepblue/server/python/pegasus-samsum-model"
    tokenizer_ckpt = "D:/STM/deepblue/server/python/tokenizer"

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_ckpt)
    model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

    pipe = pipeline("summarization", model=model_pegasus,
                    tokenizer=tokenizer)

    print("Dialogue:")
    print(transcript)

    # print("\nReference Summary:")
    # print(reference)

    print("\nModel Summary:")
    result = pipe(transcript, **gen_kwargs)[0]["summary_text"]
    return result
