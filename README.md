# Hreflang XML Sitemap Generator

This app is designed to streamline the generation of XML sitemaps containing hreflang annotations.

## Requirements
An XLSX or a CSV file with the following properties: 

<li> 
  URL
</li>
<li>
  Language
</li> 
<li>
  Region
</li>
<li>
  X-Default
</li>.

The app allows users to generate an hreflang XML sitemap for websites targeting:

<ul>
  1. Language and Region
</ul>
<ul>
  2. Only a Language or a Region
</ul>

### Important
In case you are targeting a language that merely reflects the region, make sure to leave one of the Language and Region headers as <i><b>none</b></i> in your XLSX/CSV file.

### Language and Region - Example Input

If your target website targets both a Language and a Region, you're gonna need an input file that looks like the following Excel

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/e00fe36c874ab990041e89c4eef423e529d89650/both%20input.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/e00fe36c874ab990041e89c4eef423e529d89650/both%20input.png">
  <img
    alt=""
    src="https://github.com/simodepth96/hreflang-xml-sitemap/blob/e00fe36c874ab990041e89c4eef423e529d89650/both%20input.png"
    style="max-width: 100%; height: auto;">
</picture>


When uploading either the XLSX or the CSV file, you will choose to want to use both Language and Region


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png">
  <img alt="" src="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png"
    style="max-width: 100%; height: auto;">
</picture>

### Only Language or Region - Example Input

If your website only targets a language that is spoken in the same region, then your input file should look like the following

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none%20input.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none%20input.png">
  <img alt="" src="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none%20input.png"
    style="max-width: 100%; height: auto;">
</picture>

As mentioned in the requirements, make sure to leave one of the Language and Region headers as <i>none</i> to make the app work. 

When uploading either the XLSX or the CSV file, you will select <b>No</b> when asked if you want to use both Language and Region.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none.png">
  <img alt="" src="https://github.com/simodepth96/hreflang-xml-sitemap/blob/821c8bace9ba3d323db31702fd155c7891642385/none.png"
    style="max-width: 100%; height: auto;">
</picture>



## Changelog v.2

<li>
  Introduced option to select either Language and Region or only use one of them where values are not <i>none</i>. 
</li>
<li>
  Set x-default version as the specified value in the input file header (i.e. X-Default).
</li> 
<li> 
  Fixed a few bugs.
</li> 



## Changelog v.1

<li>
  Added lastmod attribute
</li> 
<li> 
  Added X-Default column to be read in
</li> 

Find more at my <a href="https://seodepths.com/tools-for-seo/" target_blank="">SEO Toolstation</a>
