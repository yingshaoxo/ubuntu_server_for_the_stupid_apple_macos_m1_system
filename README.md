# Ubuntu SSH Server for The Stupid `Apple Macos M1 System`

## Run directly from docker-compose.yaml file
> https://hub.docker.com/r/yingshaoxo/ubuntu_ssh_server_for_the_stupid_apple_macos_m1_system

```yaml
version: "3.9"

services:
  ssh_ubuntu:
    platform: linux/amd64
    image: yingshaoxo/ubuntu_ssh_server_for_the_stupid_apple_macos_m1_system:v1
    ports:
      - "2222:22"
    environment:
      - ssh_root_password=yingshaoxo
    volumes:
      - "~/ubuntu_docker:/root"
    restart: unless-stopped
```

```bash
docker-compose up -d
ssh root@127.0.0.1 -p 2222
```

## Another method: use `multipass`

> This method allows you to use `systemd` and `snap` and `docker`

```bash
multipass stop primary
multipass delete primary
multipass purge
multipass launch 22.04 --cpus 8 --memory 16G --disk 50G --name primary

multipass umount primary 
multipass mount ~/ubuntu_docker primary:/root
multipass shell
sudo su
cd /root

export ssh_root_password=yingshaoxo
curl -sSL https://raw.githubusercontent.com/yingshaoxo/ubuntu_ssh_server_for_the_stupid_apple_macos_m1_system/main/basement/2.set_ssh_password_script.py | python3
```

```bash
multipass info primary
```

You will get an ip address like `192.168.64.16` in the output:
```
Name:           primary
State:          Running
IPv4:           192.168.64.16
                172.17.0.1
Release:        Ubuntu 22.04.2 LTS
Image hash:     f6b5b3a980f2 (Ubuntu 22.04 LTS)
CPU(s):         8
Load:           0.24 0.05 0.02
Disk usage:     2.0GiB out of 48.3GiB
Memory usage:   280.8MiB out of 15.6GiB
Mounts:         /Users/yingshaoxo/ubuntu_docker => /root
                    UID map: 501:default
                    GID map: 80:default
```

```bash
ssh root@192.168.64.16
# the password is 'yingshaoxo' here
```

## Build by yourself
### build
Edit `ssh_root_password` environment variable in `docker-compose.build.yaml` file first.

Then:

```bash
docker-compose -f docker-compose.build.yaml build
```

### Run
```bash
docker-compose -f docker-compose.build.yaml up -d
ssh root@127.0.0.1 -p 2222
```
