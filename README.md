# Paralegal
Tools to search for words in an email cache in an efficient manner. 

## Setup

First, a few housekeeping things. In order...


### Python 3.6

You'll need at least Python 3.6 so go grab that however is easiest. Also, we're not cavemen so create a virtualenv `python3 -m venv env` and activate it `source env/bin/activate`.


### Install Dependencies

Install Python dependencies with `pip install -r requirements.txt`.


## Usage

Create a pickle file which stored the trie structure

`python core/run.py --build_trie --source_dir=SOURCE_DIR  --target-directory TARGET_DIR`

Search for word in the trie

`python core/run.py --search --trie trie.p --word "one"`
