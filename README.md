# tap-capsulecrm

`tap-capsulecrm` is a Singer tap for Capsule.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
# pip
pip install git+https://github.com/Matatika/tap-capsulecrm

# pipx
pipx install git+https://github.com/Matatika/tap-capsulecrm

# poetry
poetry add git+https://github.com/Matatika/tap-capsulecrm
```

## Configuration

### Accepted Config Options

Name | Required | Default | Description
--- | --- | --- | ---
`access_token` | Yes |  | Your Capsule access token
`client_id` | No |  | Your Capsule client ID
`client_secret` | No | | Your Capsule client secret
`refresh_token` | No | | Your Capsule refresh token

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-capsulecrm --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

You can find how to get your access token here: https://www.matatika.com/docs/instant-insights/tap-capsulecrm/prerequisites

## Usage

You can easily run `tap-capsulecrm` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-capsulecrm --version
tap-capsulecrm --help
tap-capsulecrm --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_capsulecrm/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-capsulecrm` CLI interface directly using `poetry run`:

```bash
poetry run tap-capsulecrm --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-capsulecrm
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-capsulecrm --version
# OR run a test `elt` pipeline:
meltano elt tap-capsulecrm target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
