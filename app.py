import streamlit as st
from summarization import summ
from namecontext import nameandcontext
from transcript import extract
from deadline import get_deadlines
from events import get_events
from newsum import summarization_model

st.set_page_config(page_title="STM", layout="wide")
col1, col2 = st.columns((1, 1))


def main():
    with col1:
        st.header("Upload your Transcript here:")
        speech_file = st.file_uploader("", key="doc_file", type=['.docx'])
    with col2:
        st.header("Upload your Audio File here:")
        audio_file = st.file_uploader("", key="audio_file", type=[".wav"])
    if speech_file is not None:
        transcript, names, time = extract(speech_file)
        result = nameandcontext(transcript, "John Cena")
        deadlines = get_deadlines(transcript)
        events = get_events(transcript)
        summary = summarization_model(transcript)
        st.header("Results:-")
        st.subheader(f"Transcript:")
        st.text(transcript[:500] + "\n" + ".....")
        st.subheader(f"Summarization:")
        st.write(summary)
        st.subheader(f"Names of the Participants:")
        st.text(f"{names}")
        st.subheader(f"Duration of the meet: {time}")
        st.subheader(f"Where you mentioned in the meet:")
        st.text(result)
        st.header("Action Items: ")
        st.subheader("Deadlines: ")
        st.text(deadlines)
        st.subheader("Events: ")
        st.text(events)
    elif audio_file is not None:
        print("Audio file is submitted")


if __name__ == '__main__':
    main()
