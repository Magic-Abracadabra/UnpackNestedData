# How to Unpack Nested Data?
Suppose we have data like this:
```python
data = {
            "project": "Phoenix",
            "version": "2.0.1",
            "settings": {
                "debug": True,
                "database": {
                    "host": "localhost",
                    "port": 5432,
                    "credentials": ("admin", "secret")
                }
            },
            "modules": [
                {
                    "name": "auth",
                    "enabled": True,
                    "dependencies": ["crypto", "logger"]
                },
                {
                    "name": "payment",
                    "enabled": False,
                    "config": {
                        "gateway": "stripe",
                        "api_key": "sk_test_123"
                    }
                },
                (1, 2, "three"),
                42,
                "no_iteration_here",
            ],
            "metadata": None
}
```
```python
>>> light('admin', data)
(True, [('admin', 'secret')])
```
