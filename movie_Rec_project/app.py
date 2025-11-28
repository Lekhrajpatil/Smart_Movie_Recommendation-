import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Smart Movie Recommendation", page_icon="🎬", layout="wide")

data = pd.read_csv("movie_data_for_app.csv")
df = pd.read_csv("movie_dataframe_for_app.csv")
sig = joblib.load("sig_for_app.pkl")
tfv = joblib.load("tfidf_vectorizer.pkl")

def recommend(movie):
    if movie not in df['original_title'].unique():
        return []
    idx = df[df['original_title'] == movie].index[0]
    scores = list(enumerate(sig[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]
    recs = []
    for i, _ in sorted_scores:
        recs.append({
            "title": df.iloc[i]['original_title'],
            "id": df.iloc[i]['id'],
            "rating": df.iloc[i]['vote_average'],
            "overview": df.iloc[i]['overview'],
            "genres": df.iloc[i]['genres']
        })
    return recs

st.markdown("""
<h1 style='text-align:center; font-weight:800; font-size:45px; color:#00e1ff;'>
🎬 Smart Movie Recommendation
</h1>
<h4 style='text-align:center; color:#bbbbbb; margin-top:-10px;'>
Your personal AI movie assistant
</h4>
<br>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 Choose a Movie")
    movie_list = df['original_title'].values
    selected_movie = st.selectbox("", movie_list)
    btn = st.button("✨ Recommend Movies")

with col2:
    if btn:
        recs = recommend(selected_movie)
        if len(recs) == 0:
            st.error("Movie not found")
        else:
            st.markdown("### 🎥 Top Recommendations")
            for r in recs:
                c1, c2 = st.columns([1, 3])
                with c1:
                    # Display movie emoji as placeholder since poster_path is not available
                    st.markdown(f"<div style='text-align:center; font-size:120px;'>🎬</div>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<h3 style='color:#00e1ff'>{r['title']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"⭐ **Rating:** {r['rating']:.1f}")
                    st.markdown(f"🎭 **Genres:** {r['genres']}")
                    overview = str(r['overview']) if pd.notna(r['overview']) else "No overview available"
                    st.markdown(f"📝 **Overview:** {overview[:300]}{'...' if len(overview) > 300 else ''}")

st.markdown("<br><div style='text-align:center; color:#777;'>Powered by Smart AI</div>", unsafe_allow_html=True)
