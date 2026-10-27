# Reference-001 UTF-8 correction

Original commit 6570d08da8365ddf99006bfac166abfb46317e6b recorded 4220 characters/code units, but the source is 4230 UTF-8 bytes because of nine non-ASCII mathematical symbols.
Source SHA256: 408f6aeba43ca08df22a2d288b65def8d4206e5b84d01ffd085b227c8f1cd6f5.
Result SHA256: 13f126c8a2ea8aab5ba47c4923b70d74929b06f9522f32e897cf8eb871e57040.
Only input size metadata is corrected; source and result bytes unchanged. Earlier failed CI and original Git commit remain inspectable.
