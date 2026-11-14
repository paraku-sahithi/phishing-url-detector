
import streamlit as st
from urllib.parse import urlparse

def check_phishing_url(url):
    suspicious_words = ["login", "verify", "password", "banking", "update"]
    score = 0
    reasons = []

    if url.lower().startswith("http://"):
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    if "@" in url:
        score += 1
        reasons.append("Contains @ symbol")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    for word in suspicious_words:
        if word in domain:
            score += 1
            reasons.append("Contains suspicious word: " + word)

    return score, reasons, domain

st.title("Phishing URL Detector")
st.write("Check a website URL for suspicious patterns.")

url = st.text_input("Enter website URL:")

if st.button("Analyze URL"):
    if url.strip():
        score, reasons, domain = check_phishing_url(url)

        st.write("Domain:", domain)
        st.write("Risk Score:", score)

        if score >= 2:
            st.error("SUSPICIOUS URL")
        else:
            st.success("NO OBVIOUS WARNING SIGNS")

        if reasons:
            st.write("Reasons:")
            for reason in reasons:
                st.write("-", reason)
    else:
        st.warning("Please enter a URL.")
