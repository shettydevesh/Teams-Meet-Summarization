from transformers import pipeline
import torch 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


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


def summary(transcript):
    summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
    chunks = create_chunks(transcript)
    print("Chunks Created")
    res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)
    result = ' '.join([summ['summary_text'] for summ in res])
    print("Summary Done")
    return result


text = """
Good evening, everyone. Thank you for joining us for this parent-teacher meeting. I hope you all are doing well. I am here to update you on the school's activities and events throughout the year. Our school calendar includes events such as science fairs, sports meet, cultural festivals, and community service projects. We also have planned several field trips to museums, historical sites, and other places of educational importance. We believe that these activities provide an opportunity for students to explore their interests, develop skills, and create lasting memories. Now, I would like to invite our parents to share their concerns with us. Thank you.


Good evening, everyone. I am John's mother, and I am here to discuss his progress in school. Overall, John is a hardworking and dedicated student however John seems to be struggling with mathematics and English. He finds it difficult to grasp some of the concepts and needs additional support and guidance in these areas. I have been working with him at home and have noticed some improvement, but I believe he could benefit from additional help from his teachers. I would appreciate it if his teachers could provide me with some guidance on how we can work together to help John improve his performance in these subjects.


Thank you, Mrs. Smith, for bringing up John's performance in school. As his mathematics and English teacher, I have noticed that he has been struggling in these subjects. However, I have also noticed that John is a hardworking student who is always willing to learn and improve. In my experience, students who struggle in these subjects often require additional support and guidance, and I believe that John can benefit from additional practice and one-on-one instruction. We can work together to create a plan to help John improve his understanding of these subjects. We have tutoring sessions and extra study materials available to help students improve their understanding.


Good evening, everyone. Myself Mrs. Gupta and I am a parent of two students in this school. I am particularly interested in learning about the extracurricular activities that the school has planned for the upcoming academic year. Mr. Lee seems like a very nice gentleman. Could you please tell us about the extracurricular events that the school has scheduled for the next academic year?


Thank you for your question, Mrs. Gupta. I am Mr. Patel and I am in charge of managing the events for the school, and we have several exciting events planned for the upcoming academic year. We will have a conference on innovative teaching methods, which will take place on the 15th of October in the school auditorium. We also have a theatre performance scheduled for the 30th of November, which will be held in the school's theatre hall. In addition, we have a music performance scheduled for the 15th of February, which will take place in the school's main hall. We will also be organizing a carnival on the 1st of March, which will include games, food stalls, and other fun activities for students and parents to enjoy. Lastly, we have our winter competitions scheduled for the 10th of December. We encourage all interested students to submit their applications before this deadline. I hope this answers your question, Mrs. Gupta, and we look forward to seeing everyone at these exciting events.


I would like to take a moment to recognize and celebrate the achievements of some of our students. In the primary section, the first rank is secured by Sarah Sharma, who has consistently excelled in all subjects and has shown exceptional talent in creative writing. In the secondary section, the first rank is secured by Ravi Gupta, who has consistently scored high marks and has demonstrated a passion for sports. Apart from academic excellence, we also recognize the importance of developing enterprising skills and leadership qualities in our students. Therefore, we would also like to recognize the most enterprising students of the academic year. Akshay Kumar and Anjali Sharma are the two most enterprising students of the academic year. Congratulations to all the students who have been recognized today, and we wish all our student�s success in their academic and personal pursuits.


As you all know, that I Mr. Lee, teach Maths and English to the students, and I would like to take this opportunity to discuss their performance in the recent exams. Overall, I am happy to report that the students have shown significant improvement in both subjects. However, there are still areas where some of the students can improve. For instance, in Maths, some students need to focus on improving their problem-solving skills and speed. In English, some students need to work on their grammar and vocabulary. I would like to advise the students and parents to take advantage of the resources available to them, such as the library, online learning platforms, and tutoring services. Thank you for your attention, and I wish all the students the best of luck in their academic and personal pursuits.


Good evening, everyone. I am Mr. Khan and I teach Physics, Biology, Chemistry, and Computer Science. I am pleased to be here today to discuss your children's performance in the recent exams in Physics, Biology, Chemistry, and Computer Science. Overall, I am satisfied with the students' performance. They have shown a good understanding of the concepts and have demonstrated strong problem-solving skills. However, there are still areas where some students need to improve. In Physics, some students need to focus on their practical skills and understanding of the formulas. In Biology and Chemistry, some students need to work on memorizing important terms and concepts. In Computer Science, some students need to focus on their coding skills and logical reasoning. We have a science and technology fair scheduled for the 25th of September, which will take place in the school's science lab. We also have a coding competition scheduled for the 10th of December, which will take place in the school's IT lab. Students will be required to write code to solve a set of problems and complete tasks related to computer science. I encourage all interested students to participate and make the most of these opportunities.


Hey guys, I am Mr. Kittle and I'm excited to tell you about some upcoming deadlines for events and competitions that you won't want to miss out on! First off, if you're interested in theater, we've got a big production coming up on 30th of November, so make sure you've got your audition scheduled by December 15th. If you're more into music, we've got a Battle of the Bands competition happening on 15th of February, and the registration deadline is May 15th, so make sure you've got your band together and signed up by then. For those of you who are into sports, we've got a big soccer tournament happening on July 1st, and the registration deadline is June 15th. For those of you who love art, we've got an art competition happening on October 1st, and the submission deadline is September 15th. There you have it, folks. Make sure you don't miss out on these amazing opportunities and get those deadlines in your calendar. Good luck to everyone who participates!


Thank you all for attending today's parent-teacher meeting. We hope you found the information shared by our teachers helpful and informative. We encourage all parents to fill out the feedback forms by the end of the day and let us know your thoughts about today's meeting and any suggestions you may have for improvement. Once again, thank you all for coming, and we look forward to seeing you at our future events. Have a great day!
"""

result = summary(text)
print(result)
