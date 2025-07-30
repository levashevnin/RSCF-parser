# RSCF Project Data Parsers

## Project Overview
This repository contains Python parsers designed to extract and process project data from the Russian Science Foundation (RSCF) website. The primary goal is to generate comprehensive project tables for analysis purposes.

## Current Functionality
The system consists of two main parser modules:

### Module 1: Bulk Data Extraction
* Extracts comprehensive project data for a specified year
* Generates an initial Excel file containing:
 * **No.** (project number identifier)
 * **Project Number** (unique project identifier)
 * **Title and Principal Investigator** (project title and project leader)
 * **Classification Codes** (project classification codes)
 * **Competition** (competition name)
 * **Organization and Region** (organization details and region)

### Module 2: Detailed Project Information
* Processes project numbers from the initial Excel file
* Retrieves detailed information from individual project pages
* Enriches data with additional fields:
 * **Keywords** (project keywords)
 * **GRNTI Code** (GRNTI classification code)
 * **Knowledge Area** (research area classification)
* Merges extracted data with the initial dataset
* Exports the enriched dataset to a final Excel file

## Data Structure

### Initial Table (Module 1)
| Field | Description |
|-------|-------------|
| **No.** | Project number identifier |
| **Project Number** | Unique project number |
| **Title and Principal Investigator** | Project title and project leader information |
| **Classification Codes** | Project classification codes |
| **Competition** | Competition name |
| **Organization and Region** | Organization details and region information |

### Enriched Table (Module 2)
| Field | Description |
|-------|-------------|
| **No.** | Project number identifier |
| **Project Number** | Unique project number |
| **Title and Principal Investigator** | Project title and project leader information |
| **Classification Codes** | Project classification codes |
| **Competition** | Competition name |
| **Organization and Region** | Organization details and region information |
| **Keywords** | Project keywords |
| **GRNTI Code** | GRNTI classification code |
| **Knowledge Area** | Research area classification |

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

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

