# `Ubuntu SSH Server` for The Stupid `Apple Macos M1 System`

## Build
Edit `ssh_root_password` environment variable in `docker-compose.build.yaml` file first.

Then:

```bash
docker-compose -f docker-compose.build.yaml build
```

## Run
```bash
docker-compose -f docker-compose.build.yaml up -d
ssh root@127.0.0.1 -p 2222
```