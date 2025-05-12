
import streamlit as st
import json
import string
import random
import os
import time

st.set_page_config(page_title="Secure Data App", page_icon="🔐", layout="centered")

st.markdown("""
   <style>
        body {
            background-color: #fdfdfd;
            color: #333;
        }

        /* Sidebar Area */
        .stSidebar {
            background: linear-gradient(135deg, #ff9f45, #d24a7f) !important; /* Same as the button gradient */
            color: #fff;
        }

        .stSidebar nav {
            background: transparent !important;
        }

        section[data-testid="stSidebar"] label[data-baseweb="radio"] > div {
            color: #fff !important; /* Lighter text for readability */
            font-weight: 600;
            padding-left: 0.5rem;
            transition: all 0.3s ease;
            border-left: 4px solid transparent;
        }

        section[data-testid="stSidebar"] label[data-baseweb="radio"] > div:has(input:checked) {
            border-left: 4px solid #fff;
            color: #fff;
        }

        .stSidebar h2, .stSidebar h3, .stSidebar h4 {
            color: #fff;
        }

        /* Main Area Buttons */
        .stButton button {
            background: linear-gradient(135deg, #ff9f45, #d24a7f) !important; /* Same gradient */
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.4rem;
            font-weight: 600;
            box-shadow: 0 4px 14px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
        }

        .stButton button:hover {
            background: linear-gradient(135deg, #d24a7f, #ff9f45) !important;
            transform: scale(1.03) !important;
            color: #fff;
        }

        /* Input Fields */
        .stTextInput>div>div>input {
            background-color: #fafafa;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 0.5rem;
            color: #333;
        }

        .stTextInput>div>div>input:focus {
            border: 1px solid #d24a7f;
            outline: none;
        }

        h1, h2, h3, h4 {
            color: #d24a7f;
        }
    </style>
""", unsafe_allow_html=True)

FILE_NAME = "data.json"

def random_key():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

add_selectbox = st.sidebar.radio("Choose The Box: ", ("Register/Login", "Generate_Key", "Enter Data/See Data"))

if add_selectbox == "Register/Login":
    st.title("Register/Login Your Self 🚫")

    def register(email, password):
        if not email or not password:
            return "Please Enter Both Email and Password!"
        if email in data:
            return "User Already Exist!"
        data[email] = {"password": password, "passkey": "", "data": []}
        save_data(data)
        return "User Registered Successfully!"

    def login(email, password):
        if not email or not password:
            return "Please Enter Both Email and Password"
        if email in data and data[email]["password"] == password:
            st.session_state["user"] = email
            return "User Login Successfully"

    user_email = st.text_input("Enter Your Email: ").strip()
    user_password = st.text_input("Enter Your Password: ", type="password").strip()

    if st.button("Register Now"):
        reg = register(user_email, user_password)
        st.info(reg)

    if st.button("Login Now"):
        log = login(user_email, user_password)
        if log:
            st.success(log)
        else:
            st.error("Invalid Credentials")

elif add_selectbox == "Generate_Key":
    if "user" not in st.session_state:
        st.error("Please Login Or Register First")
    else:
        email = st.session_state["user"]
        st.title("Generate Your Key!")
        if st.button("Generate_Key") and not data[email]["passkey"]:
            key_generate = random_key()
            data[email]["passkey"] = key_generate
            save_data(data)
            st.success(data[email]["passkey"])
            st.warning("Key is just for 10 sec. Copy it or it will disappear!")
            time.sleep(10)
            st.rerun()
        elif data[email]["passkey"]:
            st.info("Key already generated")

elif add_selectbox == "Enter Data/See Data":
    if "user" not in st.session_state:
        st.error("Please Login Or Register First")
    else:
        email = st.session_state["user"]
        st.subheader("Enter Your Data!")
        user_input = st.text_input("Enter Your Data To Save")
        if st.button("Save Data?"):
            if user_input.strip() != "":
                data[email]["data"].append(user_input)
                save_data(data)
                st.success("Data Saved Successfully!")
            else:
                st.error("Please Enter Something!")

        st.subheader("See Your Data!")
        if "attempt" not in st.session_state:
            st.session_state["attempt"] = 5

        user_passkey = st.text_input("Enter Your Passkey!").strip()

        if st.button("Submit Passkey!"):
            if st.session_state["attempt"] > 0:
                if user_passkey:
                    if data[email]["passkey"] != user_passkey:
                        st.session_state["attempt"] -= 1
                        st.warning(f"Wrong passkey! You have {st.session_state['attempt']} attempts left.")
                    else:
                        st.header("Your Data:")
                        for idx, i in enumerate(data[email]["data"], start=1):
                            st.write(f"{idx}: {i}")
                else:
                    st.error("Please enter a passkey.")
            else:
                st.error("No attempts left. Access denied!")
