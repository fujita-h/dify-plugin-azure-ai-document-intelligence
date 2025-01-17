from typing import Any

import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class AzureAiDocumentIntelligenceProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            api_endpoint = str(credentials.get("api_endpoint", "")).strip()
            api_key = str(credentials.get("api_key", "")).strip()

            # Ensure API key and endpoint are provided
            if not api_endpoint:
                raise Exception("API endpoint is missing")
            if not api_key:
                raise Exception("API key is missing")

            # Validate the API key and endpoint
            headers = {"Ocp-Apim-Subscription-Key": api_key}
            url = (
                f"{api_endpoint}/documentintelligence/documentModels/"
                f"prebuilt-layout/analyzeResults/00000000-0000-0000-0000-000000000000"
                f"?api-version=2024-11-30"
            )

            # Check if the API key and endpoint are valid
            response = requests.get(url, headers=headers)
            json_response = response.json()
            if json_response["code"] == "NotFound":
                return
            raise Exception("API endpoint or key." + str(json_response))

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) from e
