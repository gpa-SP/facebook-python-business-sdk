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
creative_id = fixtures.create_creative().get_id()
pixel_id = fixtures.create_ad_conversion_pixel().get_id()

# !_DOC [pruno]
# _DOC open [ADGROUP_CREATE_TRACKING_ADCONVERSIONPIXELS]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, pixel_id]
from facebookads.objects import Ad

ad = Ad(parent_id=ad_account_id)
ad.update({
    Ad.Field.name: 'test',
    Ad.Field.adset_id: ad_set_id,
    Ad.Field.creative: {
        'creative_id': creative_id,
    },
    Ad.Field.tracking_specs: {
        'action.type': 'offsite_conversion',
        'offsite_pixel': pixel_id,
    },
})
ad.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_ADCONVERSIONPIXELS]

ad.remote_delete()
