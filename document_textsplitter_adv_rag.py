from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter

python_code=python_code = """
import numpy as np
from typing import List, Optional

def calculate_mean(numbers: List[float]) -> float:
    '''Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numerical values
        
    Returns:
        The mean value
    '''
    return sum(numbers) / len(numbers)

def calculate_median(numbers: List[float]) -> float:
    '''Calculate the median of a list of numbers.'''
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

class StatisticalAnalyzer:
    '''A class for performing statistical analysis on datasets.'''
    
    def __init__(self, data: List[float]):
        self.data = data
        self.mean = None
        self.median = None
    
    def analyze(self) -> dict:
        '''Perform complete statistical analysis.'''
        self.mean = calculate_mean(self.data)
        self.median = calculate_median(self.data)
        
        return {
            'mean': self.mean,
            'median': self.median,
            'count': len(self.data)
        }
    
    def get_summary(self) -> str:
        '''Return a formatted summary of the analysis.'''
        if self.mean is None:
            self.analyze()
        
        return f"Mean: {self.mean:.2f}, Median: {self.median:.2f}"

def main():
    '''Main execution function.'''
    data = [1.5, 2.3, 3.7, 4.2, 5.1]
    analyzer = StatisticalAnalyzer(data)
    results = analyzer.analyze()
    print(analyzer.get_summary())
    if __name__ == "__main__":
    main()
"""

splitter_python=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,
                                                             chunk_size=100,
                                                             chunk_overlap=10)

code_chunks=splitter_python.split_text(python_code)

print(code_chunks)

JSON_DATA = {
    "company": "AI Research Corp",
    "departments": [
        {
            "name": "Machine Learning",
            "team_size": 25,
            "projects": [
                {
                    "id": "ML001",
                    "title": "Computer Vision System",
                    "description": "Developing advanced image recognition using CNNs",
                    "status": "active",
                    "team_members": ["Alice", "Bob", "Charlie"]
                },
                {
                    "id": "ML002",
                    "title": "NLP Platform",
                    "description": "Building transformer-based language models",
                    "status": "active",
                    "team_members": ["David", "Eve"]
                }
            ]
        },
        {
            "name": "Data Engineering",
            "team_size": 15,
            "projects": [
                {
                    "id": "DE001",
                    "title": "Data Pipeline",
                    "description": "ETL pipeline for real-time data processing",
                    "status": "active"
                }
            ]
        }
    ],
    "technologies": {
        "frameworks": ["TensorFlow", "PyTorch", "scikit-learn"],
        "languages": ["Python", "R", "Julia"],
        "cloud": ["AWS", "Google Cloud", "Azure"]
    },
    "metadata": {
        "founded": 2020,
        "headquarters": "San Francisco",
        "employees": 150
    }
}

json_splitter = RecursiveJsonSplitter(
    max_chunk_size=200
)
# create the json splitter

json_splitter = RecursiveJsonSplitter(
    max_chunk_size=200
)
# return dictionaries

chunks_dict = json_splitter.split_json(json_data=JSON_DATA)

print(chunks_dict)

# return json text

chunks = json_splitter.split_text(JSON_DATA)

print(chunks)

MARKDOWN_TEXT = """# Artificial Intelligence Overview

Artificial intelligence is transforming technology and shaping the future of computing.

## Machine Learning

Machine learning is a subset of AI that focuses on pattern recognition.

### Supervised Learning

Supervised learning algorithms learn from labeled training data.
They make predictions based on input-output pairs.

Common algorithms include:
- Linear regression
- Decision trees
- Support vector machines

### Unsupervised Learning

Unsupervised learning finds patterns in unlabeled data.
It's useful for clustering and dimensionality reduction.

Common techniques:
- K-means clustering
- Principal component analysis
- Hierarchical clustering

## Deep Learning

Deep learning uses neural networks with multiple layers.

### Neural Networks

Neural networks are inspired by biological neurons.
They consist of interconnected nodes organized in layers.

### Convolutional Neural Networks

CNNs excel at image recognition tasks.
They use convolutional layers to detect features hierarchically.

## Applications

AI has applications across multiple domains:

### Healthcare

- Disease diagnosis
- Drug discovery
- Medical imaging analysis

### Finance

- Fraud detection
- Algorithmic trading
- Risk assessment
"""

headers_to_split_on = [
    ("#", "Header_1"),
    ("##", "Header_2"),
    ("###", "Header_3")
]

# create the markdown splitter
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False
)

# split the text

markdown_chunks = markdown_splitter.split_text(MARKDOWN_TEXT)

print(markdown_chunks)

for doc in markdown_chunks:
    print(doc.page_content, end="\n\n")
