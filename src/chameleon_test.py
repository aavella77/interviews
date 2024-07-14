# Write unit tests for the normalizer function in the normalizer.py
# Complete missing parts of urls
# normalize("https://example.com:8080/a/b/c") -> https://example.com:8080/a/b/c
# normalize("example.com") -> http://example.com:80/
# normalize("") -> http://localhost:80/

from normalizer import normalize

def test_sample_1():
	assert normalize("https://example.com:8080/a/b/c") == "https://example.com:8080/a/b/c"

def test_sample_2():
	assert normalize("example.com") == "http://example.com:80/"

def test_sample_3():
	assert normalize("") == "http://localhost:80/"