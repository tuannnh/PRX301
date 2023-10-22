import secrets

# Generate a secure random key
secret_key = secrets.token_urlsafe(32)

print("Generated Secret Key:", secret_key)
