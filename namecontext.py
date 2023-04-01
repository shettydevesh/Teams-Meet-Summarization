from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

model_ckpt = "D:/STM/deepblue/server/python/pegasus-samsum-model"
tokenizer_ckpt = "D:/STM/deepblue/server/python/tokenizer"


def nameandcontext(transcript, pattern):
    lines = transcript.split("\n")
    output = []

    for i, line in enumerate(lines):
        if pattern in line:
            current_line = line.strip()
            previous_line = lines[i-1].strip() if i > 0 else ""
            next_line = lines[i+1].strip() if i < len(lines)-1 else ""
            output.append(previous_line + " " + current_line + " " + next_line)

    output_str = "\n".join(output)
    print("Output STR", output_str)

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_ckpt)
    model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

    gen_kwargs = {"length_penalty": 0.8,
                  "num_beams": 8, "max_length": 128}

    pipe = pipeline("summarization", model=model_pegasus,
                    tokenizer=tokenizer)

    result = pipe(output_str, **gen_kwargs)[0]["summary_text"]
    # print the output
    return result
