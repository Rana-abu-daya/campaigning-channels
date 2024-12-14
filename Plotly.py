import plotly.graph_objects as go
import streamlit as st

# Data setup for ethnicities and voting
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

# Data setup for captains
captain_votes = {
    'Bilal Riyad': 27,
    'Hasan Syed': 97,
    'Husain Mohammed': 160,
    'Mohamed Ahmed': 13,
    'Nazeer Ahmed': 9,
    'Samir Sarhan': 9
}

# Total number of valid voters and remaining votes
votes_cast = 315
votes_remaining = 423 - votes_cast

# First Pie Chart: Ethnicity distribution
fig_ethnicity = go.Figure(data=[go.Pie(
    labels=list(ethnicity_counts.keys()),
    values=list(ethnicity_counts.values()),
    hole=.3,
    pull=[0.1 if label == "Bangladesh" else 0 for label in ethnicity_counts.keys()],
)])
fig_ethnicity.update_layout(
    title_text="Voter Distribution by Ethnicity",
    annotations=[dict(text='Ethnicities', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

# Second Pie Chart: Voting progress
fig_voting_progress = go.Figure(data=[go.Pie(
    labels=["Votes Cast", "Votes Remaining"],
    values=[votes_cast, votes_remaining],
    hole=.3
)])
fig_voting_progress.update_layout(
    title_text="Overall Voting Progress",
    annotations=[dict(text='Voting', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

# Third Bar Chart: Captain votes
fig_captain_votes = go.Figure(data=[go.Bar(
    x=list(captain_votes.keys()),
    y=list(captain_votes.values()),
    text=list(captain_votes.values()),
    textposition='auto'
)])
fig_captain_votes.update_layout(
    title_text="Captain Voting Contributions",
    xaxis_title="Captains",
    yaxis_title="Votes"
)

# Streamlit integration
st.title("Captain Voting Statistics")

# Using columns to create a layout for side by side pie charts
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Voted Voters Distribution by Ethnicity")
    st.plotly_chart(fig_ethnicity, use_container_width=True)

with col2:
    st.subheader("Overall Voting Progress")
    st.plotly_chart(fig_voting_progress, use_container_width=True)

with col3:
    st.subheader("Captain Voting Contributions")
    st.plotly_chart(fig_captain_votes, use_container_width=True)

# Summary information
st.subheader("Summary Information")
st.write(f"Total Voters of Captains: 423")
st.write(f"Voted: {votes_cast}")
st.write(f"Not Voted: {votes_remaining}")
