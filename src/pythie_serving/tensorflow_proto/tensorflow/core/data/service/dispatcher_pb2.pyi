"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tensorflow.core.data.service.common_pb2
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.protobuf.data_service_pb2
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TaskProgress(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_ID_FIELD_NUMBER: builtins.int
    COMPLETED_FIELD_NUMBER: builtins.int
    task_id: builtins.int
    """The task that this message is about."""
    completed: builtins.bool
    """Whether the task has completed."""
    def __init__(
        self,
        *,
        task_id: builtins.int = ...,
        completed: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["completed", b"completed", "task_id", b"task_id"]) -> None: ...

global___TaskProgress = TaskProgress

@typing_extensions.final
class WorkerHeartbeatRequest(google.protobuf.message.Message):
    """Next tag: 6"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKER_ADDRESS_FIELD_NUMBER: builtins.int
    TRANSFER_ADDRESS_FIELD_NUMBER: builtins.int
    WORKER_TAGS_FIELD_NUMBER: builtins.int
    WORKER_UID_FIELD_NUMBER: builtins.int
    CURRENT_TASKS_FIELD_NUMBER: builtins.int
    worker_address: builtins.str
    transfer_address: builtins.str
    @property
    def worker_tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    worker_uid: builtins.int
    """The UID of the worker Borg job, used for telemetry."""
    @property
    def current_tasks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        worker_address: builtins.str = ...,
        transfer_address: builtins.str = ...,
        worker_tags: collections.abc.Iterable[builtins.str] | None = ...,
        worker_uid: builtins.int = ...,
        current_tasks: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_tasks", b"current_tasks", "transfer_address", b"transfer_address", "worker_address", b"worker_address", "worker_tags", b"worker_tags", "worker_uid", b"worker_uid"]) -> None: ...

global___WorkerHeartbeatRequest = WorkerHeartbeatRequest

@typing_extensions.final
class WorkerHeartbeatResponse(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEW_TASKS_FIELD_NUMBER: builtins.int
    TASKS_TO_DELETE_FIELD_NUMBER: builtins.int
    @property
    def new_tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.data.service.common_pb2.TaskDef]: ...
    @property
    def tasks_to_delete(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        new_tasks: collections.abc.Iterable[tensorflow.core.data.service.common_pb2.TaskDef] | None = ...,
        tasks_to_delete: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["new_tasks", b"new_tasks", "tasks_to_delete", b"tasks_to_delete"]) -> None: ...

global___WorkerHeartbeatResponse = WorkerHeartbeatResponse

@typing_extensions.final
class WorkerUpdateRequest(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKER_ADDRESS_FIELD_NUMBER: builtins.int
    UPDATES_FIELD_NUMBER: builtins.int
    worker_address: builtins.str
    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TaskProgress]: ...
    def __init__(
        self,
        *,
        worker_address: builtins.str = ...,
        updates: collections.abc.Iterable[global___TaskProgress] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["updates", b"updates", "worker_address", b"worker_address"]) -> None: ...

global___WorkerUpdateRequest = WorkerUpdateRequest

@typing_extensions.final
class WorkerUpdateResponse(google.protobuf.message.Message):
    """Next tag: 1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WorkerUpdateResponse = WorkerUpdateResponse

@typing_extensions.final
class GetDatasetDefRequest(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_id", b"dataset_id"]) -> None: ...

global___GetDatasetDefRequest = GetDatasetDefRequest

@typing_extensions.final
class GetDatasetDefResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_DEF_FIELD_NUMBER: builtins.int
    @property
    def dataset_def(self) -> tensorflow.core.data.service.common_pb2.DatasetDef: ...
    def __init__(
        self,
        *,
        dataset_def: tensorflow.core.data.service.common_pb2.DatasetDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset_def", b"dataset_def"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_def", b"dataset_def"]) -> None: ...

global___GetDatasetDefResponse = GetDatasetDefResponse

@typing_extensions.final
class GetSplitRequest(google.protobuf.message.Message):
    """Next tag: 4"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITERATION_ID_FIELD_NUMBER: builtins.int
    REPETITION_FIELD_NUMBER: builtins.int
    SPLIT_PROVIDER_INDEX_FIELD_NUMBER: builtins.int
    iteration_id: builtins.int
    repetition: builtins.int
    split_provider_index: builtins.int
    def __init__(
        self,
        *,
        iteration_id: builtins.int = ...,
        repetition: builtins.int = ...,
        split_provider_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["iteration_id", b"iteration_id", "repetition", b"repetition", "split_provider_index", b"split_provider_index"]) -> None: ...

global___GetSplitRequest = GetSplitRequest

@typing_extensions.final
class GetSplitResponse(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPLIT_FIELD_NUMBER: builtins.int
    END_OF_SPLITS_FIELD_NUMBER: builtins.int
    @property
    def split(self) -> tensorflow.core.framework.tensor_pb2.TensorProto: ...
    end_of_splits: builtins.bool
    def __init__(
        self,
        *,
        split: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        end_of_splits: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["split", b"split"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_of_splits", b"end_of_splits", "split", b"split"]) -> None: ...

global___GetSplitResponse = GetSplitResponse

@typing_extensions.final
class GetVersionRequest(google.protobuf.message.Message):
    """Next tag: 1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetVersionRequest = GetVersionRequest

@typing_extensions.final
class GetVersionResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    version: builtins.int
    def __init__(
        self,
        *,
        version: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version", b"version"]) -> None: ...

global___GetVersionResponse = GetVersionResponse

@typing_extensions.final
class GetOrRegisterDatasetRequest(google.protobuf.message.Message):
    """Next tag: 5"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    DATASET_ID_FIELD_NUMBER: builtins.int
    @property
    def dataset(self) -> tensorflow.core.data.service.common_pb2.DatasetDef:
        """The dataset to register."""
    @property
    def metadata(self) -> tensorflow.core.protobuf.data_service_pb2.DataServiceMetadata:
        """Metadata related to tf.data service."""
    dataset_id: builtins.str
    """If provided, tf.data service will register the dataset with the specified
    ID. Otherwise, it will generate a unique dataset ID.
    """
    def __init__(
        self,
        *,
        dataset: tensorflow.core.data.service.common_pb2.DatasetDef | None = ...,
        metadata: tensorflow.core.protobuf.data_service_pb2.DataServiceMetadata | None = ...,
        dataset_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset", b"dataset", "dataset_id", b"dataset_id", "metadata", b"metadata", "optional_dataset_id", b"optional_dataset_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset", b"dataset", "dataset_id", b"dataset_id", "metadata", b"metadata", "optional_dataset_id", b"optional_dataset_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_dataset_id", b"optional_dataset_id"]) -> typing_extensions.Literal["dataset_id"] | None: ...

global___GetOrRegisterDatasetRequest = GetOrRegisterDatasetRequest

@typing_extensions.final
class GetOrRegisterDatasetResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    """The id for the registered dataset."""
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_id", b"dataset_id"]) -> None: ...

global___GetOrRegisterDatasetResponse = GetOrRegisterDatasetResponse

@typing_extensions.final
class GetDataServiceMetadataRequest(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    """The dataset id to get the data service dataset metadata."""
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_id", b"dataset_id"]) -> None: ...

global___GetDataServiceMetadataRequest = GetDataServiceMetadataRequest

@typing_extensions.final
class GetDataServiceMetadataResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> tensorflow.core.protobuf.data_service_pb2.DataServiceMetadata:
        """The retrieved data service dataset metadata."""
    def __init__(
        self,
        *,
        metadata: tensorflow.core.protobuf.data_service_pb2.DataServiceMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> None: ...

global___GetDataServiceMetadataResponse = GetDataServiceMetadataResponse

@typing_extensions.final
class GetDataServiceConfigRequest(google.protobuf.message.Message):
    """Next tag: 1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetDataServiceConfigRequest = GetDataServiceConfigRequest

@typing_extensions.final
class GetDataServiceConfigResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> tensorflow.core.protobuf.data_service_pb2.DataServiceConfig: ...
    def __init__(
        self,
        *,
        config: tensorflow.core.protobuf.data_service_pb2.DataServiceConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___GetDataServiceConfigResponse = GetDataServiceConfigResponse

@typing_extensions.final
class GetOrCreateJobRequest(google.protobuf.message.Message):
    """Next tag: 7"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    PROCESSING_MODE_DEF_FIELD_NUMBER: builtins.int
    JOB_NAME_FIELD_NUMBER: builtins.int
    NUM_CONSUMERS_FIELD_NUMBER: builtins.int
    USE_CROSS_TRAINER_CACHE_FIELD_NUMBER: builtins.int
    TARGET_WORKERS_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    """The id of the dataset to create a job for."""
    @property
    def processing_mode_def(self) -> tensorflow.core.protobuf.data_service_pb2.ProcessingModeDef:
        """A mode controlling how the tf.data service produces data for the job."""
    job_name: builtins.str
    num_consumers: builtins.int
    use_cross_trainer_cache: builtins.bool
    """True if cross-trainer cache is enabled."""
    target_workers: tensorflow.core.data.service.common_pb2.TargetWorkers.ValueType
    """Specifies which workers the client of this job reads from."""
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
        processing_mode_def: tensorflow.core.protobuf.data_service_pb2.ProcessingModeDef | None = ...,
        job_name: builtins.str = ...,
        num_consumers: builtins.int = ...,
        use_cross_trainer_cache: builtins.bool = ...,
        target_workers: tensorflow.core.data.service.common_pb2.TargetWorkers.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job_name", b"job_name", "num_consumers", b"num_consumers", "optional_job_name", b"optional_job_name", "optional_num_consumers", b"optional_num_consumers", "processing_mode_def", b"processing_mode_def"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_id", b"dataset_id", "job_name", b"job_name", "num_consumers", b"num_consumers", "optional_job_name", b"optional_job_name", "optional_num_consumers", b"optional_num_consumers", "processing_mode_def", b"processing_mode_def", "target_workers", b"target_workers", "use_cross_trainer_cache", b"use_cross_trainer_cache"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_job_name", b"optional_job_name"]) -> typing_extensions.Literal["job_name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_num_consumers", b"optional_num_consumers"]) -> typing_extensions.Literal["num_consumers"] | None: ...

global___GetOrCreateJobRequest = GetOrCreateJobRequest

@typing_extensions.final
class GetOrCreateJobResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.int
    def __init__(
        self,
        *,
        job_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_id", b"job_id"]) -> None: ...

global___GetOrCreateJobResponse = GetOrCreateJobResponse

@typing_extensions.final
class GetOrCreateIterationRequest(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    REPETITION_FIELD_NUMBER: builtins.int
    job_id: builtins.int
    """The job to create an iteration for."""
    repetition: builtins.int
    """Which repetition of the job to read from."""
    def __init__(
        self,
        *,
        job_id: builtins.int = ...,
        repetition: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_id", b"job_id", "repetition", b"repetition"]) -> None: ...

global___GetOrCreateIterationRequest = GetOrCreateIterationRequest

@typing_extensions.final
class GetOrCreateIterationResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITERATION_CLIENT_ID_FIELD_NUMBER: builtins.int
    iteration_client_id: builtins.int
    """An id for the client that will read from the iteration. When the client is
    done with the iteration, they should call ReleaseIterationClient with this
    id.
    """
    def __init__(
        self,
        *,
        iteration_client_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["iteration_client_id", b"iteration_client_id"]) -> None: ...

global___GetOrCreateIterationResponse = GetOrCreateIterationResponse

@typing_extensions.final
class MaybeRemoveTaskRequest(google.protobuf.message.Message):
    """Next tag: 4"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_ID_FIELD_NUMBER: builtins.int
    CONSUMER_INDEX_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    task_id: builtins.int
    consumer_index: builtins.int
    round: builtins.int
    def __init__(
        self,
        *,
        task_id: builtins.int = ...,
        consumer_index: builtins.int = ...,
        round: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["consumer_index", b"consumer_index", "round", b"round", "task_id", b"task_id"]) -> None: ...

global___MaybeRemoveTaskRequest = MaybeRemoveTaskRequest

@typing_extensions.final
class MaybeRemoveTaskResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REMOVED_FIELD_NUMBER: builtins.int
    removed: builtins.bool
    def __init__(
        self,
        *,
        removed: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["removed", b"removed"]) -> None: ...

global___MaybeRemoveTaskResponse = MaybeRemoveTaskResponse

@typing_extensions.final
class ReleaseIterationClientRequest(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITERATION_CLIENT_ID_FIELD_NUMBER: builtins.int
    iteration_client_id: builtins.int
    def __init__(
        self,
        *,
        iteration_client_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["iteration_client_id", b"iteration_client_id"]) -> None: ...

global___ReleaseIterationClientRequest = ReleaseIterationClientRequest

@typing_extensions.final
class ReleaseIterationClientResponse(google.protobuf.message.Message):
    """Next tag: 1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ReleaseIterationClientResponse = ReleaseIterationClientResponse

@typing_extensions.final
class ClientHeartbeatRequest(google.protobuf.message.Message):
    """Next tag: 5"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITERATION_CLIENT_ID_FIELD_NUMBER: builtins.int
    CURRENT_ROUND_FIELD_NUMBER: builtins.int
    BLOCKED_ROUND_FIELD_NUMBER: builtins.int
    iteration_client_id: builtins.int
    """The iteration client id to heartbeat for."""
    current_round: builtins.int
    blocked_round: builtins.int
    def __init__(
        self,
        *,
        iteration_client_id: builtins.int = ...,
        current_round: builtins.int = ...,
        blocked_round: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["blocked_round", b"blocked_round", "current_round", b"current_round", "optional_blocked_round", b"optional_blocked_round", "optional_current_round", b"optional_current_round"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blocked_round", b"blocked_round", "current_round", b"current_round", "iteration_client_id", b"iteration_client_id", "optional_blocked_round", b"optional_blocked_round", "optional_current_round", b"optional_current_round"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_blocked_round", b"optional_blocked_round"]) -> typing_extensions.Literal["blocked_round"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_current_round", b"optional_current_round"]) -> typing_extensions.Literal["current_round"] | None: ...

global___ClientHeartbeatRequest = ClientHeartbeatRequest

@typing_extensions.final
class ClientHeartbeatResponse(google.protobuf.message.Message):
    """Next tag: 5"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_INFO_FIELD_NUMBER: builtins.int
    BLOCK_ROUND_FIELD_NUMBER: builtins.int
    ITERATION_FINISHED_FIELD_NUMBER: builtins.int
    DEPLOYMENT_MODE_FIELD_NUMBER: builtins.int
    @property
    def task_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.data.service.common_pb2.TaskInfo]:
        """A list of all tasks that the client should read from."""
    block_round: builtins.int
    iteration_finished: builtins.bool
    """Whether the iteration has finished."""
    deployment_mode: tensorflow.core.protobuf.data_service_pb2.DeploymentMode.ValueType
    """tf.data service deployment mode. Supported values are "REMOTE",
    "COLOCATED", and "HYBRID". If unspecified, it is assumed to be "REMOTE".
    """
    def __init__(
        self,
        *,
        task_info: collections.abc.Iterable[tensorflow.core.data.service.common_pb2.TaskInfo] | None = ...,
        block_round: builtins.int = ...,
        iteration_finished: builtins.bool = ...,
        deployment_mode: tensorflow.core.protobuf.data_service_pb2.DeploymentMode.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block_round", b"block_round", "optional_block_round", b"optional_block_round"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_round", b"block_round", "deployment_mode", b"deployment_mode", "iteration_finished", b"iteration_finished", "optional_block_round", b"optional_block_round", "task_info", b"task_info"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_block_round", b"optional_block_round"]) -> typing_extensions.Literal["block_round"] | None: ...

global___ClientHeartbeatResponse = ClientHeartbeatResponse

@typing_extensions.final
class WorkerInfo(google.protobuf.message.Message):
    """Next tag: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___WorkerInfo = WorkerInfo

@typing_extensions.final
class GetWorkersRequest(google.protobuf.message.Message):
    """Next tag: 1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetWorkersRequest = GetWorkersRequest

@typing_extensions.final
class GetWorkersResponse(google.protobuf.message.Message):
    """Next tag: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKERS_FIELD_NUMBER: builtins.int
    @property
    def workers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkerInfo]:
        """A list of all workers."""
    def __init__(
        self,
        *,
        workers: collections.abc.Iterable[global___WorkerInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["workers", b"workers"]) -> None: ...

global___GetWorkersResponse = GetWorkersResponse
