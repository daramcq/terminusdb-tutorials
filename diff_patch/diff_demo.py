from pprint import pprint
from terminusdb_client import WOQLClient, DocumentTemplate, WOQLSchema

# Using TerminusDB Open API for JSON Diff and Patch

tdb_diff = WOQLClient("https://cloud.terminusdb.com/jsondiff")
tdb_patch = WOQLClient("https://cloud.terminusdb.com/jsonpatch")

# Or you can use the local version as below

# client = WOQLClient("http://localhost:6363/")
# client.connect()

### Comparing a document object ###

class Person(DocumentTemplate):
    name: str
    age: int

jane = Person(name="Jane", age=18)
janine = Person(name="Janine", age=18)

result_patch = tdb_diff.diff(jane, janine)

pprint(result_patch.content)

# apply result patch to get back final document

after_patch = tdb_patch.patch(jane, result_patch)

pprint(after_patch)
assert after_patch == janine._obj_to_dict()

### Comapring document objects in json (dict) formats

jane = { "@id" : "Person/Jane", "@type" : "Person", "name" : "Jane"}
janine = { "@id" : "Person/Jane", "@type" : "Person", "name" : "Janine"}

result_patch = tdb_diff.diff(jane, janine)

pprint(result_patch.content)

# apply result patch to get back final document

after_patch = tdb_patch.patch(jane, result_patch)

pprint(after_patch)
assert after_patch == janine


### Comparing TerminusDB schemas (Not working at the moment)
#
# class Company(DocumentTemplate):
#     name: str
#     director: Person
#
# schema1 = WOQLSchema()
# schema1.add_obj("Person", Person)
# schema2 = WOQLSchema()
# schema2.add_obj("Person", Person)
# schema2.add_obj("Company", Company)
#
# result_patch = tdb_diff.diff(schema1, schema2)
#
# pprint(result_patch.content)

# apply result patch to get back final document

# after_patch = tdb_patch.patch(schema1, result_patch)
#
# pprint(after_patch)
# assert after_patch == schema2.to_dict()

### Comparing JSON schemas (http://json-schema.org/understanding-json-schema/about.html) (Not working at the moment)

# schema1 = {
#   "type": "object",
#   "properties": {
#     "name": { "type": "string" },
#     "birthday": { "type": "string", "format": "date" },
#     "address": { "type": "string" },
#   }
# }
#
# schema2 = {
#   "type": "object",
#   "properties": {
#     "first_name": { "type": "string" },
#     "last_name": { "type": "string" },
#     "birthday": { "type": "string", "format": "date" },
#     "address": {
#       "type": "object",
#       "properties": {
#         "street_address": { "type": "string" },
#         "city": { "type": "string" },
#         "state": { "type": "string" },
#         "country": { "type" : "string" }
#       }
#     }
#   }
# }
#
# result_patch = tdb_diff.diff(schema1, schema2)
#
# pprint(result_patch.content)

# apply result patch to get back final document

# after_patch = tdb_patch.patch(schema1, result_patch)
#
# pprint(after_patch)
# assert after_patch == schema2
