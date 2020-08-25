This template will:
1. Trigger workflow when
    - git push to branch `master`
2. Build a docker image from this repo.
3. Push docker images to different Docker Registry:
  - [Docker Hub](#docker-hub)

## [Docker Hub](https://hub.docker.com/)
- [Create acceess token from Docker Hub](https://docs.docker.com/docker-hub/access-tokens/#create-an-access-token)
    - Add `secrets.DOCKER_USERNAME`, `secrets.DOCKER_PASSWORD`: Setting -> Secrets -> New secret
