import streamlit as st

from chatbot.assistant import get_response
from security_tools.password_checker import check_password
from security_tools.hash_tool import generate_hash
from security_tools.url_checker import analyze_url
from security_tools.encoding_tool import encode_base64, decode_base64


st.set_page_config(
    page_title="CyberShield",
    page_icon="🛡️",
    layout="wide"
)


st.title("🛡️ CyberShield")
st.subheader("Cybersecurity Assistant Chatbot")

st.info(
    "Educational cybersecurity assistant for defensive security "
    "learning and basic analysis."
)


menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "Chatbot",
        "Password Checker",
        "Hash Generator",
        "URL Analyzer",
        "Base64 Tool"
    ]
)


# ---------------- CHATBOT ----------------

if menu == "Chatbot":

    st.header("💬 Cybersecurity Chatbot")

    question = st.text_input("Ask a cybersecurity question:")

    if st.button("Ask"):
        if question.strip():
            response = get_response(question)
            st.write(response)
        else:
            st.warning("Please enter a question.")

# ---------------- PASSWORD ----------------

elif menu == "Password Checker":

    st.header("🔐 Password Strength Checker")

    password = st.text_input(
        "Enter password:",
        type="password"
    )

    if st.button("Check Password"):

        if password:

            strength, feedback = check_password(password)

            st.subheader(f"Strength: {strength}")

            if feedback:

                st.write("Recommendations:")

                for item in feedback:
                    st.write("•", item)

            else:

                st.success(
                    "Password meets all basic complexity checks."
                )

        else:

            st.warning("Enter a password.")


# ---------------- HASH ----------------

elif menu == "Hash Generator":

    st.header("🔑 Hash Generator")

    text = st.text_input(
        "Enter text:"
    )

    if st.button("Generate Hash"):

        if text:

            hashes = generate_hash(text)

            for algorithm, value in hashes.items():

                st.write(f"**{algorithm}**")

                st.code(value)

        else:

            st.warning("Enter some text.")


# ---------------- URL ----------------

elif menu == "URL Analyzer":

    st.header("🌐 URL Analyzer")

    url = st.text_input(
        "Enter URL:",
        placeholder="https://example.com"
    )

    if st.button("Analyze URL"):

        if url:

            result = analyze_url(url)

            for key, value in result.items():

                if key == "Warnings":

                    st.write("### Warnings")

                    if value:

                        for warning in value:
                            st.warning(warning)

                    else:

                        st.success("No basic warnings detected.")

                else:

                    st.write(f"**{key}:** {value}")

        else:

            st.warning("Enter a URL.")


# ---------------- BASE64 ----------------

elif menu == "Base64 Tool":

    st.header("🔄 Base64 Encoder / Decoder")

    operation = st.radio(
        "Operation",
        ["Encode", "Decode"]
    )

    text = st.text_area(
        "Enter text:"
    )

    if st.button("Process"):

        if text:

            if operation == "Encode":

                result = encode_base64(text)

            else:

                result = decode_base64(text)

            st.code(result)

        else:

            st.warning("Enter some text.")
