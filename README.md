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
You have your target *key* 'admin'. You're wondering where the key is in the data. The light function will shed light on every iterable objects that contain the key. The light function will return (l, values). If the *key* is in the nested data d, then l=True. The list *values* will be composed of all iterable objects containing the key in d.
```python
>>> light('admin', data)
(True, [('admin', 'secret')])
>>> light('config', data)
(True, [{'name': 'payment', 'enabled': False, 'config': {'gateway': 'stripe', 'api_key': 'sk_test_123'}}])
```
