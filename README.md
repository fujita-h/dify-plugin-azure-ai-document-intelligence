![Icon](./_assets/00819-icon-service-Form-Recognizers.svg)

# Azure AI Document Intelligence

[![GitHub Repo](https://img.shields.io/badge/GitHub_Repo-fujita--h/dify--plugin--azure--ai--document--intelligence-blue?logo=github)](https://github.com/fujita-h/dify-plugin-azure-ai-document-intelligence)  
[![GitHub Release](https://img.shields.io/github/v/release/fujita-h/dify-plugin-azure-ai-document-intelligence)](https://github.com/fujita-h/dify-plugin-azure-ai-document-intelligence/releases)
[![GitHub License](https://img.shields.io/github/license/fujita-h/dify-plugin-azure-ai-document-intelligence)](https://github.com/fujita-h/dify-plugin-azure-ai-document-intelligence/blob/main/LICENSE)

This plugin provides tools to extract text from a document using the Azure AI Document Intelligence service.

> [!IMPORTANT]  
> This plugin requires an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Learn more about the free trial [here](https://azure.microsoft.com/free/).

## Tools provided by this plugin

### Extract Document

This tool extracts text from a document using the Azure AI Document Intelligence service. The tool takes a document as input and returns the extracted text or Markdown. Supported document formats include PDF, JPEG, JPG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX, and HTML.

https://learn.microsoft.com/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0

## Configuration Steps to use this plugin

1. Create an Azure AI Document Intelligence resource in the Azure portal.
2. Get the endpoint and key from the Azure portal.
3. Install the plugin.
4. Authorize the plugin with the endpoint and key.
5. Use the tools provided by the plugin.

## Notes

This plugin uses the Document Layout Analysis API v4.0 of the [Azure AI Document Intelligence](https://azure.microsoft.com/products/ai-services/ai-document-intelligence) service. Please refer to the official documentation for more information.

## Contributing

This plugin is open-source and contributions are welcome. Please visit the GitHub repository to contribute.
