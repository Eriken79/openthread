#!/usr/bin/env python3
#
#  Copyright (c) 2019, The OpenThread Authors.
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the
#     names of its contributors may be used to endorse or promote products
#     derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#

from pktverify.addrs import Ipv6Addr
from pktverify.bytes import Bytes

DOMAIN_PREFIX = Bytes('fd00:7d03:7d03:7d03')
BACKBONE_IPV6_PREFIX = Bytes('91')

LINK_LOCAL_All_THREAD_NODES_MULTICAST_ADDRESS = Ipv6Addr('ff32:40:fd00:db8::1')
REALM_LOCAL_All_THREAD_NODES_MULTICAST_ADDRESS = Ipv6Addr('ff33:40:fd00:db8::1')
REALM_LOCAL_ALL_NODES_ADDRESS = Ipv6Addr('ff03::1')
REALM_LOCAL_ALL_ROUTERS_ADDRESS = Ipv6Addr('ff03::2')
LINK_LOCAL_ALL_NODES_MULTICAST_ADDRESS = Ipv6Addr('ff02::1')
LINK_LOCAL_ALL_ROUTERS_MULTICAST_ADDRESS = Ipv6Addr('ff02::2')
LINK_LOCAL_ALL_BBRS_MULTICAST_ADDRESS = Ipv6Addr('ff32:40:fd00:7d03:7d03:7d03:0:3')

# MA in Test Plan, make sure these are same as ../config.py
MA1 = Ipv6Addr('ff04::1234:777a:1')
MA1g = Ipv6Addr('ff0e::1234:777a:1')
MA2 = Ipv6Addr('ff05::1234:777a:1')
MA3 = Ipv6Addr('ff0e::1234:777a:3')
MA4 = Ipv6Addr('ff05::1234:777a:4')
MA5 = Ipv6Addr('ff03::1234:777a:5')
MA6 = Ipv6Addr('ff02::1')
MAe1 = Ipv6Addr('fd0e::1234:777a:1')
MAe2 = Ipv6Addr('::')
MAe3 = Ipv6Addr('cafe::e0ff')
MAS = [[Ipv6Addr(f'ff0e::{j:x}:777a:{i:x}') for j in range(16)] for i in range(16)]
ALL_MPL_FORWARDERS_MA = Ipv6Addr('ff03::fc')

LINK_LOCAL_PREFIX = Bytes("fe80")
DEFAULT_MESH_LOCAL_PREFIX = Bytes("fd00:0db8:0000:0000")
LEADER_ALOC_IID = Bytes("0000:00ff:fe00:fc00")
PBBR_ALOC_IID = Bytes("0000:00ff:fe00:fc38")
LEADER_ALOC = Ipv6Addr(DEFAULT_MESH_LOCAL_PREFIX + LEADER_ALOC_IID)
PBBR_ALOC = Ipv6Addr(DEFAULT_MESH_LOCAL_PREFIX + PBBR_ALOC_IID)

# Minimum value of the MLR Timeout parameter in the BBR Dataset
MLR_TIMEOUT_MIN = 300

# Max response delay
MLE_MAX_RESPONSE_DELAY = 1

# WPAN CMDs
WPAN_DATA_REQUEST = 4

# WPAN Frame Types
WPAN_BEACON = 0
WPAN_DATA = 1
WPAN_ACK = 2
WPAN_CMD = 3

# COAP methods
COAP_CODE_POST = 2
COAP_CODE_ACK = 68

MLE_LINK_REQUEST = 0
MLE_LINK_ACCEPT = 1
MLE_LINK_ACCEPT_AND_REQUEST = 2
MLE_ADVERTISEMENT = 4
MLE_DATA_REQUEST = 7
MLE_DATA_RESPONSE = 8
MLE_PARENT_REQUEST = 9
MLE_PARENT_RESPONSE = 10
MLE_CHILD_ID_REQUEST = 11
MLE_CHILD_ID_RESPONSE = 12
MLE_CHILD_UPDATE_REQUEST = 13
MLE_CHILD_UPDATE_RESPONSE = 14
MLE_ANNOUNCE = 15
MLE_DISCOVERY_REQUEST = 16
MLE_DISCOVERY_RESPONSE = 17
MLE_LINK_METRICS_MANAGEMENT_REQUEST = 18
MLE_LINK_METRICS_MANAGEMENT_RESPONSE = 19
MLE_LINK_PROBE = 20

# COAP URIs
ADDR_QRY_URI = '/a/aq'
ADDR_NTF_URI = '/a/an'
ADDR_ERR_URI = '/a/ae'
ADDR_SOL_URI = '/a/as'
ADDR_REL_URI = '/a/ar'
SVR_DATA_URI = '/a/sd'
ND_DATA_URI = '/a/nd'
RLY_RX_URI = '/c/rx'
RLY_TX_URI = '/c/tx'
MGMT_PANID_QUERY = '/c/pq'
MGMT_PANID_CONFLICT = '/c/pc'
MGMT_ED_SCAN = '/c/es'
MGMT_ED_REPORT = '/c/er'
MGMT_ACTIVE_GET_URI = '/c/ag'
MGMT_ACTIVE_SET_URI = '/c/as'
MGMT_PENDING_SET_URI = '/c/ps'
MGMT_PENDING_GET_URI = '/c/pg'
MGMT_DATASET_CHANGED_URI = '/c/dc'
MGMT_COMMISSIONER_GET_URI = '/c/cg'
DIAG_GET_URI = '/d/dg'
DIAG_RST_URI = '/d/dr'
MGMT_COMMISSIONER_SET_URI = '/c/cs'
LEAD_PET_URI = '/c/lp'
LEAD_KA_URI = '/c/la'
DIAG_GET_QRY_URI = '/d/dq'
DIAG_GET_ANS_URI = '/d/da'

# ADDR SOL Status
ADDR_SOL_SUCCESS = 0
ADDR_SOL_NA = 1

# MLE TLVs
SOURCE_ADDRESS_TLV = 0
MODE_TLV = 1
TIMEOUT_TLV = 2
CHALLENGE_TLV = 3
RESPONSE_TLV = 4
LINK_LAYER_FRAME_COUNTER_TLV = 5
LINK_QUALITY_TLV = 6
PARAMETER_TLV = 7
MLE_FRAME_COUNTER_TLV = 8
ROUTE64_TLV = 9
ADDRESS16_TLV = 10
LEADER_DATA_TLV = 11
NETWORK_DATA_TLV = 12
TLV_REQUEST_TLV = 13
SCAN_MASK_TLV = 14
CONNECTIVITY_TLV = 15
LINK_MARGIN_TLV = 16
STATUS_TLV = 17
VERSION_TLV = 18
ADDRESS_REGISTRATION_TLV = 19
CHANNEL_TLV = 20
PAN_ID_TLV = 21
ACTIVE_TIMESTAMP_TLV = 22
PENDING_TIMESTAMP_TLV = 23
ACTIVE_OPERATION_DATASET_TLV = 24
PENDING_OPERATION_DATASET_TLV = 25
THREAD_DISCOVERY_TLV = 26
CSL_SYNCHRONIZED_TIMEOUT = 85

# Network Layer TLVs
NL_TARGET_EID_TLV = 0
NL_MAC_EXTENDED_ADDRESS_TLV = 1
NL_RLOC16_TLV = 2
NL_ML_EID_TLV = 3
NL_STATUS_TLV = 4
NL_TIME_SINCE_LAST_TRANSACTION_TLV = 6
NL_ROUTER_MASK_TLV = 7
NL_ND_OPTION_TLV = 8
NL_ND_DATA_TLV = 9
NL_THREAD_NETWORK_DATA_TLV = 10

# Network Layer Status
NL_SUCESS = 0
NL_NO_ADDRESS_AVAILABLE = 1
NL_TOO_FEW_ROUTERS = 2
NL_HAVE_CHILD_ID_REQUEST = 3
NL_PARENT_PARTITION_CHANGE = 4

# MeshCop TLVs
NM_CHANNEL_TLV = 0
NM_PAN_ID_TLV = 1
NM_EXTENDED_PAN_ID_TLV = 2
NM_NETWORK_NAME_TLV = 3
NM_PSKC_TLV = 4
NM_NETWORK_KEY_TLV = 5
NM_NETWORK_KEY_SEQUENCE_COUNTER_TLV = 6
NM_NETWORK_MESH_LOCAL_PREFIX_TLV = 7
NM_STEERING_DATA_TLV = 8
NM_BORDER_AGENT_LOCATOR_TLV = 9
NM_COMMISSIONER_ID_TLV = 10
NM_COMMISSIONER_SESSION_ID_TLV = 11
NM_SECURITY_POLICY_TLV = 12
NM_ACTIVE_TIMESTAMP_TLV = 14
NM_COMMISSIONER_UDP_PORT_TLV = 15
NM_STATE_TLV = 16
NM_JOINER_DTLS_ENCAPSULATION_TLV = 17
NM_JOINER_UDP_PORT_TLV = 18
NM_JOINER_IID_TLV = 19
NM_JOINER_ROUTER_LOCATOR_TLV = 20
NM_JOINER_ROUTER_KEK_TLV = 21
NM_PENDING_TIMESTAMP_TLV = 51
NM_DELAY_TIMER_TLV = 52
NM_CHANNEL_MASK_TLV = 53
NM_SCAN_DURATION = 56
NM_ENERGY_LIST_TLV = 57
NM_DISCOVERY_REQUEST_TLV = 128
NM_DISCOVERY_RESPONSE_TLV = 129

# Diagnostic TLVs
DG_MAC_EXTENDED_ADDRESS_TLV = 0
DG_MAC_ADDRESS_TLV = 1
DG_MODE_TLV = 2
DG_TIMEOUT_TLV = 3
DG_CONNECTIVITY_TLV = 4
DG_ROUTE64_TLV = 5
DG_LEADER_DATA_TLV = 6
DG_NETWORK_DATA_TLV = 7
DG_IPV6_ADDRESS_LIST_TLV = 8
DG_MAC_COUNTERS_TLV = 9
DG_BATTERY_LEVEL_TLV = 14
DG_SUPPLY_VOLTAGE_TLV = 15
DG_CHILD_TABLE_TLV = 16
DG_CHANNEL_PAGES_TLV = 17
DG_TYPE_LIST_TLV = 18
DG_MAX_CHILD_TIMEOUT_TLV = 19

# MeshCop State
MESHCOP_ACCEPT = 1
MESHCOP_PENDING = 0
MESHCOP_REJECT = -1

# DTLS
HANDSHAKE_HELLO_REQUEST = 0
HANDSHAKE_CLIENT_HELLO = 1
HANDSHAKE_SERVER_HELLO = 2
HANDSHAKE_HELLO_VERIFY_REQUEST = 3
HANDSHAKE_CERTIFICATE = 11
HANDSHAKE_SERVER_KEY_EXCHANGE = 12
HANDSHAKE_CERTIFICATE_REQUEST = 13
HANDSHAKE_SERVER_HELLO_DONE = 14
HANDSHAKE_CERTIFICATE_VERIFY = 15
HANDSHAKE_CLIENT_KEY_EXCHANGE = 16
HANDSHAKE_FINISHED = 20
CONTENT_CHANGE_CIPHER_SPEC = 20
CONTENT_ALERT = 21
CONTENT_HANDSHAKE = 22
CONTENT_APPLICATION_DATA = 23

# Network Data TLVs
NWD_HAS_ROUTER_TLV = 0
NWD_PREFIX_TLV = 1
NWD_BORDER_ROUTER_TLV = 2
NWD_6LOWPAN_ID_TLV = 3
NWD_COMMISSIONING_DATA_TLV = 4
NWD_SERVICE_TLV = 5
NWD_SERVER_TLV = 6

# Link Metrics TLVs
LM_FORWARD_PROBING_REGISTRATION_SUB_TLV = 3
LM_ENHANCED_ACK_CONFIGURATION_SUB_TLV = 7

# DUA related constants

ADDRESS_QUERY_INITIAL_RETRY_DELAY = 15
ADDRESS_QUERY_MAX_RETRY_DELAY = 8
ADDRESS_QUERY_TIMEOUT = 3
ADVERTISEMENT_I_MAX = 32
ADVERTISEMENT_I_MIN = 1

CONTEXT_ID_REUSE_DELAY = 48

DATA_RESUBMIT_DELAY = 300

DUA_DAD_PERIOD = 100
DUA_DAD_QUERY_TIMEOUT = 1.0
DUA_DAD_REPEATS = 2
DUA_RECENT_TIME = 20
FAILED_ROUTER_TRANSMISSIONS = 4
ID_REUSE_DELAY = 100
ID_SEQUENCE_PERIOD = 10
INFINITE_COST_TIMEOUT = 90

REAL_LAYER_NAMES = {
    'mle',
    'coap',
    'dtls',
    'wpan',
    'eth',
    'tcp',
    'udp',
    'ip',
    'ipv6',
    'icmpv6',
    '6lowpan',
    'arp',
    'thread_bl',
    'thread_address',
    'thread_diagnostic',
    'thread_nm',
    'thread_bcn',
    'ssdp',
    'dns',
    'igmp',
    'mdns',
}

FAKE_LAYER_NAMES = {'thread_nwd', 'thread_meshcop', 'ipv6inner'}

VALID_LAYER_NAMES = REAL_LAYER_NAMES | FAKE_LAYER_NAMES

AUTO_SEEK_BACK_MAX_DURATION = 0.02

# Wireshark configs
WIRESHARK_OVERRIDE_PREFS = {
    '6lowpan.context0':
        'fd00:db8::/64',
    '6lowpan.context1':
        'fd00:7d03:7d03:7d03::/64',
    'wpan.802154_fcs_ok':
        'FALSE',
    'wpan.802154_sec_suite':
        'AES-128 Encryption, 32-bit Integrity Protection',
    'thread.thr_seq_ctr':
        '00000000',
    'uat:ieee802154_keys':
        '''"00112233445566778899aabbccddeeff","1","Thread hash"
                              "ffeeddccbbaa99887766554433221100","1","Thread hash"''',
}

WIRESHARK_DECODE_AS_ENTRIES = {
    'udp.port==61631': 'coap',
}

TIMEOUT_JOIN_NETWORK = 10
TIMEOUT_DUA_REGISTRATION = 10
TIMEOUT_DUA_DAD = 15
TIMEOUT_HOST_READY = 10
TIMEOUT_CHILD_DETACH = 120
TIMEOUT_REGISTER_MA = 5

# 802.15.4 Frame Version
MAC_FRAME_VERSION_2006 = 1
MAC_FRAME_VERSION_2015 = 2

# 802.15.4 Frame Type
MAC_FRAME_TYPE_BEACON = 0x0
MAC_FRAME_TYPE_DATA = 0x1
MAC_FRAME_TYPE_ACK = 0x2
MAC_FRAME_TYPE_MAC_CMD = 0x3

# CSL
CSL_DEFAULT_PERIOD = 3125  # 0.5s, 3125 in units of ten symbols
CSL_DEFAULT_PERIOD_IN_SECOND = 0.5
US_PER_TEN_SYMBOLS = 160
CSL_IE_ID = 0x1a
CSL_DEFAULT_TIMEOUT = 30
CSL_DEFAULT_CHANNEL = 12

# Thread Version TLV value
THREAD_VERSION_1_2 = 3

# ICMPv6 Types
ICMPV6_TYPE_DESTINATION_UNREACHABLE = 1

# Link Metrics
LINK_METRICS_STATUS_SUCCESS = 0
LINK_METRICS_STATUS_CANNOT_SUPPORT_NEW_SERIES = 1
LINK_METRICS_STATUS_SERIES_ID_ALREADY_REGISTERED = 2
LINK_METRICS_STATUS_SERIES_ID_NOT_RECOGNIZED = 3
LINK_METRICS_STATUS_NO_MATCHING_FRAMES_RECEIVED = 4
LINK_METRICS_STATUS_OTHER_ERROR = 254

LINK_METRICS_TYPE_AVERAGE_ENUM_COUNT = 0
LINK_METRICS_TYPE_AVERAGE_ENUM_EXPONENTIAL = 1

LINK_METRICS_METRIC_TYPE_ENUM_PDU_COUNT = 0
LINK_METRICS_METRIC_TYPE_ENUM_LQI = 1
LINK_METRICS_METRIC_TYPE_ENUM_LINK_MARGIN = 2
LINK_METRICS_METRIC_TYPE_ENUM_RSSI = 3

LINK_METRICS_ENH_ACK_PROBING_CLEAR = 0
LINK_METRICS_ENH_ACK_PROBING_REGISTER = 1

# THREAD_COMPANY_ID
THREAD_IEEE_802154_COMPANY_ID = 0xEAB89B

if __name__ == '__main__':
    from pktverify.addrs import Ipv6Addr

    assert Ipv6Addr("fe80:0000:0000:0000:0200:0000:0000:0004").startswith(LINK_LOCAL_PREFIX)
    assert Ipv6Addr("fd00:0db8:0000:0000:0000:00ff:fe00:8001").startswith(DEFAULT_MESH_LOCAL_PREFIX)
