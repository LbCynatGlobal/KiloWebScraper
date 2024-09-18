# KIlo-Scraper
![web](web.jpg)
# Cyber Security Job Scraper

This Python project fetches **entry-level cybersecurity** job listings from the [JSearch API on RapidAPI](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) and saves the results in a CSV file. The tool filters jobs that are remote and provides detailed information such as job title, company, description, employment type, and more.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [API Key](#api-key)
- [Usage](#usage)
- [Customization](#customization)
- [Output](#output)
- [Error Handling](#error-handling)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Features

- Fetches **entry-level cybersecurity** jobs from the JSearch API.
- Filters for **remote** job listings.
- Extracts details like title, description, company, location, etc.
- Configurable to retrieve multiple pages of job listings.
- Saves the results in a **CSV file** (`cyber_securityjobs.csv`).

## Prerequisites

Before running the project, ensure you have the following:

- **Python 3.x**
- Required Python packages:
  - `requests`
  - `csv`

Install the required packages using:

<!-- python code block -->
```python
pip install requests
```

### API Key
You need an API key from [RapidAPI's JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) to access job listings:

1. Sign up at [RapidAPI](https://rapidapi.com).
2. Subscribe to the JSearch API.
3. Obtain your API key and replace the placeholder key in the script.

## Usage

1. **Download the script**.

2. **Set up the API key**:
   Open the script and replace the placeholder API key in the `headers` dictionary with your actual API key:

   ```python
   headers = {
       "x-rapidapi-key": "YOUR_API_KEY_HERE", 
       "x-rapidapi-host": "jsearch.p.rapidapi.com"
   }
   ```

3. **Run the script**:
   To retrieve the job listings and save them to a CSV file, execute the script:

    ```python
      py KiloJsearchScraper.py
    ```

4. The script will output the job listings to a CSV file named `cyber_securityjobs.csv`.

### Customization

You can modify the query parameters in the script's `querystring` dictionary to tailor the job search:

```python
querystring = {
    "query": "entry level cyber security",
    "date_posted": "all",
    "remote_jobs_only": "true",
    "page": "1",
    "num_pages": "5"
}
```

- **query**: Modify the search term (e.g., "cybersecurity", "entry-level").
- **remote_jobs_only**: Set to `"true"` to fetch only remote jobs.
- **page** and **num_pages**: Adjust these to retrieve multiple pages of results.

## Output

The job listings are saved in a CSV file with the following columns:

- **Job Title**: Title of the job.
- **Description**: Brief description of the job.
- **Company**: Name of the hiring company.
- **Employer Logo**: URL of the company's logo.
- **Employer Website**: URL of the company's website.
- **Job Publisher**: The job publisher.
- **Employment Type**: Full-time, part-time, etc.
- **Location**: City and state of the job.
- **Remote**: Indicates if the job is remote.
- **Job Link**: URL to apply for the job.

[CSV file](cyber_securityjobs.csv)

## Error Handling

- **API Request Errors**: In case of network issues or invalid API responses, the script will print an error message.
- **JSON Parsing Errors**: If the response cannot be parsed into JSON, an error message will be displayed.

## Future Enhancements

- Add options to save in other formats like JSON.
- More advanced error handling.

## Credits
- Asha Cumberbatch
- Lathelia Brathwaite
