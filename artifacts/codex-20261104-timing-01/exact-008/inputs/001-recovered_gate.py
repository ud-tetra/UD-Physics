"""Verify recovered-source Git blobs and independently replay the face-mask algebra."""
import hashlib
import json
from itertools import combinations, product
from pathlib import Path

root = Path(__file__).with_name("recovered")
sources = json.loads((root / "manifest.json").read_text())
for item in sources:
    raw = (root / item["file"]).read_bytes()
    assert hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == item["sha"]

cells = [(0, 1, 2, 3), (0, 1, 2, 4)]
faces = sorted({f for c in cells for f in combinations(c, 3)})
edges = sorted({e for f in faces for e in combinations(f, 2)})

def boundary(simplex, face):
    return sum((-1)**i for i in range(len(simplex))
               if simplex[:i] + simplex[i+1:] == face)

b3 = [[boundary(c, f) for c in cells] for f in faces]
b2 = [[boundary(f, e) for f in faces] for e in edges]
gram = [[sum(row[i]*row[j] for row in b3) for j in range(2)] for i in range(2)]
assert gram == [[4, 1], [1, 4]]
odd = [row[0]-row[1] for row in b3]
shared = faces.index((0, 1, 2))
assert odd[shared] == 0 and all(odd[i] != 0 for i in range(7) if i != shared)
assert [sum(row[k]*odd[k] for k in range(7)) for row in zip(*b3)] == [3, -3]
assert [2*b3[shared][i]*sum(b3[shared])*(1-2*i) for i in range(2)] == [4, -4]

preserving = []
for h in product((0, 1), repeat=7):
    if all(sum(row[k]*h[k]*b3[k][i] for k in range(7)) == 0
           for row in b2 for i in range(2)):
        preserving.append(h)
assert preserving == [(0,)*7, (1,)*7]
print(json.dumps({
    "mainline_revision": "a78193d420f3bac957be081aed0525fbc1457825",
    "source_blobs_verified": len(sources),
    "boundary_gram": gram, "shared_face_odd_mode": odd[shared],
    "shared_face_instantaneous_directed_currents": [4, -4],
    "binary_masks_checked": 128, "preserve_full_top_coexact_sector": preserving,
    "nonpreserving_masks": 126,
    "event_observer": "recovered candidate; no Pachner reset or no-miss sampling law supplied",
}, indent=2))
