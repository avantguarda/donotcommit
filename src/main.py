from http import HTTPStatus
from pathlib import Path
from typing import Final

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI(title='donotcommit.com')

PROJECT_ROOT: Final = Path(__file__).parent.parent
GITIGNORE_FOLDER: Final = PROJECT_ROOT / 'gitignore'
TEMPLATES: Final = tuple(GITIGNORE_FOLDER.rglob('*.gitignore'))


@app.get('/')
async def read_root():
    return {'message': 'Hello, world!'}


@app.get('/api/list', response_class=PlainTextResponse)
async def list_templates():
    """
    Lists all available gitignore templates by github.com/github/gitignore
    """
    language_names = sorted([
        Path(file).name.lower().removesuffix('.gitignore')
        for file in TEMPLATES
    ])

    formatted_names = ',\n'.join(
        ','.join(language_names[i : i + 5])
        for i in range(0, len(language_names), 5)
    )

    return formatted_names


@app.get('/api/{templates}', response_class=PlainTextResponse)
async def get_template(templates: str):
    """
    Return gitignore content with all the languages.
    The template names should be passed in lower case, no spaces, and comma
    separated.

    To get all available templates, make a request to `/api/list`

    Example:
        `https://donotcommit.com/api/python,lua,zig`
    """
    templates_names = templates.split(',')

    gitignore_response = ''
    for template in templates_names:
        found_template = tuple(
            GITIGNORE_FOLDER.glob(
                f'{template}.gitignore', case_sensitive=False
            )
        )

        if not found_template:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f'Template "{template}" not found.',
            )

        template_content = Path(found_template[0]).read_text(encoding='utf-8')
        content = f'## {template.capitalize()}\n\n{template_content}\n'
        gitignore_response += content

    return gitignore_response
