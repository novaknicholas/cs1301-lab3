# Lab 3: API data page
# TODO: Rename this file to fit your page. Keep the number at the front, since it sets the
#       page's order in the sidebar (for example, 2_Pokedex.py).
#
# This page shows data from your API, processed with your own Python code. No AI on this page.
# It should have:
#   - at least 2 meaningful user inputs (for example st.selectbox, st.text_input, st.slider)
#   - at least 2 dynamic visuals that change based on the user's input: charts, displays of
#     images, or other visualizations (see the example website for examples!)

import streamlit as st
import csv
modelNames = []
applePhones = []
with open("Mobiles Dataset (2025).csv", encoding="cp1252", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Company Name"] == "Apple":
            modelNames.append(row["Model Name"])
            applePhones.append(row)

#label, options
iphone1 = st.selectbox("First iPhone", modelNames)
iphone2 = st.selectbox("Second iPhone", modelNames)

selectedPhone1 =  None
selectedPhone2 = None

for phone in applePhones:
    if phone["Model Name"] == iphone1:
        selectedPhone1 = phone
    if phone["Model Name"] == iphone2:
        selectedPhone2 = phone



if selectedPhone1 is not None and selectedPhone2 is not None:
    st.subheader("iPhone Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.write(selectedPhone1["Model Name"])
        st.write("RAM:", selectedPhone1["RAM"])
        st.write("Processor:", selectedPhone1["Processor"])
        st.write("Screen Size:", selectedPhone1["Screen Size"])

    with col2:
        st.write(selectedPhone2["Model Name"])
        st.write("RAM:", selectedPhone2["RAM"])
        st.write("Processor:", selectedPhone2["Processor"])
        st.write("Screen Size:", selectedPhone2["Screen Size"])

    ram1 = float(selectedPhone1["RAM"].replace("GB", ""))
    ram2 = float(selectedPhone2["RAM"].replace("GB", ""))

    screen1 = float(selectedPhone1["Screen Size"].replace(" inches", ""))
    screen2 = float(selectedPhone2["Screen Size"].replace(" inches", ""))

    #visualization 1, RAM
    st.subheader("RAM Comparison (GB)")
    st.bar_chart({
        "First iPhone:": [ram1],
        "Second iPhone": [ram2]
    })
    st.subheader("Screen Size Comparison (in)")
    st.bar_chart({
        "First iPhone:" [screen1],
        "Second iPhone:" [screen2]
    }) 



