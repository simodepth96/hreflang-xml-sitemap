import streamlit as st
import pandas as pd
from datetime import datetime
import base64
from io import BytesIO


def generate_hreflang_sitemap(df, use_both):
    # Define sitemap header and footer
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    sitemap_footer = '</urlset>'

    # Generate XML in memory
    buffer = BytesIO()
    buffer.write(sitemap_header.encode('utf-8'))

    # Process each row
    for _, row in df.iterrows():
        today_date = datetime.today().strftime('%Y-%m-%d')
        buffer.write(f'<url>\n  <loc>{row["URL"]}</loc>\n'.encode('utf-8'))

        # Add alternate links
        for _, link_row in df.iterrows():
            if use_both:
                alternate_value = f'{link_row["Language"]}-{link_row["Region"]}' if link_row["Language"] != "none" and link_row["Region"] != "none" else "x-default"
            else:
                alternate_value = link_row["Language"] if link_row["Language"] != "none" else link_row["Region"]

            buffer.write(f'  <xhtml:link rel="alternate" hreflang="{alternate_value}" href="{link_row["URL"]}"/>\n'.encode('utf-8'))

        buffer.write(f'  <xhtml:link rel="alternate" hreflang="x-default" href="{row["X-Default"]}"/>\n  <lastmod>{today_date}</lastmod>\n</url>\n'.encode('utf-8'))

    buffer.write(sitemap_footer.encode('utf-8'))
    buffer.seek(0)  # Reset buffer position

    return buffer


# Streamlit UI
st.title("Hreflang XML Sitemap Generator")

st.markdown(
    "This app streamlines bulk hreflang markup implementation on an XML sitemap file for websites serving Language and/or Region based audiences."
    "In case you are targeting a language that merely reflects the region, make sure to leave one of the Language and Region headers as none in your XLSX/CSV file."
    )

# File Upload
file = st.file_uploader("Please, upload an XLSX or a CSV file with the following headers: URL, Language, Region, X-Default", type=["xlsx", "csv"])

if file is not None:
    st.write("File Uploaded Successfully!")

    # Read the file content
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    # Display file content
    st.dataframe(df)

    # User choice
    use_both = st.radio("Do you want to use both Language and Region?", options=["Yes", "No"]) == "Yes"

    # Generate sitemap on button click
    if st.button("Generate Hreflang Sitemap"):
        buffer = generate_hreflang_sitemap(df, use_both)

        # Provide download link for XML file
        st.markdown("### Download XML Sitemap")
        xml_data = buffer.getvalue()
        b64 = base64.b64encode(xml_data).decode()  # Encode XML to base64
        href = f'<a href="data:application/xml;base64,{b64}" download="hreflang_sitemap.xml">Download hreflang_sitemap.xml</a>'
        st.markdown(href, unsafe_allow_html=True)
