"""Synthetic controls for both offset spaces and malformed dimensions."""

import json
from copy import deepcopy

from jsonschema import Draft202012Validator

from validate_offsets import SCHEMA, check_dimensions


def main():
    schema = json.loads(SCHEMA.read_text())
    Draft202012Validator.check_schema(schema)
    contract = schema["properties"]["calibration"]
    keys = ("offset_space", "model", "offset", "input_ids", "readout_to_modal")
    rules = {
        "$defs": schema["$defs"],
        "type": "object",
        "properties": {key: contract["properties"][key] for key in keys},
        "required": list(keys),
        "oneOf": contract["oneOf"],
    }
    validator = Draft202012Validator(rules)

    def passes(record):
        if not validator.is_valid(record):
            return False
        try:
            check_dimensions(record)
        except ValueError:
            return False
        return True

    for n in (14, 16):
        channel = {
            "offset_space": "channel", "model": "z=M(y-b)",
            "offset": [0]*n, "input_ids": [str(i) for i in range(n)],
            "readout_to_modal": [[0]*n for _ in range(14)],
        }
        modal = dict(channel, offset_space="modal", model="z=My-b", offset=[0]*14)
        assert passes(channel) and passes(modal)
        assert not passes(dict(channel, model="z=My-b"))
        assert not passes(dict(channel, offset=[0]*(n+1)))
        assert not passes(dict(modal, offset=[0]*15))
        ragged = deepcopy(channel)
        ragged["readout_to_modal"][0].pop()
        assert not passes(ragged)
    print("PASS: schema metaschema and eight rejection controls across N=14 and N=16")
    print("PASS: channel and modal forms both accepted at N=14 and N=16")


if __name__ == "__main__":
    main()
