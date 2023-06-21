# PROJECT: NoSQL

AUTHOR: Matthew Allen

## TASKS:

### 0. List all databases - `0-list_databases`

Script that lists all databases in MongoDB.

### 1. Create a database - `1-use_or_create_database`

Script that creates or uses the database `my_db`.

### 2. Insert document - `2-insert`

Script that inserts a document in the collection `school`:

* The document has one attribute `name` with value "Holberton school"
* The database name is passed as option of `mongo` command

### 3. All documents - `3-all`

Script that lists all documents in the collection `school`:

* The database name is passed as option of `mongo` command

### 4. All matches - `4-match`

Script that lists all documents with `name="Holberton school"` in the collection `school`:

* The database name is passed as option of `mongo` command

### 5. Count - `5-count`

Script that displays the number of documents in the collection `school`:

* The database name is passed as option of `mongo` command

### 6. Update - `6-update`

Script that adds a new attribute to a document in the collection `school`:

* Script updates only document with `name="Holberton school"` (all of them)
* The update adds the attribute `address` with the value "972 Mission street"
* The database name is passed as option of `mongo` command

### 7. Delete by match - `7-delete`

Script that deletes all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command

### 8. List all documents in Python - `8-all.py`

Python function that lists all documents in a collection:

* Prototype: `def list_all(mongo_collection):`
* Returns an empty list if no document in the collection
* `mongo_collection` is the `pymongo` collection object

### 9. Insert a document in Python - `9-insert_school.py`

Python function that inserts a new document in a collection based on `kwargs`:

* Prototype: `def insert_school(mongo_collection, **kwargs):`
* `mongo_collection` is the `pymongo` collection object
* Returns the new `_id`

### 10. Change school topics - `10-update_topics.py`

Python function that changes all topics of a school document based on the name:

* Prototype: `def update_topics(mongo_collection, name, topics):`
* `mongo_collection` is the `pymongo` collection object
* `name` (string) is the school name to update
* `topics` (list of strings) is the list of topics approached in the school

### 11. Where can I learn Python? - `11-schools_by_topic.py`

Python function that returns the list of school having a specific topic:

* Prototype: `def schools_by_topic(mongo_collection, topic):`
* `mongo_collection` is the `pymongo` collection object
* `topic` (string) is the topic searched

### 12. Log stats - `12-log_stats.py`

Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: `logs`
* Collection: `nginx`
* Display (same as the example):
  * first line: `x logs` where `x` is the number of documents in this collection
  * second line: `Methods:`
  * 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (with a tab before each line)
  * one line with the number of documents with:
    * `method=GET`
    * `path=/status`

Uses the dump stored in `dump.zip`.
