import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="🚗 Car Crashes Dashboard", layout="wide")


# --- Load Data ---
df = sns.load_dataset("car_crashes")

# --- Sidebar: Filters & Calculator ---
st.sidebar.header("🔍 Filter Options")

# Multiselect state filter
selected_states = st.sidebar.multiselect(
    "Select States:", options=df['abbrev'].unique(), default=df['abbrev'].unique()
)

# Filtered data
filtered_df = df[df['abbrev'].isin(selected_states)]

# Crash Risk Calculator
st.sidebar.header("🚦 Crash Risk Calculator")
premium = st.sidebar.slider("Insurance Premium ($)", 400, 1300, 800)
alcohol_rate = st.sidebar.slider("Alcohol Rate (%)", 0, 10, 5)

risk_score = (premium * 0.01) + (alcohol_rate * 2)
st.sidebar.metric("Estimated Crash Risk Score", f"{risk_score:.2f}")

# --- Dashboard Title ---
st.title("🚘 US Car Crashes Dashboard")
st.markdown("**Dataset Source:** Seaborn `car_crashes` | Filtered by selected states.")

# --- KPI Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("📊 Avg Crashes", f"{filtered_df['total'].mean():.2f}")
col2.metric("💰 Max Premium", f"${filtered_df['ins_premium'].max():.2f}")
col3.metric("🍷 Avg Alcohol Involvement", f"{filtered_df['alcohol'].mean():.2f}")

# --- Tabs for Charts ---
tab1, tab2, tab3 = st.tabs(["🚗 Crash Overview", "📉 Insurance & Alcohol", "🧪 Correlations"])

# ---------------- Tab 1 ----------------
with tab1:
    st.subheader("1️⃣ Total Crashes per State")
    fig1 = px.bar(filtered_df, x='abbrev', y='total', title="Total Crashes by State", labels={'abbrev': 'State'})
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("2️⃣ Speeding vs Total Crashes")
    fig2 = px.scatter(filtered_df, x='speeding', y='total', size='total', color='abbrev',
                      title="Speeding Contribution to Total Crashes")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("3️⃣ Not Distracted vs Total Crashes")
    fig3 = px.scatter(filtered_df, x='not_distracted', y='total', color='abbrev',
                      title="Not Distracted vs Total Crashes (Lower = More Distraction)")
    st.plotly_chart(fig3, use_container_width=True)

# ---------------- Tab 2 ----------------
with tab2:
    st.subheader("4️⃣ Insurance Premium vs Losses")
    fig4 = px.scatter(filtered_df, x='ins_premium', y='ins_losses', color='abbrev',
                      title="Premium vs Insurance Losses",
                      hover_data=['total', 'alcohol', 'speeding'])
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("5️⃣ Alcohol Involvement per State")
    fig5 = px.bar(filtered_df.sort_values(by='alcohol', ascending=False), x='abbrev', y='alcohol',
                  title="Alcohol-Related Accidents by State")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("6️⃣ Insurance Premium Distribution")
    fig6 = px.box(filtered_df, y='ins_premium', title="Insurance Premium Spread by State")
    st.plotly_chart(fig6, use_container_width=True)

# ---------------- Tab 3 ----------------
with tab3:
    st.subheader("7️⃣ Correlation Heatmap")
    corr = filtered_df.select_dtypes(include='number').corr()
    fig7 = px.imshow(corr, text_auto=True, title="Correlation Matrix of Features")
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("8️⃣ Total Accidents Distribution")
    fig8 = px.histogram(filtered_df, x='total', nbins=15, title="Histogram of Total Accidents")
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("9️⃣ Top 10 States by Insurance Losses")
    top10 = filtered_df.sort_values(by='ins_losses', ascending=False).head(10)
    fig9 = px.bar(top10, x='abbrev', y='ins_losses', title="Top 10 States with Highest Insurance Losses")
    st.plotly_chart(fig9, use_container_width=True)

    st.subheader("🔟 Pairwise Feature Comparison")
    fig10 = px.scatter_matrix(filtered_df,
                              dimensions=['total', 'speeding', 'alcohol', 'ins_premium', 'ins_losses'],
                              color='abbrev', title="Scatter Matrix of Key Features")
    st.plotly_chart(fig10, use_container_width=True)

# --- Download Button ---
st.download_button("📥 Download Filtered Data as CSV",
                   data=filtered_df.to_csv(index=False),
                   file_name="car_crashes_filtered.csv",
                   mime="text/csv")