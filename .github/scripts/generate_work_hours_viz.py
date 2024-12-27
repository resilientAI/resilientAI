import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# GitHub API endpoint
api_url = "https://api.github.com/repos/{owner}/{repo}/commits"

# Your GitHub username and repository name
owner = "resilientAI"
repo = "resilientAI"

# GitHub token for authentication
github_token = os.environ['GITHUB_TOKEN']

# Headers for API request
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Get commits for the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Make API request
params = {
    "since": start_date.isoformat(),
    "until": end_date.isoformat()
}
response = requests.get(api_url.format(owner=owner, repo=repo), headers=headers, params=params)
commits = response.json()

# Process commit data
work_hours = [0] * 24
for commit in commits:
    commit_time = datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
    work_hours[commit_time.hour] += 1

# Create visualization
plt.figure(figsize=(12, 6))
plt.bar(range(24), work_hours)
plt.title("Work Hours Distribution (Last 30 Days)")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Commits")
plt.xticks(range(0, 24, 2))
plt.savefig('work_hours_viz.png')
