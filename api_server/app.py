from concurrent import futures
import os
import grpc
from grpc_reflection.v1alpha import reflection

from protos import inference_service_pb2
from protos import inference_service_pb2_grpc

from utils.logging import init_logger
logger = init_logger("app")

SERVER_PORT = "18000"

# def get_ips():
#     ip_list = []
#     for interface in netifaces.interfaces():
#         addr = netifaces.ifaddresses(interface)
#         if netifaces.AF_INET in addr:
#             for link in addr[netifaces.AF_INET]:
#                 ip_list.append(link['addr'])
#     return ip_list


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    InferenceServicer = None
 
    logger.info("using TPU backend")
    from services.tpu_inference_service import TpuInferenceServicer
    
    model_path = os.environ.get('MODEL_PATH', './models/BM1684X/qwen-7b_int4_1dev.bmodel')
    tokenizer_path = os.environ.get('TOKENIZER_PATH', './token_config')
    dev_id = os.environ.get('DEV_ID', 0)
    
    InferenceServicer = TpuInferenceServicer(model_path, tokenizer_path, dev_id)
    inference_service_pb2_grpc.add_InferenceServiceServicer_to_server(InferenceServicer, server)
    
    logger.info("starting server")

    # TODO: add secure TLS channels
    # creds = grpc.ssl_server_credentials([(server_key, server_cert)])
    # server.add_secure_port("[::]:443", creds)

    # 增加反射以允许gRPC grpcurl进行服务发现
    SERVICE_NAMES = (
        inference_service_pb2.DESCRIPTOR.services_by_name['InferenceService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:' + SERVER_PORT)
    server.start()
    logger.info("server is up at port " + SERVER_PORT)

    # For receiving shutdown signals in the future, e.g. k8s
    # def handle_sigterm(*_):
    #     print("Received shutdown signal")
    #     all_rpcs_done_event = server.stop(30)
    #     all_rpcs_done_event.wait(30)
    #     print("Shut down gracefully")
    #
    # signal(SIGTERM, handle_sigterm)

    server.wait_for_termination()


if __name__ == '__main__':
    serve()
