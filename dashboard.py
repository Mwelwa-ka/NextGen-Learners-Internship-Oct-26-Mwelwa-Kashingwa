# Mwelwa Kashingwa
# NextGen Learners Internship October batch 01
# Week 3 — Intermediate: SQL + Program Performance Dashboard


import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

# Connects to the SQLite database, loads applicant, intern and hackathon score data into DataFrames, and filters all three datasets by the selected domain.
db_path = Path(__file__).parent / "nextgen.db"

st.write("Database being used:", db_path.resolve())

conn = sqlite3.connect(db_path)

applicants = pd.read_sql("SELECT * FROM applicants;", conn)
interns = pd.read_sql("SELECT * FROM interns;", conn)
scores = pd.read_sql("SELECT * FROM hackathon_scores;", conn)

conn.close()

st.write("Latest applicant data:")
st.dataframe(applicants[['applicant_id', 'name']])


st.title("NextGen Learners Dashboard")


domain_list = ['All'] + sorted(applicants['domain'].unique().tolist())

selected_domain = st.selectbox('Filter by Domain', domain_list)

if selected_domain != 'All':
    applicants_filtered = applicants[
        applicants['domain'] == selected_domain
    ]

    interns_filtered = interns[
        interns['domain'] == selected_domain
    ]

    scores_filtered = scores[
        scores['domain'] == selected_domain
    ]

else:
    applicants_filtered = applicants
    interns_filtered = interns
    scores_filtered = scores


#  FUNNEL: TOTAL APPLICANTS VS INTERNS


st.header("Programme Funnel")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Applicants", len(applicants_filtered))

with col2:
    st.metric(
        "Total Interns",
        interns_filtered['intern_id'].nunique()
    )


# COMPLETION RATE PER DOMAIN


st.header("Completion Rate per Domain")

completion = interns_filtered.groupby('domain').agg(
    total_interns=('intern_id', 'nunique'),
    completed=('completion_status', lambda x: (x == 'Completed').sum())
).reset_index()

completion['completion_rate'] = (
    completion['completed'] / completion['total_interns'] * 100
)

completion_chart = completion.set_index('domain')[['completion_rate']]

st.bar_chart(
    completion_chart,
    y_label="Completion Rate (%)",
    x_label="Domain"
)


# AVERAGE HACKATHON SCORE PER DOMAIN


st.header("Average Hackathon Score per Domain")

average_scores = scores_filtered.groupby('domain')['score'].mean().reset_index()
average_scores = average_scores.set_index('domain')

st.bar_chart(
    average_scores,
    y_label="Average Hackathon Score (out of 100)",
    x_label="Domain"
)


# LEADERBOARD: TOP 10 PERFORMERS


st.header("Top 10 Hackathon Performers")

leaderboard = scores.merge(
    interns[['intern_id', 'applicant_id']],
    on='intern_id',
    how='left'
).merge(
    applicants[['applicant_id', 'name']],
    on='applicant_id',
    how='left'
)

if selected_domain != 'All':
    leaderboard = leaderboard[
        leaderboard['domain'] == selected_domain
    ]

leaderboard = leaderboard.sort_values(
    by='score',
    ascending=False
).head(10)

leaderboard = leaderboard[
    ['name', 'domain', 'score']
]

st.dataframe(leaderboard, hide_index=True)
