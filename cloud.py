import os
import re
import requests
from wordcloud import WordCloud
from dotenv import load_dotenv

# Load environment variables from .env file (if used)
load_dotenv()

# GitHub API token
github_token = os.getenv('GITHUB_TOKEN')

# Function to fetch issue titles from GitHub repository
def fetch_issue_titles(repo_owner, repo_name):
    url = f"https://api.github.com/repos/Shubhi/ShubhiiDixit/issues"
    headers = {
        'Authorization': f'token {github_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        issues = response.json()
        titles = [issue['title'] for issue in issues]
        return titles
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        return []

# Main function to generate word cloud
def generate_wordcloud():
    repo_owner = 'ShubhiiDixit'  
    repo_name = 'ShubhiiDixit'   
    issues_titles = fetch_issue_titles(repo_owner, repo_name)
    
    if issues_titles:
        text = ' '.join(issues_titles)
        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Save word cloud image
        wordcloud.to_file('wordcloud.png')
        print("Word cloud generated successfully.")
    else:
        print("No issues found or failed to fetch issues.")

if __name__ == "__main__":
    generate_wordcloud()
