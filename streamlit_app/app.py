import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from pathlib import Path
# Resolve project root directory safely (works locally + cloud)
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ola | Analytics & Forecasting",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* Global Readability Improvements */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #000000 !important;
    }

    /* Refine table readability: headers, cells, hover & selection */
    [data-testid="stDataFrame"] table thead th, 
    [data-testid="stDataFrame"] [role="columnheader"] {
        color: #000000 !important;
        background-color: #f8fafc !important;
        font-weight: 800 !important;
    }
    
    [data-testid="stDataFrame"] [role="gridcell"], 
    [data-testid="stDataFrame"] [role="row"] {
        color: #000000 !important;
    }

    /* Ensure text remains black on hover and selection */
    [data-testid="stDataFrame"] div:hover, 
    [data-testid="stDataFrame"] .selected,
    [data-testid="stDataFrame"] [aria-selected="true"] {
        color: #000000 !important;
    }

    /* Fix expander (dropdown) title colors */
    [data-testid="stExpander"] p {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
    }

    /* Force Light Theme Colors */
    .stAppViewContainer {
        background-color: #f0f2f6 !important;
    }

    .stHeader {
        background-color: #f0f2f6 !important;
    }

    /* Section Card and description text */
    .section-card {
        background: #ffffff !important;
        padding: 2.5rem;
        border-radius: 16px;
        border: 2px solid #000000; /* Stronger border */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }

    .section-card h3 {
        color: #000000 !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-bottom: 1rem;
    }

    .section-card .subtext {
        color: #000000 !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        line-height: 1.6;
    }

    /* High-Contrast KPI Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        color: #000000 !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #000000 !important;
    }

    .stMetric {
        background: white !important;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 2px solid #000000;
    }

    /* High-Contrast Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: #f0f2f6;
    }

    .stTabs [data-baseweb="tab"] {
        height: 70px;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 25px;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        color: #4b5563; 
    }

    /* Fix yellow highlight - Change to charcoal selection */
    .stTabs [aria-selected="true"] {
        color: #000000 !important; 
        border-bottom: 4px solid #000000 !important;
        background-color: rgba(0,0,0,0.05) !important;
    }

    h1 { font-size: 2.8rem !important; font-weight: 900 !important; color: #000000 !important; }
    h2 { font-size: 2.22rem !important; font-weight: 800 !important; color: #000000 !important; }
    h4 { font-size: 1.6rem !important; font-weight: 800 !important; color: #000000 !important; margin-bottom: 1.2rem !important; }

    /* Footer Text */
    .footer-text {
        text-align: center;
        color: #4b5563;
        font-size: 1rem;
        font-weight: 500;
        padding: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([0.15, 0.85])

with col1:
    st.image("BASE_DIR/assets/download.png", width=130)

with col2:
    st.markdown("<h1 style='margin-bottom:0;'>Ola Analytics & Forecast Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#374151; font-size:1.2rem; font-weight:500;'>Operational performance today and predictive insights for tomorrow.</p>", unsafe_allow_html=True)

st.markdown("<hr style='margin:1.5rem 0; opacity:0.1; border-top: 1px solid #000;'>", unsafe_allow_html=True)

# ---------------- TABS ----------------
tab1, tab2 = st.tabs([
    "📊 Operational Dashboards",
    "🔮 Predictive Forecasting"
])

# ---------------- TAB 1 : POWER BI ----------------
with tab1:
    st.markdown("""
    <div class="section-card">
        <h3>Operational Insights</h3>
        <p class="subtext">
            Monitor real-time performance across bookings, cancellations, and revenue metrics. 
            Use the navigation within the dashboard to drill down into specific service areas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    powerbi_url = (
        "https://app.powerbi.com/view?"
        "r=eyJrIjoiNjc1N2UwMzUtOGUzMC00YWM3LThmYjQtOGRhNzQyOWNkY2ZiIiwidCI6"
        "ImE1MzE0YTU4LTFlNTYtNGM0Ni1hNWFjLTlkZGFiMTlkODVjOCJ9"
        "&pageView=fitToWidth"
    )

    st.components.v1.iframe(
        src=powerbi_url,
        height=850,
        scrolling=False
    )

# ---------------- TAB 2 : FORECAST ----------------
with tab2:
    st.markdown("""
    <div class="section-card">
        <h3>Demand & Revenue Projection</h3>
        <p class="subtext">
            Forecasted demand patterns for the next 6 months to assist in capacity planning and strategic decision-making. 
            These projections are based on historical seasonal trends and growth models.
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        file_path = "BASE_DIR/forecasting/forecast_output.csv"
        df = pd.read_csv(file_path)
        df['booking_date'] = pd.to_datetime(df['booking_date'])
        df['revenue_millions'] = df['forecast_revenue'] / 1_000_000
        
        # KPI Row
        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        avg_rides = int(df['forecast_rides'].mean())
        m1.metric("Avg. Monthly Rides", f"{avg_rides:,}")
        
        avg_rev = df['forecast_revenue'].mean()
        m2.metric("Avg. Monthly Revenue", f"₹{avg_rev/1e6:.2f}M")
        
        m3.metric("Forecast Horizon", f"{len(df)} Months")

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Charts Section
        c1, c2 = st.columns(2)

        # Common chart layout settings for high contrast
        chart_font = dict(family="Inter, sans-serif", size=14, color="#000000")
        
        with c1:
            st.markdown("#### Ride Demand Forecast")
            fig_rides = px.line(
                df, x='booking_date', y='forecast_rides',
                markers=True, line_shape='spline',
                color_discrete_sequence=['#d4e02b']
            )
            fig_rides.update_traces(
                line=dict(width=4),
                marker=dict(size=10, line=dict(width=2, color='black'))
            )
            fig_rides.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=chart_font,
                xaxis=dict(
                    title=dict(
                        text="Time Period (Months)",
                        font=dict(size=14, color="#000000")
                    ),
                    tickfont=dict(size=12, color="#000000"),
                    gridcolor="#e5e7eb"
                ),
                yaxis=dict(
                    title=dict(
                        text="Number of Rides",
                        font=dict(size=14, color="#000000")
                    ),
                    tickfont=dict(size=12, color="#000000"),
                    gridcolor="#e5e7eb",
                    range=[df['forecast_rides'].min() * 0.9, df['forecast_rides'].max() * 1.1]
                ),
                margin=dict(l=0, r=0, t=20, b=0)
            )
            st.plotly_chart(fig_rides, key="rides_chart_v5", use_container_width=True)

        with c2:
            st.markdown("#### Revenue Forecast (INR Millions)")
            fig_rev = px.line(
                df, x='booking_date', y='revenue_millions',
                markers=True, line_shape='spline',
                color_discrete_sequence=['#222222']
            )
            fig_rev.update_traces(
                line=dict(width=4),
                marker=dict(size=10, line=dict(width=2, color='#d4e02b'))
            )
            fig_rev.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=chart_font,
                xaxis=dict(
                    title=dict(
                        text="Time Period (Months)",
                        font=dict(size=14, color="#000000")
                    ),
                    tickfont=dict(size=12, color="#000000"),
                    gridcolor="#e5e7eb"
                ),
                yaxis=dict(
                    title=dict(
                        text="Revenue (INR Millions)",
                        font=dict(size=14, color="#000000")
                    ),
                    tickfont=dict(size=12, color="#000000"),
                    gridcolor="#e5e7eb",
                    range=[df['revenue_millions'].min() * 0.9, df['revenue_millions'].max() * 1.1]
                ),
                margin=dict(l=0, r=0, t=20, b=0)
            )
            st.plotly_chart(fig_rev, key="revenue_chart_v5", use_container_width=True)

        # Detailed Table
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📄 View Detailed Forecast Data Table"):
            st.dataframe(
                df.style.format({
                    'forecast_rides': '{:,}',
                    'forecast_revenue': '₹{:,.2f}',
                    'revenue_millions': '{:.2f}M'
                }),
                width='stretch'
            )

    except Exception as e:
        st.error(f"Error initializing forecast dashboard: {e}")

# ---------------- FOOTER ----------------
st.markdown("<br><hr style='opacity:0.1; border-top: 1px solid #000;'>", unsafe_allow_html=True)
st.markdown(
    "<div class='footer-text'>Ola Analytics Platform | Delivering Strategic Data Insights</div>",
    unsafe_allow_html=True
)

