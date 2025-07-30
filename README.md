# RSCF-parser
It is necessary to write a parser for projects on the RSF website to generate tables for 2024 and 2025 in the following format: number; codeProject; nameProject; keyWords; author; mainCodeNumber; mainCodeTitle; dopCodeNumber; dopCodeTitle; dopCodeNumber2; dopCodeTitle2; competitionTitle; affiliation; organization; region; affil; grnti; find grnti.

The first parser module unloads a table for all projects for a given year into a separate Excel table. 

Then the second parser module:
1) The parser takes data on project numbers from the final table rscf_projects_2024.xlsx
2) The parser substitutes project numbers under the URL: https://rscf.ru/project/"Project Number" thereby opening project cards
3) The parser takes information from the project card: keywords, GRNTI code, Knowledge Area and adds it to each project from the first table rscf_projects_2024.xlsx
4) A new table with new columns is exported - rscf_projects_2024.xlsx
