# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests

url = "https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/patch/{spec}"


headers = {
    "Accept": "application/json",
    "Authorization": "Bearer p0tABzS7rekleoEYZ7rQVfxkQ-k5wunoJZVIGRDLwq8RS2XeLlDWMUcA0BBfrWozgqmjYclp4fCrUhKvjkQ1FllcO5ri3m-vAtPtfMBng_LmGKXAvYlnNLxEYKuahz1DzW4A46z1LucvFtBIRP1j-p6hkWYv"
}

base_url = "https://bitbucket.org/synchronisation-during-codepromotion/test1/commits/84ad195a6cd77e92b8a4eb71619fbe34e4b09172"
workspace = "synchronisation-during-codepromotion"
repo_slug = "test1"
spec = "84ad195a6cd77e92b8a4eb71619fbe34e4b09172"

formatted_url = url.format(
    workspace=workspace,
    repo_slug=repo_slug,
    spec=spec,
)

response = requests.get(formatted_url, headers=headers)


# headers = {
#   "Authorization": "Bearer <access_token>"
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers
# )

print(response.text)