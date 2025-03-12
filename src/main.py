from pathlib import Path
from typing import Final

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

PROJECT_ROOT: Final = Path(__file__).parent.parent
GITIGNORE_FOLDER: Final = PROJECT_ROOT / 'gitignore'
TEMPLATES: Final = GITIGNORE_FOLDER.glob('*.gitignore')


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
