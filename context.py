import nltk
import pandas as pd

text = """
Good afternoon, everyone. I want to welcome you all to our annual meeting for the year 2023. It's great to see all of you here today. I hope you all had a productive year and have some exciting updates to share with us. As the President of this club, I am proud to say that we had an incredible year in 2022. We organized several successful events that brought our members and the community together. Our basketball team also made it to the finals, and we couldn't be prouder of them. It's a testament to the hard work and dedication of our players and coaches. In terms of our finances, I am pleased to announce that we had a successful year. We generated a significant amount of revenue from our events and sponsorships, and our club's balance remains healthy. But it's not just about the numbers. It's about the sense of community and belonging that our club provides. We had 80 active members last year, and we welcomed 15 new members to our family. I want to thank all of you for your contributions to the club's success. Your hard work and dedication have helped us achieve our goals, and I am confident that we will continue to grow and thrive in the years to come. So, without further ado, let's begin the meeting and discuss our plans for the year ahead. Thank you all again for being here today.


Good afternoon, everyone. As the Secretary of this club, I have some important updates to share with you all. Firstly, I am pleased to announce that our members have elected a new Chairman for the year 2023, and his name is Michael. We are confident that he will do an excellent job leading the club and taking it to new heights. Now, moving on to the events and activities that we have planned for the year ahead. We have a packed schedule, and I am excited to share the details with you all. Our first event is a charity walkathon that will take place on May 21st and it will be held at Central Park. We will be raising funds for a local charity that supports underprivileged children. The event will start at 8 am, and we encourage all members to participate and bring along their friends and family. Next, we have our annual basketball tournament, which will take place on June 11th and June 12th and it will be held at the City Sports Arena, and we are expecting teams from across the city to participate. We have some exciting prizes lined up for the winners, and it's sure to be a fun-filled weekend. In July, we have a soccer clinic for kids aged between 8 to 12 years old and it will be held on July 15th 2022 at the local soccer field, and we will be inviting professional coaches to conduct the training. It's a great opportunity for kids to learn new skills and make new friends. In August, we have a community volleyball game that will take place on August 20th. The game will be held at the local beach, and we encourage all members to participate and bring along their friends and family. It's a great way to spend a day at the beach while also engaging in some healthy competition. Finally, in September, we have a fitness challenge that will take place on September 17th. The challenge will be held at the local gym, and we will be testing members' endurance, strength, and agility. It's a great way to push yourself and stay motivated to achieve your fitness goals. So, these are the events and activities that we have planned for the year ahead. We will be sending out more information and updates as the dates approach, and we encourage all members to participate and make these events a success. Thank you.


Good afternoon, everyone. I am honoured to be elected as the new Chairman of this club, and I am excited to take on this role. Before I share my plans for the year ahead, I want to give a brief introduction about myself. I have been a member of this club for five years, and I have seen it grow and flourish over the years. I am passionate about sports and community involvement, and I believe that this club embodies both of those things. As the new Chairman, I want to focus on three things: inclusivity, innovation, and impact. Firstly, I want to make sure that our club is inclusive of everyone. We want to create a welcoming environment where people of all backgrounds and abilities feel comfortable and empowered to participate in sports. Secondly, I want to bring in some innovation to the club. While we have had some successful events and activities in the past, I believe that there is always room for improvement and new ideas. I want to encourage our members to come forward with their suggestions and feedback so that we can make our events more engaging and impactful. Lastly, I want to focus on impact. While we have raised funds for charities in the past, I believe that we can do more to make a positive impact in the community. We can partner with local organizations to create more opportunities for youth sports or organize events that benefit our environment. I am looking forward to working with all of you to achieve these goals and make our club even better than it already is. Thank you.



Good afternoon, everyone. As the Treasurer of this club, I want to assure you that we are in a stable financial position, and I will be working hard to maintain this throughout the year. I will be keeping accurate records of all financial transactions and ensuring that our budgets are realistic and feasible. We have some exciting events planned for the year ahead, and I will make sure that we are financially prepared for them. However, I also want to announce that I will be retiring as Treasurer at the end of this year, and we need to start looking for a new Treasurer to take over and I encourage all members who have an interest in this position to come forward and apply and we will be accepting applications until the end of May. We will make sure to train and guide the new Treasurer to ensure a smooth transition. In the meantime, I will continue to work diligently as the Treasurer and make sure that the club's finances are in order. Thank you.


Good afternoon, everyone. As the Vice President of this club, I am proud to say that we have had a successful year. We have hosted multiple events and activities, and we have seen an increase in our membership and participation rates. The single most important achievement of the club this year was our charity fundraiser for the local children's hospital. We were able to raise $10,000, which will go a long way in supporting the hospital and the children who need their services. In the previous 12 months, we have been successful in creating a more inclusive and diverse club. We have welcomed new members from different backgrounds and abilities, and we have made sure that everyone feels valued and appreciated. I am excited to announce that we will be hosting a grand sports event named "Sports for All" on July 20th at the City Stadium. This event will feature multiple sports and activities, and it will be open to the entire community. We want to showcase the diversity and inclusivity of our club and encourage more people to join us. We are also announcing the formation of new club teams for basketball and volleyball. If you are interested in joining these teams, please speak to one of the team captains for more information. We are accepting forms for coaches' applications for soccer and swimming teams and their application deadline for submission is May 31st, and we encourage all qualified individuals to apply. Thank you.        


Thank you to all the members who attended this year's Sports Club Association Annual Meeting. I am proud to say that we have accomplished a lot in the previous year and have set some exciting goals for the year ahead. We have a strong team of leaders who are committed to making this club a welcoming and inclusive space for everyone. I encourage all members to participate in the upcoming events and activities and take advantage of the opportunities to connect with fellow sports enthusiasts. As we move forward, let us continue to support each other and work towards our shared goals. Let us continue to promote diversity and inclusivity in our club and in the larger community. Thank you again for your continued support, and I look forward to another successful year ahead. Have a great day!"""


def search_pattern(text, pattern):
    sent_text = nltk.sent_tokenize(text)

    entry = []

    result = []

    for line_number, line in enumerate(sent_text):
        if pattern in line:
            index = line_number
            result.append(sent_text[index - 1])
            result.append(sent_text[index])
            result.append(sent_text[index + 1])
        if len(result) > 2:
            entry.append(result)
        result = []

    entries = []

    for ent in entry:
        joined_list = [" ".join(ent)]
        entries.append(joined_list)

    return entries


def run(pattern):
    result = search_pattern(text, pattern)
    # print(result)

    # results = []

    # for res in result:
    #     res = summ(res)
    #     print(res)
    #     results.append(res)
    df = pd.DataFrame(result, columns=['Context'])
    df.index = range(1, len(df) + 1)
    print("Context Extracted")

    return df
