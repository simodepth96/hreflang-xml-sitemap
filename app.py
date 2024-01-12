import streamlit as st
import os
import pandas as pd
from datetime import datetime

def generate_hreflang_sitemap(file_path):
    xls = pd.ExcelFile(file_path)

    # Define sitemap header and footer
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    sitemap_footer = '</urlset>'

    # Save output to a single XML file
    output_file_path = 'hreflang_sitemap.xml'
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_header)

        # Process each sheet and append to the same file
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            
            for _, row in df.iterrows():
                today_date = datetime.today().strftime('%Y-%m-%d')
                f.write(f'<url>\n  <loc>{row["URL"]}</loc>\n')
                
                # Add xhtml:link elements
                for _, link_row in df.iterrows():
                    f.write(f'  <xhtml:link rel="alternate" hreflang="{link_row["Language"]}-{link_row["Region"]}" href="{link_row["URL"]}"/>\n')
                
                f.write(f'  <xhtml:link rel="alternate" hreflang="x-default" href="{row["URL"]}"/>\n  <lastmod>{today_date}</lastmod>\n</url>\n')

        f.write(sitemap_footer)

    st.success("hreflang XML sitemap generated successfully.")

# Streamlit UI
st.title("Hreflang XML Sitemap Generator")

# File upload
file = st.file_uploader("Upload XLSX or CSV file", type=["xlsx", "csv"])

if file is not None:
    st.write("File Uploaded Successfully!")

    # Display file content
    st.dataframe(pd.read_excel(file))  # You can change this line based on the file type

    # Generate hreflang sitemap on button click
    if st.button("Generate Hreflang Sitemap"):
        generate_hreflang_sitemap(file.name)
