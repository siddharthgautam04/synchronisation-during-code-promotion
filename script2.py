import requests
import os
import requests
import base64

commit_api_url = "https://github.com/matplotlib/matplotlib/pull/25993"
compare_api_url = "https://api.github.com/repos/{owner}/{repo}/compare/{base}...{head}"
pull_api_url = "https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}/files"


def github_read_file(username, repository_name, file_path, branch='main', github_token=None):
    headers = {}
    if github_token:
        headers['Authorization'] = f"token {github_token}"

    url = f'https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}?ref={branch}'
    try:
        print(url)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        file_content = data['content']
        file_content_encoding = data.get('encoding')

        if file_content_encoding == 'base64':
            file_content = base64.b64decode(file_content).decode()

        return file_content

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

    except KeyError:
        print("Invalid response received from GitHub API.")
   
    except Exception as e:
        print(f"An error occurred: {e}")

    return None



def get_changed_files(owner, repo, pull_request_number):
    url = pull_api_url.format(owner=owner, repo=repo, pull_request_number=pull_request_number)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
        changed_files = [file_data['filename'] for file_data in data]
        # print(changed_files)
        return changed_files

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

    except KeyError:
        print("Invalid response received from GitHub API.")

    except Exception as e:
        print(f"An error occurred: {e}")

    return []

if __name__ == '__main__':
    owner = "Project-OSRM"
    repo = "osrm-backend"
    pull_id = "6632"
    github_token="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"
    # file_content = github_read_file(owner, repo, file_path, github_token)
    # if file_content:
    #     print(f"File content:\n{file_content}")
    changed_files = get_changed_files(owner, repo, pull_id)
    print("Changed files:")
    for file in changed_files:
        print(github_read_file(username="lliehu",repository_name=repo,file_path=file,github_token=github_token,branch="gcc-13-build-fix"))
        # print("Filename:", file['filename'])
        # print("Content:")
        # print(file['content'])
        # print()