pip install openpyxl
import pandas as pd
import streamlit as st
from datetime import datetime
import os

def generate_hreflang_sitemap(df):
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    sitemap_footer = '</urlset>'

    with open('hreflang_sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_header)
        for _, row in df.iterrows():
            today_date = datetime.today().strftime('%Y-%m-%d')
            f.write(f'<url>\n  <loc>{row["URL"]}</loc>\n{xhtml_row(row)}\n  <xhtml:link rel="alternate" hreflang="x-default" href="{row["URL"]}"/>\n  <lastmod>{today_date}</lastmod>\n</url>\n')
        f.write(sitemap_footer)

def xhtml_row(row):
    return '  '.join([f'<xhtml:link rel="alternate" hreflang="{row["Language"]}-{row["Region"]}" href="{row["URL"]}"/>'])

# Streamlit App
st.title("Hreflang XML Sitemap Generator")

# Upload CSV or Excel file
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read CSV or Excel based on file type
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    # Check if the file exists or generate it
    if not os.path.exists('hreflang_sitemap.xml'):
        generate_hreflang_sitemap(df)

    # Download link for XML
    st.markdown("### Download XML Sitemap")
    st.markdown("Click the link below to download the generated hreflang XML sitemap.")
    with open('hreflang_sitemap.xml', 'rb') as file:
        st.download_button(label='Download hreflang_sitemap.xml', data=file, key='download_button')

    # Show DataFrame
    st.markdown("### Preview of DataFrame")
    st.write(df.head())
else:
    st.warning("Please upload a CSV or Excel file.")
