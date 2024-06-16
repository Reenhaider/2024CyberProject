import requests

def get_repo_summary(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        summary = {
            'name': data.get('name'),
            'description': data.get('description'),
            'stars': data.get('stargazers_count'),
            'forks': data.get('forks_count'),
            'watchers': data.get('watchers_count'),
            'open_issues': data.get('open_issues_count'),
            'last_commit': data.get('pushed_at'),
            'contributors_url': data.get('contributors_url'),
            'releases_url': data.get('releases_url').replace('{/id}', '')
        }
        return summary
    else:
        return {'error': f'Error {response.status_code}: Unable to fetch repository information'}

owner = 'Reenhaider'  # Replace with the repository owner's username
repo = '2024CyberProject'  # Replace with the repository name
summary = get_repo_summary(owner, repo)
print(summary)
