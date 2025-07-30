# RSF Project Data Parsers

## Project Overview
This repository contains Python parsers designed to extract and process project data from the Russian Science Foundation (RSF) website. The primary goal is to generate comprehensive project tables for analysis purposes.

## Current Functionality
The system consists of two main parser modules:

### Module 1: Bulk Data Extraction
* Extracts comprehensive project data for a specified year
* Generates an initial Excel file containing:
  * Project number
  * Project code
  * Project name
  * Author information
  * Organization details
  * Region
  * Competition title
  * Affiliation data

### Module 2: Detailed Project Information
* Processes project numbers from the initial Excel file
* Retrieves detailed information from individual project pages
* Collects:
  * Keywords
  * GRNTI codes
  * Knowledge area classifications
* Merges extracted data with the initial dataset
* Exports the enriched dataset to a final Excel file

## Data Structure
The generated tables include the following fields:
* **number** (project number)
* **codeProject** (project code)
* **nameProject** (project title)
* **keyWords** (project keywords)
* **author** (project author)
* **mainCodeNumber/Title** (main classification code and title)
* **dopCodeNumber/Title** (additional classification codes and titles)
* **competitionTitle** (competition name)
* **affiliation** (author affiliation)
* **organization** (organization details)
* **region** (region information)
* **affil** (affiliation code)
* **grnti** (GRNTI classification)
* **find grnti** (additional GRNTI information)

## Future Development
Planned enhancements include:
* Development of a graphical user interface (GUI)
* Implementation of year-based data selection
* Creation of user-friendly controls for:
  * Full project table export (Excel format)
  * Separate keyword and classification export
  * Merged data export functionality

## Usage
The current parsers are fully functional and produce accurate results. The system is designed for automated data extraction and processing, providing researchers with structured project information for further analysis.

