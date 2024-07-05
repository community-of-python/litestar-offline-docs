import typing

import litestar
import pytest

from litestar_offline_docs import generate_static_files_config
from litestar_offline_docs.testing import assert_static_files_available


@pytest.fixture(scope="session", autouse=True)
def anyio_backend() -> str:
    return "asyncio"


async def test_static_handler() -> None:
    static_path: typing.Final = "/statc/path"
    litestar_app: typing.Final = litestar.Litestar(
        static_files_config=[generate_static_files_config(static_files_handler_path=static_path)]
    )

    await assert_static_files_available(litestar_app, static_path)
