# ImageUriToBlob

This allows you to use uri-to-blob conversion in the Flow rather than during doc processing.

## Why?

- Instead of processing input and query images separately, use one Executor to do them both.
- Saves you having to write a `for` loop to convert every image (since many encoders expect `blob`s).

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://ImageUriToBlob')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://ImageUriToBlob')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
