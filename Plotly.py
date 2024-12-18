import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as px
from math import ceil

st.set_page_config(layout="wide")
st.title("Campaigns Voting Analysis")
st.header("Captain Voting")
# Captains and their votes
captain_votes = {
    'Bilal Riyad': 27,
    'Hasan Syed': 97,
    'Husain Mohammed': 160,
    'Mohamed Ahmed': 13,
    'Nazeer Ahmed': 9,
    'Samir Sarhan': 9
}

# # Total voters and those who voted
# total_voters = 423
# voted = 315
# VotedNovNOTAUG = 165
# # Funnel chart for captains
# fig_captains = go.Figure()
#
# fig_captains.add_trace(go.Funnel(
#     name = 'Voting Progress',
#     y = ["Total Voters", "Voted"],
#     x = [total_voters, voted],
#     textinfo = "value+percent previous"
# ))
#
# fig_captains.add_trace(go.Funnel(
#     name = 'By Captains',
#     y = list(captain_votes.keys()),
#     x = list(captain_votes.values()),
#     textinfo = "value+percent total"
# ))
#
# fig_captains.update_layout(title_text="Voting Funnel for Captains")
# st.plotly_chart(fig_captains, use_container_width=True, key='captains_chart')


# Data for the campaign
total_voters = 423
voted = 315
voted_nov_not_aug = 165

# Creating the funnel chart
fig = go.Figure()

# Total Voters to Voted
fig.add_trace(go.Funnel(
    name='Total to Voted',
    y=["Total Voters", "Voted", "Voted in Nov (Not Aug)"],
    x=[total_voters, voted, voted_nov_not_aug],
    text=[
        f"Total Voters: {total_voters} (100%)",
        f"Voted: {voted} ({ceil(voted / total_voters * 100)}%)",
        f"Voted in Nov (Not Aug): {voted_nov_not_aug} ({ceil(voted_nov_not_aug / total_voters * 100)}%)"
    ],
    textposition="inside"
))

fig.update_layout(
    title="Voting Progression Analysis",
    funnelmode="stack"  # This setting will align all parts of the funnel vertically
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

################# Captain and Ethnicity
# # Sample data
# captains = ["Ali H Ali", "Bilal Riyad", "Hasan Syed", "Husain Mohammed", "Mohamed Ahmed", "Nazeer Ahmed", "Samir Sarhan"]
# voted = [0, 27, 97, 160, 13, 9, 9]
# all_statuses = [1, 34, 113, 230, 21, 11, 12]
#
# # Create the figure
# fig = go.Figure(data=[
# go.Bar(name='Approached Voters', x=captains, y=all_statuses, marker_color='lightblue'),
#     go.Bar(name='Voted Voters', x=captains, y=voted, marker_color='blue')
#
# ])
#
# # Change the bar mode
# fig.update_layout(
#     barmode='group',
#     title="Voted voter for each Captain Overview",
#     xaxis_title="Captains",
#     yaxis_title="Counts",
#     legend_title="Categories"
# )
# st.plotly_chart(fig, use_container_width=True)


# Captain data
data = {
    'Ali H Ali': {'Total': 1, 'Voted in Nov': 0, 'Voted in Nov & Not Voted in Aug': 0},
    'Bilal Riyad': {'Total': 34, 'Voted in Nov': 27, 'Voted in Nov & Not Voted in Aug': 23},
    'Hasan Syed': {'Total': 113, 'Voted in Nov': 97, 'Voted in Nov & Not Voted in Aug': 44},
    'Husain Mohammed': {'Total': 230, 'Voted in Nov': 160, 'Voted in Nov & Not Voted in Aug': 87},
    'Mohamed Ahmed': {'Total': 21, 'Voted in Nov': 13, 'Voted in Nov & Not Voted in Aug': 5},
    'Nazeer Ahmed': {'Total': 11, 'Voted in Nov': 9, 'Voted in Nov & Not Voted in Aug': 1}
}

# Streamlit title and setup
st.header("Captain-Specific Voting Analysis")

# Iterate over each captain's data to create separate funnel charts
for index, (captain, values) in enumerate(data.items()):
    total = values['Total']
    voted_nov = values['Voted in Nov']
    voted_nov_not_aug = values['Voted in Nov & Not Voted in Aug']

    # Calculate percentages
    percent_voted_nov = ceil(voted_nov / total * 100) if total > 0 else 0
    percent_voted_nov_not_aug = ceil(voted_nov_not_aug / total * 100) if total > 0 else 0

    # Creating funnel chart for each captain
    fig = go.Figure(go.Funnel(
        y=["Total", "Voted in Nov", "Voted in Nov & Not Voted in Aug"],
        x=[total, voted_nov, voted_nov_not_aug],
        text=[f"(100%)",
              f"({percent_voted_nov}%)",
              f" ({percent_voted_nov_not_aug}%)"],
        textposition="inside"
    ))

    fig.update_layout(title=f"Voting Funnel for {captain}")

    # Use Streamlit columns to display two charts per row
    if index % 2 == 0:
        col1, col2 = st.columns(2)

    with col1 if index % 2 == 0 else col2:
        st.plotly_chart(fig, use_container_width=True)

############ Rana
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
st.header('Voting Percentages by Captain and Ethnicity')

# Generating the Bar Chart
fig = px.bar(
    df,  # Filter out entries where Voted is zero for visual aesthetics
    x="Captain",
    y="Visual Length",  # Use the normalized length for display
    color="Ethnicity",
    text="Percentage",  # Display computed percentages on the bars
    title="Votes by Captain and Ethnicity"
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

####################  phone bakning


# Specific results data
total_calls = 8244
failed_calls = 7364
completed_calls = 880
completed_calls_long_duration = 607  # Assuming 'Duration (Seconds)' >= 16

# Streamlit App Setup
st.title("Phone Banking Campaign Analysis")

# Creating the funnel chart
fig = go.Figure()

# Adding total calls
fig.add_trace(go.Funnel(
    name="Total Calls",
    y=["Total Calls"],
    x=[total_calls],
    text=[f"(100%)"],
    textposition="inside"
))

# Adding failed calls
fig.add_trace(go.Funnel(
    name="Failed Calls",
    y=["Failed Calls"],
    x=[failed_calls],
    text=[f"({ceil(failed_calls / total_calls * 100)}%)"],
    textposition="inside"
))

# Adding completed calls
fig.add_trace(go.Funnel(
    name="Completed Calls",
    y=["Completed Calls"],
    x=[completed_calls],
    text=[f"({ceil(completed_calls / total_calls * 100)}%)"],
    textposition="inside"
))

# Adding completed calls with long duration
fig.add_trace(go.Funnel(
    name="Long Duration Completed Calls",
    y=["Long Duration Completed Calls"],
    x=[completed_calls_long_duration],
    text=[f"({ceil(completed_calls_long_duration / total_calls * 100)}%)"],
    textposition="inside"
))

fig.update_layout(
    title="Detailed Analysis of Phone Banking Campaign Results",
    funnelmode="stack"
)

# Display the funnel chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

############# Failed pie chart #############


# Call data including failed categories and completed
call_data = {
    'machine_detection': 5381,
    'hungup': 26,
    'failed': 1144,
    'completed': 880,
    'no-answer': 573,
    'busy': 194,
    'declined': 46

}

# Calculate total failed by subtracting completed from total
total_failed = sum(value for key, value in call_data.items() if key != 'completed')

# Streamlit App Setup

# Creating the pie chart for failed call types
failed_labels = [key for key in call_data if key != 'completed']
failed_values = [value for key, value in call_data.items() if key != 'completed']

fig_pie = go.Figure(data=[go.Pie(
    labels=failed_labels,
    values=failed_values,
    hoverinfo='label+percent',
    textinfo='label+percent',
    hole=.4  # Creating a donut-style pie chart
)])

fig_pie.update_layout(
    title="Breakdown of Failed Calls",
    annotations=[{
        'text': f'{total_failed}',
        'showarrow': False,
        'font': {'size': 22}
    }]
)

# Display the pie chart in Streamlit
st.plotly_chart(fig_pie, use_container_width=True)



# Data for the completed call analysis
total_completed = 880
completed_duration_16 = 607
muslim_voted = 247
muslim_voted_nov_not_aug = 195



# Creating the funnel chart
fig = go.Figure()

# Adding total completed calls
fig.add_trace(go.Funnel(
    name='Total Completed Calls',
    y=["Total Completed Calls", "Long Duration >= 16s", "Muslims Voted", "Muslims Voted in Nov (Not Aug)"],
    x=[total_completed, completed_duration_16, muslim_voted, muslim_voted_nov_not_aug],
    text=[
        f"(100%)",
        f"({ceil(completed_duration_16 / total_completed * 100)}%)",
        f"({ceil(muslim_voted / total_completed * 100)}%)",
        f"({ceil(muslim_voted_nov_not_aug / total_completed * 100)}%)"
    ],
    textposition="inside"
))

# Update layout settings to enhance the visual
fig.update_layout(
    title="Analysis of Completed Calls",
    funnelmode="stack"  # Ensures the funnel segments are displayed in a stacked format
)

# Display the funnel chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


##############  End PHone banking



################### text 1


# Data for Text 1 campaign
total_texts = 29125
muslim_texted = 6405
muslim_votes = 3304

# Streamlit App Setup
st.title("Text 1 Campaign Analysis")
st.subheader("Effectiveness of Campaign Targeting Muslims")

# Creating the funnel chart with updated text information
fig = go.Figure(go.Funnel(
    y=["Total Texts Sent", "Muslims Texted", "Muslims Voted"],
    x=[total_texts, muslim_texted, muslim_votes],
    textposition="inside",
    # Updated to include percentages directly in the text
    text=[f"Total Texts Sent:  (100%)",
          f"Muslims Texted:  ({muslim_texted / total_texts * 100:.2f}%)",
          f"Muslims Voted:  ({muslim_votes / total_texts * 100:.2f}%)"],
    hoverinfo="none"  # Optionally disable hover to keep the chart cleaner
))

fig.update_layout(
    title="Conversion from Texts to Votes",
    # Adjusting the layout to make the text more readable
    funnelgap=0.1,  # Adjust the space between segments
    funnelgroupgap=0.1  # Adjust the space between groups
)

fig.update_layout(title="Conversion from Texts to Votes")
st.plotly_chart(fig, use_container_width=True)



# Subheader and column setup
col1, col2 = st.columns(2)

# First Pie Chart: Percentage of Muslims texted
with col1:
    st.subheader("Percentage of Muslims Texted")
    labels = ['Muslims Texted', 'Others Texted']
    values = [muslim_texted, total_texts - muslim_texted]
    colors = ['lightgreen', 'grey']

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+percent')
    fig1.update_layout(title_text="Muslims Texted vs Total Texts")

    st.plotly_chart(fig1, use_container_width=True)

# Second Pie Chart: Percentage of Muslims who voted from those texted
with col2:
    st.subheader("Percentage of Muslims Voted from Texted")
    labels = ['Muslims Voted', 'Muslims Not Voted']
    values = [muslim_votes, muslim_texted - muslim_votes]
    colors = ['lightcoral', 'lightgrey']

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    fig2.update_traces(marker=dict(colors=colors), textinfo='label+percent')
    fig2.update_layout(title_text="Muslim Voting Rate Among Texted")

    st.plotly_chart(fig2, use_container_width=True)

# Summary information
st.write("Summary Information")
st.write(f"Total Texts Sent: {total_texts:,}")
st.write(f"Total Muslims Texted: {muslim_texted:,}")
st.write(f"Total Muslims Voted: {muslim_votes:,}")



########################3 text 2

# Data for Text 2 campaign
total_texts = 12090
muslim_texted = 7177
muslim_votes = 3488

# Streamlit App Setup
st.title("Text 2 Campaign Analysis")
st.subheader("Effectiveness of Campaign Targeting Muslims")

# Creating the funnel chart with hovertemplate for more detailed hover text
# Creating the funnel chart with updated text information
fig = go.Figure(go.Funnel(
    y=["Total Texts Sent", "Muslims Texted", "Muslims Voted"],
    x=[total_texts, muslim_texted, muslim_votes],
    textposition="inside",
    # Updated to include percentages directly in the text
    text=[f"Total Texts Sent:  (100%)",
          f"Muslims Texted:  ({muslim_texted / total_texts * 100:.2f}%)",
          f"Muslims Voted:  ({muslim_votes / total_texts * 100:.2f}%)"],
    hoverinfo="none"  # Optionally disable hover to keep the chart cleaner
))

fig.update_layout(
    title="Conversion from Texts to Votes",
    # Adjusting the layout to make the text more readable
    funnelgap=0.1,  # Adjust the space between segments
    funnelgroupgap=0.1  # Adjust the space between groups
)
fig.update_layout(title="Conversion from Texts to Votes")
st.plotly_chart(fig, use_container_width=True)

# Subheader and column setup
col1, col2 = st.columns(2)

# First Pie Chart: Percentage of Muslims texted
with col1:
    st.subheader("Percentage of Muslims Texted")
    labels = ['Muslims Texted', 'Others Texted']
    values = [muslim_texted, total_texts - muslim_texted]
    colors = ['lightgreen', 'grey']

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+percent')
    fig1.update_layout(title_text="Muslims Texted vs Total Texts")

    st.plotly_chart(fig1, use_container_width=True)

# Second Pie Chart: Percentage of Muslims who voted from those texted
with col2:
    st.subheader("Percentage of Muslims Voted from Texted")
    labels = ['Muslims Voted', 'Muslims Not Voted']
    values = [muslim_votes, muslim_texted - muslim_votes]
    colors = ['lightcoral', 'lightgrey']

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    fig2.update_traces(marker=dict(colors=colors), textinfo='label+percent')
    fig2.update_layout(title_text="Muslim Voting Rate Among Texted")

    st.plotly_chart(fig2, use_container_width=True)

# Summary information
st.write("Summary Information")
st.write(f"Total Texts Sent: {total_texts:,}")
st.write(f"Total Muslims Texted: {muslim_texted:,}")
st.write(f"Total Muslims Voted: {muslim_votes:,}")
