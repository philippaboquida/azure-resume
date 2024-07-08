# Your API lives here

Python based API binded to CosmosDB to trigger Azure Functions

**Python Code**
Since my goal with this is to learn Azure itself, rather than coding, I used ChatGPT prompts to create the python code here to count visitors
This does not align with the guide video I used, as that was using C#.

I did not at first understand why the application was not working, after creating the backend using VS Code, it did not create the appropriate directory structure. Using Microsoft documentation and a few other's who have completed this challenge's github repo's, I eventually discovered this issue and was able to load locally the application to my web browser and understand the problem.

This also included adding 'azure-cosmos' to the requirements.txt and creation of function.json in the 'ResumeCountFunc' directory.

I ran into the issue of "No job functions found" numerous times before understanding the problem.

Upon successfully linking the Function with CosmosDB, I had an issue now where it would read out the entire item including the extra details that are added in upon saving it in Azure Portal. I used ChatGPT to solve this but will need to delve deeper as to understand what it did to correct this.