import requests
import os
import requests
import base64

commit_api_url = "https://api.github.com/repos/Project-OSRM/osrm-backend/commits/0ca913132acea46e0c56e4665af50d68f53eec68"
compare_api_url = "https://api.github.com/repos/{owner}/{repo}/compare/{base}...{head}"

def github_read_file(username, repository_name, file_path, github_token=None):
    headers = {}
    if github_token:
        headers['Authorization'] = f"token {github_token}"

    url = f'https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}'
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



def get_changed_files(owner, repo, commit_id):
    commit_url = commit_api_url.format(owner=owner, repo=repo, commit_id=commit_id)
    response = requests.get(commit_url)
    if response.status_code == 200:
        commit_data = response.json()
        commit_sha = commit_data['sha']
        base_sha = commit_data['parents'][0]['sha']

        compare_url = compare_api_url.format(owner=owner, repo=repo, base=base_sha, head=commit_sha)
        response = requests.get(compare_url)
        if response.status_code == 200:
            compare_data = response.json()
            files_changed = compare_data.get('files', [])
            changed_files = []
            print(files_changed)
            for file in files_changed:
                filename = file['filename']
                raw_url = file['raw_url']
                print(filename)
                print(raw_url)
                changed_files.append(filename)
                # raw_response = requests.get(raw_url)
                # if raw_response.status_code == 200:
                #     raw_content = raw_response.text
                #     # changed_files.append({'filename': filename, 'content': raw_content})
                #     changed_files.append(filename)
                # else:
                #     print("Failed to fetch raw file content for file:", filename)
            return changed_files
        else:
            print("Failed to fetch compare data:", response.text)
    else:
        print("Failed to fetch commit data:", response.text)

    return []

if __name__ == '__main__':
 #   github_token = os.environ['GITHUB_TOKEN']
    github_token = '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'
    owner = "Project-OSRM"
    repo = "osrm-backend"
    commit_id = "0ca913132acea46e0c56e4665af50d68f53eec68"
    # file_content = github_read_file(owner, repo, file_path, github_token)
    # if file_content:
    #     print(f"File content:\n{file_content}")
    changed_files = get_changed_files(owner, repo, commit_id)
    print("Changed files:")
    for file in changed_files:
        print(github_read_file(owner,repo,file,github_token))
        # print("Filename:", file['filename'])
        # print("Content:")
        # print(file['content'])
        # print()
        
