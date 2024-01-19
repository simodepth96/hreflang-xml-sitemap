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
</li>



The app allows users to generate an hreflang XML sitemap for websites targeting:

<ul>
  1. Language and Region
</ul>
<ul>
  2. Only a Language or a Region
</ul>

### Language and Region - Example Input

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://github.com/simodepth96/hreflang-xml-sitemap/blob/525c5c398833d648ac5581ed9ee27a14eb1d89ad/both.png">
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

Find more at my [SEO Toolstation]([https://seodepths.com/tools-for-seo/)
