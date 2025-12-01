# git-actions-examples

Sample GitHub Actions workflows included in this repository:

- `matrix-strategy.yml` – demonstrates a build matrix that exercises Node.js 16/18/20 on Ubuntu and Windows runners.
- `different-runner.yml` – shows how to fan out the same checks across Ubuntu, Windows, and macOS runners.
- `docker-build.yml` – builds the sample `Dockerfile` using Docker Buildx on every push to `main`.
- `sequential-workflow.yml` – runs build → test → deploy stages sequentially via `needs` dependencies.
- `parallel-workflow.yml` – runs linting, static analysis, and integration tests in parallel with no dependencies.