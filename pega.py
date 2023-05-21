from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def create_chunks(transcript):
    max_chunk = 500
    ARTICLE = transcript.strip()
    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')
    sentences = ARTICLE.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks

def summarization_model(transcript):

    model_ckpt = "D:/STM/deepblue/server/python/pegasus-samsum-model"
    tokenizer_ckpt = "D:/STM/deepblue/server/python/tokenizer"

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_ckpt)
    model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

    chunks = create_chunks(transcript)
    print("Chunks Created")
    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128, "min_length":30, "do_sample":False}

    pipe = pipeline("summarization", model=model_pegasus,
                    tokenizer=tokenizer)

    res = pipe(chunks, **gen_kwargs)
    result = ' '.join([summ['summary_text'] for summ in res])
    print("Summary done")
    return result
