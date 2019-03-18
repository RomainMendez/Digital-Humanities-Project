#! /bin/bash
grep -h -i -E -f keywords ../data/trimmed/*.jsonl > ../data/filtered.jsonl
