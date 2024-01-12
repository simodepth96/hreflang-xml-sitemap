import streamlit as st
import pandas as pd
from datetime import datetime
import os
import base64 

def generate_hreflang_sitemap(df):
    # Define sitemap header and footer
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    sitemap_footer = '</urlset>'

    # Save output to a single XML file
    output_file_path = 'hreflang_sitemap.xml'
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_header)

        # Process each row and append to the same file
        for _, row in df.iterrows():
            today_date = datetime.today().strftime('%Y-%m-%d')
            f.write(f'<url>\n  <loc>{row["URL"]}</loc>\n')
            
            # Add xhtml:link elements
            for _, link_row in df.iterrows():
                f.write(f'  <xhtml:link rel="alternate" hreflang="{link_row["Language"]}-{link_row["Region"]}" href="{link_row["URL"]}"/>\n')
            
            f.write(f'  <xhtml:link rel="alternate" hreflang="x-default" href="{row["URL"]}"/>\n  <lastmod>{today_date}</lastmod>\n</url>\n')

        f.write(sitemap_footer)

    st.success("hreflang XML sitemap generated successfully.")
    return output_file_path

# Streamlit UI
st.title("Hreflang XML Sitemap Generator")

# Introduction
st.markdown("""
This Streamlit app generates an hreflang XML sitemap based on the provided XLSX or CSV file. 
Ensure your file includes columns 'URL', 'Language', and 'Region' and has a single URL with alternate versions by tab (i.e. sheet if Excel)
""")

# File upload
file = st.file_uploader("Upload XLSX or CSV file", type=["xlsx", "csv"])

if file is not None:
    st.write("File Uploaded Successfully!")

    # Read the file content
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    # Display file content
    st.dataframe(df)

    # Generate hreflang sitemap on button click
    if st.button("Generate Hreflang Sitemap"):
        output_file_path = generate_hreflang_sitemap(df)

        # Download link for XML
        st.markdown("### Download XML Sitemap")
        st.markdown(f"Click the link below to download the generated hreflang XML sitemap.")
        
        # Generate a download link
        with open(output_file_path, 'rb') as f:
            st.markdown(f'<a href="data:application/xml;base64,{base64.b64encode(f.read()).decode()}" download="hreflang_sitemap.xml">Download hreflang_sitemap.xml</a>', unsafe_allow_html=True)
