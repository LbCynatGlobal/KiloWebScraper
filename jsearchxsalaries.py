import requests
import csv

# Define the API endpoint and query parameters
url = "https://jsearch.p.rapidapi.com/search"
querystring = {
    "query": "entry level cyber security",
    "date_posted": "all",
    "remote_jobs_only": "true",  # Include remote jobs
    "page": "1", "num_pages": "5"
}

# Define the request headers
headers = {
    "x-rapidapi-key": "0beb7f2182mshdaa8d0a1d500f2ep1490ebjsnc5d5ee125d5d", 
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

# Function to retrieve and filter cybersecurity-related jobs from the API
def get_cyber_securityjobs():
    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for unsuccessful requests

        # Parse the JSON response
        data = response.json()

        # Print the response for debugging
        #print("API Response:", data)
        
        # Check if 'data' contains job listings
        if 'data' in data and isinstance(data['data'], list):
            jobs = data['data']
            print(f"Found {len(jobs)} jobs.")

            # Extract job details
            job_list = []
            for job in jobs:
                job_title = job.get('job_title', 'No Job Title Provided')
                job_description = job.get('job_description', 'No Description Provided')
                company = job.get('employer_name', 'No Company Provided')
                employer_logo = job.get('employer_logo', 'No Logo Provided')
                employer_website = job.get('employer_website', 'No Website Provided')
                job_publisher = job.get("job_publisher", "No Publisher")
                job_employment_type = job.get("job_employment_type", "No Employment Type")
                #job_posting_language = job.get('job_posting_language', 'Unknown')

                location = (job.get('job_city') or 'No City Provided') + ", " + (job.get('job_state') or 'No State Provided')
                job_link = job.get('job_apply_link', 'No Job Link Provided')

                # Determine remote status based on the API response
                remote = "Yes" if job.get('job_is_remote', False) else "No"

                job_list.append({
                    'Job Title': job_title,
                    'Description': job_description,
                    'Company': company,
                    'Employer Logo': employer_logo,
                    'Employer Website': employer_website,
                    'Job Publisher': job_publisher,
                    'Employment Type': job_employment_type,
                    #'Job Posting Language': job_posting_language,
                    'Location': location,
                    'Remote': remote,
                    'Job Link': job_link
                })
                print(f"Added job: {job_title}")
                
            return job_list
        else:
            print("Unexpected JSON structure or no jobs found.")
            return []

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return []

# Function to save jobs to a CSV file
def save_to_csv(jobs, filename="cyber_securityjobs.csv"):
    if jobs:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Job Title", "Description", "Company", "Employer Logo", "Employer Website", 
                "Job Publisher", "Employment Type", #"Job Posting Language", 
                "Location", 
                "Remote", "Job Link"
            ])

            for job in jobs:
                writer.writerow([
                    job['Job Title'],
                    job['Description'],
                    job['Company'],
                    job['Employer Logo'],
                    job['Employer Website'],
                    job['Job Publisher'],
                    job['Employment Type'],
                    #job['Job Posting Language'],
                    job['Location'],
                    job['Remote'],
                    job['Job Link']
                ])
        print(f"Successfully saved {len(jobs)} job listings to {filename}")
    else:
        print("No jobs to save.")

if __name__ == "__main__":
    # Retrieve and filter jobs
    cyber_securityjobs = get_cyber_securityjobs()

    # Save the filtered jobs to a CSV file
    save_to_csv(cyber_securityjobs)
