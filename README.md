# RSCF-parser
It is necessary to write a parser for projects on the RSF website to generate tables for 2024 and 2025 in the following format: number; codeProject; nameProject; keyWords; author; mainCodeNumber; mainCodeTitle; dopCodeNumber; dopCodeTitle; dopCodeNumber2; dopCodeTitle2; competitionTitle; affiliation; organization; region; affil; grnti; find grnti.

The first parser module unloads a table for all projects for a given year into a separate Excel table. Then the second parser module opens a project card for each project number and takes the rest of the information from it and unloads it into a separate Excel table, combined with the first table.
