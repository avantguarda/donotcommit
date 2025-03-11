# Do not commit it

I once commit a file I should ignore. Do you know what happened? A coworker computer exploded. Now you know this is serious, you should consider using our API.

This API wil be compliant with [gitignore.io](https://www.toptal.com/developers/gitignore) by toptal, so you can just change your request from:

`toptal.com/developers/gitignore/api/`

to 

`donotcommit.com/api/`

Nice, right?

# Templates source

For now, we are using [github/gitignore](https://github.com/github/gitignore) as the gitignore templates source, but we recognize that they take some time to accept PRs. This delay also motivated toptal team to make their own gitignore source, but it is archived now. That's why we are building an alternative.

# Clients

Use one client to make your life easier when managing gitignore files:

- zignr: <https://github.com/ivansantiagojr/zignr>

You can list your client here, just open a PR!

# Contributing

## Setting Up the Development Environment

To set up the development environment, you'll need to have Python 3.13 installed. You should use [uv](https://docs.astral.sh/uv/) to manage dependencies and run commands.

1. **Clone the Repository:**

   ```sh
   git clone git@github.com:brasilisclub/donotcommit.com.git
   cd donotcommit.com
   ```

2. **Install uv:**

   If you don't have uv installed, you can install it by following the instructions on the [uv installation page](https://docs.astral.sh/uv/getting-started/installation/).

3. **Install Dependencies:**

   ```sh
   uv sync
   ```

   This command will install all the necessary dependencies for both the application and development.

4. **Activate the Virtual Environment:**
   ```sh
   source .venv/bin/activate
   ```

## Running locally

To run the application, use the following command:

```sh
task run
```

This command will start a local development server.

## Development Commands

We use `taskipy` for task management. Here are some useful commands:

- **Linting:**

  ```sh
  task lint
  ```

  This command will run Ruff to check for code issues and display any differences.

- **Formatting:**

  ```sh
  task format
  ```

  This command will automatically format your code using Ruff.

- **Run Tests:**

  ```sh
  task test
  ```

  This will run the test suite using pytest and display coverage information.

- **Run Mypy:**

  ```sh
  mypy .
  ```

  This will run Mypy for type checking.

## Development Tools Configuration

- **Pytest:**

  Configuration for pytest is specified in `pyproject.toml` under `[tool.pytest.ini_options]`.

- **Mypy:**

  Configuration for Mypy is specified under `[tool.mypy]`.

- **Ruff:**

  Configuration for Ruff, including linting and formatting settings, is specified under `[tool.ruff]`.

## Contribution

If you would like to contribute to donotcommit API, please fork the repository and submit a pull request with your changes. Ensure that your changes pass the linting and testing requirements before submitting.

