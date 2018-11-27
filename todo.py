import uuid

from flask import make_response, abort


# Data to serve with our API
TODO = {
    "fca2faa9-c68c-4a97-a8e4-1e4a16de2cb9": {
        "id": "fca2faa9-c68c-4a97-a8e4-1e4a16de2cb9",
        "title": "Do the shopping",
        "body": "Milk, eggs and bread",
        "completed": "pending"
    },
    "dfb498a1-5916-4cf1-9792-dff80543a682": {
        "id": "dfb498a1-5916-4cf1-9792-dff80543a682",
        "title": "Fix the microwave",
        "body": "It doesn't work",
        "completed": "completed"
    }
}


def read_all():
    """
    This function responds to a requests for /api/todo
    with the complete list of entries

    :return:    sorted list of entries
    """
    return [TODO[key] for key in sorted(TODO.keys())]


def read_one(entryId):
    """
    This function responds to a request for /api/todo/{id}
    with one matching entry from TODO list

    :param entryId:  id of the entry to find
    :return:    entry matching the id
    """
    if entryId in TODO:
        entry = TODO.get(entryId)
        return entry
    else:
        abort(404, "Entry with id {entryId} not found".format(entryId=entryId))


def create(entry):
    """
    This function created a new entry in the TODO list
    based on the passed in entry data

    :param entry:   entry to create in TODO list
    :return:        201 on success, 406 on entry exists
    """

    title = entry.get("title", None)
    body = entry.get("body", None)

    entry_id = uuid.uuid4()

    TODO[entry_id] = {
        "id": entry_id,
        "title": title,
        "body": body,
        "completed": False
    }

    return make_response(
        "Entry successfully created", 201
    )


def update(entryId, entry):
    title = entry.get("title", None)
    body = entry.get("body", None)
    completed = entry.get("completed", None)

    if entryId in TODO:
        TODO[entryId] = {
            "id": entryId,
            "title": title,
            "body": body,
            "completed": completed
        }
        return make_response(
            "{entry_id} successfully updated".format(entry_id=entryId), 200
        )
    else:
        abort(
            404, "Entry with id {entry_id} not found".format(entry_id=entryId)
        )


def delete(entryId):
    """
    This function deletes a entry from the TODO list

    :param entry:   id of the entry to delete
    :return:        200 on successful delete, 404 if not found
    """

    if entryId in TODO:
        del TODO[entryId]
        return make_response(
            "{entry_id} successfully deleted".format(entry_id=entryId), 200
        )
    else:
        abort(
            404, "Entry with id {entry_id} not found".format(entry_id=entryId)
        )

