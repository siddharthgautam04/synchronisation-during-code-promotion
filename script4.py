# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests

url = "https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch"

headers = {
  "Authorization": "Bearer 78mZvk2fFcG312RLUMOKBDDd9uZXUfcPCf_2TuenhAwLUlGYG2icc1NNXDGwL4B2-MEBbKDyuIAXwWE5kQS0U_U-UXU-qty307omb0cYRbku7S6EkvvV_e_wQesB4kkSZD9dZcxuSK4I0jUjD_p_noz-O9ic"
}
base_url = "https://bitbucket.org/synchronisation-during-codepromotion/test1/pull-requests/2"
workspace = "synchronisation-during-codepromotion"
repo_slug = "test1"
spec = "2"

formatted_url = url.format(
    workspace=workspace,
    repo_slug=repo_slug,
    pull_request_id=spec,
)
# response = requests.request(
#    "GET",
#    url,
#    headers=headers
# )
response = requests.get(formatted_url, headers=headers)

print(response.text)