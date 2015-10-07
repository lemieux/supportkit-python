# SupportKit Python SDK

## Installation
`pip install supportkit`

## Usage
All of these calls (except the jwt) are returning a promise.

```
import SupportKit

## If you need to target another server url than the production one :
## SupportKit.apiUrl = 'https://sdk.supportkit.io'

// Webhooks
SupportKit.webhooks.create(target, jwt, options)
SupportKit.webhooks.update(webhook_id, target, jwt, options)
SupportKit.webhooks.destroy(webhook_id, jwt, options)
SupportKit.webhooks.list(jwt, options)

// Conversations
SupportKit.conversations.get(user_id, jwt, options)

// Messages
SupportKit.messages.create(user_id, message, role, jwt, options)

// JWT
SupportKit.jwt.generate(body, secret, key_id)
```