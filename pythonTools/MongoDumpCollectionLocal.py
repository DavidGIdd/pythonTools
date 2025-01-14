from pymongo import MongoClient
from datetime import datetime


def empty_collections(uri, database_name, collection_names):
    # Connect to the MongoDB client
    client = MongoClient(uri)
    database = client[database_name]
    now = datetime.now()

    # Iterate through the list of collection names and delete all documents
    print(f"Process started at {now} on server")
    database["ParameterValues"].drop()
    print("ParameterValues collection dropped")
    database["ParameterValuesSyncInfo"].drop()
    print("ParameterValuesSyncInfo collection dropped")
    database["ParameterRecord"].drop()
    print("ParameterRecord collection dropped")
    for collection_name in collection_names:
        collection = database[collection_name]
        result = collection.delete_many({})
        print(f"{result.deleted_count} documents were deleted from {collection_name}.")

    # Close the connection to the MongoDB client
    client.close()
    print(f"Process finished at {now}")


if __name__ == "__main__":
    # MongoDB connection URI
    uri = f"mongodb://localhost:27017/"

    # Name of the database
    database_name = "PDV"

    # List of collection names to be emptied
    collection_names = ["Casings", "EventHistory", "EventRecord", "GhostValues", "Ghosts", "ParameterRecordHistory",
                        "ParameterRecord", "ParameterValuesSyncInfo", "Personnel", "PersonnelSession", "Points",
                        "ShotPlans", "StageMetrics", "Stages", "SwitchInventory", "TimeLine", "ToolBuilder", "WellPads",
                        "Wellbores", "Wells", "WellsiteRepresentatives"]

    # Call the function to empty the collections
    empty_collections(uri, database_name, collection_names)
