# litestar-offline-docs

This package enables "offline mode" for FastAPI (in other words lets you avoid loading assets from CDN).

# Installation

```sh
poetry add litestar-offline-docs
```

# Usage

Just construct static file handler and add it to Litestar application during initialization:

```python
import litestar

from litestar_offline_docs import generate_static_files_config

app = litestar.Litestar(
    static_files_config=[generate_static_files_config()],
    ...
)
```

That's it. Now, the assets for API docs are served locally, not from CDN.

See also: [fastapi-offline-docs](https://github.com/community-of-python/fastapi-offline-docs).
