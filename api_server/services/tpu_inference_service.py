import threading
import time

from protos import inference_service_pb2, inference_service_pb2_grpc
from utils.logging import init_logger
from transformers import AutoTokenizer
from utils.qwen import Qwen

import sophon.sail as sail



logger = init_logger(__name__)



class TpuInferenceServicer(inference_service_pb2_grpc.InferenceServiceServicer):

    def __init__(self, model_path, tokenizer_path, dev_id) -> None:

        self.handle = sail.Handle(dev_id)
        logger.info("from path: %s, load bmodel", model_path)
        self.net =  sail.Engine(model_path, 0, sail.IOMode.DEVIO)
        logger.info("from path: %s, load tokenizer", tokenizer_path)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, trust_remote_code=True)
        #self.lock = threading.Lock()


    def Complete(self, request, context):
        logger.info("complete: %s", request)
        try:

            logger.info(f'system message: {request.system_message}')

            #TODO:添加回答逻辑

            #self.lock.acquire()
            response = inference_service_pb2.Completion()
            response.output_text = 'hello'

            logger.info("complete response: %s", response.output_text)
            return response
        except Exception as e:
            logger.error(str(e))
        finally:
            #self.lock.release()
            logger.info("complete done")



    def StreamComplete(self, request, context):
        logger.info("stream complete: %s", request)
        try:
            client = Qwen(self.handle, self.net, self.tokenizer)
            logger.info(f'system message: {request.system_message}')
            #self.lock.acquire()
            input_str, history = self.get_input(request.history)
            tok_num = 0
            for text in client.chat_stream(input_str, history, request.system_message):
                tok_num += 1
                response = inference_service_pb2.Completion()
                response.output_text = text
                if text.startswith('##'):
                    response.output_text = " "
                    response.finished = True
                    res = text[2:]
                    if res == "LENGTH":
                        response.finish_reason = 2
                    elif res == "STOP":
                        response.finish_reason = 1
                    elif res == "ERROR":
                        response.finish_reason = 3
                    else: 
                        response.finish_reason = 0    
                
                response.token_usage = tok_num
                yield response

        except Exception as e:
            logger.error(str(e))
            print("An error occurred:", str(e))
        finally:
            #self.lock.release()
            logger.info("stream complete done")

        # return super().Complete(request, context)
        
    def get_input(self, messages):
        history = []
        input_str = ''
        for item in messages:
            if (item.role == 2):
                history.append({"role": "assitant", "content": item.content})
            elif (item.role == 1):
                history.append({"role": "user", "content": item.content})
            else:
                raise Exception(f"Invalid Type of role:  {item.role}")
        history_len = len(history)
        if (history_len == 0):
            raise Exception("no question input")
        input_item = history[history_len - 1]
        if (input_item["role"] != "user"):
            raise Exception(f"Invalid Format of history: {history}")
        input_str = input_item["content"]
        history = history[:(history_len - 1)]
        if (not input_str):
            raise Exception("no question input")
        return input_str, history


