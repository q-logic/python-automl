# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/prediction_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl_v1.proto import (
    annotation_payload_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2,
)
from google.cloud.automl_v1.proto import (
    data_items_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2,
)
from google.cloud.automl_v1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2,
)
from google.cloud.automl_v1.proto import (
    operations_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_operations__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/prediction_service.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=b"\n\032com.google.cloud.automl.v1B\026PredictionServiceProtoP\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n5google/cloud/automl_v1/proto/prediction_service.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x35google/cloud/automl_v1/proto/annotation_payload.proto\x1a-google/cloud/automl_v1/proto/data_items.proto\x1a%google/cloud/automl_v1/proto/io.proto\x1a-google/cloud/automl_v1/proto/operations.proto\x1a#google/longrunning/operations.proto"\xf4\x01\n\x0ePredictRequest\x12\x31\n\x04name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1b\x61utoml.googleapis.com/Model\x12<\n\x07payload\x18\x02 \x01(\x0b\x32&.google.cloud.automl.v1.ExamplePayloadB\x03\xe0\x41\x02\x12\x42\n\x06params\x18\x03 \x03(\x0b\x32\x32.google.cloud.automl.v1.PredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8b\x02\n\x0fPredictResponse\x12:\n\x07payload\x18\x01 \x03(\x0b\x32).google.cloud.automl.v1.AnnotationPayload\x12\x42\n\x12preprocessed_input\x18\x03 \x01(\x0b\x32&.google.cloud.automl.v1.ExamplePayload\x12G\n\x08metadata\x18\x02 \x03(\x0b\x32\x35.google.cloud.automl.v1.PredictResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xda\x02\n\x13\x42\x61tchPredictRequest\x12\x31\n\x04name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1b\x61utoml.googleapis.com/Model\x12J\n\x0cinput_config\x18\x03 \x01(\x0b\x32/.google.cloud.automl.v1.BatchPredictInputConfigB\x03\xe0\x41\x02\x12L\n\routput_config\x18\x04 \x01(\x0b\x32\x30.google.cloud.automl.v1.BatchPredictOutputConfigB\x03\xe0\x41\x02\x12G\n\x06params\x18\x05 \x03(\x0b\x32\x37.google.cloud.automl.v1.BatchPredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x91\x01\n\x12\x42\x61tchPredictResult\x12J\n\x08metadata\x18\x01 \x03(\x0b\x32\x38.google.cloud.automl.v1.BatchPredictResult.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x85\x04\n\x11PredictionService\x12\xaf\x01\n\x07Predict\x12&.google.cloud.automl.v1.PredictRequest\x1a\'.google.cloud.automl.v1.PredictResponse"S\x82\xd3\xe4\x93\x02\x37"2/v1/{name=projects/*/locations/*/models/*}:predict:\x01*\xda\x41\x13name,payload,params\x12\xf2\x01\n\x0c\x42\x61tchPredict\x12+.google.cloud.automl.v1.BatchPredictRequest\x1a\x1d.google.longrunning.Operation"\x95\x01\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*\xda\x41&name,input_config,output_config,params\xca\x41\'\n\x12\x42\x61tchPredictResult\x12\x11OperationMetadata\x1aI\xca\x41\x15\x61utoml.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xc2\x01\n\x1a\x63om.google.cloud.automl.v1B\x16PredictionServiceProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_operations__pb2.DESCRIPTOR,
        google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,
    ],
)


_PREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
    name="ParamsEntry",
    full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=621,
    serialized_end=666,
)

_PREDICTREQUEST = _descriptor.Descriptor(
    name="PredictRequest",
    full_name="google.cloud.automl.v1.PredictRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.PredictRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A\035\n\033automl.googleapis.com/Model",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.automl.v1.PredictRequest.payload",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="google.cloud.automl.v1.PredictRequest.params",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_PREDICTREQUEST_PARAMSENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=422,
    serialized_end=666,
)


_PREDICTRESPONSE_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=889,
    serialized_end=936,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
    name="PredictResponse",
    full_name="google.cloud.automl.v1.PredictResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.automl.v1.PredictResponse.payload",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="preprocessed_input",
            full_name="google.cloud.automl.v1.PredictResponse.preprocessed_input",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.automl.v1.PredictResponse.metadata",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_PREDICTRESPONSE_METADATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=669,
    serialized_end=936,
)


_BATCHPREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
    name="ParamsEntry",
    full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=621,
    serialized_end=666,
)

_BATCHPREDICTREQUEST = _descriptor.Descriptor(
    name="BatchPredictRequest",
    full_name="google.cloud.automl.v1.BatchPredictRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.BatchPredictRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A\035\n\033automl.googleapis.com/Model",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="input_config",
            full_name="google.cloud.automl.v1.BatchPredictRequest.input_config",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="output_config",
            full_name="google.cloud.automl.v1.BatchPredictRequest.output_config",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="google.cloud.automl.v1.BatchPredictRequest.params",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_BATCHPREDICTREQUEST_PARAMSENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=939,
    serialized_end=1285,
)


_BATCHPREDICTRESULT_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=889,
    serialized_end=936,
)

_BATCHPREDICTRESULT = _descriptor.Descriptor(
    name="BatchPredictResult",
    full_name="google.cloud.automl.v1.BatchPredictResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.automl.v1.BatchPredictResult.metadata",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_BATCHPREDICTRESULT_METADATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1288,
    serialized_end=1433,
)

_PREDICTREQUEST_PARAMSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name[
    "payload"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2._EXAMPLEPAYLOAD
)
_PREDICTREQUEST.fields_by_name["params"].message_type = _PREDICTREQUEST_PARAMSENTRY
_PREDICTRESPONSE_METADATAENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name[
    "payload"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2._ANNOTATIONPAYLOAD
)
_PREDICTRESPONSE.fields_by_name[
    "preprocessed_input"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2._EXAMPLEPAYLOAD
)
_PREDICTRESPONSE.fields_by_name[
    "metadata"
].message_type = _PREDICTRESPONSE_METADATAENTRY
_BATCHPREDICTREQUEST_PARAMSENTRY.containing_type = _BATCHPREDICTREQUEST
_BATCHPREDICTREQUEST.fields_by_name[
    "input_config"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2._BATCHPREDICTINPUTCONFIG
)
_BATCHPREDICTREQUEST.fields_by_name[
    "output_config"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2._BATCHPREDICTOUTPUTCONFIG
)
_BATCHPREDICTREQUEST.fields_by_name[
    "params"
].message_type = _BATCHPREDICTREQUEST_PARAMSENTRY
_BATCHPREDICTRESULT_METADATAENTRY.containing_type = _BATCHPREDICTRESULT
_BATCHPREDICTRESULT.fields_by_name[
    "metadata"
].message_type = _BATCHPREDICTRESULT_METADATAENTRY
DESCRIPTOR.message_types_by_name["PredictRequest"] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name["PredictResponse"] = _PREDICTRESPONSE
DESCRIPTOR.message_types_by_name["BatchPredictRequest"] = _BATCHPREDICTREQUEST
DESCRIPTOR.message_types_by_name["BatchPredictResult"] = _BATCHPREDICTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType(
    "PredictRequest",
    (_message.Message,),
    {
        "ParamsEntry": _reflection.GeneratedProtocolMessageType(
            "ParamsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _PREDICTREQUEST_PARAMSENTRY,
                "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictRequest.ParamsEntry)
            },
        ),
        "DESCRIPTOR": _PREDICTREQUEST,
        "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2",
        "__doc__": """Request message for [PredictionService.Predict][google.cloud.automl.v1
  .PredictionService.Predict].
  Attributes:
      name:
          Required. Name of the model requested to serve the prediction.
      payload:
          Required. Payload to perform a prediction on. The payload must
          match the problem type that the model was trained to solve.
      params:
          Additional domain-specific parameters, any string must be up
          to 25000 characters long.  AutoML Vision Classification
          ``score_threshold``    (float) A value from 0.0 to 1.0. When
          the model makes predictions for    an image, it will only
          produce results that have at least this    confidence score.
          The default is 0.5.  AutoML Vision Object Detection
          ``score_threshold``    (float) When Model detects objects on
          the image, it will only produce    bounding boxes which have
          at least this confidence score. Value in 0    to 1 range,
          default is 0.5. ``max_bounding_box_count``    (int64) The
          maximum number of bounding boxes returned. The default is
          100. The number of returned bounding boxes might be limited by
          the    server.  AutoML Tables  ``feature_importance``
          (boolean) Whether  [feature_importance][google.cloud.automl.v1
          .TablesModelColumnInfo.feature_importance] is populated in the
          returned list of
          [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation]
          objects. The default is false.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictRequest)
    },
)
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.ParamsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType(
    "PredictResponse",
    (_message.Message,),
    {
        "MetadataEntry": _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _PREDICTRESPONSE_METADATAENTRY,
                "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictResponse.MetadataEntry)
            },
        ),
        "DESCRIPTOR": _PREDICTRESPONSE,
        "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2",
        "__doc__": """Response message for [PredictionService.Predict][google.cloud.automl.v
  1.PredictionService.Predict].
  Attributes:
      payload:
          Prediction result. AutoML Translation and AutoML Natural
          Language Sentiment Analysis return precisely one payload.
      preprocessed_input:
          The preprocessed example that AutoML actually makes prediction
          on. Empty if AutoML does not preprocess the input example.
          For AutoML Natural Language (Classification, Entity
          Extraction, and Sentiment Analysis), if the input is a
          document, the recognized text is returned in the
          [document_text][google.cloud.automl.v1.Document.document_text]
          property.
      metadata:
          Additional domain-specific prediction response metadata.
          AutoML Vision Object Detection  ``max_bounding_box_count``
          (int64) The maximum number of bounding boxes to return per
          image.  AutoML Natural Language Sentiment Analysis
          ``sentiment_score``    (float, deprecated) A value between -1
          and 1, -1 maps to least    positive sentiment, while 1 maps to
          the most positive one and the    higher the score, the more
          positive the sentiment in the document is.    Yet these values
          are relative to the training data, so e.g. if all    data was
          positive then -1 is also positive (though the least).
          ``sentiment_score`` is not the same as “score” and “magnitude”
          from    Sentiment Analysis in the Natural Language API.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictResponse)
    },
)
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.MetadataEntry)

BatchPredictRequest = _reflection.GeneratedProtocolMessageType(
    "BatchPredictRequest",
    (_message.Message,),
    {
        "ParamsEntry": _reflection.GeneratedProtocolMessageType(
            "ParamsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _BATCHPREDICTREQUEST_PARAMSENTRY,
                "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictRequest.ParamsEntry)
            },
        ),
        "DESCRIPTOR": _BATCHPREDICTREQUEST,
        "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2",
        "__doc__": """Request message for [PredictionService.BatchPredict][google.cloud.auto
  ml.v1.PredictionService.BatchPredict].
  Attributes:
      name:
          Required. Name of the model requested to serve the batch
          prediction.
      input_config:
          Required. The input configuration for batch prediction.
      output_config:
          Required. The Configuration specifying where output
          predictions should be written.
      params:
          Additional domain-specific parameters for the predictions, any
          string must be up to 25000 characters long.  AutoML Natural
          Language Classification  ``score_threshold``    (float) A
          value from 0.0 to 1.0. When the model makes predictions for
          a text snippet, it will only produce results that have at
          least this    confidence score. The default is 0.5.  AutoML
          Vision Classification  ``score_threshold``    (float) A value
          from 0.0 to 1.0. When the model makes predictions for    an
          image, it will only produce results that have at least this
          confidence score. The default is 0.5.  AutoML Vision Object
          Detection  ``score_threshold``    (float) When Model detects
          objects on the image, it will only produce    bounding boxes
          which have at least this confidence score. Value in 0    to 1
          range, default is 0.5. ``max_bounding_box_count``    (int64)
          The maximum number of bounding boxes returned per image. The
          default is 100, the number of bounding boxes returned might be
          limited by the server. AutoML Video Intelligence
          Classification ``score_threshold``    (float) A value from 0.0
          to 1.0. When the model makes predictions for    a video, it
          will only produce results that have at least this
          confidence score. The default is 0.5.
          ``segment_classification``    (boolean) Set to true to request
          segment-level classification. AutoML    Video Intelligence
          returns labels and their confidence scores for the    entire
          segment of the video that user specified in the request
          configuration. The default is true. ``shot_classification``
          (boolean) Set to true to request shot-level classification.
          AutoML    Video Intelligence determines the boundaries for
          each camera shot in    the entire segment of the video that
          user specified in the request    configuration. AutoML Video
          Intelligence then returns labels and    their confidence
          scores for each detected shot, along with the start    and end
          time of the shot. The default is false.  WARNING: Model
          evaluation is not done for this classification type, the
          quality of it depends on training data, but there are no
          metrics provided to describe that quality.
          ``1s_interval_classification``    (boolean) Set to true to
          request classification for a video at    one-second intervals.
          AutoML Video Intelligence returns labels and    their
          confidence scores for each second of the entire segment of the
          video that user specified in the request configuration. The
          default    is false.  WARNING: Model evaluation is not done
          for this classification type, the quality of it depends on
          training data, but there are no metrics provided to describe
          that quality.  AutoML Video Intelligence Object Tracking
          ``score_threshold``    (float) When Model detects objects on
          video frames, it will only    produce bounding boxes which
          have at least this confidence score.    Value in 0 to 1 range,
          default is 0.5. ``max_bounding_box_count``    (int64) The
          maximum number of bounding boxes returned per image. The
          default is 100, the number of bounding boxes returned might be
          limited by the server. ``min_bounding_box_size``    (float)
          Only bounding boxes with shortest edge at least that long as
          a relative value of video frame size are returned. Value in 0
          to 1    range. Default is 0.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictRequest)
    },
)
_sym_db.RegisterMessage(BatchPredictRequest)
_sym_db.RegisterMessage(BatchPredictRequest.ParamsEntry)

BatchPredictResult = _reflection.GeneratedProtocolMessageType(
    "BatchPredictResult",
    (_message.Message,),
    {
        "MetadataEntry": _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _BATCHPREDICTRESULT_METADATAENTRY,
                "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictResult.MetadataEntry)
            },
        ),
        "DESCRIPTOR": _BATCHPREDICTRESULT,
        "__module__": "google.cloud.automl_v1.proto.prediction_service_pb2",
        "__doc__": """Result of the Batch Predict. This message is returned in
  [response][google.longrunning.Operation.response] of the operation
  returned by the [PredictionService.BatchPredict][google.cloud.automl.v
  1.PredictionService.BatchPredict].
  Attributes:
      metadata:
          Additional domain-specific prediction response metadata.
          AutoML Vision Object Detection  ``max_bounding_box_count``
          (int64) The maximum number of bounding boxes returned per
          image.  AutoML Video Intelligence Object Tracking
          ``max_bounding_box_count``    (int64) The maximum number of
          bounding boxes returned per frame.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictResult)
    },
)
_sym_db.RegisterMessage(BatchPredictResult)
_sym_db.RegisterMessage(BatchPredictResult.MetadataEntry)


DESCRIPTOR._options = None
_PREDICTREQUEST_PARAMSENTRY._options = None
_PREDICTREQUEST.fields_by_name["name"]._options = None
_PREDICTREQUEST.fields_by_name["payload"]._options = None
_PREDICTRESPONSE_METADATAENTRY._options = None
_BATCHPREDICTREQUEST_PARAMSENTRY._options = None
_BATCHPREDICTREQUEST.fields_by_name["name"]._options = None
_BATCHPREDICTREQUEST.fields_by_name["input_config"]._options = None
_BATCHPREDICTREQUEST.fields_by_name["output_config"]._options = None
_BATCHPREDICTRESULT_METADATAENTRY._options = None

_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
    name="PredictionService",
    full_name="google.cloud.automl.v1.PredictionService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\025automl.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    create_key=_descriptor._internal_create_key,
    serialized_start=1436,
    serialized_end=1953,
    methods=[
        _descriptor.MethodDescriptor(
            name="Predict",
            full_name="google.cloud.automl.v1.PredictionService.Predict",
            index=0,
            containing_service=None,
            input_type=_PREDICTREQUEST,
            output_type=_PREDICTRESPONSE,
            serialized_options=b'\202\323\344\223\0027"2/v1/{name=projects/*/locations/*/models/*}:predict:\001*\332A\023name,payload,params',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="BatchPredict",
            full_name="google.cloud.automl.v1.PredictionService.BatchPredict",
            index=1,
            containing_service=None,
            input_type=_BATCHPREDICTREQUEST,
            output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
            serialized_options=b"\202\323\344\223\002<\"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\001*\332A&name,input_config,output_config,params\312A'\n\022BatchPredictResult\022\021OperationMetadata",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name["PredictionService"] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
