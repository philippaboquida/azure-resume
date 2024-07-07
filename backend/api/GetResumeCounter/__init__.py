import os
import logging
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
from datetime import datetime
import uuid

# Get Cosmos DB configuration from environment variables
endpoint = os.getenv('COSMOSDB_ENDPOINT')
key = os.getenv('COSMOSDB_KEY')
database_name = os.getenv('COSMOSDB_DATABASE_NAME')
visitors_container_name = os.getenv('COSMOSDB_VISITORS_CONTAINER_NAME')

client = CosmosClient(endpoint, key)
database = client.get_database_client(database_name)
visitors_container = database.get_container_client(visitors_container_name)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        visitor_id = str(uuid.uuid4())
        visitor = {
            "id": visitor_id,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Log the visitor
        visitors_container.create_item(body=visitor)
        logging.info("New visitor logged")

        return func.HttpResponse("Page loaded", status_code=200)
    
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Cosmos DB error: {str(e)}")
        return func.HttpResponse("Internal server error", status_code=500)