#!/usr/bin/env bash
#CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build ./internal/admin/cmd/main.go
version=$1
docker build -t registry.cn-shanghai.aliyuncs.com/xcess-cr/aiircwms:${version} .
docker login --username=xcessadmin -p "xcess@)@!" registry.cn-shanghai.aliyuncs.com
docker push registry.cn-shanghai.aliyuncs.com/xcess-cr/aiircwms:${version}
docker rmi $(docker images registry.cn-shanghai.aliyuncs.com/xcess-cr/aiircwms:${version})
