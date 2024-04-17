## 使用方式
需要使用最新版本[sophon-sail](https://gerrit-ai.sophgo.vip:8443/#/admin/projects/sophon-sail), sail的编译可参考sophon-sail手册，sail的编译参数为
```bash
cmake -DONLY_RUNTIME=ON ..
make pysail
```

还需要安装第三方库
```bash
pip3 install -r requirements.txt
```

下载模型
```bash
./scripts/download.sh
```
如需修改模型路径和一些参数，修改app.py
```python
model_path = os.environ.get('MODEL_PATH', './models/BM1684X/qwen-7b_int4_1dev.bmodel')
tokenizer_path = os.environ.get('TOKENIZER_PATH', './token_config')
dev_id = os.environ.get('DEV_ID', 0)
```


启动grpc服务
```bash
python3 api_server/app.py
```

## 接口说明
### StreamComplete
接收请求参数需要传入system_message和history，history的形式为`[{"role": 1, "content": xxx}, {"role": 2, "content": xxx}, {"role": 1, "content": xxx}]`, history最后一项必须为`"role": 1`, 例如：
```json
{
    "history": [{"role": 1, "content": "你好"}],
    "system_message": "You are a helpful assistant.",
}
```

返回response
```json
{"model_id": "","output_text": "你好","create_time": null,"token_usage": 1,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "!","create_time": null,"token_usage": 2,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "很高兴","create_time": null,"token_usage": 3,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "见到","create_time": null,"token_usage": 4,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "你","create_time": null,"token_usage": 5,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "。","create_time": null,"token_usage": 6,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "有什么","create_time": null,"token_usage": 7,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "我可以","create_time": null,"token_usage": 8,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "帮助","create_time": null,"token_usage": 9,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "你的","create_time": null,"token_usage": 10,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "吗","create_time": null,"token_usage": 11,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": "? ","create_time": null,"token_usage": 12,"finished": false,
"finish_reason": "UNKNOWN"}
{"model_id": "","output_text": " ","create_time": null,"token_usage": 13,"finished": false,
"finish_reason": "STOP"}
```
