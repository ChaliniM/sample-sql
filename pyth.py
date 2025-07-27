import streamlit as st
import pandas as pd
import plotly.express as px
#this is for displaying the csv formatted file
df=pd.read_csv(r"C:\Users\Chalini\Documents\Blogs\sample\export.csv")
st.title("Mini dashboard")
st.dataframe(df)
#map statsus_id to readable names
status_map={1:'Not Started', 2:'In Progress', 3:'Completed'}
df['STATUS']=df['STATUS_ID'].map(status_map)
st.title("Project task status dashboard")
st.subheader("Project Data Overview")
st.dataframe(df)
#pie chart of status distribution
status_counts=df['STATUS'].value_counts().reset_index()
status_counts.columns=['Status','Count']
fig = px.pie(
    status_counts,
    names='Status',
    values='Count',
    title='Task Status Distribution',
    color_discrete_sequence=px.colors.qualitative.Set3
)

st.plotly_chart(fig, use_container_width=True)
# Summary counts
st.subheader("Task Status Summary")
st.write(f" Completed Tasks: {df[df['STATUS'] == 'Completed'].shape[0]}")
st.write(f" In Progress Tasks: {df[df['STATUS'] == 'In Progress'].shape[0]}")
st.write(f" Not Started Tasks: {df[df['STATUS'] == 'Not Started'].shape[0]}")