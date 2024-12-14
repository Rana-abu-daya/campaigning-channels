import plotly.graph_objects as go
import streamlit as st
st.set_page_config(layout="wide")
st.title("Campaigns Voting Analysis")
st.header("Captain Voting Funnel Chart")
# Captains and their votes
captain_votes = {
    'Bilal Riyad': 27,
    'Hasan Syed': 97,
    'Husain Mohammed': 160,
    'Mohamed Ahmed': 13,
    'Nazeer Ahmed': 9,
    'Samir Sarhan': 9
}

# Total voters and those who voted
total_voters = 423
voted = 315

# Funnel chart for captains
fig_captains = go.Figure()

fig_captains.add_trace(go.Funnel(
    name = 'Voting Progress',
    y = ["Total Voters", "Voted"],
    x = [total_voters, voted],
    textinfo = "value+percent previous"
))

fig_captains.add_trace(go.Funnel(
    name = 'By Captains',
    y = list(captain_votes.keys()),
    x = list(captain_votes.values()),
    textinfo = "value+percent total"
))

fig_captains.update_layout(title_text="Voting Funnel for Captains")
st.plotly_chart(fig_captains, use_container_width=True, key='captains_chart')

# Streamlit integration for Captains Funnel Chart
# Data setup for ethnicities
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

# Funnel chart for ethnicities
fig_ethnicities = go.Figure()

fig_ethnicities.add_trace(go.Funnel(
    name = 'Voting Progress',
    y = ["Total Voters", "Voted"],
    x = [total_voters, voted],
    textinfo = "value+percent previous"
))

fig_ethnicities.add_trace(go.Funnel(
    name = 'By Ethnicity',
    y = list(ethnicity_counts.keys()),
    x = list(ethnicity_counts.values()),
    textinfo = "value+percent total"
))
fig_ethnicities.update_layout(title_text="Voting Funnel by Ethnicity")




st.plotly_chart(fig_ethnicities, use_container_width=True, key='ethnicities_chart')

# Summary Information
st.subheader("Summary Information")
st.write("This analysis covers the flow of voters from registration to actual voting, segmented by captain leadership and ethnic groups within the voter population.")
