import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="CLT Demo - Salaries", layout="wide")

st.title("📊 Central Limit Theorem Demo")
st.subheader("Using Data Scientist Salaries in India")

# Sidebar Controls
st.sidebar.header("Controls")
sample_size = st.sidebar.slider("Sample size (n)", 2, 50, 5)
num_samples = st.sidebar.slider("Number of samples", 10, 500, 100)

# Generate Skewed Salary Data
def generate_salaries(n=10000):
    salaries = np.random.lognormal(mean=2.3, sigma=0.6, size=n)
    return salaries * 2

if "population" not in st.session_state:
    st.session_state.population = generate_salaries()

population = st.session_state.population

# Show Population Distribution
st.markdown("## 🔴 Step 1: Population (Actual Salaries)")
fig1, ax1 = plt.subplots()
ax1.hist(population, bins=50)
ax1.set_title("Skewed Salary Distribution (Not Normal)")
ax1.set_xlabel("Salary (LPA)")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

st.info("👉 Real salaries are skewed: few very high earners, many mid/low salaries")

# Sampling Button
if st.button("🎯 Draw Samples and See CLT in Action"):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size)
        sample_means.append(np.mean(sample))
    sample_means = np.array(sample_means)

    st.markdown("## 🟢 Step 2: Distribution of Sample Means")
    fig2, ax2 = plt.subplots()
    ax2.hist(sample_means, bins=30)
    ax2.set_title("Distribution of Sample Means (Becomes Normal!)")
    ax2.set_xlabel("Average Salary (LPA)")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

    st.success("✨ Notice how this looks like a bell curve—even though the original data was skewed!")

# Reset Button
if st.button("🔄 Generate New Population"):
    st.session_state.population = generate_salaries()
    st.warning("New salary distribution generated!")
