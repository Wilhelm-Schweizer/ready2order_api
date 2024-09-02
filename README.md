# Ready2Order API Wrapper

A Python wrapper for the Ready2Order API that simplifies the interaction with various endpoints provided by the Ready2Order platform.

## Current Features

- Fetch company information
- Fetch product information
- Fetch all bills (invoices)
- Fetch a specific invoice by its ID

## Installation

You can install the package via pip:

```bash
pip install ready2order-api-wrapper
```

## Usage Example

```python
from ready2order_api.api import Ready2OrderAPI as r2o

api = r2o("YOUR_ACCOUNT_TOKEN")

print(api.get_products())
```


