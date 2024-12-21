import io
from collections.abc import Generator
from typing import Any

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class ExtractDocument(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Ensure runtime and credentials
        if not self.runtime or not self.runtime.credentials:
            raise ToolProviderCredentialValidationError("Tool runtime or credentials are missing")

        # Get endpoint and api key
        endpoint = str(self.runtime.credentials.get("azure_ai_document_intelligence_api_endpoint"))
        api_key = str(self.runtime.credentials.get("azure_ai_document_intelligence_api_key"))

        # Create credential
        credential = AzureKeyCredential(api_key)

        # Get file
        file = tool_parameters.get("file")
        file_binary = io.BytesIO(file.blob)  # type: ignore

        # Get output format
        output_format = tool_parameters.get("output_format")

        # Create client and analyze document
        document_analysis_client = DocumentIntelligenceClient(endpoint, credential)
        poller = document_analysis_client.begin_analyze_document(
            model_id="prebuilt-layout",
            body=file_binary,
            content_type="application/octet-stream",
            output_content_format="markdown" if output_format == "markdown" else None,
        )
        result = poller.result()

        yield self.create_text_message(result.content)
