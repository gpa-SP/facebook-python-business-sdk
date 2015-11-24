# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from examples.docs import fixtures
from facebookads import test_config

ad_account_id = test_config.account_id
ad_set_id = fixtures.create_adset().get_id()
post_id = fixtures.create_post()['id']
page_id = test_config.page_id
creative_id = fixtures.create_creative_from_object_story_id(post_id).get_id()
post_id = post_id.split('_')[1]

# _DOC open [ADGROUP_CREATE_TRACKING_POST_ENGAGEMENT]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, post_id:s, page_id:s]
from facebookads.objects import Ad

ad = Ad(parent_id=ad_account_id)
ad[Ad.Field.name] = 'My First Ad'
ad[Ad.Field.adset_id] = ad_set_id
ad[Ad.Field.creative] = {'creative_id': creative_id}
ad[Ad.Field.tracking_specs] = {
    'action.type': 'post_engagement',
    'post': post_id,
    'page': page_id,
}

ad.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_POST_ENGAGEMENT]

ad.remote_delete()
