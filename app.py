import streamlit as st
from summarization import summarization_model
from namecontext import nameandcontext
from transcript import extract

st.set_page_config(page_title="STM", layout="wide")


def main():
    st.title("Teams Meeting Summarization")
    st.header("Upload your Transcript here:")
    speech_file = st.file_uploader("", key="doc_file", type=['.docx'])
    if speech_file is not None:
        transcript, names, time = extract(speech_file)
        result = nameandcontext(transcript, "Sanmitha")
        # summary = summarization_model(transcript)
        st.header("Results:-")
        st.subheader(f"Names of the Participants:")
        st.text(f"{names}")
        st.subheader(f"Duration of the meet: {time}")
        st.subheader(f"Transcript:")
        st.text(transcript[:1000])
        st.subheader(f"Where you mentioned in the meet:")
        st.text(result)
        st.subheader(f"Summarization:")
        # st.text(summary)


if __name__ == '__main__':
    main()
