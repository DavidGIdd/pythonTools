import pymongo
from pymongo.errors import ConnectionFailure
from datetime import datetime, timedelta
from bson.objectid import ObjectId
import pytz
import logging

# Creates/edits a log that includes date and time when the script was executed
logging.basicConfig(filename='script_log.txt', level=logging.INFO)
logging.info(f"Notification deleter script executed at {datetime.now()}")

# Eliminates timezone issues for each server
target_timezone = pytz.timezone('UTC')
time_range = timedelta(hours=2)

# List of XTO servers
xto_ips = {
    "GR_DS049_PHANTOM": "100.119.248.175",
    "ST_DS070_BLACK": "100.92.183.129",
    "GR_DS075_SPARTAN": "100.66.166.91",
    "GR_DS081_IRON": "100.75.200.12",
    "ST_DS082_RED": "100.109.189.10",
    "ST_DS092_WHITE": "100.65.17.58",
    "HB_DS097_THOR": "100.70.123.84",
    "LT_DS139_XTO": "100.123.128.94",
    "ST_DS140_OMEGA": "100.97.50.123",
    "LT_DS142_KIOWA": "100.112.124.57"

}

# Checks the mongoDB for each server
for key, ip in xto_ips.items():
    print(f"Notifications for {key} -> {ip}")

    try:
        client = pymongo.MongoClient(f"mongodb://{ip}:27017/")
        db = client["PDV"]
        notification_collection = db["Notifications"]
        stage_collection = db["Stages"]

        notification_cursor = notification_collection.find()

        # Loop that will check the stage status and deletes notification if the stage is completed
        for document in notification_cursor:
            stage_id = ObjectId(document["stageId"])
            stage_cursor = stage_collection.find({"_id": stage_id})
            # print(document)
            # print(stage_cursor[0])

            # print(f"Title: {document['title']}")
            print(document["stageId"])
            print(f"Stage status: {document['status']} Approval status: {document['documentStatus']}\n")

            if stage_cursor[0]["status"] == "completed":
                notification_collection.delete_many({"stageId": stage_id})
                print("Deleted Completed Stage Notification:")
                # print(document)

        current_time_with_timezone = datetime.now(target_timezone)
        time_range_delete = current_time_with_timezone - time_range

        # If the notification was sent mora than 2 hours ago it will be deleted
        query = {"timestamp": {"$lte": int(time_range_delete.timestamp()) * 1000}}

        result = notification_collection.delete_many(query)

        print(f"Deleted {result.deleted_count} notifications over 2 hours")

        client.close()

        print('\n\n')

    # Catches the error when the server is not available.
    except ConnectionFailure:
        print("Server not available")
        print('\n\n')
