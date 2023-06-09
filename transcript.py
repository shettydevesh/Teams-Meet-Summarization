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
        hour = time[-11:-10]
        min = time[-9:-7]
        sec = time[-6:-4]
        if (line[1] not in names):
            names.append(line[1])
    print("Extraction done")
    return "\n".join(finalText), ",".join(names), f"{hour}hr {min}min {sec} seconds"
