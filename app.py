import streamlit as st
import joblib
import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse

# Model, scaler, aur feature columns load karo
model = joblib.load('phishing_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_cols = joblib.load('feature_columns.pkl')

shortening_services = ['bit.ly', 'goo.gl', 'tinyurl', 't.co', 'ow.ly', 'is.gd', 'buff.ly']
suspicious_keywords = ['login', 'verify', 'secure', 'account', 'bank', 'update',
                        'confirm', 'signin', 'password', 'security']

def extract_features(url):
    features = {}
    url = url.replace('https://', '').replace('http://', '')
    if url.startswith('www.'):
        url = url[4:]
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_at'] = url.count('@')
    features['num_question'] = url.count('?')
    features['num_equal'] = url.count('=')
    features['num_underscore'] = url.count('_')
    features['num_slash'] = url.count('/')
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['digit_ratio'] = features['num_digits'] / features['url_length'] if features['url_length'] > 0 else 0
    url_lower = url.lower()
    features['suspicious_keyword_count'] = sum(1 for kw in suspicious_keywords if kw in url_lower)
    features['is_shortened'] = 1 if any(s in url_lower for s in shortening_services) else 0
    try:
        domain = urlparse(url if url.startswith('http') else 'http://' + url).netloc
        features['num_subdomains'] = domain.count('.')
    except:
        features['num_subdomains'] = 0
    features['url_length_log'] = np.log1p(features['url_length'])
    return features

st.title("🔗 Malicious URL Detector")
st.write("Koi bhi URL daalo aur pata karo ke wo safe hai ya malicious (phishing/malware/defacement).")

user_url = st.text_input("URL yahan daalo (jaise: bit.ly/xyz123 ya google.com)")

if st.button("Check URL"):
    if user_url.strip() == "":
        st.warning("Pehle koi URL likho.")
    else:
        feats = extract_features(user_url)
        input_df = pd.DataFrame([feats])[feature_cols]
        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            st.error(f"⚠️ Ye URL MALICIOUS ho sakta hai (Risk: {probability:.1%})")
        else:
            st.success(f"✅ Ye URL SAFE lagta hai (Risk: {probability:.1%})")