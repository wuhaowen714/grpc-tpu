# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inference_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17inference_service.proto\x12&com.sophgo.lmcs.inferenceservice.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xef\x03\n\x17\x43reateCompletionRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x16\n\x0esystem_message\x18\n \x01(\t\x12X\n\x07history\x18\x0b \x03(\x0b\x32G.com.sophgo.lmcs.inferenceservice.proto.CreateCompletionRequest.History\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x16\n\x0emax_new_tokens\x18\x03 \x01(\x05\x12\x11\n\tnum_beams\x18\x04 \x01(\x05\x12\r\n\x05top_k\x18\x05 \x01(\x05\x12\r\n\x05top_p\x18\x06 \x01(\x02\x12\x13\n\x0btemperature\x18\x07 \x01(\x02\x12\x1a\n\x12repetition_penalty\x18\x08 \x01(\x02\x12\x11\n\tdo_sample\x18\t \x01(\x08\x1a\xb2\x01\n\x07History\x12\x61\n\x04role\x18\x01 \x01(\x0e\x32S.com.sophgo.lmcs.inferenceservice.proto.CreateCompletionRequest.History.HistoryRole\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"3\n\x0bHistoryRole\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tASSISTANT\x10\x01\x12\x08\n\x04USER\x10\x02\"\xa1\x02\n\nCompletion\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x13\n\x0boutput_text\x18\x02 \x01(\t\x12/\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0btoken_usage\x18\x04 \x01(\x05\x12\x10\n\x08\x66inished\x18\x05 \x01(\x08\x12V\n\rfinish_reason\x18\x06 \x01(\x0e\x32?.com.sophgo.lmcs.inferenceservice.proto.Completion.FinishReason\"<\n\x0c\x46inishReason\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\n\n\x06LENGTH\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x32\xa2\x02\n\x10InferenceService\x12\x81\x01\n\x08\x43omplete\x12?.com.sophgo.lmcs.inferenceservice.proto.CreateCompletionRequest\x1a\x32.com.sophgo.lmcs.inferenceservice.proto.Completion\"\x00\x12\x89\x01\n\x0eStreamComplete\x12?.com.sophgo.lmcs.inferenceservice.proto.CreateCompletionRequest\x1a\x32.com.sophgo.lmcs.inferenceservice.proto.Completion\"\x00\x30\x01\x42\x34\n0com.sophgo.lmcs.inferenceservice.proto.generatedP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n0com.sophgo.lmcs.inferenceservice.proto.generatedP\001'
  _globals['_CREATECOMPLETIONREQUEST']._serialized_start=101
  _globals['_CREATECOMPLETIONREQUEST']._serialized_end=596
  _globals['_CREATECOMPLETIONREQUEST_HISTORY']._serialized_start=418
  _globals['_CREATECOMPLETIONREQUEST_HISTORY']._serialized_end=596
  _globals['_CREATECOMPLETIONREQUEST_HISTORY_HISTORYROLE']._serialized_start=545
  _globals['_CREATECOMPLETIONREQUEST_HISTORY_HISTORYROLE']._serialized_end=596
  _globals['_COMPLETION']._serialized_start=599
  _globals['_COMPLETION']._serialized_end=888
  _globals['_COMPLETION_FINISHREASON']._serialized_start=828
  _globals['_COMPLETION_FINISHREASON']._serialized_end=888
  _globals['_INFERENCESERVICE']._serialized_start=891
  _globals['_INFERENCESERVICE']._serialized_end=1181
# @@protoc_insertion_point(module_scope)
