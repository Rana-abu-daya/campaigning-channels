import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as px

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
go.Bar(name='Approached Voters', x=captains, y=all_statuses, marker_color='lightblue'),
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


# Sample data setup
data = {
    'Captain': ['Ali H Ali', 'Bilal Riyad', 'Bilal Riyad', 'Bilal Riyad', 'Hasan Syed', 'Hasan Syed', 'Hasan Syed', 'Husain Mohammed', 'Mohamed Ahmed', 'Mohamed Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Nazeer Ahmed', 'Samir Sarhan'],
    'Ethnicity': ['Somalia', 'Egypt', 'Jordan', 'Palestine', 'Ethiopia', 'India', 'Pakistan', 'Bangladesh', 'Bangladesh', 'Egypt', 'Brunei', 'Pakistan', 'Palestine', 'Saint Vincent and the Grenadines', 'Somalia', 'Palestine'],
    'Voted': [0, 2, 1, 24, 1, 11, 85, 160, 0, 13, 1, 2, 5, 0, 1, 9]
}

df = pd.DataFrame(data)

# Calculate total votes per captain for percentage calculations
df['Total Votes by Captain'] = df.groupby('Captain')['Voted'].transform('sum')

# Calculate percentage of total votes for each ethnicity per captain
df['Percentage'] = (df['Voted'] / df['Total Votes by Captain'] * 100).round(2).astype(str) + '%'

# Handle zeros by setting a minimal visual length for aesthetic reasons (e.g., 1)
df['Visual Length'] = df['Voted'].apply(lambda x: 1 if x > 0 else 0)

# Streamlit App Setup
st.title('Uniform Bar Lengths with Voting Percentages by Captain and Ethnicity')

# Generating the Bar Chart
fig = px.bar(
    df[df['Voted'] > 0],  # Filter out entries where Voted is zero for visual aesthetics
    x="Captain",
    y="Visual Length",  # Use the normalized length for display
    color="Ethnicity",
    text="Percentage",  # Display computed percentages on the bars
    title="Votes by Captain and Ethnicity (Uniform Bar Lengths)"
)

# Update layout for text inside bars and hover info for actual votes
fig.update_traces(
    textposition='inside',
    hoverinfo="text",
    hovertext=df['Voted']
)

# Update y-axis to not show misleading values since bars are uniform
fig.update_yaxes(showticklabels=False, title='')

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Summary Information
st.subheader("Summary Information")
st.write("This analysis covers the flow of voters from registration to actual voting, segmented by captain leadership and ethnic groups within the voter population.")
