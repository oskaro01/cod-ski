# Shopify Expiring Offline Token Procedure

This guide explains how to connect this workspace to the Shopify Admin API and keep access working with Shopify's expiring offline tokens.

## What You Get

Shopify now returns two important tokens when you request an expiring offline token:

- `SHOPIFY_ACCESS_TOKEN`: short-lived token used for Admin API requests, usually valid for about 1 hour.
- `SHOPIFY_REFRESH_TOKEN`: longer-lived token used to get a new access token, usually valid for about 90 days.

The refresh token is the "90 days token" people usually mean. It is not the token you send to the Admin API. You use it to rotate the access token.

## Required `.env` Values

Keep these in `.env`:

```env
SHOPIFY_API_KEY=your_app_client_id
SHOPIFY_API_SECRET=your_app_client_secret
SHOPIFY_SHOP=your-store.myshopify.com
SCOPES=read_products,read_orders 

SHOPIFY_ACCESS_TOKEN=
SHOPIFY_REFRESH_TOKEN=
SHOPIFY_ACCESS_TOKEN_EXPIRES_AT=
SHOPIFY_REFRESH_TOKEN_EXPIRES_AT=
```

Never commit real token values.

## Step 1: Start OAuth In The Browser

Open an authorization URL like this:

```text
https://YOUR_STORE.myshopify.com/admin/oauth/authorize?client_id=YOUR_SHOPIFY_API_KEY&scope=COMMA_SEPARATED_SCOPES&redirect_uri=YOUR_REDIRECT_URL&state=RANDOM_STATE
```

Example shape:

```text
https://your-store.myshopify.com/admin/oauth/authorize?client_id=abc123&scope=read_products,read_orders&redirect_uri=https%3A%2F%2Fexample.com%2F&state=random123
```

Notes:

- For offline access, do not request online/per-user access.
- Your `redirect_uri` must be allowed in the Shopify app settings.
- Shopify redirects back with query params including `code`, `hmac`, `shop`, `timestamp`, and sometimes `host`.
- The `code` is single-use. If you exchange it once, it cannot be reused.

## Step 2: Verify The Callback HMAC

Before exchanging the `code`, verify the callback really came from Shopify:

1. Read all query params from the callback URL.
2. Remove `hmac` and `signature`.
3. Sort the remaining params alphabetically by key.
4. Join them as `key=value` pairs with `&`.
5. Compute HMAC-SHA256 using `SHOPIFY_API_SECRET`.
6. Compare the computed hex digest to Shopify's `hmac`.

If the HMAC does not match, do not exchange the code.

## Step 3: Exchange The Code For An Expiring Offline Token

Send a POST request to:

```text
https://YOUR_STORE.myshopify.com/admin/oauth/access_token
```

Use `application/x-www-form-urlencoded` body:

```text
client_id=YOUR_SHOPIFY_API_KEY
client_secret=YOUR_SHOPIFY_API_SECRET
code=THE_CALLBACK_CODE
expiring=1
```

The important field is:

```text
expiring=1
```

Without it, Shopify can return a non-expiring offline token, and new Admin API calls may fail with:

```text
[API] Non-expiring access tokens are no longer accepted for the Admin API.
```

Expected response shape:

```json
{
  "access_token": "access_token_value",
  "expires_in": 3600,
  "refresh_token": "refresh_token_value",
  "refresh_token_expires_in": 7776000,
  "scope": "read_products,read_orders"
}
```

Save these values:

```env
SHOPIFY_ACCESS_TOKEN=response.access_token
SHOPIFY_REFRESH_TOKEN=response.refresh_token
SHOPIFY_ACCESS_TOKEN_EXPIRES_AT=current_utc_time_plus_expires_in
SHOPIFY_REFRESH_TOKEN_EXPIRES_AT=current_utc_time_plus_refresh_token_expires_in
```

## Step 4: Test Admin API Access

Use the access token, not the refresh token:

```powershell
$shop = "YOUR_STORE.myshopify.com"
$token = "YOUR_ACCESS_TOKEN"
$body = @{
  query = "{ shop { name myshopifyDomain } products(first: 1) { edges { node { title handle } } } }"
} | ConvertTo-Json -Compress

Invoke-RestMethod `
  -Method Post `
  -Uri "https://$shop/admin/api/2026-04/graphql.json" `
  -Headers @{ "X-Shopify-Access-Token" = $token; "Content-Type" = "application/json" } `
  -Body $body
```

## Step 5: Refresh Before The Access Token Expires

Before any Admin API request, check `SHOPIFY_ACCESS_TOKEN_EXPIRES_AT`. If it is expired or less than about 5 minutes away from expiring, refresh first.

POST to:

```text
https://YOUR_STORE.myshopify.com/admin/oauth/access_token
```

Use `application/x-www-form-urlencoded` body:

```text
client_id=YOUR_SHOPIFY_API_KEY
client_secret=YOUR_SHOPIFY_API_SECRET
grant_type=refresh_token
refresh_token=YOUR_CURRENT_SHOPIFY_REFRESH_TOKEN
```

Expected response shape:

```json
{
  "access_token": "new_access_token",
  "expires_in": 3600,
  "refresh_token": "new_refresh_token",
  "refresh_token_expires_in": 7776000,
  "scope": "read_products,read_orders"
}
```

Important: every refresh returns a new refresh token and invalidates the old one. Always save both new tokens immediately:

```env
SHOPIFY_ACCESS_TOKEN=new_access_token
SHOPIFY_REFRESH_TOKEN=new_refresh_token
SHOPIFY_ACCESS_TOKEN_EXPIRES_AT=current_utc_time_plus_expires_in
SHOPIFY_REFRESH_TOKEN_EXPIRES_AT=current_utc_time_plus_refresh_token_expires_in
```

## If The Refresh Token Expires

If `SHOPIFY_REFRESH_TOKEN_EXPIRES_AT` passes, you need merchant interaction again:

1. Open the OAuth authorize URL again.
2. Get a fresh callback URL with a new `code`.
3. Exchange it with `expiring=1`.
4. Save the new access token, refresh token, and expiry times.

## Handy Debug Checks

Common errors:

- `401 Unauthorized`: token is wrong, revoked, copied from the wrong app/shop, or not an Admin API token.
- `403 Forbidden` with non-expiring token message: exchange or migrate using `expiring=1`.
- `400 Bad Request` during code exchange: the OAuth `code` was already used, expired, or does not match the app/shop.

Official docs:

- Expiring offline tokens: https://shopify.dev/docs/apps/auth/access-token-types/offline/
- Authorization code grant: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens


=======
https://ecommerized-branch.myshopify.com/admin/oauth/authorize?client_id=0804228a0372f2ca49f7e2057f28f3f5

https://example.com/?code=4c762bfa7f212d8dcd964ef79895971c&hmac=6bb17b5b8376414c76520edea1921c0348ae64d2c19b8cb2bbc4b88cbf0a9c23&host=YWRtaW4uc2hvcGlmeS5jb20vc3RvcmUvZWNvbW1lcml6ZWQtYnJhbmNo&shop=ecommerized-branch.myshopify.com&timestamp=1779054608




==============

https://ecommerized-branch.myshopify.com/admin/oauth/authorize?client_id=0804228a0372f2ca49f7e2057f28f3f5

https://example.com/?code=4c762bfa7f212d8dcd964ef79895971c&hmac=6bb17b5b8376414c76520edea1921c0348ae64d2c19b8cb2bbc4b88cbf0a9c23&host=YWRtaW4uc2hvcGlmeS5jb20vc3RvcmUvZWNvbW1lcml6ZWQtYnJhbmNo&shop=ecommerized-branch.myshopify.com&timestamp=1779054608




==============

Use this authorize link shape:

https://ecommerized-branch.myshopify.com/admin/oauth/authorize?client_id=0804228a0372f2ca49f7e2057f28f3f5&scope=read_products,read_orders&redirect_uri=https%3A%2F%2Fexample.com%2F&state=random123
For your app, if Shopify already has scopes/redirect configured, this simpler link also works, like you used before:

https://ecommerized-branch.myshopify.com/admin/oauth/authorize?client_id=0804228a0372f2ca49f7e2057f28f3f5
After Shopify redirects you to:

https://example.com/?code=NEW_CODE&hmac=...&shop=ecommerized-branch.myshopify.com&timestamp=...
Then the POST must include expiring=1:

client_id=YOUR_API_KEY
client_secret=YOUR_API_SECRET
code=NEW_CODE
expiring=1
So: link gets the code; POST with expiring=1 gets the 90-day refresh token.
=======