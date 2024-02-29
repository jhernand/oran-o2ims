# -*- coding: utf-8 -*-

#
# Copyright (c) 2023 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#

import logging

class Formatter:
    INFO_PREFIX = "\033[32;1mI:\033[0m "
    WARNING_PREFIX = "\033[33;1mW:\033[0m "
    ERROR_PREFIX = "\033[31;1mE:\033[0m "

    def format(self, record: logging.LogRecord) -> str:
        msg = str(record.msg) % record.args
        prefix = __class__.INFO_PREFIX
        match record.levelno:
            case logging.CRITICAL | logging.ERROR:
                prefix = __class__.ERROR_PREFIX
            case logging.WARNING:
                prefix = __class__.WARNING_PREFIX
        return prefix + msg