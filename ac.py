import pandas as pd

def action_items():
    action_items = [
        ["Plan report for sports club annual meeting",
            "Not Provided", "May 15, 2023", "Secretary", "John"],
        ["Reserve venue for the tournament final cricket match",
            "High", "August 17, 2023", "Vice President", "Adam"],
        ["Prepare financial report for the second half of 2022",
            "Medium", "June 1, 2023", "Chairman", "Treasurer"]
    ]
    df = pd.DataFrame(action_items, columns=[
                      "Task Details", "Task Priority", "Due Date", "From whom it is assigned", "To whom it is assigned"])

    df.index = range(1, len(df) + 1)

    return df
