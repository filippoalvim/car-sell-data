import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')
car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])

# ── Section 1: Data viewer ──────────────────────────────────────────────────
st.header('Data viewer')

show_small = st.checkbox('Include manufacturers with less than 1000 ads', value=True)

if show_small:
    filtered = car_data.copy()
else:
    counts = car_data['manufacturer'].value_counts()
    filtered = car_data[car_data['manufacturer'].isin(counts[counts >= 1000].index)]

st.dataframe(filtered)

# ── Section 2: Vehicle types by manufacturer ────────────────────────────────
st.header('Vehicle types by manufacturer')

fig_bar = px.histogram(
    filtered,
    x='manufacturer',
    color='type',
    category_orders={'manufacturer': sorted(filtered['manufacturer'].unique())},
)
fig_bar.update_layout(xaxis_title='manufacturer', yaxis_title='count', bargap=0.1)
st.plotly_chart(fig_bar, use_container_width=True)

# ── Section 3: Histogram of condition vs model_year ─────────────────────────
st.markdown(
    "### Histogram of "
    "<span style='color:#19D3F3'>condition</span>"
    " vs "
    "<span style='color:#636EFA'>model_year</span>",
    unsafe_allow_html=True,
)

fig_hist = px.histogram(filtered, x='model_year', color='condition')
fig_hist.update_layout(xaxis_title='model_year', yaxis_title='count')
st.plotly_chart(fig_hist, use_container_width=True)

# ── Section 4: Compare price distribution between manufacturers ─────────────
st.header('Compare price distribution between manufacturers')

manufacturers = sorted(filtered['manufacturer'].unique())

m1 = st.selectbox('Select manufacturer 1', manufacturers,
                  index=manufacturers.index('chevrolet') if 'chevrolet' in manufacturers else 0)
m2 = st.selectbox('Select manufacturer 2', manufacturers,
                  index=manufacturers.index('hyundai') if 'hyundai' in manufacturers else 1)

normalize = st.checkbox('Normalize histogram')

compare = filtered[filtered['manufacturer'].isin([m1, m2])]

fig_compare = px.histogram(
    compare,
    x='price',
    color='manufacturer',
    barmode='overlay',
    opacity=0.7,
    histnorm='percent' if normalize else None,
)
fig_compare.update_layout(
    xaxis_title='price',
    yaxis_title='percent' if normalize else 'count',
)
st.plotly_chart(fig_compare, use_container_width=True)
