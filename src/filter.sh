#! /bin/bash
grep -h -i -f keywords ../data/trimmed/*.jsonl > ../data/filtered.jsonl
