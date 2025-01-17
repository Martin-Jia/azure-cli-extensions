# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_monitor_create
from .example_steps import step_monitor_show
from .example_steps import step_monitor_list
from .example_steps import step_monitor_list2
from .example_steps import step_monitor_update
from .example_steps import step_deployment_info_list
from .example_steps import step_monitored_resource_list
from .example_steps import step_tag_rule_create
from .example_steps import step_tag_rule_show
from .example_steps import step_tag_rule_list
from .example_steps import step_tag_rule_delete
from .example_steps import step_vm_collection_update
from .example_steps import step_vm_host_list
from .example_steps import step_vm_ingestion_detail
from .example_steps import step_monitor_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_monitor_create(test, checks=[
        test.check("name", "{myMonitor}", case_sensitive=False),
        test.check("location", "westus2", case_sensitive=False),
        test.check("sku.name", "ess-monthly-consumption_Monthly", case_sensitive=False),
        test.check("tags.Environment", "Dev", case_sensitive=False),
    ])
    step_monitor_show(test, checks=[
        test.check("name", "{myMonitor}", case_sensitive=False),
        test.check("location", "westus2", case_sensitive=False),
        test.check("tags.Environment", "Dev", case_sensitive=False),
    ])
    step_monitor_list(test, checks=[
        test.check('length(@)', 37),
    ])
    step_monitor_list2(test, checks=[
        test.check('length(@)', 1),
    ])
    step_monitor_update(test, checks=[
        test.check("name", "{myMonitor}", case_sensitive=False),
        test.check("location", "westus2", case_sensitive=False),
        test.check("sku.name", "ess-monthly-consumption_Monthly", case_sensitive=False),
        test.check("tags.Environment", "Dev", case_sensitive=False),
    ])
    step_deployment_info_list(test, checks=[])
    step_monitored_resource_list(test, checks=[])
    step_tag_rule_create(test, checks=[])
    step_tag_rule_show(test, checks=[])
    step_tag_rule_list(test, checks=[])
    # Error  (ResourceDeletionFailed) Resource deletion failed as RP returned status code: 'UnprocessableEntity'
    # step_tag_rule_delete(test, checks=[])
    step_vm_collection_update(test, checks=[])
    step_vm_host_list(test, checks=[])
    step_vm_ingestion_detail(test, checks=[])
    step_monitor_delete(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class ElasticScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(ElasticScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myMonitor': 'myMonitor',
        })

    @ResourceGroupPreparer(name_prefix='clitestelastic_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_elastic_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
