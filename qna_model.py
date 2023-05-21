import streamlit as st
from qna import extractor
from context import run

st.set_page_config(page_title="STM", layout="wide")
col1, col2 = st.columns((1, 1))

context = """
    Good afternoon, everyone. I want to welcome you all to our annual meeting for the year 2023. It's great to see all of you here today. I hope you all had a productive year and have some exciting updates to share with us. As the President of this club, I am proud to say that we had an incredible year in 2022. We organized several successful events that brought our members and the community together. Our basketball team also made it to the finals, and we couldn't be prouder of them. It's a testament to the hard work and dedication of our players and coaches. In terms of our finances, I am pleased to announce that we had a successful year. We generated a significant amount of revenue from our events and sponsorships, and our club's balance remains healthy. But it's not just about the numbers. It's about the sense of community and belonging that our club provides. We had 80 active members last year, and we welcomed 15 new members to our family. I want to thank all of you for your contributions to the club's success. Your hard work and dedication have helped us achieve our goals, and I am confident that we will continue to grow and thrive in the years to come. So, without further ado, let's begin the meeting and discuss our plans for the year ahead. Thank you all again for being here today.
"""

def main():
    st.header("QNA Model")
    query = st.text_input("Enter your query: ")
    if query:
        answer = extractor(query, context)
        if answer:
            st.write(f"Answer: {answer}")
    st.subheader(f"Were you mentioned in the meet?")
    pattern = st.text_input("Enter name")
    print(pattern)
    if pattern:
        result = run(pattern)
        st.table(result)


if __name__ == '__main__':
    main()