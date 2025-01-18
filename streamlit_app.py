import streamlit as st
from database import get_user_role, fetch_data_for_role

def main():
    st.title("DocWire Application")

    # Simulated user login (replace with actual login system)
    username = st.text_input("Enter Username", key="username")
    if st.button("Login"):
        role = get_user_role(username)  # Fetch user role from database

        if role == "Vendor":
            vendor_dashboard(username)
        elif role == "Approver":
            approver_dashboard(username)
        elif role == "Admin":
            admin_dashboard(username)
        elif role == "Accountant":
            accountant_dashboard(username)
        else:
            st.error("Invalid user role or user not found.")

def vendor_dashboard(username):
    st.header("Vendor Dashboard")
    st.write(f"Welcome, {username}")
    # Add logic for vendors to submit data

def approver_dashboard(username):
    st.header("Approver Dashboard")
    st.write(f"Welcome, {username}")
    # Add logic for approvers to approve/reject data

def admin_dashboard(username):
    st.header("Admin Dashboard")
    st.write(f"Welcome, {username}")
    # Add logic for admins to manage users

def accountant_dashboard(username):
    st.header("Accountant Dashboard")
    st.write(f"Welcome, {username}")
    # Add logic for accountants to track data

if __name__ == "__main__":
    main()
