# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/regression.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/regression.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1B\017RegressionProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2google/cloud/automl_v1beta1/proto/regression.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto"\xbb\x01\n\x1bRegressionEvaluationMetrics\x12\x1f\n\x17root_mean_squared_error\x18\x01 \x01(\x02\x12\x1b\n\x13mean_absolute_error\x18\x02 \x01(\x02\x12&\n\x1emean_absolute_percentage_error\x18\x03 \x01(\x02\x12\x11\n\tr_squared\x18\x04 \x01(\x02\x12#\n\x1broot_mean_squared_log_error\x18\x05 \x01(\x02\x42\xb4\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x0fRegressionProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,],
)


_REGRESSIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="RegressionEvaluationMetrics",
    full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="root_mean_squared_error",
            full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics.root_mean_squared_error",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="mean_absolute_error",
            full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics.mean_absolute_error",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="mean_absolute_percentage_error",
            full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics.mean_absolute_percentage_error",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="r_squared",
            full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics.r_squared",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="root_mean_squared_log_error",
            full_name="google.cloud.automl.v1beta1.RegressionEvaluationMetrics.root_mean_squared_log_error",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=114,
    serialized_end=301,
)

DESCRIPTOR.message_types_by_name[
    "RegressionEvaluationMetrics"
] = _REGRESSIONEVALUATIONMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegressionEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "RegressionEvaluationMetrics",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGRESSIONEVALUATIONMETRICS,
        "__module__": "google.cloud.automl_v1beta1.proto.regression_pb2",
        "__doc__": """Metrics for regression problems.
  Attributes:
      root_mean_squared_error:
          Output only. Root Mean Squared Error (RMSE).
      mean_absolute_error:
          Output only. Mean Absolute Error (MAE).
      mean_absolute_percentage_error:
          Output only. Mean absolute percentage error. Only set if all
          ground truth values are are positive.
      r_squared:
          Output only. R squared.
      root_mean_squared_log_error:
          Output only. Root mean squared log error.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.RegressionEvaluationMetrics)
    },
)
_sym_db.RegisterMessage(RegressionEvaluationMetrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
