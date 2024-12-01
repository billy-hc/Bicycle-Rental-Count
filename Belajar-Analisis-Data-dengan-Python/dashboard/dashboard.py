# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# LOAD DATA
@st.cache_resource
def load_data():
    data = pd.read_csv("dashboard\hour.csv")
    return data


data = load_data()

# TITLE DASHBOARD
# Set page title
st.title("Bike Share Dashboard")

# SIDEBAR
st.sidebar.title("Created By:")
st.sidebar.markdown("**• Nama: Nyoman Bagus William Ernilo Heria Chandra**")
st.sidebar.markdown("**• Email: nbwilliam.hc@gmail.com**")

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/drive/folders/1Uk2CDwEwimKPy395dDDqfA8rUc1WCTvI?usp=sharing)")

# VISUALIZATION
df_bsd_day = pd.read_csv("dashboard\day.csv")
df_bsd_hour = pd.read_csv("dashboard\hour.csv")
# df_bsd_day
df_bsd_day["dteday"] = pd.to_datetime(df_bsd_day["dteday"])
# df_bsd_hour
df_bsd_hour["dteday"] = pd.to_datetime(df_bsd_hour["dteday"])


## Question 1
st.subheader("1. What is the total number of bicycle rental count (cnt) for 2011 during winter (season 4)?")
# Filter: 2011 and Winter (season == 4)
filtered_data = df_bsd_day[(df_bsd_day["yr"] == 0) & (df_bsd_day["season"] == 4)]

# Filtered Bicycle Rental Count (cnt)
total_cnt = filtered_data["cnt"].sum()

# Plot Function
fig = px.bar(filtered_data, x='dteday', y='cnt', title='Winter 2011 Bicycle Rental Count')
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Bicycle Rental Count")

st.plotly_chart(fig, use_container_width=True)



st.subheader("2. How many rental bicycles were used on holidays (holidays = 0) during winter (season 4) in 2011?")
# Filter: 2011 (yr == 0) and Winter (season == 4), Holiday
filtered_data = df_bsd_day[(df_bsd_day["yr"] == 0) &
                           (df_bsd_day["season"] == 4) &
                           (df_bsd_day["holiday"] == 1)]

# Filtered Bicycle Rental Count
total_cnt = filtered_data["cnt"].sum()


# Plot Function
fig = px.bar(filtered_data, x='dteday', y='cnt', title='2011 Winter Holiday Bicycle Rental Count')
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Bicycle Rental Count")

st.plotly_chart(fig, use_container_width=True)


st.subheader("3. How to increase the number of rental bicycle count used by casual users on weekdays (weekday = 1)?")
# Filter: Casual Bike, Weekday
filtered_data = df_bsd_day[(df_bsd_day["workingday"] == 1) & (df_bsd_day["casual"] > 0)]

#Plot Function
fig = px.bar(filtered_data, x="weekday", y="casual", title="Weekdays casual bike rental count")
fig.update_xaxes(title="Weekdays")
fig.update_yaxes(title="Casual bike rental count")

st.plotly_chart(fig, use_container_width=True)


st.subheader("4. What is the effect of weather (weathersit) on the number of bicycle rental count (cnt) during winter (season 4)?")
# Filter Fall
filtered_data = df_bsd_day[df_bsd_day["season"] == 3]

# Plot Function
fig = px.bar(filtered_data, x="weathersit", y="cnt", title="Weather Situation on Bicycle Rental Count (Fall)")
fig.update_xaxes(title="Weather Situation (weathersit)")
fig.update_yaxes(title="Bicycle Rental Count (cnt)")

st.plotly_chart(fig, use_container_width=True)



st.subheader("5. What is the hourly distribution of bicycle rental count (cnt) on Christmas Day (holiday = 0) in 2011 (year = 0)?")
# Filter: Christmas (holiday == 0) 2011 (yr == 0)
filtered_data = df_bsd_hour[(df_bsd_hour["yr"] == 0) & 
                             (df_bsd_hour["holiday"] == 0)]

# Hourly bicycle rental count post-filtered
distribusi_per_jam = filtered_data.groupby("hr")["cnt"].sum()

#Plot Function
fig = px.bar(x=distribusi_per_jam.index, y=distribusi_per_jam.values,
             labels={'x': 'hr', 'cnt': 'Bicycle Rental Count'},
             title="Hourly Bicycle Rental Count on Christmas 2011")
fig.update_xaxes(title="Time")
fig.update_yaxes(title="Bicycle Rental Count")

st.plotly_chart(fig, use_container_width=True)

st.subheader("Conclusion")
st.markdown("1. What is the total number of bicycle rental count (cnt) for 2011 during winter (season 4)?\n"
            "2. How many rental bicycles were used on holidays (holidays = 0) during winter (season 4) in 2011?\n"
            "3. How to increase the number of rental bicycle count used by casual users on weekdays (weekday = 1)?\n"
            "4. What is the effect of weather (weathersit) on the number of bicycle rental count (cnt) during winter (season 4)?\n"
            "5. What is the hourly distribution of bicycle rental count (cnt) on Christmas Day (holiday = 0) in 2011 (year = 0)?\n")