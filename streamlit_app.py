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
import streamlit as st
import matplotlib.pyplot as plt

# Fixed values for voters and votes
total_voters = 423  # Total voters for captains
votes_cast = 315    # Number of votes cast (Accepted or Challenged)
votes_remaining = total_voters - votes_cast

# Example captain vote data (you can replace this with real data or customize it)
captain_votes = {
    "Captain A": 100,
    "Captain B": 80,
    "Captain C": 70,
    "Captain D": 65
}

# Display pie chart for overall voting progress
st.title("Captain Voting Statistics")

fig1, ax1 = plt.subplots()
ax1.pie(
    [votes_cast, votes_remaining],
    labels=["Votes Cast", "Votes Remaining"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#1f77b4", "#ff7f0e"]
)
ax1.axis("equal")  # Equal aspect ratio ensures pie chart is circular.
st.pyplot(fig1)

# Pie chart for captain votes
if captain_votes:
    st.subheader("Votes by Captain")
    fig2, ax2 = plt.subplots()
    ax2.pie(
        captain_votes.values(),
        labels=captain_votes.keys(),
        autopct="%1.1f%%",
        startangle=90,
        colors=["#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    )
    ax2.axis("equal")
    st.pyplot(fig2)

# Summary
st.write(f"Total Voters: {total_voters}")
st.write(f"Votes Cast: {votes_cast}")
st.write(f"Votes Remaining: {votes_remaining}")
