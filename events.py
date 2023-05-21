import re
from dateutil.parser import parse
from datetime import datetime
import nltk
import pandas as pd

# ner_model = spacy.load(
#     "C:/Users/Pratham/Downloads/STM/Teams-Meet-Summarization/ner_model_events")


def is_past_due(date_string):
    due_date = parse(date_string)
    res = datetime.now().date() > due_date.date(
    ) if datetime.now().date() != due_date.date() else False
    if res == True:
        return "Past Event"
    else:
        return "Active Event"

def convert_date_into_format(dates):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    conv_dates = []

    for date in dates:
        if date:
            day = re.search(r'\d{1,2}', date).group()

            month = None
            for m in months:
                if re.search(m, date):
                    month = month_dict[m]
                    break
            if not month:
                month = '01'

            year_match = re.search(r'\d{4}', date)
            if year_match:
                year = year_match.group()
            else:
                year = '2023'

            date_str = f"{day}/{month}/{year}"

            conv_dates.append(date_str)
        else:
            conv_dates.append('None')

    return conv_dates


def get_eventss(text):

    events_list = ['conference', 'theatre performance', 'music performance', 'carnival',
                   'winter competitions', 'science and technology fair', 'coding competition',
                   'grand sports event', 'charity walkathon', 'basketball tournament', 'soccer clinic', 'community volleyball game', 'fitness challenge']
    date_list = ['15th of October', '30th of November', '15th of February',
                 '1st of March', '10th of December', '25th of September', '10th of December',
                 'July 15th 2022', 'May 21st', 'June 11th', 'July 20th',
                 'December 20th', 'September 17th']
    venue_list = ['school auditorium', 'school theatre hall',
                  'school main hall', 'school science lab', 'school IT lab',
                  'City Stadium', 'Central Park', 'City Sports Arena', 'local soccer field']

    sentences = nltk.sent_tokenize(text)

    event_sentences = []

    for sentence in sentences:

        for event in events_list:
            if event in sentence:
                event_sentences.append(sentence)

    table = []

    single_event = []

    for sentence in event_sentences:

        for event in events_list:
            if event in sentence:
                event = event.title()
                single_event.append(event)

        for date in date_list:
            if date in sentence:
                single_event.append(date)

        for venue in venue_list:
            if venue in sentence:
                venue = venue.title()
                single_event.append(venue)

        single_event = [item for i, item in enumerate(
            single_event) if item not in single_event[:i]]
        table.append(single_event)
        single_event = []

    df = pd.DataFrame(table, columns=['Event', 'Date', 'Venue'])

    dates = df['Date'].tolist()

    status = []

    for date in dates:
        if date:
            res = is_past_due(date)
            status.append(res)
        else:
            status.append('None')

    conv_dates = convert_date_into_format(dates)

    print(conv_dates)

    df['Status'] = status
    df['Date'] = conv_dates
    df.index = range(1, len(df) + 1)
    print("Events Extracted")
    return df
