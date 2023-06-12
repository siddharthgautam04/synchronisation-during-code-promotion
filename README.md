# synchronisation-during-code-promotion
Documentation to use the tools for synchronization during code promotion

Create a consumer for OAuth in bitbucket
OAuth needs a key and secret, together these are know as an OAuth consumer. You can create a consumer on any existing workspace. To create a consumer, do the following:
1.	Select your avatar (Your profile and settings) from the navigation bar at the top of the screen.
2.	Under Recent workspaces, select the workspace that will be accessed using the consumer; or find and open the workspace under All workspaces.
3.	On the sidebar, select Settings to open the Workspace settings.
4.	On the sidebar, under Apps and features, select OAuth consumers.
5.	Click the Add consumer button.  
The system requests the following information:
Name: The display name for your consumer. This must be unique within your account. This is required.
Description: An optional description of what your consumer does.
Callback URL: Required for OAuth 2.0 consumers.
Name , description , callback URL are mandatory and please fill any safe URL as per your choice and give the access as per your requirement and save the consumer.
Now since we have successfully created the consumer we have to generate an access token 
So, to generate access token we have to first go to this link https://bitbucket.org/site/oauth2/authorize?client_id={client_id}&response_type=code and replace client id with your generated consumer id key 
And press enter you will be redirected to a new window an in the url you can find temporary key in it 
Copy and save it 
Now go again and use this url in postman  https://bitbucket.org/site/oauth2/access_token \
  -d grant_type=authorization_code -d code={code}
Authenticate the request and generate your access token 
Please remember that access token is valid for only 72 min 
Paste token in the script file and get details of any pull request and commit 


Commit code 

