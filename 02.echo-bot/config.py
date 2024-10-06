#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
# Add Azure Sentiment Analysis API details
    AZURE_LANGUAGE_KEY = os.environ.get("AZURE_LANGUAGE_KEY", "")
    AZURE_LANGUAGE_ENDPOINT = os.environ.get("AZURE_LANGUAGE_ENDPOINT", "")

    print(AZURE_LANGUAGE_ENDPOINT)
    print(AZURE_LANGUAGE_KEY)
