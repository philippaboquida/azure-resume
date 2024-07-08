# azure-resume
My Azure hosted resume, following alongside GPS (Through A Cloud Guru) Tutorial video.
https://www.youtube.com/watch?v=ieYrBWmkfno

## Technologies used
- Visual Studio Code
- html / js templates provided by A Cloud Guru
- Python
- Azure CosmosDB
- Azure Functions
- Azure Storage + Static Website Hosting
- Azure CDN
- Azure DNS


## Initial Front end setup

- Used supplied template, contained in the *frontend* folder.
- Added and changed relevant details to index.html for my usecase.
- main.js is visitor function code.


## Back end setup

- Used Visual Studio Code and Python 3.11
- Using Functions extensions in VS Code, created the groundwork for the Counter function


## Linking CosmosDB and Function

- Chat GPT was heavily used in creation of the code as it was not the primary purpose of this project and out of scope for my current skillset, this came with a number of difficulties as was not the same as ACG Projects guide.
- Used a number of prompts and resources to create the same functionality, this section probably took about 3 or 4 hours of trouble-shooting to come to a working solution
- Tested locally using func host start command, with application open in browser
- Created CosmosDB NoSQL storage, added a Database called AzureResume, then a container called "Counter" with an item simply labelled with 1 and a value inside it that would be used as the counter for http requests


## Deploying to Azure

- Deployed code to an Azure Function
- Grabbed the function URL, placed it into the js code in the front end
- Using Azure Storage Account, deployed the front end to Static Website Hosting
- Enabled CORS and added the website link to enable the counter