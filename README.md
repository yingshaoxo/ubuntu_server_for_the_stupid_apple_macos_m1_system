# ubuntu_server_for_the_stupid_apple_macos_m1_system

## build
Edit `ssh_root_password` environment variable in `docker-compose.build.yaml` file first.

Then:

```bash
docker-compose -f docker-compose.build.yaml build
```

## run
```bash
docker-compose -f docker-compose.build.yaml up -d
ssh root@127.0.0.1 -p 2222
```