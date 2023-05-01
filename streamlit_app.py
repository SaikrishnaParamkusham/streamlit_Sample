import streamlit as st 
import pandas as pd
import base64

st.header("Equal Weighted Index Inputs")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Source", "Table", "Field", "Date"])

st.subheader("Data Block")

num_new_rows = st.number_input("Add the number of data pulls",1,50)
ncol = st.session_state.df.shape[1]  # col count
rw = -1

def update_table_options(source):
    table_options = []
    if source == "FNDB":
        table_options = ["equity_security_content", "equity_security_master", "giw_index_weight"]
    elif source == "SMAQ":
        table_options = ["marketcaptable", "pricetable", "otherfield"]
    elif source == "GESU":
        table_options = ["exampletableA", "exampletableB", "exampletableC"]
    return table_options

with st.form(key="add form", clear_on_submit= True):
    cols = st.columns(ncol)
    rwdta = []

    source = cols[0].selectbox("Source", ["FNDB", "SMAQ", "GESU"])
    table_options = update_table_options(source)
    table = cols[1].selectbox("Table", table_options)
    field_options = ["fullmarketcapusd", "freefloatfactorreuters", "micbb", "addtvusd3monthsreuters"]
    field = cols[2].multiselect("Field", field_options)
    date = cols[3].date_input(st.session_state.df.columns[3])

    rwdta = [source, table, field, date]

    if st.form_submit_button("Add"):
        if st.session_state.df.shape[0] == num_new_rows:
            st.error("Add row limit reached. Can't add any more records.")
        else:
            rw = st.session_state.df.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            st.session_state.df.loc[rw] = rwdta

            if st.session_state.df.shape[0] == num_new_rows:
                st.error("Add row limit reached.")


st.dataframe(st.session_state.df)

if st.button("Clear"):
    st.session_state.df = pd.DataFrame(columns=["Source", "Table", "Field", "Date"])

# if st.button("Download CSV"):
#     csv = st.session_state.df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV file</a>'
#     st.markdown(href, unsafe_allow_html=True)

if "df2" not in st.session_state:
    st.session_state.df2 = pd.DataFrame(columns=["Fields", "Transformation Type", "Assign To"])

st.subheader("Input Data transformation")

num_new_rows2 = st.number_input("Add the number of transformations", 1, 50)
ncol2 = st.session_state.df2.shape[1]
rw2 = -1

with st.form(key="add form 2", clear_on_submit=True):
    cols2 = st.columns(ncol2)
    rwdta2 = []

    field_options = ["fullmarketcapusd", "freefloatfactorreuters", "micbb", "addtvusd3monthsreuters"]
    fields = cols2[0].multiselect("Fields", field_options)
    transformation_options = ["add", "subtract", "multiply", "divide"]
    transformation_type = cols2[1].selectbox("Transformation Type", transformation_options)
    assign_to = cols2[2].text_input("Assign To")

    rwdta2 = [fields, transformation_type, assign_to]

    if st.form_submit_button("Add"):
        if st.session_state.df2.shape[0] == num_new_rows2:
            st.error("Add row limit reached. Can't add any more records.")
        else:
            rw2 = st.session_state.df2.shape[0] + 1
            st.info(f"Row: {rw2} / {num_new_rows2} added")
            st.session_state.df2.loc[rw2] = rwdta2

            if st.session_state.df2.shape[0] == num_new_rows2:
                st.error("Add row limit reached.")

st.dataframe(st.session_state.df2)

if st.button("Clear 2"):
    st.session_state.df2 = pd.DataFrame(columns=["Fields", "Transformation Type", "Assign To"])

# if st.button("Download CSV 2"):
#     csv2 = st.session_state.df2.to_csv(index=False)
#     b64_2 = base64.b64encode(csv2.encode()).decode()
#     href2 = f'<a href="data:file/csv;base64,{b64_2}" download="data2.csv">Download CSV file 2</a>'
#     st.markdown(href2, unsafe_allow_html=True)


if "df3" not in st.session_state:
    st.session_state.df3 = pd.DataFrame(columns=["Eligibility Field", "Operator", "Threshold", "Valid List"])

st.subheader("Eligibility Block")

num_new_rows3 = st.number_input("Add the number of filter conditions", 1, 50)
ncol3 = st.session_state.df3.shape[1]
rw3 = -1

with st.form(key="add form 3", clear_on_submit=True):
    cols3 = st.columns(ncol3)
    rwdta3 = []

    field_options = ["NA","fullmarketcapusd", "freefloatfactorreuters", "micbb", "addtvusd3monthsreuters"]
    eligibility_field = cols3[0].selectbox("Eligibility Field", field_options, index=0)
    operator = cols3[1].selectbox("Operator", ["NA", ">=", "=<", "==", ">", "<", "!=", "include", "exclude"], index=0)
    threshold = cols3[2].number_input("Threshold")
    valid_list = cols3[3].text_input("Valid List", value="NA")

    rwdta3 = [eligibility_field, operator, threshold, valid_list]

    if st.form_submit_button("Add"):
        if st.session_state.df3.shape[0] == num_new_rows3:
            st.error("Add row limit reached. Can't add any more records.")
        else:
            rw3 = st.session_state.df3.shape[0] + 1
            st.info(f"Row: {rw3} / {num_new_rows3} added")
            st.session_state.df3.loc[rw3] = rwdta3

            if st.session_state.df3.shape[0] == num_new_rows3:
                st.error("Add row limit reached.")


st.dataframe(st.session_state.df3)

if st.button("Clear 3"):
    st.session_state.df3 = pd.DataFrame(columns=["Eligibility Field", "Operator", "Threshold", "Valid List"])

# if st.button("Download CSV 3"):
#     csv3 = st.session_state.df3.to_csv(index=False)
#     b64_3 = base64.b64encode(csv3.encode()).decode()
#     href3 = f'<a href="data:file/csv;base64,{b64_3}" download="data3.csv">Download CSV file 3</a>'
#     st.markdown(href3, unsafe_allow_html=True)


if "df4" not in st.session_state:
    st.session_state.df4 = pd.DataFrame(columns=["Operation", "Field", "Operation Type", "Threshold", "Assign To"])

st.subheader("Selection Block")

num_new_rows = st.number_input("Add the number of steps for selection", 1, 50)
ncol = st.session_state.df4.shape[1]
rw = -1

with st.form(key="sales form", clear_on_submit=True):
    cols = st.columns(ncol)
    rwdta = []

    operation_options = ["NA", "rank", "select", "transform"]
    operation = cols[0].selectbox("Operation", operation_options, index=0)
    field = cols[1].text_input("Field")
    operation_type = cols[2].selectbox("Operation Type", ["Greater than", "Less than", "Equal to"])
    threshold = cols[3].number_input("Threshold", value=0)
    assign_to = cols[4].text_input("Assign To", value="NA")

    rwdta = [operation, field, operation_type, threshold, assign_to]

    if st.form_submit_button("Add"):
        if st.session_state.df4.shape[0] == num_new_rows:
            st.error("Add row limit reached. Can't add any more records.")
        else:
            rw = st.session_state.df4.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            st.session_state.df4.loc[rw] = rwdta

            if st.session_state.df4.shape[0] == num_new_rows:
                st.error("Add row limit reached.")


st.dataframe(st.session_state.df4)

if st.button("Clear 4"):
    st.session_state.df4 = pd.DataFrame(columns=["Operation", "Field", "Operation Type", "Threshold", "Assign To"])

# if st.button("Download CSV"):
#     csv = st.session_state.df4.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="sales_data.csv">Download Sales Data CSV file</a>'
#     st.markdown(href, unsafe_allow_html=True)

if "df5" not in st.session_state:
    st.session_state.df5 = pd.DataFrame(columns=["Weighting Type", "Based on Field", "Shares Adjustment"])

st.subheader("Weighting Block")

num_new_rows = st.number_input("Add the number of steps for weighting", 1, 50)
ncol = st.session_state.df5.shape[1]
rw = -1

with st.form(key="weather form", clear_on_submit=True):
    cols = st.columns(ncol)
    rwdta = []

    weighting_options = ["NA", "equalweighted", "multicap", "singlecap", "customcap"]
    weighting_type = cols[0].selectbox("Weighting Type", weighting_options, index=0)
    based_on_field = cols[1].text_input("Based on Field")
    shares_options = ["NA", "trilliondollar", "mcap", "custom"]
    shares_adjustment = cols[2].selectbox("Shares Adjustment", shares_options, index=0)

    rwdta = [weighting_type, based_on_field, shares_adjustment]

    if st.form_submit_button("Add"):
        if st.session_state.df5.shape[0] == num_new_rows:
            st.error("Add row limit reached. Can't add any more records.")
        else:
            rw = st.session_state.df5.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            st.session_state.df5.loc[rw] = rwdta

            if st.session_state.df5.shape[0] == num_new_rows:
                st.error("Add row limit reached.")

st.dataframe(st.session_state.df5)

if st.button("Clear 5"):
    st.session_state.df5 = pd.DataFrame(columns=["Weighting Type", "Based on Field", "Shares Adjustment"])

# if st.button("Download CSV"):
#     csv = st.session_state.df5.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="weather_data.csv">Download Weather Data CSV file</a>'
#     st.markdown(href, unsafe_allow_html=True)
