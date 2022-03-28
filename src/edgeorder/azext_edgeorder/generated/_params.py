# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_edgeorder.action import (
    AddRegisteredFeatures,
    AddFilterableProperties,
    AddShippingAddress,
    AddContactDetails,
    AddNotificationPreferences,
    AddTransportPreferences,
    AddEncryptionPreferences,
    AddManagementResourcePreferences
)


def load_arguments(self, _):

    with self.argument_context('edgeorder order show') as c:
        c.argument('name', type=str, help='The name of the order', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group, id_part='name')

    with self.argument_context('edgeorder list-config') as c:
        c.argument('skip_token', type=str, help='$skipToken is supported on list of configurations, which provides the '
                   'next page in the list of configurations.')
        c.argument('configuration_filters', type=validate_file_or_dict, help='Holds details about product hierarchy '
                   'information and filterable property. Expected value: json-string/json-file/@json-file.')
        c.argument('registered_features', action=AddRegisteredFeatures, nargs='+', help='List of registered feature '
                   'flags for subscription', arg_group='Customer Subscription Details')
        c.argument('location_placement_id', type=str, help='Location placement Id of a subscription',
                   arg_group='Customer Subscription Details')
        c.argument('quota_id', type=str, help='Quota ID of a subscription', arg_group='Customer Subscription Details')

    with self.argument_context('edgeorder list-family') as c:
        c.argument('expand', type=str, help='$expand is supported on configurations parameter for product, which '
                   'provides details on the configurations for the product.')
        c.argument('skip_token', type=str, help='$skipToken is supported on list of product families, which provides '
                   'the next page in the list of product families.')
        c.argument('filterable_properties', action=AddFilterableProperties, nargs='+', help='Dictionary of filterable '
                   'properties on product family. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('registered_features', action=AddRegisteredFeatures, nargs='+', help='List of registered feature '
                   'flags for subscription', arg_group='Customer Subscription Details')
        c.argument('location_placement_id', type=str, help='Location placement Id of a subscription',
                   arg_group='Customer Subscription Details')
        c.argument('quota_id', type=str, help='Quota ID of a subscription', arg_group='Customer Subscription Details')

    with self.argument_context('edgeorder list-metadata') as c:
        c.argument('skip_token', type=str, help='$skipToken is supported on list of product families metadata, which '
                   'provides the next page in the list of product families metadata.')

    with self.argument_context('edgeorder address list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('filter_', options_list=['--filter'], type=str, help='$filter is supported to filter based on '
                   'shipping address properties. Filter supports only equals operation.')
        c.argument('skip_token', type=str, help='$skipToken is supported on Get list of addresses, which provides the '
                   'next page in the list of address.')

    with self.argument_context('edgeorder address show') as c:
        c.argument('address_name', options_list=['--name', '-n', '--address-name'], type=str, help='The name of the '
                   'address Resource within the specified resource group. address names must be between 3 and 24 '
                   'characters in length and use any alphanumeric and underscore only', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('edgeorder address create') as c:
        c.argument('address_name', options_list=['--name', '-n', '--address-name'], type=str, help='The name of the '
                   'address Resource within the specified resource group. address names must be between 3 and 24 '
                   'characters in length and use any alphanumeric and underscore only')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='Shipping details for the address')
        c.argument('contact_details', action=AddContactDetails, nargs='+', help='Contact details for the address')

    with self.argument_context('edgeorder address update') as c:
        c.argument('address_name', options_list=['--name', '-n', '--address-name'], type=str, help='The name of the '
                   'address Resource within the specified resource group. address names must be between 3 and 24 '
                   'characters in length and use any alphanumeric and underscore only', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('if_match', type=str, help='Defines the If-Match condition. The patch will be performed only if the '
                   'ETag of the job on the server matches this value.')
        c.argument('tags', tags_type)
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='Shipping details for the address')
        c.argument('contact_details', action=AddContactDetails, nargs='+', help='Contact details for the address')

    with self.argument_context('edgeorder address delete') as c:
        c.argument('address_name', options_list=['--name', '-n', '--address-name'], type=str, help='The name of the '
                   'address Resource within the specified resource group. address names must be between 3 and 24 '
                   'characters in length and use any alphanumeric and underscore only', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('edgeorder order list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('skip_token', type=str, help='$skipToken is supported on Get list of order, which provides the next '
                   'page in the list of order.')

    with self.argument_context('edgeorder order-item list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('filter_', options_list=['--filter'], type=str, help='$filter is supported to filter based on order '
                   'id. Filter supports only equals operation.')
        c.argument('expand', type=str, help='$expand is supported on device details, forward shipping details and '
                   'reverse shipping details parameters. Each of these can be provided as a comma separated list. '
                   'Device Details for order item provides details on the devices of the product, Forward and Reverse '
                   'Shipping details provide forward and reverse shipping details respectively.')
        c.argument('skip_token', type=str, help='$skipToken is supported on Get list of order items, which provides '
                   'the next page in the list of order items.')

    with self.argument_context('edgeorder order-item show') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('expand', type=str, help='$expand is supported on device details, forward shipping details and '
                   'reverse shipping details parameters. Each of these can be provided as a comma separated list. '
                   'Device Details for order item provides details on the devices of the product, Forward and Reverse '
                   'Shipping details provide forward and reverse shipping details respectively.')

    with self.argument_context('edgeorder order-item create') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('order_item_resource', type=validate_file_or_dict, help='Order item details from request body. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('edgeorder order-item update') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('if_match', type=str, help='Defines the If-Match condition. The patch will be performed only if the '
                   'ETag of the order on the server matches this value.')
        c.argument('tags', tags_type)
        c.argument('notification_email_list', nargs='+', help='Additional notification email list.')
        c.argument('notification_preferences', action=AddNotificationPreferences, nargs='+', help='Notification '
                   'preferences.', arg_group='Preferences')
        c.argument('transport_preferences', action=AddTransportPreferences, nargs='+', help='Preferences related to '
                   'the shipment logistics of the order.', arg_group='Preferences')
        c.argument('encryption_preferences', action=AddEncryptionPreferences, nargs='+', help='Preferences related to '
                   'the Encryption.', arg_group='Preferences')
        c.argument('management_resource_preferences', action=AddManagementResourcePreferences, nargs='+',
                   help='Preferences related to the Management resource.', arg_group='Preferences')
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='Shipping details for the address',
                   arg_group='Forward Address')
        c.argument('contact_details', action=AddContactDetails, nargs='+', help='Contact details for the address',
                   arg_group='Forward Address')

    with self.argument_context('edgeorder order-item delete') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('edgeorder order-item cancel') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('reason', type=str, help='Reason for cancellation.')

    with self.argument_context('edgeorder order-item return') as c:
        c.argument('order_item_name', options_list=['--name', '-n', '--order-item-name'], type=str, help='The name of '
                   'the order item', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('return_reason', type=str, help='Return Reason.')
        c.argument('service_tag', type=str, help='Service tag (located on the bottom-right corner of the device)')
        c.argument('shipping_box_required', arg_type=get_three_state_flag(), help='Shipping Box required')
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='Shipping details for the address',
                   arg_group='Return Address')
        c.argument('contact_details', action=AddContactDetails, nargs='+', help='Contact details for the address',
                   arg_group='Return Address')
