# Website

![Lines of code](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/furqunali/humanoid-robotics-textbook/main/.github/badges/loc.json)

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

Using SSH:

```bash
USE_SSH=true yarn deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.


## Engineering Validation

The textbook tooling now includes deterministic BM25 lexical search over the knowledge corpus, Unicode-aware tokenization, and stricter validation for knowledge chunk sizes and ingestion inputs. These checks keep the knowledge layer deterministic and fail early on malformed configuration.
