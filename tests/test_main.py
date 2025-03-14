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


@pytest.mark.asyncio
async def test_passing_template_name_must_return_gitignore(
    client: AsyncClient,
):
    response = await client.get('/api/python')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/plain; charset=utf-8'
    assert response.text


@pytest.mark.asyncio
async def test_passing_invalid_template_name_must_return_not_found(
    client: AsyncClient,
):
    invalid_template_name = 'blabla'
    response = await client.get(f'/api/{invalid_template_name}')

    expected_response = {
        'detail': f'Template "{invalid_template_name}" not found.'
    }

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == expected_response
