import json
import os
import sys

try:
    import jsonschema
except ImportError:
    print("jsonschema not installed", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SCHEMAS_DIR = os.path.join(ROOT, "schemas")
EXAMPLES_DIR = os.path.join(ROOT, "projects", "decision.forum", "examples")

# Load schemas
schemas = {}
for fn in os.listdir(SCHEMAS_DIR):
    if not fn.endswith(".json"):
        continue
    path = os.path.join(SCHEMAS_DIR, fn)
    with open(path, "r", encoding="utf-8") as f:
        schemas[fn] = json.load(f)

# Resolve local refs like ./foo.schema.json
resolver = jsonschema.RefResolver(
    base_uri="file://" + SCHEMAS_DIR + "/",
    referrer=None,
    store={"file://" + os.path.join(SCHEMAS_DIR, k): v for k, v in schemas.items()},
)

# Map example files to schema files
mapping = {
    "decision-record.example.json": "decision-record.schema.json",
    "crosscheck-report.example.json": "crosscheck-report.schema.json",
    "clearance-certificate.example.json": "clearance-certificate.schema.json",
    "anchor-receipt.example.json": "anchor-receipt.schema.json",
}

errors = 0
for example_fn, schema_fn in mapping.items():
    example_path = os.path.join(EXAMPLES_DIR, example_fn)
    schema = schemas.get(schema_fn)
    if schema is None:
        print(f"Missing schema: {schema_fn}", file=sys.stderr)
        errors += 1
        continue
    with open(example_path, "r", encoding="utf-8") as f:
        instance = json.load(f)
    try:
        jsonschema.validate(instance=instance, schema=schema, resolver=resolver)
        print(f"OK {example_fn} validates against {schema_fn}")
    except jsonschema.ValidationError as e:
        print(f"FAIL {example_fn}: {e.message}", file=sys.stderr)
        errors += 1

if errors:
    sys.exit(1)
