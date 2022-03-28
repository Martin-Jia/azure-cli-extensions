# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._static_members_operations import build_create_or_update_request, build_delete_request, build_get_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class StaticMembersOperations:
    """StaticMembersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2021_05_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        network_manager_name: str,
        network_group_name: str,
        static_member_name: str,
        **kwargs: Any
    ) -> "_models.StaticMember":
        """Gets the specified static member.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param network_group_name: The name of the network group.
        :type network_group_name: str
        :param static_member_name: The name of the static member.
        :type static_member_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StaticMember, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2021_05_01_preview.models.StaticMember
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StaticMember"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            network_manager_name=network_manager_name,
            network_group_name=network_group_name,
            static_member_name=static_member_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('StaticMember', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/networkGroups/{networkGroupName}/staticMembers/{staticMemberName}'}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        network_manager_name: str,
        network_group_name: str,
        static_member_name: str,
        parameters: "_models.StaticMember",
        **kwargs: Any
    ) -> "_models.StaticMember":
        """Creates or updates a static member.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param network_group_name: The name of the network group.
        :type network_group_name: str
        :param static_member_name: The name of the static member.
        :type static_member_name: str
        :param parameters: Parameters supplied to the specify the static member to create.
        :type parameters: ~azure.mgmt.network.v2021_05_01_preview.models.StaticMember
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StaticMember, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2021_05_01_preview.models.StaticMember
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StaticMember"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'StaticMember')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            network_manager_name=network_manager_name,
            network_group_name=network_group_name,
            static_member_name=static_member_name,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('StaticMember', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('StaticMember', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/networkGroups/{networkGroupName}/staticMembers/{staticMemberName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        network_manager_name: str,
        network_group_name: str,
        static_member_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a static member.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param network_group_name: The name of the network group.
        :type network_group_name: str
        :param static_member_name: The name of the static member.
        :type static_member_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            network_manager_name=network_manager_name,
            network_group_name=network_group_name,
            static_member_name=static_member_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/networkGroups/{networkGroupName}/staticMembers/{staticMemberName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        network_manager_name: str,
        network_group_name: str,
        top: Optional[int] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.StaticMemberListResult"]:
        """Lists the specified static member.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param network_group_name: The name of the network group.
        :type network_group_name: str
        :param top: An optional query parameter which specifies the maximum number of records to be
         returned by the server.
        :type top: int
        :param skip_token: SkipToken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skipToken parameter that specifies a starting point to use for subsequent calls.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StaticMemberListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2021_05_01_preview.models.StaticMemberListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StaticMemberListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    network_manager_name=network_manager_name,
                    network_group_name=network_group_name,
                    top=top,
                    skip_token=skip_token,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    network_manager_name=network_manager_name,
                    network_group_name=network_group_name,
                    top=top,
                    skip_token=skip_token,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("StaticMemberListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/networkGroups/{networkGroupName}/staticMembers'}  # type: ignore
