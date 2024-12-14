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


# Sample data
captains = ["Ali H Ali", "Bilal Riyad", "Hasan Syed", "Husain Mohammed", "Mohamed Ahmed", "Nazeer Ahmed", "Samir Sarhan"]
voted = [0, 27, 97, 160, 13, 9, 9]
all_statuses = [1, 34, 113, 230, 21, 11, 12]

# Create the figure
fig = go.Figure(data=[
go.Bar(name='All Voters', x=captains, y=all_statuses, marker_color='lightblue'),
    go.Bar(name='Voted Voters', x=captains, y=voted, marker_color='blue')

])

# Change the bar mode
fig.update_layout(
    barmode='group',
    title="Voted voter for each Captain Overview",
    xaxis_title="Captains",
    yaxis_title="Counts",
    legend_title="Categories"
)
st.plotly_chart(fig, use_container_width=True)



import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# Sample data in the form of a dictionary which should ideally come from a DataFrame for easier manipulation
data = {
    'Captain': ['Ali H Ali', 'Bilal Riyad', 'Bilal Riyad', 'Bilal Riyad', 'Hasan Syed', 'Hasan Syed', 'Hasan Syed', 'Husain Mohammed', 'Mohamed Ahmed', 'Mohamed Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Samir Sarhan'],
    'Ethnicity': ['Somalia', 'Egypt', 'Jordan', 'Palestine', 'Ethiopia', 'India', 'Pakistan', 'Bangladesh', 'Bangladesh', 'Egypt', 'Brunei', 'Pakistan', 'Palestine', 'Saint Vincent and the Grenadines', 'Somalia', 'Palestine'],
    'Total Voters': [1, 2, 1, 31, 1, 12, 100, 229, 1, 20, 1, 2, 6, 1, 1, 12],
    'Voted': [0, 2, 1, 24, 1, 11, 85, 160, 0, 13, 1, 2, 5, 0, 1, 9]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Grouping the data by 'Captain' and 'Ethnicity' and create a bar for each group
fig = go.Figure()

for captain in df['Captain'].unique():
    captain_data = df[df['Captain'] == captain]
    fig.add_trace(go.Bar(
        x=captain_data['Ethnicity'],
        y=captain_data['Total Voters'],
        name=f'Total Voters - {captain}',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=captain_data['Ethnicity'],
        y=captain_data['Voted'],
        name=f'Voted - {captain}',
        marker_color='lightblue'
    ))

# Update layout for clear visualization
fig.update_layout(
    barmode='group',
    title="Voting Details by Captain and Ethnicity",
    xaxis_title="Ethnicity",
    yaxis_title="Number of Voters",
    legend_title="Group",
    xaxis={'categoryorder':'total descending'}
)

# Display this plot in Streamlit
st.title("Detailed Voting Analysis by Captain and Ethnicity")
st.plotly_chart(fig, use_container_width=True)

import pandas as pd
import plotly.express as px
import streamlit as st

# Sample data setup
data = {
    'Captain': ['Ali H Ali', 'Bilal Riyad', 'Bilal Riyad', 'Bilal Riyad', 'Hasan Syed', 'Hasan Syed', 'Hasan Syed', 'Husain Mohammed', 'Mohamed Ahmed', 'Mohamed Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Samir Sarhan'],
    'Ethnicity': ['Somalia', 'Egypt', 'Jordan', 'Palestine', 'Ethiopia', 'India', 'Pakistan', 'Bangladesh', 'Bangladesh', 'Egypt', 'Brunei', 'Pakistan', 'Palestine', 'Saint Vincent and the Grenadines', 'Somalia', 'Palestine'],
    'Voted': [0, 2, 1, 24, 1, 11, 85, 160, 0, 13, 1, 2, 5, 0, 1, 9]
}

df = pd.DataFrame(data)

# Streamlit app setup
st.title("Treemap Visualization of Captain Voting Statistics by Ethnicity")

# Generate a treemap for each captain
for captain in df['Captain'].unique():
    fig = px.treemap(
        df[df['Captain'] == captain],
        path=['Captain', 'Ethnicity'],  # Hierarchical levels: captain and ethnicity
        values='Voted',
        title=f"Voting Distribution for {captain}"
    )
    st.plotly_chart(fig, use_container_width=True)


# Summary Information
st.subheader("Summary Information")
st.write("This analysis covers the flow of voters from registration to actual voting, segmented by captain leadership and ethnic groups within the voter population.")
