from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_root_must_return_hello_world(client: AsyncClient):
    response = await client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, world!'}


@pytest.mark.asyncio
async def test_list_templates_must_return_available_gitignore_templates(
    client: AsyncClient,
):
    response = await client.get('/api/list')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/plain; charset=utf-8'
    assert response.text
