
This is the result of a technical assessment.  
The main task is:  
```
1) Write a function that takes as input (sentence: String, n: Number)
and returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
This list should be sorted by decreasing frequency and alphabetical order in case of tie.

Example:
Input: ("bar baz foo foo zblah zblah zblah baz toto bar", 3)
Output:
[
   ("zblah", 3),
   ("bar", 2),
   ("baz", 2),
]

2) Write tests for the function you just wrote
```
and tests are available for a coverage score greater than 90%  

# Getting started  

### Prerequisites

- Make sure that you have at least [Python 3.10](https://www.python.org/downloads/) with [PIP](https://pip.pypa.io/en/stable/) included.

### Installation

```commandline
git clone https://github.com/xakiv/foodles foodles
cd foodles/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# How to use it

```commandline
cd foodles/
source venv/bin/activate
python main.py SENTENCE SIZE_RESULT_LIST
```


# How to test it  
Run simple tests
```commandline
cd foodles/
source venv/bin/activate
pytest -v
```

Run tests and show coverage report when venv is activated
```commandline
cd foodles/
source venv/bin/activate
coverage run --module pytest -v && coverage report --show-missing
```