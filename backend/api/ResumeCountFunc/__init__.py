import logging
import os
import json  # Import the json module
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions

# Database Container Variables
endpoint = os.environ["COSMOSDB_ENDPOINT"]
account_key = os.environ["COSMOSDB_KEY"]
database_name = os.environ["COSMOSDB_DATABASE_NAME"]
container_name = os.environ["COSMOSDB_CONTAINER_NAME"]
client = CosmosClient(endpoint, account_key)

# Function to handle HTTP GET request
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Known item ID
    item_id = '1'

    # Retrieve item from Cosmos DB
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    
    try:
        # Read the item from Cosmos DB
        response = container.read_item(item=item_id, partition_key=item_id)
        item = response
        
        # Extract and update the count
        if 'count' in item:
            item['count'] += 1
        else:
            item['count'] = 1
        
        # Write the updated item back to Cosmos DB
        container.replace_item(item=item_id, body=item)
        
        # Return the updated item as JSON
        return func.HttpResponse(body=json.dumps(item), mimetype="application/json", status_code=200)
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f'Error retrieving or updating item from Cosmos DB: {str(e)}')
        return func.HttpResponse(f'Error retrieving or updating item: {str(e)}', status_code=500)
    except Exception as e:
        logging.error(f'Unexpected error: {str(e)}')
        return func.HttpResponse(f'Unexpected error: {str(e)}', status_code=500)
