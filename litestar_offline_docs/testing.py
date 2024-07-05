import os
import pathlib
import typing

import litestar
from litestar import status_codes
from litestar.testing import AsyncTestClient


async def assert_static_files_available(litestar_applicaton: litestar.Litestar, static_path: str) -> None:
    static_dir_path: typing.Final = pathlib.Path(__file__).parent / "static"

    async with AsyncTestClient(app=litestar_applicaton) as async_client:
        assert (await async_client.get(f"{static_path}/random-path")).status_code == status_codes.HTTP_404_NOT_FOUND  # noqa: S101

        for static_file_name in os.listdir(static_dir_path):
            assert (await async_client.get(f"{static_path}/{static_file_name}")).status_code == status_codes.HTTP_200_OK  # noqa: S101
