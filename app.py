import streamlit as st
from asr import stt
from transcript import extract
# from asr import stt
from pega import summarization_model
from deadline import deadlines
from events import get_eventss
from context import run
from ac import action_items


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
        summary = summarization_model(transcript)
        dl = deadlines(transcript)
        et = get_eventss(transcript)
        action = action_items()
        # summarization = summ(transcript)
        with open("transcript.txt", "w") as file:
            file.write(transcript)
        st.header("Results:-")
        st.subheader(f"Transcript:")
        st.write(transcript[:500] + "\n" + ".....")
        st.subheader(f"Summarization:")
        st.write(summary)
        # st.write("The conversation took place in a parent-teacher meeting where the principal, Mrs. Smith, Mr. Lee, Mrs. Gupta, and Mr. Patel were present. The principal opened the meeting by thanking everyone for attending and updating them on the school's activities and events planned for the year. Mrs. Smith expressed her concern about her son's academic performance in math and English and requested the teachers' help. Mr. Lee, John's math and English teacher, acknowledged the concern and reassured her that they had resources to help students who struggle and promised to work with Mrs. Smith to improve John's performance. Mrs. Gupta asked about the extracurricular events planned for the upcoming academic year, and Mr. Patel, in charge of managing school events, explained the events, including a conference on innovative teaching methods, theater and music performances, a carnival, and winter competitions. Finally, the principal recognized and celebrated the achievements of some of the school's students.")
        st.subheader(f"Names of the Participants:")
        st.write(f"{names}")
        st.subheader(f"Meeting Duration: ")
        st.write(f"{time}")
        st.header("Action Items: ")
        st.subheader("Deadlines: ")
        st.table(dl)
        st.subheader("Events: ")
        st.table(et)
        st.subheader("Tasks: ")
        st.table(action)
    elif audio_file is not None:
        audio_transcript = stt(audio_file)
        summary_audio = summarization_model(audio_transcript)
        st.header("Results:-")
        st.subheader(f"Transcript:")
        st.write(f"{audio_transcript}")
        st.subheader("Summary: ")
        st.write(f"{summary_audio}")


if __name__ == '__main__':
    main()