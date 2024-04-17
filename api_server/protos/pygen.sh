#!/bin/bash
# 假设api proto被放置在 ../../apis
echo '如失败，检查是否安装了 grpcio grpcio-tools ...'
protoc -I=../../../apis/ --python_out=./ ../../../apis/backend_and_gpu.proto
python -m grpc_tools.protoc -I=../../../apis --python_out=./ --grpc_python_out=./ ../../../apis/inference_service.proto && \
touch __init__.py && \
echo '成功完成!'
echo '生成的_grpc.py中，可能需要手动调整首行import以满足文件组织'
