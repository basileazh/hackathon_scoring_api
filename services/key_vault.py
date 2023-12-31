# Create a module that connects to Azure Key Vault and retrieves secrets through a retrieve_secret function
import os
from azure.keyvault.secrets import SecretClient

from services.identity import credential
from core.config import get_setting

key_vault_uri = get_setting("key_vault_uri")
client = SecretClient(vault_url=key_vault_uri, credential=credential)


def retrieve_secret(secret_name: str) -> str:
    """
    Retrieves a secret from Azure Key Vault
    :param secret_name: Name of the secret
    :return: secret value
    """
    secret = client.get_secret(secret_name)
    return secret.value

