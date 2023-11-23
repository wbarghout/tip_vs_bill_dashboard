# importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title= "Tips Dashboard",
                   page_icon= None,
                   layout= "wide",
                   initial_sidebar_state= "expanded")

# uploading data
df = pd.read_csv("tips.csv")

# sidebar
st.sidebar.header("Tips DashBoard")
st.sidebar.image("tips.jpg")
st.sidebar.write("This dashboard is using Tips dataset from seaborn for educational purposes")
st.sidebar.write("")
st.sidebar.write("Filter your data: ")
cat_filter = st.sidebar.selectbox("Categorical Filtering", [None, "sex", "smoker", "day", "time"])
num_filter = st.sidebar.selectbox("Numerical Filtering", [None, "total_bill", "tip"])
row_filter = st.sidebar.selectbox("Row Filtering", [None, "sex", "smoker", "day", "time"])
col_filter = st.sidebar.selectbox("Column Filtering", [None, "sex", "smoker", "day", "time"])

st.sidebar.write("")
st.sidebar.markdown("Made With :writing_hand: by Eng. [Walid Barghot](https://www.linkedin.com/in/walid-barghot-6b5278243/)")


# Dashboard body
# row a
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max. Tota Bill", df["total_bill"].max())
a2.metric("Max. Tip", df["tip"].max())
a3.metric("Min. Tota Bill", df["total_bill"].min())
a4.metric("Min. Tip", df["tip"].min())

# row b
st.subheader("Total Bill Vs. Tips")
fig = px.scatter(df, x = "total_bill", y = "tip", color= cat_filter, size= num_filter, facet_row= row_filter, facet_col= col_filter)
st.plotly_chart(fig, use_container_width= True)

# row c
c1, c2, c3 = st.columns((4,3,3))
with c1:
    st.text("Sex Vs. Total Bill")
    fig = px.bar(df, x= "sex", y= "total_bill", color= cat_filter)
    st.plotly_chart(fig, use_container_width= True)

with c2:
    st.text("Smokers / None Smokers Vs. Tips")
    fig = px.pie(df, names= "smoker", values= "tip")
    st.plotly_chart(fig, use_container_width= True)

with c3:
    st.text("Days Vs. Tips")
    fig = px.pie(df, names= "day", values= "tip", hole= 0.3)
    st.plotly_chart(fig, use_container_width= True)
