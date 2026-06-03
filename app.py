import streamlit as st
import pandas as pd

# Load CSV data
df = pd.read_csv("task.csv") 

# Dashboard title
st.title("Task & Workflow Tracking System")

# Show task table
st.subheader("Task Details")
st.dataframe(df)

# Count completed tasks
completed_tasks = df[df["Status"] == "Completed"].shape[0]

# Show metric
st.metric("Completed Tasks", completed_tasks)

# Show task status chart
st.subheader("Task Status Overview")
st.bar_chart(df["Status"].value_counts())
