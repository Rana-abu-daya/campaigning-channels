# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Upload CSV file
# st.title("Captain Voting Statistics")
# uploaded_file = st.file_uploader("AMAC_Voters_Data_Religion_wise_bulk", type=["csv"])
#
# if uploaded_file:
#     # Load the CSV file into a DataFrame
#     df = pd.read_csv(uploaded_file)
#
#     # Filter rows where 'captain' column is not null
#     df["captain"] = df["captain"].fillna("").str.lower()
#
#     # Filter rows where 'captain' is not null or "none"
#     valid_voters = df[~df["captain"].isin(["", "none"])]
#     total_voters = valid_voters.shape[0]
#
#     # Get votes cast (you can modify this logic as needed)
#     # Filter rows for votes cast (Nov 2024 Status is "Accepted" or "Challenged")
#     votes_cast = valid_voters[valid_voters["Nov 2024 Status"].isin(["Accepted", "Challenged"])].shape[0]
#     votes_remaining = total_voters - votes_cast
#
#     # Optionally, aggregate votes per captain
#     captain_votes = df["captain"].value_counts().to_dict()
#
#     # Display pie chart for overall voting progress
#     st.subheader("Overall Voting Progress")
#     fig1, ax1 = plt.subplots()
#     ax1.pie(
#         [votes_cast, votes_remaining],
#         labels=["Votes Cast", "Votes Remaining"],
#         autopct="%1.1f%%",
#         startangle=90,
#         colors=["#1f77b4", "#ff7f0e"]
#     )
#     ax1.axis("equal")  # Equal aspect ratio ensures pie chart is circular.
#     st.pyplot(fig1)
#
#     # Pie chart for captain votes (if data exists)
#     if captain_votes:
#         st.subheader("Votes by Captain")
#         fig2, ax2 = plt.subplots()
#         ax2.pie(
#             captain_votes.values(),
#             labels=captain_votes.keys(),
#             autopct="%1.1f%%",
#             startangle=90,
#             colors=["#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]
#         )
#         ax2.axis("equal")
#         st.pyplot(fig2)
#
#     # Summary
#     st.write(f"Total Voters: {total_voters}")
#     st.write(f"Votes Cast: {votes_cast}")
#     st.write(f"Votes Remaining: {votes_remaining}")
# else:
#     st.write("Please upload a CSV file to proceed.")
# import streamlit as st
# import matplotlib.pyplot as plt
#
# # Hardcoded Ethnicity Counts
# ethnicity_counts = {
#     'Bangladesh': 160,
#     'Pakistan': 87,
#     'Palestine': 38,
#     'Egypt': 15,
#     'India': 11,
#     'Brunei': 1,
#     'Ethiopia': 1,
#     'Somalia': 1,
#     'Jordan': 1
# }

# Total number of valid voters (assuming it's 315 from your context)
# votes_cast = 315
# votes_remaining = 423 - votes_cast  # Assuming total voters is 423
#
# # Display the pie chart for Ethnicity classification
# st.title("Captain Voting Statistics")
# st.subheader("Voter Distribution by Ethnicity")
# fig2, ax2 = plt.subplots(figsize=(12, 10))  # Increased figure size
# ax2.pie(
#     ethnicity_counts.values(),
#     startangle=90,
#     colors=["#2ca02c", "#d62728", "#9467bd", "#8c564b", "#ff7f0e", "#1f77b4", "#8c564b", "#7f7f7f", "#c7c7c7"],
#     pctdistance=0.85,
#     explode=[0.1, 0, 0, 0, 0, 0, 0, 0, 0],
#     textprops={'fontsize': 10}
# )
# centre_circle = plt.Circle((0,0),0.70,fc='white')
# fig2.gca().add_artist(centre_circle)
# ax2.axis("equal")
# # Adding a legend outside the chart
# ax2.legend(
#     ethnicity_counts.keys(),
#     loc='center left',
#     bbox_to_anchor=(1, 0.5),
#     title="Ethnicities"
# )
# st.pyplot(fig2)
#
# # Pie chart for overall voting progress
# st.subheader("Overall Captain Voting Progress")
# fig1, ax1 = plt.subplots()
# ax1.pie(
#     [votes_cast, votes_remaining],
#     labels=["Voted", "Not voted"],
#     autopct="%1.1f%%",
#     startangle=90,
#     colors=["#1f77b4", "#ff7f0e"]
# )
# ax1.axis('equal')
# st.pyplot(fig1)
#
# # Summary information
# st.write(f"Total Voters of Captains: 423")
# st.write(f"Not voted: {votes_cast}")
# st.write(f"Not voted: {votes_remaining}")
import streamlit as st
import matplotlib.pyplot as plt

# Hardcoded Ethnicity Counts
ethnicity_counts = {
    'Bangladesh': 160,
    'Pakistan': 87,
    'Palestine': 38,
    'Egypt': 15,
    'India': 11,
    'Brunei': 1,
    'Ethiopia': 1,
    'Somalia': 1,
    'Jordan': 1
}

# Total number of valid voters
votes_cast = 315
votes_remaining = 423 - votes_cast

# Setting up the Streamlit title
st.title("Captain Voting Statistics")

# Using beta_columns to create a layout for side by side pie charts
col1, col2 = st.beta_columns(2)

# First column for ethnicity distribution pie chart
with col1:
    st.subheader("Captains' Voted Voters Distribution by Ethnicity")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.pie(
        ethnicity_counts.values(),
        startangle=90,
        colors=["#2ca02c", "#d62728", "#9467bd", "#8c564b", "#ff7f0e", "#1f77b4", "#8c564b", "#7f7f7f", "#c7c7c7"],
        pctdistance=0.85,
        explode=[0.1, 0, 0, 0, 0, 0, 0, 0, 0],
        textprops={'fontsize': 10}
    )
    centre_circle = plt.Circle((0,0),0.70, fc='white')
    fig2.gca().add_artist(centre_circle)
    ax2.axis('equal')
    ax2.legend(
        ethnicity_counts.keys(),
        loc='center left',
        bbox_to_anchor=(1, 0.5),
        title="Ethnicities"
    )
    st.pyplot(fig2)

# Second column for overall voting progress pie chart
with col2:
    st.subheader("Captains Voting Progress")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.pie(
        [votes_cast, votes_remaining],
        labels=["Voted", "Not Voted"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["#1f77b4", "#ff7f0e"]
    )
    ax1.axis('equal')
    st.pyplot(fig1)
