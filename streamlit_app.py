import streamlit as st
import psycopg2

# Set up the Streamlit app
st.title("DocWire Application")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "View Data", "Add Data"])

# Database connection
@st.cache_resource
def connect_to_db():
    conn = psycopg2.connect(
        dbname="docwire",
        user="docwire_user",
        password="Venkat@31",
        host="localhost",
        port=5432
    )
    return conn

if options == "Home":
    st.write("Welcome to the DocWire Application!")

elif options == "View Data":
    st.subheader("View Data")
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_general_users;")
        rows = cursor.fetchall()
        for row in rows:
            st.write(row)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

elif options == "Add Data":
    st.subheader("Add Data")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            query = "INSERT INTO tbl_general_users (email, password) VALUES (%s, %s);"
            cursor.execute(query, (email, password))
            conn.commit()
            st.success("Data added successfully!")
        except Exception as e:
            st.error(f"Error adding data: {e}")
