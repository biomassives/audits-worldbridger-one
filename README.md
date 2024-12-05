# wb1_Audits
nft audits of metadata via the graph and grphql



## Tinybox Eth Subgraph

img(https://github.com/biomassives/wb1_Audits/blob/main/tinybox_trait_distributions_20241205_123958.png?raw=true)


Subgraph Schema Analysis:

Type: Aggregation_interval

Type: Approval
  - id: NON_NULL
  - owner: NON_NULL
  - approved: NON_NULL
  - tokenId: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: ApprovalForAll
  - id: NON_NULL
  - owner: NON_NULL
  - operator: NON_NULL
  - approved: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: ApprovalForAll_filter

Type: ApprovalForAll_orderBy

Type: Approval_filter

Type: Approval_orderBy

Type: Attribute
  - id: NON_NULL
  - traitType: String
  - value: String
  - token: NON_NULL
  - metadata: NON_NULL

Type: Attribute_filter

Type: Attribute_orderBy

Type: BigDecimal

Type: BigInt

Type: BlockChangedFilter

Type: Block_height

Type: Boolean

Type: Bytes

Type: Float

Type: ID

Type: Int

Type: Int8

Type: Metadata
  - id: NON_NULL
  - tokenId: NON_NULL
  - name: String
  - description: String
  - image: String
  - traits: LIST

Type: Metadata_filter

Type: Metadata_orderBy

Type: OrderDirection

Type: Query
  - approval: Approval
  - approvals: NON_NULL
  - approvalForAll: ApprovalForAll
  - approvalForAlls: NON_NULL
  - redeemedLE: RedeemedLE
  - redeemedLEs: NON_NULL
  - roleAdminChanged: RoleAdminChanged
  - roleAdminChangeds: NON_NULL
  - roleGranted: RoleGranted
  - roleGranteds: NON_NULL
  - roleRevoked: RoleRevoked
  - roleRevokeds: NON_NULL
  - settingsChanged: SettingsChanged
  - settingsChangeds: NON_NULL
  - transfer: Transfer
  - transfers: NON_NULL
  - metadata: Metadata
  - metadata_collection: NON_NULL
  - token: Token
  - tokens: NON_NULL
  - attribute: Attribute
  - attributes: NON_NULL
  - _meta: _Meta_

Type: RedeemedLE
  - id: NON_NULL
  - by: NON_NULL
  - TinyBoxes_id: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: RedeemedLE_filter

Type: RedeemedLE_orderBy

Type: RoleAdminChanged
  - id: NON_NULL
  - role: NON_NULL
  - previousAdminRole: NON_NULL
  - newAdminRole: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: RoleAdminChanged_filter

Type: RoleAdminChanged_orderBy

Type: RoleGranted
  - id: NON_NULL
  - role: NON_NULL
  - account: NON_NULL
  - sender: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: RoleGranted_filter

Type: RoleGranted_orderBy

Type: RoleRevoked
  - id: NON_NULL
  - role: NON_NULL
  - account: NON_NULL
  - sender: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: RoleRevoked_filter

Type: RoleRevoked_orderBy

Type: SettingsChanged
  - id: NON_NULL
  - settings: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: SettingsChanged_filter

Type: SettingsChanged_orderBy

Type: String

Type: Subscription
  - approval: Approval
  - approvals: NON_NULL
  - approvalForAll: ApprovalForAll
  - approvalForAlls: NON_NULL
  - redeemedLE: RedeemedLE
  - redeemedLEs: NON_NULL
  - roleAdminChanged: RoleAdminChanged
  - roleAdminChangeds: NON_NULL
  - roleGranted: RoleGranted
  - roleGranteds: NON_NULL
  - roleRevoked: RoleRevoked
  - roleRevokeds: NON_NULL
  - settingsChanged: SettingsChanged
  - settingsChangeds: NON_NULL
  - transfer: Transfer
  - transfers: NON_NULL
  - metadata: Metadata
  - metadata_collection: NON_NULL
  - token: Token
  - tokens: NON_NULL
  - attribute: Attribute
  - attributes: NON_NULL
  - _meta: _Meta_

Type: Timestamp

Type: Token
  - id: NON_NULL
  - tokenId: NON_NULL
  - owner: NON_NULL
  - randomness: BigInt
  - animation: BigInt
  - shapes: Int
  - hatching: Int
  - size: NON_NULL
  - spacing: NON_NULL
  - mirroring: Int
  - color: NON_NULL
  - contrast: Int
  - shades: Int
  - scheme: Int
  - type: Int
  - columns: Int
  - hue: Int
  - lightness: Int
  - maxheight: Int
  - maxwidth: Int
  - minheight: Int
  - minwidth: Int
  - minted: Int
  - phase: Int
  - rendered: Int
  - saturation: Int
  - spread: Int

Type: Token_filter

Type: Token_orderBy

Type: Transfer
  - id: NON_NULL
  - from: NON_NULL
  - to: NON_NULL
  - tokenId: NON_NULL
  - blockNumber: NON_NULL
  - blockTimestamp: NON_NULL
  - transactionHash: NON_NULL

Type: Transfer_filter

Type: Transfer_orderBy

Type: _Block_
  - hash: Bytes
  - number: NON_NULL
  - timestamp: Int
  - parentHash: Bytes

Type: _Meta_
  - block: NON_NULL
  - deployment: NON_NULL
  - hasIndexingErrors: NON_NULL

Type: _SubgraphErrorPolicy_
(base) greg@scdhub:~/g4/tiny
