## Simple Python Function to Get Failed Jobs from Jenkins
``` python
import requests  # Library to make HTTP requests

def get_failed_jobs(jenkins_url, username=None, password=None):
    # Form the API URL to get the list of all jobs
    jobs_api_url = f"{jenkins_url}/api/json"

    # Make the request to Jenkins API
    response = requests.get(jobs_api_url, auth=(username, password) if username and password else None)
    
    if response.status_code != 200:
        print("Failed to connect to Jenkins API.")
        return []

    # Get the list of jobs from the response
    jobs = response.json().get('jobs', [])
    failed_jobs = []

    # Loop through the jobs to find failed ones
    for job in jobs:
        # Get details of the last build for each job
        last_build_api_url = f"{job['url']}lastBuild/api/json"
        last_build_response = requests.get(last_build_api_url, auth=(username, password) if username and password else None)

        if last_build_response.status_code == 200:
            last_build_data = last_build_response.json()
            # Check if the last build result is 'FAILURE'
            if last_build_data.get('result') == 'FAILURE':
                failed_jobs.append(job['name'])

    return failed_jobs

# Example usage
jenkins_url = 'http://your-jenkins-url'  # Replace with your Jenkins URL
username = 'your-username'  # Optional: Jenkins username for authentication
password = 'your-password'  # Optional: Jenkins password or API token for authentication

failed_jobs = get_failed_jobs(jenkins_url, username, password)
print("Failed jobs:", failed_jobs)
```

Simplified Explanation:
Import requests:

We use this library to make HTTP requests.
Function Definition:

get_failed_jobs(jenkins_url, username=None, password=None):
Takes the Jenkins URL and optional username and password.
Form the API URL:

We create the URL to get the list of jobs by adding /api/json to the Jenkins URL.
Make the HTTP Request:

Use requests.get() to fetch the list of jobs from Jenkins.
If credentials are provided, they are included for authentication.
Check for a Successful Response:

If the request is not successful, print an error message and return an empty list.
Get the Jobs List:

Extract the list of jobs from the response.
Find Failed Jobs:

For each job, get the URL for its last build details.
Request the last build details and check if the result is FAILURE.
If it is, add the job's name to the list of failed jobs.
Return the List of Failed Jobs:

The function returns the names of all jobs that have failed.
Key Points:
This script directly interacts with Jenkins' REST API to get job statuses.
It is simplified by focusing on just fetching the necessary data and checking the status.
Optional authentication is included to handle Jenkins servers that require login.
How to Use:
Replace the Placeholder Values:

Change jenkins_url, username, and password to match your Jenkins setup.
Run the Script:

It will print the list of jobs that have failed their last build.
