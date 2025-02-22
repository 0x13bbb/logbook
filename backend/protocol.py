from db import db
from notifier import notifier

class Protocol:
    def run_check():
        # protocol logic
        # get data
        # mood_data = db.get_mood()
        # update view compute composite score and output
        # notifier.send_notification()
        pass

# TODO example send_notification call
#     notifier.send_notification(
#         ["test@gmail.com", "test1@gmail.com"],
#         "Group Notification",
#         "This is a group message"
#     )

proto = Protocol()