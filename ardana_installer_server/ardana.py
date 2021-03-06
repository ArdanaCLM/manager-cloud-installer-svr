# (c) Copyright 2017-2018 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from . import util
from flask import Blueprint
from flask import request
from oslo_config import cfg

bp = Blueprint('ardana', __name__)


@bp.route("/api/v1/clm/<path:url>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def ardana(url):

    url = cfg.CONF.general.ardana_service_url + "/api/v2/" + url
    return util.forward(url, request)
