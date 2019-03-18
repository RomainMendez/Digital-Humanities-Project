#! /bin/bash
grep -h -i -f -E keywords ../data/trimmed/*.jsonl > ../data/filtered.jsonl
