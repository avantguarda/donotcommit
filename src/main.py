from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Hello, world!'}


@app.get('/api/list', response_class=PlainTextResponse)
async def list_templates():
    """
    Lists all available gitignore templates by github.com/github/gitignore
    """
    project_root = Path(__file__).parent.parent
    gitignore_folder = project_root / 'gitignore'

    templates = gitignore_folder.glob('*.gitignore')
    language_names = sorted([
        Path(file).name.lower().removesuffix('.gitignore')
        for file in templates
    ])

    formatted_names = ',\n'.join(
        ','.join(language_names[i : i + 5])
        for i in range(0, len(language_names), 5)
    )

    return formatted_names
