import docx


def extract(path):
    doc = docx.Document(path)
    fullText = []
    names = []
    finalText = []
    time = ""
    for para in doc.paragraphs:
        fullText.append(para.text)
    for lines in fullText:
        line = lines.splitlines()
        finalText.append(line[2])
        finalText.append("\n")
        time = line[0]
        time = time[-12:]
        if (line[1] not in names):
            names.append(line[1])
    return "".join(finalText), "\n".join(names), time
