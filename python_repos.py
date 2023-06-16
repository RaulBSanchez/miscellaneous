import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")


#examine the first repository



for repo_dict in repo_dicts:
	print("Sselected info about the first repository")
	print('Name: ' , repo_dict['name'])
	print('Owner: ' , repo_dict['owner']['login'])
	print('Stars: ', repo_dict['stargazers_count'])
	print('Repository: ', repo_dict['html_url'])

