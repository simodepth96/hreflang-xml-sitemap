import streamlit as st
import pandas as pd
from datetime import datetime
import os
import base64 

def generate_hreflang_sitemap(df, use_language_region):
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
            
            # Add xhtml:link elements based on user choice
            if use_language_region:
                alternate_values = row[["Language", "Region"]]
            else:
                alternate_values = row[["Language", "Region"]].apply(lambda x: x if x != "none" else None)
            
            # Add xhtml:link elements
            for col, value in alternate_values.items():
                if value:
                    f.write(f'  <xhtml:link rel="alternate" hreflang="{value}" href="{row["URL"]}"/>\n')
            
            # Add X-Default
            x_default_value = row["X-Default"]
            if x_default_value != "none":
                f.write(f'  <xhtml:link rel="alternate" hreflang="x-default" href="{x_default_value}"/>\n')
            
            f.write(f'  <lastmod>{today_date}</lastmod>\n</url>\n')

        f.write(sitemap_footer)

    st.success("hreflang XML sitemap generated successfully.")
    return output_file_path

# Streamlit UI
st.title("Hreflang XML Sitemap Generator")

# Introduction
st.markdown("""
This Streamlit app generates an hreflang XML sitemap based on the provided XLSX or CSV file. 
Ensure your file includes columns 'URL', 'Language', 'Region', and 'X-Default'.
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

    # Checkbox for user choice
    use_language_region = st.checkbox("Use both Language and Region for alternate versions")

    # Generate hreflang sitemap on button click
    if st.button("Generate Hreflang Sitemap"):
        output_file_path = generate_hreflang_sitemap(df, use_language_region)

        # Download link for XML
        st.markdown("### Download XML Sitemap")
        st.markdown(f"Click the link below to download the generated hreflang XML sitemap.")
        
        # Generate a download link
        with open(output_file_path, 'rb') as f:
            st.markdown(f'<a href="data:application/xml;base64,{base64.b64encode(f.read()).decode()}" download="hreflang_sitemap.xml">Download hreflang_sitemap.xml</a>', unsafe_allow_html=True)
