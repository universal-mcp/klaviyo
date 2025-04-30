from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class KlaviyoApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='klaviyo', integration=integration, **kwargs)
        self.base_url = "https://a.klaviyo.com"

    def get_accounts(self, fields_account=None) -> dict[str, Any]:
        """
        Retrieves account data via API request, returning parsed JSON response.
        
        Args:
            fields_account: Optional string of fields to include for accounts in API response (None returns all available fields).
        
        Returns:
            Dictionary containing account data parsed from API response.
        
        Raises:
            requests.HTTPError: Raised for 4XX/5XX status codes in API responses.
        
        Tags:
            fetch, api, accounts, management, data-retrieval, important
        """
        url = f"{self.base_url}/api/accounts/"
        query_params = {k: v for k, v in [('fields[account]', fields_account)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_account(self, id, fields_account=None) -> dict[str, Any]:
        """
        Retrieves account details from the API by ID.
        
        Args:
            id: Unique identifier of the account to retrieve.
            fields_account: Optional comma-separated fields to include in the account response (if None, all fields are returned). Defaults to None.
        
        Returns:
            Dictionary containing the account data as returned by the API.
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided.
            requests.HTTPError: Raised if the API request fails (e.g., 404 Not Found or 503 Service Unavailable).
        
        Tags:
            account, management, get, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/accounts/{id}/"
        query_params = {k: v for k, v in [('fields[account]', fields_account)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaigns(self, filter, fields_campaign_message=None, fields_campaign=None, fields_tag=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieve campaign data with optional filtering, field selection, pagination, and sorting.
        
        Args:
            filter: Mandatory filter conditions for selecting campaigns
            fields_campaign_message: List of campaign-message fields to include in response (comma-separated)
            fields_campaign: List of campaign fields to include in response (comma-separated)
            fields_tag: List of tag fields to include in response (comma-separated)
            include: Related resources to include in response (comma-separated)
            page_cursor: Pagination cursor for retrieving specific page
            sort: Sort order for results
        
        Returns:
            Dictionary containing campaign data and metadata from API response
        
        Raises:
            ValueError: If required parameter 'filter' is not provided
            requests.HTTPError: If API request fails (4xx/5xx status code)
        
        Tags:
            campaign-retrieval, api-wrapper, filter, pagination, include-related, important
        """
        if filter is None:
            raise ValueError("Missing required parameter 'filter'")
        url = f"{self.base_url}/api/campaigns/"
        query_params = {k: v for k, v in [('filter', filter), ('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[tag]', fields_tag), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign(self, data) -> dict[str, Any]:
        """
        Creates a campaign by sending a POST request to the specified API endpoint with the given data.
        
        Args:
            data: A dictionary containing campaign data required for creation.
        
        Returns:
            A dictionary containing the response from the server as JSON.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
        
        Tags:
            create, campaign, important, management
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign(self, id, fields_campaign_message=None, fields_campaign=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
        Retrieves a campaign by its ID, allowing specification of fields and inclusion of additional data.
        
        Args:
            id: The unique identifier of the campaign to retrieve.
            fields_campaign_message: Specifies fields related to the campaign message; defaults to None.
            fields_campaign: Specifies fields related to the campaign; defaults to None.
            fields_tag: Specifies fields related to tags; defaults to None.
            include: Additional data to include in the response; defaults to None.
        
        Returns:
            A dictionary containing campaign data.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            fetch, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign(self, id, data) -> dict[str, Any]:
        """
        Updates an existing campaign with the provided data using a PATCH request.
        
        Args:
            id: The unique identifier of the campaign to update.
            data: The data to update in the campaign.
        
        Returns:
            A dictionary containing the updated campaign data.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is missing.
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_campaign(self, id) -> Any:
        """
        Deletes a campaign by its ID.
        
        Args:
            id: The ID of the campaign to delete.
        
        Returns:
            The JSON response from the server after deletion.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
            requests.exceptions.HTTPError: Raised if the HTTP request encounters an error or the response status code indicates failure.
        
        Tags:
            delete, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message(self, id, fields_campaign_message=None, fields_campaign=None, fields_template=None, include=None) -> dict[str, Any]:
        """
        Retrieves a campaign message by ID, optionally including specified fields.
        
        Args:
            id: The ID of the campaign message to retrieve.
            fields_campaign_message: Optional fields to include from the campaign message.
            fields_campaign: Optional fields to include from the campaign.
            fields_template: Optional fields to include from the template.
            include: Optional items to include alongside the message.
        
        Returns:
            A dictionary containing the retrieved campaign message.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            retrieve, campaign-message, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign_message(self, id, data) -> dict[str, Any]:
        """
        Updates a campaign message by sending a patch request to the specified API endpoint.
        
        Args:
            id: The ID of the campaign message to be updated.
            data: The updated data to be applied to the campaign message.
        
        Returns:
            A dictionary containing the updated campaign message data.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is None.
        
        Tags:
            update, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-messages/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_send_job(self, id, fields_campaign_send_job=None) -> dict[str, Any]:
        """
        Retrieves a campaign send job by its ID, optionally specifying fields to include in the response.
        
        Args:
            id: Unique identifier of the campaign send job.
            fields_campaign_send_job: Optional list of fields to include in the response.
        
        Returns:
            A dictionary containing the campaign send job details.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing or null.
        
        Tags:
            get, job, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-send-jobs/{id}/"
        query_params = {k: v for k, v in [('fields[campaign-send-job]', fields_campaign_send_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign_send_job(self, id, data) -> Any:
        """
        Updates an existing campaign send job with the provided data.
        
        Args:
            id: The identifier of the campaign send job to be updated.
            data: The data used to update the campaign send job.
        
        Returns:
            The JSON response from the API after updating the campaign send job.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' is missing.
        
        Tags:
            update, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation_job(self, id, fields_campaign_recipient_estimation_job=None) -> dict[str, Any]:
        """
        Retrieve details for a specific campaign recipient estimation job by ID.
        
        Args:
            id: The unique identifier of the campaign recipient estimation job.
            fields_campaign_recipient_estimation_job: Optional fields to include in the response (comma-separated string). Omit for all fields.
        
        Returns:
            A dictionary containing the campaign recipient estimation job's data, including status, metadata, and results.
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided.
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., invalid ID or server error).
        
        Tags:
            retrieve, api, campaign, estimation-job, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs/{id}/"
        query_params = {k: v for k, v in [('fields[campaign-recipient-estimation-job]', fields_campaign_recipient_estimation_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation(self, id, fields_campaign_recipient_estimation=None) -> dict[str, Any]:
        """
        Retrieve campaign recipient estimation details for a specific campaign ID.
        
        Args:
            id: Campaign identifier (required) to fetch recipient estimation data
            fields_campaign_recipient_estimation: Optional fields filter for campaign recipient estimation response
        
        Returns:
            Dictionary containing campaign recipient estimation details and metadata
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            requests.HTTPError: Raised for failed HTTP requests (4xx/5xx status codes)
        
        Tags:
            retrieve, campaign, recipient-estimation, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimations/{id}/"
        query_params = {k: v for k, v in [('fields[campaign-recipient-estimation]', fields_campaign_recipient_estimation)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_clone(self, data) -> dict[str, Any]:
        """
        Creates a clone of a campaign using the provided data.
        
        Args:
            data: A dictionary containing the necessary data for creating a campaign clone.
        
        Returns:
            A dictionary containing the JSON response from the campaign cloning request.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing.
        
        Tags:
            clone, campaign, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-clone/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_message_assign_template(self, data) -> dict[str, Any]:
        """
        Creates a campaign message by assigning a template with provided data.
        
        Args:
            data: Dictionary containing data necessary for the campaign message assignment.
        
        Returns:
            A dictionary containing the response from assigning the template to a campaign message.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing.
        
        Tags:
            assign, campaign, message, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-message-assign-template/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_send_job(self, data) -> dict[str, Any]:
        """
        Creates a campaign send job by sending data to the API endpoint, handling request validation and response parsing.
        
        Args:
            data: Dictionary containing campaign send job configuration data. Must be non-null.
        
        Returns:
            Dictionary containing API response data with details of the created campaign send job.
        
        Raises:
            ValueError: Raised when required parameter 'data' is None.
            requests.HTTPError: Raised when the API request fails (status code ≥ 400).
        
        Tags:
            create, async-job, campaign, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_recipient_estimation_job(self, data) -> dict[str, Any]:
        """
        Initiates an asynchronous job to estimate campaign recipients by submitting provided data to the API.
        
        Args:
            data: Payload containing information required for recipient estimation (e.g., campaign parameters or targeting criteria). Must not be None.
        
        Returns:
            Dictionary containing the API response data with details of the created estimation job.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
            requests.exceptions.HTTPError: Raised for 4XX/5XX status codes from the API.
        
        Tags:
            campaign, async_job, recipient-estimation, api, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message_relationships_campaign(self, id) -> dict[str, Any]:
        """
        Retrieves campaign relationship data for a specific campaign message from the API.
        
        Args:
            id: The unique identifier of the campaign message for which to fetch relationships (required)
        
        Returns:
            Dictionary containing relationship data between the specified campaign message and its associated campaign.
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided
            HTTPError: Raised for unsuccessful API responses (4xx/5xx status codes)
        
        Tags:
            retrieve, campaign, relationships, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/campaign/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message_campaign(self, id, fields_campaign=None) -> dict[str, Any]:
        """
        Retrieve campaign details for a specific campaign message using its ID and optional field filtering.
        
        Args:
            id: Unique identifier for the campaign message to fetch associated campaign data
            fields_campaign: Optional fields to include in the returned campaign data. If None, returns all fields (default: None)
        
        Returns:
            Dictionary containing campaign details as key-value pairs
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided
            Exception: Raised when the HTTP request fails (via response.raise_for_status)
        
        Tags:
            get, campaign, api, retrieve, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/campaign/"
        query_params = {k: v for k, v in [('fields[campaign]', fields_campaign)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message_relationships_template(self, id) -> dict[str, Any]:
        """
        Retrieve the template relationships for a specific campaign message.
        
        Args:
            id: Unique identifier of the campaign message for which to fetch template relationships
        
        Returns:
            Dictionary containing template relationship data retrieved from the API endpoint
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            requests.HTTPError: Raised for unsuccessful HTTP requests (e.g., 4xx/5xx status codes)
        
        Tags:
            campaign, template, relationships, retrieve, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/template/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message_template(self, id, fields_template=None) -> dict[str, Any]:
        """
        Fetches the message template for a campaign based on the provided ID.
        
        Args:
            id: The unique ID of the campaign.
            fields_template: Optional fields to include in the template.
        
        Returns:
            A dictionary containing the campaign message template.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing or None.
        
        Tags:
            fetch, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/template/"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_relationships_tags(self, id) -> dict[str, Any]:
        """
        Retrieve tag relationships for a specific campaign via API endpoint.
        
        Args:
            id: Unique identifier of the campaign to fetch tag relationships for
        
        Returns:
            Dictionary containing tag relationship data from the API response
        
        Raises:
            ValueError: When 'id' parameter is None
            requests.exceptions.HTTPError: If the API request fails (e.g., non-2xx status code)
        
        Tags:
            campaign-tags, api, get, relationships, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/tags/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_tags(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Fetches tags associated with a campaign by ID from an API.
        
        Args:
            id: The unique identifier of the campaign.
            fields_tag: Optional parameter to filter tag fields.
        
        Returns:
            A dictionary containing campaign tags with their associated information.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing or set to None.
        
        Tags:
            retrieve, campaign, tag-management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/tags/"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_relationships_campaign_messages(self, id) -> dict[str, Any]:
        """
        Fetches campaign relationships for campaign messages by a given campaign ID.
        
        Args:
            id: The ID of the campaign for which relationships are to be retrieved.
        
        Returns:
            A dictionary containing campaign relationship data for messages.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            fetch, campaign, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/campaign-messages/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_campaign_messages(self, id, fields_campaign_message=None, fields_campaign=None, fields_template=None, include=None) -> dict[str, Any]:
        """
        Retrieve campaign messages for a specified campaign ID, allowing for customizable field selection and inclusion.
        
        Args:
            id: The identifier of the campaign to fetch messages from.
            fields_campaign_message: Optional; fields to include in the campaign message response.
            fields_campaign: Optional; fields to include in the campaign response.
            fields_template: Optional; fields to include in the template response.
            include: Optional; additional data or objects to include in the response.
        
        Returns:
            A dictionary containing campaign messages and other included data.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            fetch, campaign, messages, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/campaign-messages/"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_items(self, fields_catalog_item=None, fields_catalog_variant=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves catalog items from the API, allowing for specification of fields, filters, and sorting.
        
        Args:
            fields_catalog_item: Optional list of fields to include for catalog items.
            fields_catalog_variant: Optional list of fields to include for catalog variants.
            filter: Optional filter query to apply to the results.
            include: Optional list of related resources to include.
            page_cursor: Optional cursor for pagination.
            sort: Optional sorting criteria.
        
        Returns:
            A dictionary containing the response data from the API.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, api, catalog, important
        """
        url = f"{self.base_url}/api/catalog-items/"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_item(self, data) -> dict[str, Any]:
        """
        Creates a new catalog item using provided data by sending a POST request to the catalog-items endpoint.
        
        Args:
            data: Required data dictionary containing catalog item attributes
        
        Returns:
            Dictionary containing the created catalog item's data from the API response
        
        Raises:
            ValueError: Raised when 'data' parameter is None
            requests.HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes)
        
        Tags:
            create, catalog-item, post, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item(self, id, fields_catalog_item=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
        Retrieve a specific catalog item with optional field filtering and related data inclusion
        
        Args:
            id: The unique identifier of the catalog item to retrieve
            fields_catalog_item: Comma-separated fields to include for the catalog item (None returns all fields)
            fields_catalog_variant: Comma-separated fields to include for associated catalog variants (None returns all fields)
            include: Related resources to include in the response (comma-separated)
        
        Returns:
            Dictionary containing the catalog item data and requested associations
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            HTTPError: Raised when the API request fails (e.g., invalid ID or server error)
        
        Tags:
            retrieve, catalog, api, data, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_item(self, id, data) -> dict[str, Any]:
        """
        Updates a catalog item by sending a PATCH request with the provided data to the specified catalog item ID.
        
        Args:
            id: The unique identifier of the catalog item to be updated.
            data: The updated data payload to be sent in the request body. Must be a valid dictionary with fields matching the catalog item schema.
        
        Returns:
            A dictionary containing the updated catalog item data, including server-generated fields (e.g., timestamps, computed values) where applicable.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameter is None, indicating missing required input.
            HTTPError: Raised by response.raise_for_status() for unsuccessful HTTP responses (4XX/5XX status codes).
        
        Tags:
            update, catalog-management, api-call, async_job, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_item(self, id) -> Any:
        """
        Deletes a catalog item based on the provided ID.
        
        Args:
            id: The ID of the catalog item to delete.
        
        Returns:
            JSON response after successful deletion.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            delete, catalog-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variants(self, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves catalog variants from the API with optional filtering, sorting, and pagination.
        
        Args:
            fields_catalog_variant: Fields to include in the catalog variant response. Defaults to None.
            filter: Filter criteria for the catalog variants. Defaults to None.
            page_cursor: Page cursor for pagination. Defaults to None.
            sort: Sorting criteria for the catalog variants. Defaults to None.
        
        Returns:
            A dictionary containing the retrieved catalog variants.
        
        Raises:
            requests.exceptions.HTTPError: If the HTTP request fails due to a server error or invalid response.
        
        Tags:
            fetch, catalog, management, important
        """
        url = f"{self.base_url}/api/catalog-variants/"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_variant(self, data) -> dict[str, Any]:
        """
        Creates a catalog variant using the provided data.
        
        Args:
            data: The data used to create the catalog variant. It must be a dictionary-like object and cannot be None.
        
        Returns:
            A dictionary containing the response from creating the catalog variant.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing or None.
        
        Tags:
            create, catalog-management, variant, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variant(self, id, fields_catalog_variant=None) -> dict[str, Any]:
        """
        Retrieves a catalog variant from the API based on its ID, optionally specifying fields to return.
        
        Args:
            id: The unique identifier of the catalog variant to retrieve.
            fields_catalog_variant: An optional list of fields to include in the catalog variant response.
        
        Returns:
            A dictionary containing the details of the catalog variant.
        
        Raises:
            ValueError: Raised if the required parameter 'id' is missing.
        
        Tags:
            fetch, catalog, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}/"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_variant(self, id, data) -> dict[str, Any]:
        """
        Updates a catalog variant by ID with provided data using a PATCH request.
        
        Args:
            id: The unique identifier of the catalog variant to update.
            data: The data payload containing fields to update for the catalog variant.
        
        Returns:
            A dictionary containing the updated catalog variant data from the JSON response.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameters are None.
            requests.exceptions.HTTPError: Raised when the PATCH request fails (e.g., invalid ID or malformed data).
        
        Tags:
            update, catalog-variant, patch, api, important, management
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_variant(self, id) -> Any:
        """
        Deletes a catalog variant by its ID.
        
        Args:
            id: The ID of the catalog variant to be deleted.
        
        Returns:
            The JSON response from the server after deletion.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing or None.
            HTTPError: Raised if the HTTP request fails or returns an unsuccessful status code.
        
        Tags:
            delete, catalog-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_categories(self, fields_catalog_category=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves catalog categories via API with optional filtering and pagination
        
        Args:
            fields_catalog_category: Optional list of fields to include in the catalog category response
            filter: Optional filter to apply to the catalog categories
            page_cursor: Optional page cursor for pagination
            sort: Optional parameter to sort the catalog categories
        
        Returns:
            A dictionary containing the catalog categories data
        
        Raises:
            HTTPError: If the API request fails (e.g., invalid URL, network errors, server errors)
        
        Tags:
            list, management, catalog, api-call, important
        """
        url = f"{self.base_url}/api/catalog-categories/"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_category(self, data) -> dict[str, Any]:
        """
        Creates a new catalog category by sending a POST request with the provided data.
        
        Args:
            data: The data used to create the catalog category. Must be a dictionary.
        
        Returns:
            A dictionary containing the newly created catalog category's details.
        
        Raises:
            ValueError: Raised when the required parameter 'data' is missing.
        
        Tags:
            create, catalog, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_category(self, id, fields_catalog_category=None) -> dict[str, Any]:
        """
        Retrieves a catalog category by its ID, optionally specifying fields to include.
        
        Args:
            id: The ID of the catalog category to fetch.
            fields_catalog_category: Optional list of fields to include in the response for the catalog category.
        
        Returns:
            A dictionary containing the catalog category details.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            fetch, catalog, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_category(self, id, data) -> dict[str, Any]:
        """
        Updates a catalog category by making a PATCH request to the API endpoint with provided data.
        
        Args:
            id: Unique identifier of the catalog category to update.
            data: Dictionary containing updated category details.
        
        Returns:
            Dictionary containing the updated catalog category data from the API response.
        
        Raises:
            ValueError: If either 'id' or 'data' parameter is None.
            requests.exceptions.HTTPError: If the API request fails (non-2xx status code).
        
        Tags:
            update, catalog, category, api, patch, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_category(self, id) -> Any:
        """
        Deletes a catalog category by its ID.
        
        Args:
            id: Unique identifier of the catalog category to delete.
        
        Returns:
            Parsed JSON response from the API call, typically containing deletion confirmation or status.
        
        Raises:
            ValueError: Raised if 'id' is None or invalid.
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., 404 Not Found, 500 Internal Server Error).
        
        Tags:
            delete, catalog, management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_items_jobs(self, fields_catalog_item_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of catalog item bulk create jobs from an API with optional filtering and pagination.
        
        Args:
            fields_catalog_item_bulk_create_job: Optional fields to include in the response for the catalog item bulk create jobs.
            filter: Optional filter for the query.
            page_cursor: Optional cursor for pagination.
        
        Returns:
            A dictionary containing the response data.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, api, catalog, async_job, management, important
        """
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-create-job]', fields_catalog_item_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_create_items_job(self, data) -> dict[str, Any]:
        """
        Initiates a job to create items in bulk using the provided data.
        
        Args:
            data: The data used for bulk item creation. Must be a dictionary.
        
        Returns:
            A dictionary containing the response from the server after initiating the creation job.
        
        Raises:
            ValueError: Raised if the required 'data' parameter is missing.
        
        Tags:
            create, bulk, job, catalog, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_items_job(self, job_id, fields_catalog_item_bulk_create_job=None, fields_catalog_item=None, include=None) -> dict[str, Any]:
        """
        Retrieves details of a catalog item bulk creation job by its ID, including options for specifying which fields and related data to include.
        
        Args:
            job_id: The ID of the catalog item bulk creation job to retrieve.
            fields_catalog_item_bulk_create_job: Optional parameter to specify fields for the bulk create job.
            fields_catalog_item: Optional parameter to specify fields for the catalog items.
            include: Optional parameter to specify related items to include.
        
        Returns:
            Dictionary with details of the job.
        
        Raises:
            ValueError: Raised if the 'job_id' is None.
        
        Tags:
            fetch, retrieve, management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-create-job]', fields_catalog_item_bulk_create_job), ('fields[catalog-item]', fields_catalog_item), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_items_jobs(self, fields_catalog_item_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieve paginated list of catalog item bulk update jobs using REST API endpoint.
        
        Args:
            fields_catalog_item_bulk_update_job: Fields to include for each catalog item bulk update job (comma-delimited string)
            filter: Query filter to limit results (string)
            page_cursor: Pagination cursor for fetching subsequent pages (string)
        
        Returns:
            Dictionary containing paginated API response data with job listings
        
        Raises:
            requests.exceptions.HTTPError: When API request fails with HTTP error status code
        
        Tags:
            list, management, api, bulk-operations, pagination, important
        """
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-update-job]', fields_catalog_item_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_update_items_job(self, data) -> dict[str, Any]:
        """
        Spawns an asynchronous job to update catalog items in bulk.
        
        Args:
            data: Dictionary of data used for updating catalog items.
        
        Returns:
            Dictionary with job details returned as JSON.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing or null.
        
        Tags:
            update, bulk-job, async_job, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_items_job(self, job_id, fields_catalog_item_bulk_update_job=None, fields_catalog_item=None, include=None) -> dict[str, Any]:
        """
        Retrieves details of a catalog item bulk update job by its ID.
        
        Args:
            job_id: The ID of the catalog item bulk update job.
            fields_catalog_item_bulk_update_job: Optional fields to include for the catalog item bulk update job.
            fields_catalog_item: Optional fields to include for the catalog item.
            include: Optional parameters to include in the response.
        
        Returns:
            A dictionary containing job details.
        
        Raises:
            ValueError: Raised if the required 'job_id' parameter is missing.
        
        Tags:
            retrieve, job, api, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-update-job]', fields_catalog_item_bulk_update_job), ('fields[catalog-item]', fields_catalog_item), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_items_jobs(self, fields_catalog_item_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of catalog item bulk delete jobs with specified fields and filtering.
        
        Args:
            fields_catalog_item_bulk_delete_job: Optional list of fields to include in the response for catalog item bulk delete jobs.
            filter: Optional filter to apply to the results.
            page_cursor: Optional cursor for pagination.
        
        Returns:
            A dictionary containing the catalog item bulk delete jobs.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, catalog, management, important
        """
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-delete-job]', fields_catalog_item_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_delete_items_job(self, data) -> dict[str, Any]:
        """
        Initiates a job to delete items in bulk.
        
        Args:
            data: Data required for the bulk delete operation
        
        Returns:
            A dictionary containing the response from the bulk delete job initiation
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing
        
        Tags:
            bulk, delete, async_job, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_items_job(self, job_id, fields_catalog_item_bulk_delete_job=None) -> dict[str, Any]:
        """
        Retrieves a catalog item bulk delete job based on the provided job ID.
        
        Args:
            job_id: The ID of the catalog item bulk delete job to retrieve.
            fields_catalog_item_bulk_delete_job: Optional fields to include in the response for the catalog item bulk delete job.
        
        Returns:
            A dictionary containing details of the catalog item bulk delete job.
        
        Raises:
            ValueError: Raised when the required 'job_id' parameter is missing or None.
        
        Tags:
            get, job, catalog, api, management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-delete-job]', fields_catalog_item_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_jobs(self, fields_catalog_variant_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves catalog variant bulk create jobs data from the API.
        
        Args:
            fields_catalog_variant_bulk_create_job: Optional list or string specifying fields to include in the response.
            filter: Optional filter criteria for the results.
            page_cursor: Optional page cursor for pagination purposes.
        
        Returns:
            A dictionary containing the API response data.
        
        Raises:
            requests.exceptions.HTTPError: Raised when an HTTP error occurs in the request.
        
        Tags:
            retrieve, batch, catalog, important
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-create-job]', fields_catalog_variant_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_create_variants_job(self, data) -> dict[str, Any]:
        """
        Initiates an asynchronous job to bulk-create catalog variants using the provided data.
        
        Args:
            data: Required dictionary containing the variant data to be created in bulk. Must not be None.
        
        Returns:
            Dictionary containing the job details as returned by the API, including job identifiers and initial status.
        
        Raises:
            ValueError: Raised when the 'data' parameter is not provided (None value)
            requests.HTTPError: Raised when the API request fails with a non-2xx status code
        
        Tags:
            async-job, catalog, bulk-operations, create, variant-management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_job(self, job_id, fields_catalog_variant_bulk_create_job=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
        Retrieves a Catalog Variant Bulk Create Job by its ID, allowing for customizable data fields and inclusions.
        
        Args:
            job_id: The unique identifier for the bulk create job.
            fields_catalog_variant_bulk_create_job: Optional fields to include for the bulk create job.
            fields_catalog_variant: Optional fields to include for each catalog variant.
            include: Optional resources to include in the response.
        
        Returns:
            A dictionary containing the job details and any requested inclusions.
        
        Raises:
            ValueError: Raised if the required 'job_id' parameter is missing.
        
        Tags:
            fetch, job, catalog, management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-create-job]', fields_catalog_variant_bulk_create_job), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_jobs(self, fields_catalog_variant_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieve paginated catalog variant bulk update jobs via API endpoint with filtering and field selection.
        
        Args:
            fields_catalog_variant_bulk_update_job: Comma-separated fields to include in catalog variant job objects
            filter: Criteria to filter jobs, formatted as API-specific filter expression
            page_cursor: Pagination cursor for fetching specific results page
        
        Returns:
            Dictionary containing API response data including jobs list and pagination details
        
        Raises:
            requests.HTTPError: On invalid API request or server errors (4XX/5XX status codes)
        
        Tags:
            retrieve, list, catalog, bulk-job, pagination, api, important
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-update-job]', fields_catalog_variant_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_update_variants_job(self, data) -> dict[str, Any]:
        """
        Spawns a job to update variants in bulk via an API request.
        
        Args:
            data: Data used for the bulk update job.
        
        Returns:
            A dictionary containing the response from the API.
        
        Raises:
            ValueError: Raised if the required 'data' parameter is missing or None.
        
        Tags:
            update, job, bulk, api-request, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_job(self, job_id, fields_catalog_variant_bulk_update_job=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
        Retrieves details of a specific catalog variant bulk update job using the provided job ID.
        
        Args:
            job_id: The unique identifier of the catalog variant bulk update job to retrieve.
            fields_catalog_variant_bulk_update_job: Optional fields to include in the catalog-variant-bulk-update-job response (comma-separated string).
            fields_catalog_variant: Optional fields to include for catalog variants in the response (comma-separated string).
            include: Optional related resources to include in the response (comma-separated string).
        
        Returns:
            A dictionary containing the job details and requested fields/relationships.
        
        Raises:
            ValueError: When the required 'job_id' parameter is not provided.
            HTTPError: When the API request fails (e.g., invalid job ID or server error).
        
        Tags:
            get, async-job, catalog, variant, management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-update-job]', fields_catalog_variant_bulk_update_job), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_jobs(self, fields_catalog_variant_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves catalog variant bulk delete jobs with optional filtering and pagination.
        
        Args:
            fields_catalog_variant_bulk_delete_job: Optional fields to include in the response for catalog variant bulk delete jobs.
            filter: Optional query filter to narrow down the results.
            page_cursor: Optional page cursor for pagination.
        
        Returns:
            A dictionary containing the response from the API about catalog variant bulk delete jobs.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, bulk, delete, management, important
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-delete-job]', fields_catalog_variant_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_delete_variants_job(self, data) -> dict[str, Any]:
        """
        Initiates an asynchronous job to delete multiple catalog variants using bulk delete operation.
        
        Args:
            data: Payload containing the variants to be deleted. Must not be None.
        
        Returns:
            Dictionary containing metadata and status of the spawned bulk-delete job.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None, indicating missing required input.
            HTTPError: Raised when the API request fails (handled via response.raise_for_status()).
        
        Tags:
            async_job, bulk-delete, catalog, variants, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_job(self, job_id, fields_catalog_variant_bulk_delete_job=None) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific catalog variant bulk delete job.
        
        Args:
            job_id: The unique identifier of the bulk delete job to retrieve (required).
            fields_catalog_variant_bulk_delete_job: Optional comma-separated string specifying fields to include in the response.
        
        Returns:
            A dictionary containing the job status and details as returned by the API.
        
        Raises:
            ValueError: Raised when the required 'job_id' parameter is not provided.
            requests.exceptions.HTTPError: Raised for invalid/expired job IDs or API request failures.
        
        Tags:
            catalog, variant, management, async_job, status, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-delete-job]', fields_catalog_variant_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_jobs(self, fields_catalog_category_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves a list of catalog category bulk create jobs, optionally filtering by specified criteria or fields.
        
        Args:
            fields_catalog_category_bulk_create_job: Fields to include in the response for each catalog category bulk create job.
            filter: Criteria to filter the jobs by.
            page_cursor: Cursor for pagination, indicating where to start or resume retrieving jobs.
        
        Returns:
            A dictionary containing the catalog category bulk create jobs with metadata.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, management, catalog, async_job, important
        """
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-create-job]', fields_catalog_category_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_create_categories_job(self, data) -> dict[str, Any]:
        """
        Initiates an asynchronous job to create categories in the catalog by submitting a data payload.
        
        Args:
            data: Payload containing category data for creation (required)
        
        Returns:
            Dictionary containing the job details and response data from the API after successful submission
        
        Raises:
            ValueError: If 'data' parameter is None or missing
            requests.HTTPError: If the API request fails (e.g., 4XX/5XX status codes)
        
        Tags:
            create, async_job, catalog, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_job(self, job_id, fields_catalog_category_bulk_create_job=None, fields_catalog_category=None, include=None) -> dict[str, Any]:
        """
        Retrieves information about a bulk category creation job based on the provided job ID.
        
        Args:
            job_id: The ID of the job to retrieve information from.
            fields_catalog_category_bulk_create_job: Optional fields to include in the bulk category creation job response.
            fields_catalog_category: Optional fields to include for each catalog category in the response.
            include: Optional parameters to include in the response.
        
        Returns:
            A dictionary containing the job details.
        
        Raises:
            ValueError: Raised if the required 'job_id' parameter is missing.
        
        Tags:
            retrieve, job, catalog-management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-create-job]', fields_catalog_category_bulk_create_job), ('fields[catalog-category]', fields_catalog_category), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_jobs(self, fields_catalog_category_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieve paginated list of catalog category bulk update jobs from the API endpoint.
        
        Args:
            fields_catalog_category_bulk_update_job: Fields to include for each catalog-category-bulk-update-job resource (None returns all fields)
            filter: Filter criteria for selecting jobs (None returns all jobs)
            page_cursor: Pagination cursor for accessing subsequent result pages
        
        Returns:
            Dictionary containing API response data with job listings and pagination details
        
        Raises:
            requests.exceptions.HTTPError: When the API returns a non-success status code (4XX/5XX)
        
        Tags:
            retrieve, list, pagination, api, catalog, category-update, batch, management, important
        """
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-update-job]', fields_catalog_category_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_update_categories_job(self, data) -> dict[str, Any]:
        """
        Initiates an asynchronous bulk update job for categories using the provided data.
        
        Args:
            data: Mandatory payload containing category update information. Must not be None.
        
        Returns:
            Dictionary containing the created bulk update job details and metadata.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
            HTTPError: Raised when the API request fails (non-2xx response).
        
        Tags:
            update, async_job, bulk, catalog, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_job(self, job_id, fields_catalog_category_bulk_update_job=None, fields_catalog_category=None, include=None) -> dict[str, Any]:
        """
        Retrieves details of a catalog category bulk update job by its ID.
        
        Args:
            job_id: Unique identifier for the bulk category update job.
            fields_catalog_category_bulk_update_job: Optional fields to include for the bulk update job (comma-separated).
            fields_catalog_category: Optional fields to include for associated catalog categories (comma-separated).
            include: Optional related resources to include in the response (comma-separated).
        
        Returns:
            A dictionary containing the job details and requested fields from the API response.
        
        Raises:
            ValueError: Raised when job_id is not provided.
            HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes).
        
        Tags:
            category-management, async-job, status, api, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-update-job]', fields_catalog_category_bulk_update_job), ('fields[catalog-category]', fields_catalog_category), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_jobs(self, fields_catalog_category_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Retrieve paginated results of catalog category bulk deletion jobs from the API.
        
        Args:
            fields_catalog_category_bulk_delete_job: Comma-separated fields to include for each job object
            filter: Criteria to filter the jobs
            page_cursor: Pagination cursor for the next set of results
        
        Returns:
            Dictionary containing the API response with job listings
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures, such as unauthorized access or server errors
        
        Tags:
            retrieve, list, catalog, api, management, async_job, batch, important
        """
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-delete-job]', fields_catalog_category_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_delete_categories_job(self, data) -> dict[str, Any]:
        """
        Initiates a job to delete categories in bulk by sending a POST request to the API endpoint.
        
        Args:
            data: Dictionary containing the data required for deleting categories.
        
        Returns:
            A dictionary containing the JSON response from the API.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing.
        
        Tags:
            delete, categories, bulk, async_job, api, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_job(self, job_id, fields_catalog_category_bulk_delete_job=None) -> dict[str, Any]:
        """
        Retrieves the details of a catalog category bulk delete job by ID.
        
        Args:
            job_id: The ID of the job to retrieve.
            fields_catalog_category_bulk_delete_job: Optional list of fields to include in the response.
        
        Returns:
            A dictionary containing the details of the catalog category bulk delete job.
        
        Raises:
            ValueError: Raised when the required 'job_id' parameter is missing.
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            search, management, job-status, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-delete-job]', fields_catalog_category_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_back_in_stock_subscription(self, data) -> Any:
        """
        Creates a back-in-stock subscription by sending a POST request to the specified API endpoint.
        
        Args:
            data: A dictionary containing the necessary data for the subscription.
        
        Returns:
            A JSON response from the server after creating the subscription.
        
        Raises:
            ValueError: Raised when the required parameter 'data' is missing.
        
        Tags:
            create, subscription, async_job, e-commerce, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/back-in-stock-subscriptions/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_category_items(self, id, fields_catalog_item=None, fields_catalog_variant=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieve items belonging to a catalog category with optional filtering, sorting, and field selection.
        
        Args:
            id: Identifier of the catalog category (required)
            fields_catalog_item: Comma-separated fields to include for catalog items
            fields_catalog_variant: Comma-separated fields to include for catalog variants
            filter: Filter criteria for catalog items
            include: Related resources to include in the response
            page_cursor: Pagination cursor for paginated results
            sort: Sort order for returned items
        
        Returns:
            Dictionary containing paginated catalog items and variants from the specified category
        
        Raises:
            ValueError: Raised when the required 'id' parameter is not provided
            HTTPError: Raised when the API request fails (e.g., invalid parameters or server error)
        
        Tags:
            retrieve, catalog, items, pagination, api, filter, sort, category, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/items/"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item_variants(self, id, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Fetches variant items for a catalog item by ID, optionally filtering, sorting, or pagination.
        
        Args:
            id: The ID of the catalog item to fetch variants for.
            fields_catalog_variant: Optional fields to include in the catalog variant response.
            filter: Optional filter parameter to narrow down variant results.
            page_cursor: Optional cursor for pagination.
            sort: Optional sorting parameters.
        
        Returns:
            A dictionary containing the variant items for the specified catalog item.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
        
        Tags:
            fetch, catalog, api, pagination, filtering, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/variants/"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item_categories(self, id, fields_catalog_category=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieve categories associated with a specific catalog item using filtering, pagination, and sorting parameters.
        
        Args:
            id: Identifier of the catalog item for which to fetch categories
            fields_catalog_category: (Optional) Fields to include in the catalog category response
            filter: (Optional) Filter criteria for category selection
            page_cursor: (Optional) Pagination cursor for iterating through result pages
            sort: (Optional) Sorting criteria for the returned categories
        
        Returns:
            Dictionary containing the catalog item categories data and response metadata
        
        Raises:
            ValueError: When the required 'id' parameter is not provided
            requests.HTTPError: If the API request fails (e.g., invalid ID or server error)
        
        Tags:
            retrieve, catalog-item, categories, pagination, api-endpoint, filtering, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/categories/"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_category_relationships_items(self, id, page_cursor=None) -> dict[str, Any]:
        """
        Fetches catalog category related items through paginated API request.
        
        Args:
            id: Unique identifier of the catalog category (required)
            page_cursor: Pagination cursor for retrieving subsequent result pages (optional, defaults to None)
        
        Returns:
            Dictionary containing paginated API response data with catalog items
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes)
        
        Tags:
            fetch, catalog, pagination, api, relationships, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items/"
        query_params = {k: v for k, v in [('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_category_relationships_items(self, id, data) -> Any:
        """
        Creates a relationship between a catalog category and items.
        
        Args:
            id: The ID of the catalog category.
            data: Data required to establish the relationship.
        
        Returns:
            JSON response from the API after creating the relationship.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' is missing.
            HTTPError: Raised if the API request fails.
        
        Tags:
            create, relationship, management, catalog, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_category_relationships_items(self, id, data) -> Any:
        """
        Updates item relationships for a specific catalog category by sending a PATCH request to the API endpoint.
        
        Args:
            id: Unique identifier of the catalog category whose item relationships will be updated
            data: Dictionary containing updated relationship data to be sent in the request body
        
        Returns:
            Parsed JSON response from the API containing updated relationship information
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameters are missing
            HTTPError: Raised if the API request fails (handled via response.raise_for_status())
        
        Tags:
            update, catalog-category, relationships, api-patch, important, data-management
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_category_relationships_items(self, id, data) -> Any:
        """
        Delete items related to a catalog category by ID and relationship data.
        
        Args:
            id: Identifier of the catalog category whose relationships will be modified (required).
            data: Payload data specifying the items to be removed from the category relationships (required).
        
        Returns:
            Parsed JSON response from the API containing deletion results.
        
        Raises:
            ValueError: Raised if `id` or `data` parameters are None.
            HTTPError: Raised if the API request fails (handled by response.raise_for_status()).
        
        Tags:
            delete, catalog, relationships, items, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item_relationships_categories(self, id, page_cursor=None) -> dict[str, Any]:
        """
        Fetches the relationship categories for a catalog item using its ID.
        
        Args:
            id: The ID of the catalog item.
            page_cursor: Optional page cursor for pagination.
        
        Returns:
            A dictionary containing the relationship categories for the catalog item.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
            HTTPError: Raised if the HTTP request was unsuccessful.
        
        Tags:
            fetch, catalog, item-relationships, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories/"
        query_params = {k: v for k, v in [('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_item_relationships_categories(self, id, data) -> Any:
        """
        Creates relationships between a catalog item and categories by sending a POST request to the API.
        
        Args:
            id: The unique identifier of the catalog item.
            data: The data to be sent in the request body.
        
        Returns:
            The JSON response from the API after establishing the relationships.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is missing.
        
        Tags:
            create, relationship, api-call, catalog-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_item_relationships_categories(self, id, data) -> Any:
        """
        Updates the categories relationship for a specified catalog item.
        
        Args:
            id: The unique identifier of the catalog item to update.
            data: The data to update in the categories relationship.
        
        Returns:
            A JSON response containing the updated categories relationship data.
        
        Raises:
            ValueError: Raised if either the 'id' or 'data' parameter is missing.
        
        Tags:
            update, catalog-item, categories, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_item_relationships_categories(self, id, data) -> Any:
        """
        Deletes category relationships for a catalog item by ID with specified data.
        
        Args:
            id: ID of the catalog item whose category relationships will be deleted
            data: Data payload containing the category relationship information to delete
        
        Returns:
            JSON response from the API containing the deletion result
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameter is missing
            HTTPError: Raised when the API request fails (e.g., 4XX/5XX status code)
        
        Tags:
            delete, catalog-items, categories, relationships, async, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupons(self, fields_coupon=None, page_cursor=None) -> dict[str, Any]:
        """
        Fetches coupons from the API with optional filtering by fields and pagination.
        
        Args:
            fields_coupon: A list of fields to include in the coupon response
            page_cursor: A cursor for pagination of the results
        
        Returns:
            A dictionary containing the API response with coupons and related metadata
        
        Raises:
            requests.RequestException: When an HTTP request exception occurs, such as network issues or server errors
        
        Tags:
            fetch, coupons, api, important
        """
        url = f"{self.base_url}/api/coupons/"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon(self, data) -> dict[str, Any]:
        """
        Creates a new coupon using the provided data.
        
        Args:
            data: The data required to create a coupon. Must not be None.
        
        Returns:
            A dictionary containing the newly created coupon's details.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing.
        
        Tags:
            create, coupon, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon(self, id, fields_coupon=None) -> dict[str, Any]:
        """
        Retrieves a specific coupon's details from the API using the provided identifier.
        
        Args:
            id: The unique identifier of the coupon to retrieve.
            fields_coupon: Optional string specifying which coupon fields to include in the response.
        
        Returns:
            Dictionary containing the coupon's data as returned by the API.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
            requests.HTTPError: Raised if the API request fails (e.g., 404 Not Found or 500 Internal Error).
        
        Tags:
            retrieve, coupon, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon(self, id, data) -> dict[str, Any]:
        """
        Updates an existing coupon's data by sending a PATCH request to the API endpoint.
        
        Args:
            id: Unique identifier for the coupon to update (str or int).
            data: Dictionary containing key-value pairs to update for the coupon (dict[str, Any]).
        
        Returns:
            Dictionary containing the updated coupon data from the API response (dict[str, Any]).
        
        Raises:
            ValueError: When either 'id' or 'data' parameter is None.
            HTTPError: If the API request fails (e.g., 4XX client error or 5XX server error).
        
        Tags:
            update, coupon, management, api, patch, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon(self, id) -> Any:
        """
        Deletes a coupon from the server using its unique identifier.
        
        Args:
            id: The unique identifier of the coupon to delete. Must not be None.
        
        Returns:
            Parsed JSON response from the server containing deletion confirmation or coupon details.
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided (None).
            HTTPError: Raised if the API request fails (e.g., invalid permissions, non-existent coupon, or server error).
        
        Tags:
            delete, coupon, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes(self, fields_coupon_code=None, fields_coupon=None, filter=None, include=None, page_cursor=None) -> dict[str, Any]:
        """
        Fetches coupon codes from an API with optional filtering and pagination.
        
        Args:
            fields_coupon_code: Fields to include in the coupon code response.
            fields_coupon: Fields to include in the coupon response.
            filter: Filters to apply to the coupon code query.
            include: Fields to include as related resources.
            page_cursor: Cursor to paginate the results.
        
        Returns:
            A dictionary containing the response data from the API.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            fetch, coupon, api-call, important
        """
        url = f"{self.base_url}/api/coupon-codes/"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('fields[coupon]', fields_coupon), ('filter', filter), ('include', include), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon_code(self, data) -> dict[str, Any]:
        """
        Creates a new coupon code by posting data to the coupon codes API endpoint.
        
        Args:
            data: A dictionary containing the data required for creating the coupon code.
        
        Returns:
            A dictionary containing details about the newly created coupon code.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing.
        
        Tags:
            create, coupon-code, api-post, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code(self, id, fields_coupon_code=None, fields_coupon=None, include=None) -> dict[str, Any]:
        """
        Fetches a coupon code from the API by its ID, with optional fields and includes.
        
        Args:
            id: The unique identifier of the coupon code.
            fields_coupon_code: Optional fields to include for the coupon-code.
            fields_coupon: Optional fields to include for the coupon.
            include: Optional related records to include with the response.
        
        Returns:
            A dictionary containing the response from the API.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            fetch, coupon-management, api-call, optional-params, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('fields[coupon]', fields_coupon), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon_code(self, id, data) -> dict[str, Any]:
        """
        Updates a coupon code by sending a PATCH request with provided data to the coupon code API endpoint.
        
        Args:
            id: Unique identifier of the coupon code to update.
            data: Dictionary of data to update the coupon code with.
        
        Returns:
            A dictionary containing the updated coupon code details.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is missing.
        
        Tags:
            update, coupon, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon_code(self, id) -> Any:
        """
        Delete a coupon code by ID using the API endpoint.
        
        Args:
            id: Unique identifier of the coupon code to delete (required).
        
        Returns:
            JSON response data from the API after successful deletion.
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided.
            requests.HTTPError: Raised if the API request fails (e.g., invalid ID or server error).
        
        Tags:
            delete, coupon-code, management, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code_bulk_create_jobs(self, fields_coupon_code_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Fetches bulk coupon code creation jobs with optional filtering and pagination.
        
        Args:
            fields_coupon_code_bulk_create_job: Fields to include for coupon code bulk create job resource
            filter: Criteria to filter bulk coupon creation jobs
            page_cursor: Pagination cursor to retrieve specific results page
        
        Returns:
            Dictionary containing paginated results of coupon code bulk creation jobs
        
        Raises:
            Exception: When HTTP request fails or server returns error status
        
        Tags:
            list, fetch, async_job, coupon, management, important
        """
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs/"
        query_params = {k: v for k, v in [('fields[coupon-code-bulk-create-job]', fields_coupon_code_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_coupon_code_bulk_create_job(self, data) -> dict[str, Any]:
        """
        Initiates a bulk creation job for coupon codes using provided data.
        
        Args:
            data: Dictionary containing coupon code batch creation parameters (required). None will raise ValueError.
        
        Returns:
            Dictionary containing the API response with job details (typically includes job ID and status).
        
        Raises:
            ValueError: Raised when 'data' parameter is None.
            HTTPError: Raised for failed API requests (status code >= 400).
        
        Tags:
            coupon-code, bulk-create, async-job, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code_bulk_create_job(self, job_id, fields_coupon_code_bulk_create_job=None, fields_coupon_code=None, include=None) -> dict[str, Any]:
        """
        Retrieves a bulk coupon code creation job by job ID.
        
        Args:
            job_id: The ID of the bulk coupon code creation job.
            fields_coupon_code_bulk_create_job: Optional fields to include in the job details.
            fields_coupon_code: Optional fields to include for each coupon code.
            include: Optional relationships to include in the response.
        
        Returns:
            A dictionary containing details of the bulk coupon code creation job.
        
        Raises:
            ValueError: Raised if the job ID is missing.
            HTTPError: Raised if the HTTP request fails (e.g., if the API endpoint returns an error).
        
        Tags:
            get, coupon-code, bulk, job, management, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[coupon-code-bulk-create-job]', fields_coupon_code_bulk_create_job), ('fields[coupon-code]', fields_coupon_code), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_for_coupon_code(self, id, fields_coupon=None) -> dict[str, Any]:
        """
        Retrieve coupon details associated with a specific coupon code ID.
        
        Args:
            id: The unique identifier of the coupon code to fetch the associated coupon.
            fields_coupon: Optional filters specifying which coupon fields to include in the response.
        
        Returns:
            A dictionary containing the coupon details retrieved from the API.
        
        Raises:
            ValueError: Raised when the required parameter 'id' is not provided.
            requests.exceptions.HTTPError: Raised when the API request fails (e.g., invalid ID or server error).
        
        Tags:
            fetch, coupon, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/coupon/"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_relationships_coupon_codes(self, id) -> dict[str, Any]:
        """
        Fetches the coupon relationship data associated with a specific coupon code ID by making a GET request to the API endpoint.
        
        Args:
            id: The unique identifier of the coupon code for which to retrieve relationship data (required).
        
        Returns:
            A dictionary containing the coupon relationship data from the API response.
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided.
            HTTPError: Raised when the API request fails (e.g., invalid ID or network error).
        
        Tags:
            fetch, coupon-codes, api, relationships, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/relationships/coupon/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes_for_coupon(self, id, fields_coupon_code=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Fetches coupon codes for a specific coupon identified by ID.
        
        Args:
            id: Required unique identifier of the coupon.
            fields_coupon_code: Optional fields to include in the coupon code response.
            filter: Optional filter criteria for the coupon codes.
            page_cursor: Optional cursor for pagination.
        
        Returns:
            A dictionary containing coupon codes for the specified coupon.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
            HTTPError: Raised if the HTTP request fails.
        
        Tags:
            fetch, coupon, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/coupon-codes/"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code_relationships_coupon(self, id, page_cursor=None) -> dict[str, Any]:
        """
        Retrieves the relationships between a coupon and its codes.
        
        Args:
            id: The ID of the coupon.
            page_cursor: Optional cursor for pagination.
        
        Returns:
            A dictionary containing the relationship data.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
        
        Tags:
            retrieve, coupon, relationship, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/relationships/coupon-codes/"
        query_params = {k: v for k, v in [('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_profile_deletion(self, data) -> Any:
        """
        Initiates a profile deletion request by posting data to a privacy deletion endpoint.
        
        Args:
            data: Payload containing necessary information for processing the deletion request, must not be None.
        
        Returns:
            Parsed JSON response from the server containing deletion job details.
        
        Raises:
            ValueError: When 'data' parameter is None, indicating missing required payload.
            HTTPError: When the API request fails, typically due to invalid parameters or server issues.
        
        Tags:
            request, privacy, deletion, async_job, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/data-privacy-deletion-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events(self, fields_event=None, fields_metric=None, fields_profile=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves events data from the API with customizable field selection and filtering.
        
        Args:
            fields_event: Fields to include for events.
            fields_metric: Fields to include for metrics.
            fields_profile: Fields to include for profiles.
            filter: Filter criteria for event selection.
            include: Additional data to include in the response.
            page_cursor: Cursor for pagination.
            sort: Sorting criteria for the returned events.
        
        Returns:
            A dictionary containing the event data.
        
        Raises:
            HTTPError: Raised if there is an HTTP request error or if the response status code indicates failure.
        
        Tags:
            fetch, events, api, important
        """
        url = f"{self.base_url}/api/events/"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[metric]', fields_metric), ('fields[profile]', fields_profile), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_event(self, data) -> Any:
        """
        Creates a new event by sending a POST request with the provided data to the events API.
        
        Args:
            data: The data required to create the event. It must be provided to avoid raising a ValueError.
        
        Returns:
            The JSON response from the server after successfully creating the event.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing or None.
        
        Tags:
            create, event, api-call, data-management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/events/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(self, id, fields_event=None, fields_metric=None, fields_profile=None, include=None) -> dict[str, Any]:
        """
        Retrieves event data from an API using the provided ID and optional field selectors.
        
        Args:
            id: The ID of the event to retrieve.
            fields_event: Optional list of fields to include in the event data.
            fields_metric: Optional list of fields to include in the metric data.
            fields_profile: Optional list of fields to include in the profile data.
            include: Optional parameters to include in the response.
        
        Returns:
            A dictionary containing the event data as JSON.
        
        Raises:
            ValueError: Raised when the 'id' parameter is None.
        
        Tags:
            fetch, event, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[metric]', fields_metric), ('fields[profile]', fields_profile), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_events(self, data) -> Any:
        """
        Creates multiple events in bulk using a POST request to the event-bulk-create-jobs API endpoint.
        
        Args:
            data: The list of event data to be created in bulk; cannot be None.
        
        Returns:
            A JSON response generated by the API upon successful creation.
        
        Raises:
            ValueError: Raised if the required 'data' parameter is missing.
        
        Tags:
            bulk, create, events, async_job, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/event-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_metric(self, id, fields_metric=None) -> dict[str, Any]:
        """
        Retrieve detailed metric data for a specific event by ID.
        
        Args:
            id: Unique identifier of the event to fetch metrics for
            fields_metric: (Optional) Comma-separated fields to include in the metric response
        
        Returns:
            Dictionary containing the requested event metric data
        
        Raises:
            ValueError: Raised when the required 'id' parameter is not provided
            requests.HTTPError: Raised for HTTP request failures (e.g., 404 Not Found)
        
        Tags:
            get, metrics, event, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/metric/"
        query_params = {k: v for k, v in [('fields[metric]', fields_metric)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_profile(self, id, additional_fields_profile=None, fields_profile=None) -> dict[str, Any]:
        """
        Retrieves an event profile by ID, including optional additional or specific fields.
        
        Args:
            id: Required event ID to fetch the profile.
            additional_fields_profile: Optional parameter to specify additional fields for the event profile.
            fields_profile: Optional parameter to specify specific fields for the event profile.
        
        Returns:
            A dictionary containing the event profile data (key-value pairs).
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing (None).
        
        Tags:
            fetch, profile, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/profile/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_relationships_metric(self, id) -> dict[str, Any]:
        """
        Fetches event relationships metric data from the API.
        
        Args:
            id: The event identifier required to retrieve the metric data.
        
        Returns:
            A dictionary containing the event relationships metric data.
        
        Raises:
            ValueError: Raised if the `id` parameter is missing.
        
        Tags:
            search, metric, event, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/metric/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_relationships_profile(self, id) -> dict[str, Any]:
        """
        Fetches and returns the event relationships profile data for the specified event ID.
        
        Args:
            id: The unique identifier of the event for which to retrieve relationships profile data.
        
        Returns:
            A dictionary containing the relationships profile data.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, profile, relationship, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/profile/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows(self, fields_flow_action=None, fields_flow=None, fields_tag=None, filter=None, include=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves flow data with optional filtering, pagination, and field selection from the API.
        
        Args:
            fields_flow_action: Comma-separated fields to include for flow-action items (None returns all fields)
            fields_flow: Comma-separated fields to include for flow items (None returns all fields)
            fields_tag: Comma-separated fields to include for tag items (None returns all fields)
            filter: Filter criteria string to match flows against
            include: Related resources to include in the response
            page_cursor: Pagination cursor for paginated results
            page_size: Maximum number of results per page
            sort: Sorting criteria for results
        
        Returns:
            Dictionary containing API response data (parsed JSON) with flow entries and metadata
        
        Raises:
            requests.exceptions.HTTPError: Raised for non-2xx HTTP responses from the API endpoint
        
        Tags:
            api, retrieve, pagination, filtering, flows, important
        """
        url = f"{self.base_url}/api/flows/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow]', fields_flow), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow(self, id, fields_flow_action=None, fields_flow=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
        Fetches flow data from the API for a given flow ID with optional fields for customization.
        
        Args:
            id: The unique identifier of the flow to retrieve.
            fields_flow_action: Optional list of fields related to flow actions to include.
            fields_flow: Optional list of fields related to flows to include.
            fields_tag: Optional list of fields related to tags to include.
            include: Optional parameter for additional data inclusion.
        
        Returns:
            A dictionary containing flow data with specified fields.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            retrieve, data-fetch, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow]', fields_flow), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_flow(self, id, data) -> dict[str, Any]:
        """
        Updates a flow by sending a PATCH request with the provided data to the specified flow ID.
        
        Args:
            id: The ID of the flow to be updated.
            data: The data to be used for updating the flow.
        
        Returns:
            A dictionary containing the updated flow data.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' is None, indicating missing required parameters.
        
        Tags:
            update, patch, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flows/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_flow(self, id) -> Any:
        """
        Deletes a flow by its ID from the API endpoint.
        
        Args:
            id: The unique identifier of the flow to be deleted.
        
        Returns:
            The JSON response from the server after the deletion
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing
        
        Tags:
            delete, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action(self, id, fields_flow_action=None, fields_flow_message=None, fields_flow=None, include=None) -> dict[str, Any]:
        """
        Retrieves a flow action's details by ID, with optional field filtering and related resource inclusion.
        
        Args:
            id: The unique identifier of the flow action to retrieve.
            fields_flow_action: (Optional) Specific fields to include from the flow-action resource.
            fields_flow_message: (Optional) Specific fields to include from the flow-message resource in the response.
            fields_flow: (Optional) Specific fields to include from the flow resource in the response.
            include: (Optional) Related resources to include in the response.
        
        Returns:
            A dictionary containing the flow action's details and any requested related resources.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is not provided.
            requests.exceptions.HTTPError: Raised when the API request fails (e.g., invalid ID or server error).
        
        Tags:
            retrieve, api, flow-action, details, inclusion, filter, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow-message]', fields_flow_message), ('fields[flow]', fields_flow), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message(self, id, fields_flow_action=None, fields_flow_message=None, fields_template=None, include=None) -> dict[str, Any]:
        """
        Retrieves a flow message by its ID, optionally filtering fields and including related data.
        
        Args:
            id: The identifier of the flow message to retrieve. Required.
            fields_flow_action: Optionally specifies fields related to flow actions.
            fields_flow_message: Optionally specifies fields related to flow messages.
            fields_template: Optionally specifies fields related to templates.
            include: Optionally includes additional related data in the response.
        
        Returns:
            A dictionary containing the flow message details.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing or None.
        
        Tags:
            fetch, message, api, flow-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow-message]', fields_flow_message), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_flow_actions(self, id, fields_flow_action=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieve flow actions for a specified flow via API, with optional filtering and pagination.
        
        Args:
            id: Unique identifier of the flow (required)
            fields_flow_action: Specific fields to include for the flow action
            filter: Criteria to filter the flow actions
            page_cursor: Pagination cursor for result set continuation
            page_size: Number of items to return per page
            sort: Ordering criteria for the results
        
        Returns:
            Dictionary containing the parsed JSON response with flow actions data
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            requests.exceptions.HTTPError: Raised for HTTP request failures
        
        Tags:
            retrieve, flow-actions, api, pagination, filtering, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/flow-actions/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_relationships_flow_actions(self, id, filter=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves relationships between flows and flow actions for a specified flow ID
        
        Args:
            id: Unique identifier of the flow
            filter: Optional filter parameter for narrowing down results
            page_size: Optional parameter for specifying the number of items per page
            sort: Optional parameter for specifying the sort order of the results
        
        Returns:
            A dictionary containing relationships between flows and flow actions
        
        Raises:
            ValueError: Raised if the 'id' parameter is None
        
        Tags:
            fetch, flow, relationships, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/flow-actions/"
        query_params = {k: v for k, v in [('filter', filter), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_relationships_tags(self, id) -> dict[str, Any]:
        """
        Retrieve tags associated with a specific flow's relationships by ID.
        
        Args:
            id: Unique identifier of the flow whose relationship tags to fetch.
        
        Returns:
            Dictionary containing tag data from the API response.
        
        Raises:
            ValueError: Raised when 'id' parameter is None.
            HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes).
        
        Tags:
            fetch, relationships, tags, api-client, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/tags/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_tags(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieves tags for a specific flow identified by its ID.
        
        Args:
            id: The unique identifier of the flow.
            fields_tag: Optional parameter to specify fields related to tags.
        
        Returns:
            A dictionary containing tags for the flow.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            fetch, metadata, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/tags/"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action_flow(self, id, fields_flow=None) -> dict[str, Any]:
        """
        Retrieves flow actions based on the provided ID and optional flow fields.
        
        Args:
            id: The unique ID of the flow action to retrieve.
            fields_flow: Optional list of flow fields to include in the response.
        
        Returns:
            A dictionary containing the flow action information.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            retrieve, flow-action, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow/"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action_relationships_flow(self, id) -> dict[str, Any]:
        """
        Retrieve relationships flow data for a specific flow action by ID from the API.
        
        Args:
            id: The unique identifier of the flow action for which to fetch relationship data
        
        Returns:
            A dictionary containing the flow relationships data from the API response
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided (None)
            requests.HTTPError: Raised when the API request fails (non-2XX status code)
        
        Tags:
            fetch, relationships, flow-action, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action_messages(self, id, fields_flow_message=None, filter=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves flow action messages associated with a given ID.
        
        Args:
            id: The unique identifier required to fetch flow action messages.
            fields_flow_message: Optional specification of fields to include in flow messages.
            filter: Optional filter criteria for flow messages.
            page_size: Optional number of flow messages to return per page.
            sort: Optional sorting criteria for flow messages.
        
        Returns:
            A dictionary containing flow action messages.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
        
        Tags:
            retrieve, important, management, flow-action
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow-messages/"
        query_params = {k: v for k, v in [('fields[flow-message]', fields_flow_message), ('filter', filter), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action_relationships_messages(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves flow action relationships messages from a specified ID with optional filtering, pagination, and sorting.
        
        Args:
            id: Required identifier for the flow action.
            filter: Optional filter for narrowing down the results.
            page_cursor: Optional cursor for pagination.
            page_size: Optional size of each page for pagination.
            sort: Optional parameter for sorting results.
        
        Returns:
            A dictionary containing flow action relationships messages.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            fetch, relationships, pagination, important, api-call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow-messages/"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message_action(self, id, fields_flow_action=None) -> dict[str, Any]:
        """
        Retrieves a specific flow message action from the API using its ID and optional field filtering.
        
        Args:
            id: Unique identifier of the flow message action to retrieve.
            fields_flow_action: Optional string specifying which fields to include in the flow-action resource response (comma-separated).
        
        Returns:
            A dictionary containing the flow message action details, parsed from the JSON response.
        
        Raises:
            ValueError: When the 'id' parameter is None or not provided.
            requests.HTTPError: When the HTTP request fails (e.g., 404 Not Found or 500 Internal Server Error).
        
        Tags:
            retrieve, api, flow-action, async_job, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/flow-action/"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message_relationships_action(self, id) -> dict[str, Any]:
        """
        Retrieve flow action relationships for a specified flow message ID by querying the API endpoint.
        
        Args:
            id: The unique identifier of the flow message for which to fetch relationships. Required.
        
        Returns:
            Dictionary containing relationship data for the flow action associated with the specified message ID.
        
        Raises:
            ValueError: Raised when 'id' parameter is None.
            requests.HTTPError: Raised if the API request fails (e.g., invalid ID or server error).
        
        Tags:
            fetch, relationships, flow-action, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/flow-action/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message_relationships_template(self, id) -> dict[str, Any]:
        """
        Retrieves the template relationships data for a specific flow message.
        
        Args:
            id: The unique identifier of the flow message (required)
        
        Returns:
            A dictionary containing the template relationships data from the API response
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided
            requests.HTTPError: Raised when the API request fails (handled via response.raise_for_status())
        
        Tags:
            retrieve, flow-messages, api, relationships, template, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/template/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message_template(self, id, fields_template=None) -> dict[str, Any]:
        """
        Retrieve a flow message template by ID, optionally specifying fields to include in the template.
        
        Args:
            id: The unique identifier of the flow message template to retrieve
            fields_template: (Optional) Comma-separated fields to include in the template response
        
        Returns:
            Dictionary containing the flow message template data
        
        Raises:
            ValueError: If the 'id' parameter is not provided
            requests.HTTPError: If the API request fails (e.g., 404 for invalid ID or 500 for server errors)
        
        Tags:
            retrieve, api, flow-messages, template, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/template/"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_forms(self, fields_form=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves forms from an API endpoint with optional filtering, pagination, and sorting.
        
        Args:
            fields_form: Optional parameter to filter forms based on specific fields.
            filter: Optional filter to apply when retrieving forms.
            page_cursor: Cursor for pagination to retrieve the next set of forms.
            page_size: Number of forms to retrieve per page.
            sort: Optional parameter to sort the retrieved forms.
        
        Returns:
            A dictionary containing the requested forms.
        
        Raises:
            HTTPError: Raised if the HTTP request to the API fails.
        
        Tags:
            list, forms, api_request, pagination, important
        """
        url = f"{self.base_url}/api/forms/"
        query_params = {k: v for k, v in [('fields[form]', fields_form), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form(self, id, fields_form_version=None, fields_form=None, include=None) -> dict[str, Any]:
        """
        Retrieves a form by its ID with optional parameters to specify form version, fields, and included data.
        
        Args:
            id: The ID of the form to retrieve.
            fields_form_version: The version of the form fields.
            fields_form: The specific fields of the form.
            include: Additional data to be included in the response.
        
        Returns:
            A dictionary containing the form data.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            retrieve, management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version), ('fields[form]', fields_form), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_version(self, id, fields_form_version=None) -> dict[str, Any]:
        """
        Retrieves a specific form version's details by ID from the API.
        
        Args:
            id: The unique identifier of the form version to fetch[1][2].
            fields_form_version: Optional comma-separated fields to include in the response (e.g., 'name,status'). Omit for all fields[1][2].
        
        Returns:
            A dictionary containing the form version's data as returned by the API[1][2].
        
        Raises:
            ValueError: If the 'id' parameter is None[1][2].
            requests.HTTPError: If the API request fails (e.g., authentication error, invalid ID, or server error)[1][2].
        
        Tags:
            get, form-version, api-call, retrieve, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_versions_for_form(self, id, fields_form_version=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves paginated form versions for a specified form ID with optional filtering, sorting, and field selection.
        
        Args:
            id: Unique identifier of the form whose versions are being retrieved
            fields_form_version: Comma-separated list of specific fields to include in each form version (optional)
            filter: Criteria to filter form versions (optional)
            page_cursor: Pagination cursor for fetching specific result pages (optional)
            page_size: Number of form versions to return per page (optional)
            sort: Sorting criteria for form versions (optional)
        
        Returns:
            Dictionary containing paginated form version data from the API response
        
        Raises:
            ValueError: When 'id' parameter is not provided
            requests.HTTPError: When API request fails (4xx/5xx status codes)
        
        Tags:
            get, list, form-versions, pagination, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/form-versions/"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_version_ids_for_form(self, id) -> dict[str, Any]:
        """
        Retrieves version IDs for a specific form identified by its ID.
        
        Args:
            id: The unique identifier of the form to fetch version IDs for.
        
        Returns:
            A dictionary mapping version IDs to their respective details.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, api-call, form-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/relationships/form-versions/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_id_for_form_version(self, id) -> dict[str, Any]:
        """
        Retrieves the form ID associated with a specific form version.
        
        Args:
            id: The ID of the form version to retrieve the form ID for.
        
        Returns:
            A dictionary containing the form ID for the specified form version.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, form, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/relationships/form/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_for_form_version(self, id, fields_form=None) -> dict[str, Any]:
        """
        Fetches a form for a specified form version.
        
        Args:
            id: Unique identifier of the form version.
            fields_form: Optional parameter to specify fields[form] in the query.
        
        Returns:
            A dictionary containing the form data.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, form, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/form/"
        query_params = {k: v for k, v in [('fields[form]', fields_form)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_images(self, fields_image=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieve a paginated list of images from the API endpoint with optional filtering, sorting, and field selection.
        
        Args:
            fields_image: Comma-separated fields to include in the 'image' resource response (None returns all fields)
            filter: Criteria to filter images (format depends on API implementation)
            page_cursor: Pagination cursor for retrieving specific page of results
            page_size: Maximum number of items to return per page
            sort: Field(s) and direction to sort results (format: 'field1,-field2')
        
        Returns:
            Dictionary containing parsed JSON response with image data and pagination information
        
        Raises:
            requests.HTTPError: When the API request fails (non-2xx status code)
        
        Tags:
            retrieve, list, pagination, api, images, important
        """
        url = f"{self.base_url}/api/images/"
        query_params = {k: v for k, v in [('fields[image]', fields_image), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image(self, id, fields_image=None) -> dict[str, Any]:
        """
        Retrieves an image by its ID from an API, allowing optional specification of image fields.
        
        Args:
            id: The unique identifier of the image to be retrieved.
            fields_image: Optional parameter to specify which fields of the image are returned.
        
        Returns:
            A dictionary containing the image data as per the specified fields.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            retrieve, api-call, image-fetching, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/images/{id}/"
        query_params = {k: v for k, v in [('fields[image]', fields_image)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image(self, id, data) -> dict[str, Any]:
        """
        Updates an image's data via a PATCH request to the API endpoint.
        
        Args:
            id: The unique identifier of the image to update.
            data: The updated image data to send in the request body.
        
        Returns:
            A dictionary containing the updated image details from the API response.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' parameters are None.
            requests.HTTPError: Raised if the API request fails (handled by response.raise_for_status()).
        
        Tags:
            update, patch, api, image, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/images/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_lists(self, fields_list=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a paginated collection of lists with optional filtering, sorting, and field selection.
        
        Args:
            fields_list: Optional comma-separated fields to include for list objects
            fields_tag: Optional comma-separated fields to include for tag objects
            filter: Optional filter criteria to apply to the list collection
            include: Optional related resources to include in the response
            page_cursor: Cursor token for paginating through large result sets
            sort: Optional sort order for the returned list collection
        
        Returns:
            Dictionary containing the API response with list collection data and pagination details
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails (non-2xx status code)
        
        Tags:
            list, pagination, api-client, filtering, sorting, important
        """
        url = f"{self.base_url}/api/lists/"
        query_params = {k: v for k, v in [('fields[list]', fields_list), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_list(self, data) -> dict[str, Any]:
        """
        Creates a list by sending a POST request to the API endpoint with the provided data.
        
        Args:
            data: (Any) Data to include in the list creation request. Must not be None.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API containing the created list details.
        
        Raises:
            ValueError: Raised if the 'data' parameter is None.
            HTTPError: Raised if the API request fails (HTTP status code 4XX/5XX).
        
        Tags:
            create, api, post, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list(self, id, additional_fields_list=None, fields_list=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
        Retrieves a specific list's details by ID from an API endpoint
        
        Args:
            id: Unique identifier of the list to retrieve (required)
            additional_fields_list: Optional additional fields to include for the list
            fields_list: Optional specific fields to return for the list
            fields_tag: Optional specific fields to return for associated tags
            include: Optional related resources to include in the response
        
        Returns:
            Dictionary containing the list details and requested fields from the API response
        
        Raises:
            ValueError: Raised when required parameter 'id' is None
            requests.exceptions.HTTPError: Raised for HTTP request failures (4XX/5XX status codes)
        
        Tags:
            list, retrieve, api, details, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/"
        query_params = {k: v for k, v in [('additional-fields[list]', additional_fields_list), ('fields[list]', fields_list), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_list(self, id, data) -> dict[str, Any]:
        """
        Updates a list by sending a PATCH request to the specified API endpoint.
        
        Args:
            id: The identifier of the list to update.
            data: The data to update in the list.
        
        Returns:
            A dictionary containing the updated list data.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is missing from the request.
        
        Tags:
            update, patch, api-call, list-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_list(self, id) -> Any:
        """
        Deletes a list by its ID and returns the response in JSON format.
        
        Args:
            id: The ID of the list to be deleted.
        
        Returns:
            The JSON response from the server after deleting the list.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            delete, list, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_relationships_tags(self, id) -> dict[str, Any]:
        """
        Retrieves tag relationships for a specified list ID by querying the API endpoint.
        
        Args:
            id: The unique identifier of the list for which to fetch relationships and tags (required).
        
        Returns:
            Parsed JSON response containing tag relationships data as a dictionary.
        
        Raises:
            ValueError: Raised if 'id' parameter is None or missing.
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., invalid ID or server error).
        
        Tags:
            retrieve, list, relationships, tags, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/tags/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_tags(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieve tags associated with a specific list by ID, with optional field filtering.
        
        Args:
            id: The unique identifier of the list whose tags to retrieve
            fields_tag: Optional comma-separated fields to include in the tag response (None returns all fields)
        
        Returns:
            Dictionary containing tag data from the API response
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            requests.HTTPError: Raised for 4XX/5XX status codes from the API
        
        Tags:
            list, retrieve, tags, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/tags/"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_relationships_profiles(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves the list of relationships between a specified list and profiles, optionally filtered, paginated, and sorted.
        
        Args:
            id: The ID of the list for which relationships are to be retrieved.
            filter: Optional filter to apply to the retrieved relationships.
            page_cursor: Optional cursor for pagination.
            page_size: Optional size of each page for pagination.
            sort: Optional criteria to sort the retrieved relationships.
        
        Returns:
            A dictionary containing the list of relationships and pagination information.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
        
        Tags:
            list, profiles, relationships, async, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles/"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_list_relationships(self, id, data) -> Any:
        """
        Creates relationships between a list and profiles by sending a POST request to the API endpoint.
        
        Args:
            id: The unique identifier of the list to which relationships will be added.
            data: The data containing profile relationship details to be associated with the list.
        
        Returns:
            A JSON-decoded response from the API containing the created relationships or operation results.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' parameter is not provided.
            requests.HTTPError: Raised if the API request fails (handled by response.raise_for_status()).
        
        Tags:
            create, relationships, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_list_relationships(self, id, data) -> Any:
        """
        Deletes relationships between a list and associated profiles based on the provided ID and data.
        
        Args:
            id: The ID of the list to delete relationships from.
            data: Data required for the deletion operation.
        
        Returns:
            The JSON response from the server after deletion.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is None, as both are required parameters.
        
        Tags:
            delete, list-management, relationship, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_profiles(self, id, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of profiles associated with a specified list id, including optional filtering and pagination.
        
        Args:
            id: Required identifier of the list to fetch profiles from.
            additional_fields_profile: Optional list of additional fields to include in the profile data.
            fields_profile: Optional list of fields to include in the profile data.
            filter: Optional filter criteria to apply to the profiles.
            page_cursor: Optional cursor to specify the starting point of the page.
            page_size: Optional number of items to return in each page.
            sort: Optional criteria to sort the profiles.
        
        Returns:
            A dictionary containing the response data from the API call.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing or None.
        
        Tags:
            retrieve, profiles, list, api_call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/profiles/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metrics(self, fields_metric=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
        Fetches metrics data from the API endpoint with optional filtering and pagination.
        
        Args:
            fields_metric: Optional string specifying fields to include for metrics. None returns default fields.
            filter: Optional filter string to constrain results. None applies no filters.
            page_cursor: Optional pagination cursor for API result pagination. None fetches the first page.
        
        Returns:
            Dictionary containing metrics data in the API response format.
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes).
        
        Tags:
            fetch, metrics, pagination, api, data-retrieval, important
        """
        url = f"{self.base_url}/api/metrics/"
        query_params = {k: v for k, v in [('fields[metric]', fields_metric), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric(self, id, fields_metric=None) -> dict[str, Any]:
        """
        Retrieve a specific metric's data by ID from the API endpoint.
        
        Args:
            id: The unique identifier of the metric to fetch (required).
            fields_metric: Optional fields to include in the metric response (str | None).
        
        Returns:
            Dictionary containing the metric data parsed from the JSON response.
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided.
            requests.HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes).
        
        Tags:
            retrieve, metric, api, get, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/"
        query_params = {k: v for k, v in [('fields[metric]', fields_metric)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_metric_aggregates(self, data) -> dict[str, Any]:
        """
        Query metric aggregates by sending provided data to the API endpoint and returning the parsed JSON response.
        
        Args:
            data: Required data payload containing metric parameters for the API request. Must not be None.
        
        Returns:
            dict[str, Any]: Parsed JSON response containing metric aggregation results from the API.
        
        Raises:
            ValueError: If input 'data' parameter is None, indicating missing required data.
            requests.HTTPError: If the HTTP POST request fails (non-2xx response code).
        
        Tags:
            query, metrics, aggregates, api, post, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/metric-aggregates/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles(self, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Fetches profiles from the API with optional filtering and pagination.
        
        Args:
            additional_fields_profile: Optional list of additional fields to include in the profile.
            fields_profile: Optional list of fields to include in the profile.
            filter: Optional filter criteria for selecting profiles.
            page_cursor: Optional cursor for pagination.
            page_size: Optional number of profiles to return per page.
            sort: Optional sorting criteria for profiles.
        
        Returns:
            A dictionary containing profiles based on the query parameters.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a network error or a non-200 status code.
        
        Tags:
            fetch, profiles, api, management, important
        """
        url = f"{self.base_url}/api/profiles/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_profile(self, data) -> dict[str, Any]:
        """
        Creates a new profile by sending a POST request to the API endpoint with the provided data.
        
        Args:
            data: Required parameter containing the profile data to be created. Must not be None.
        
        Returns:
            dict[str, Any]: A dictionary containing the created profile data from the API response.
        
        Raises:
            ValueError: Raised if the 'data' parameter is None.
            requests.HTTPError: Raised if the API request fails (e.g., 4xx/5xx status code).
        
        Tags:
            create, profile, api, post, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile(self, id, additional_fields_profile=None, fields_list=None, fields_profile=None, fields_segment=None, include=None) -> dict[str, Any]:
        """
        Retrieves a profile by ID with optional additional fields.
        
        Args:
            id: Required profile ID.
            additional_fields_profile: Optional additional fields to include in the profile.
            fields_list: Optional fields to include for lists.
            fields_profile: Optional fields to include from the profile.
            fields_segment: Optional fields to include from segments.
            include: Additional items to include in the response.
        
        Returns:
            A dictionary containing the profile information.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing.
        
        Tags:
            retrieve, profile, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[list]', fields_list), ('fields[profile]', fields_profile), ('fields[segment]', fields_segment), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_profile(self, id, data) -> dict[str, Any]:
        """
        Updates a user profile by sending a PATCH request with the provided data to the specified profile ID.
        
        Args:
            id: The ID of the profile to update.
            data: The data to be updated in the profile.
        
        Returns:
            A dictionary containing the updated profile details.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' is missing.
        
        Tags:
            update, profile, important, management
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_jobs(self, fields_profile_bulk_import_job=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of bulk profile import jobs with optional filtering, sorting, and pagination.
        
        Args:
            fields_profile_bulk_import_job: Optional list of fields to include in the response for each profile bulk import job.
            filter: Optional filter query to narrow down the results.
            page_cursor: Optional page cursor for pagination.
            page_size: Optional number of items per page.
            sort: Optional sort order for the results.
        
        Returns:
            A dictionary containing the paginated list of bulk profile import jobs.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters an error (non-successful status code).
        
        Tags:
            list, management, import, important
        """
        url = f"{self.base_url}/api/profile-bulk-import-jobs/"
        query_params = {k: v for k, v in [('fields[profile-bulk-import-job]', fields_profile_bulk_import_job), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def spawn_bulk_profile_import_job(self, data) -> dict[str, Any]:
        """
        Spawns a bulk profile import job by sending the provided data to the profile bulk import API endpoint.
        
        Args:
            data: The data to be used for the bulk import job.
        
        Returns:
            A dictionary containing the response data from the API endpoint.
        
        Raises:
            ValueError: Raised if the required 'data' parameter is missing.
        
        Tags:
            spawn, bulk, import, async_job, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-bulk-import-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job(self, job_id, fields_list=None, fields_profile_bulk_import_job=None, include=None) -> dict[str, Any]:
        """
        Retrieves details of a bulk profile import job by ID with optional field filtering.
        
        Args:
            job_id: (str) Required identifier for the bulk profile import job
            fields_list: (Optional[str]) Comma-separated fields to include for list-related data
            fields_profile_bulk_import_job: (Optional[str]) Comma-separated fields specific to the profile bulk import job resource
            include: (Optional[str]) Additional related resources to include in the response
        
        Returns:
            dict[str, Any]: JSON response containing job details and requested fields
        
        Raises:
            ValueError: When job_id parameter is not provided
            requests.exceptions.HTTPError: For HTTP request failures (4xx/5xx status codes)
        
        Tags:
            retrieve, profile-import, management, async-job, http-client, important
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{job_id}/"
        query_params = {k: v for k, v in [('fields[list]', fields_list), ('fields[profile-bulk-import-job]', fields_profile_bulk_import_job), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_profile(self, data) -> dict[str, Any]:
        """
        Creates or updates a user profile by sending data to a profile import API endpoint.
        
        Args:
            data: A dictionary containing profile data to be processed (required). None values will be removed from the request body.
        
        Returns:
            Dictionary containing the API response json with imported profile details
        
        Raises:
            ValueError: Raised when 'data' parameter is None
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes)
        
        Tags:
            profile-management, api-client, async_job, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-import/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def merge_profiles(self, data) -> dict[str, Any]:
        """
        Merges user profile data by sending a POST request to the profile-merge API endpoint.
        
        Args:
            data: Profile data to be merged. Must not be None.
        
        Returns:
            dict[str, Any]: Parsed JSON response containing merged profile data from the API.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None or missing.
            requests.exceptions.HTTPError: Raised when the API request fails, based on HTTP status code.
        
        Tags:
            merge, user-profiles, api, post, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-merge/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def suppress_profiles(self, data) -> Any:
        """
        Supresses profiles by creating a bulk job through a POST request.
        
        Args:
            data: The data required for the profile suppression operation.
        
        Returns:
            The JSON response from the server.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing or None.
        
        Tags:
            bulk, profiles, suppression, create, api, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unsuppress_profiles(self, data) -> Any:
        """
        Deletes suppressed profiles in bulk by issuing a POST request with the provided data.
        
        Args:
            data: A collection of data to unsuppress profiles; required parameter.
        
        Returns:
            The JSON response from the server after the bulk delete operation.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing (i.e., None).
        
        Tags:
            bulk-delete, profile-management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscribe_profiles(self, data) -> Any:
        """
        Initiates bulk profile subscription jobs by sending provided data to a specified API endpoint.
        
        Args:
            data: Required data payload for profile subscriptions, typically containing subscription details (dict/list). None values are automatically filtered from the request.
        
        Returns:
            Parsed JSON response containing details of the created bulk subscription job.
        
        Raises:
            ValueError: Raised when 'data' parameter is not provided.
            requests.HTTPError: Raised for HTTP request failures, propagated from the '_post' call.
        
        Tags:
            bulk-subscription, async-job, profile-management, api-call, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-create-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unsubscribe_profiles(self, data) -> Any:
        """
        Initiates a bulk unsubscribe job for profiles using provided data
        
        Args:
            data: Required payload containing profile identifiers for unsubscribing. Must not be None
        
        Returns:
            Parsed JSON response containing the created bulk unsubscribe job details
        
        Raises:
            ValueError: Raised when 'data' parameter is None, indicating missing required input
            requests.exceptions.HTTPError: Raised for HTTP request failures (4XX/5XX status codes)
        
        Tags:
            unsubscribe, batch, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-delete-jobs/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_push_token(self, data) -> Any:
        """
        Creates and registers a push token using the provided data.
        
        Args:
            data: Data required to create a push token.
        
        Returns:
            JSON response from the push token creation request.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing.
        
        Tags:
            create, register, push-token, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/push-tokens/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_lists(self, id, fields_list=None) -> dict[str, Any]:
        """
        Retrieve profile lists for a specified profile ID, with optional field filtering.
        
        Args:
            id: Profile ID to fetch associated lists (required)
            fields_list: Optional list of fields to include in the response. If None, returns all fields (default: None)
        
        Returns:
            Dictionary containing the profile lists data from the API response
        
        Raises:
            ValueError: Raised when 'id' parameter is not provided
            HTTPError: Raised when the HTTP request fails (e.g., invalid profile ID or server error)
        
        Tags:
            get, retrieve, profile, lists, api, http, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/lists/"
        query_params = {k: v for k, v in [('fields[list]', fields_list)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_relationships_lists(self, id) -> dict[str, Any]:
        """
        Fetches relationship lists for a profile based on the given ID.
        
        Args:
            id: The unique identifier of the profile.
        
        Returns:
            A dictionary containing relationship lists for the profile.
        
        Raises:
            ValueError: Raised if the 'id' parameter is missing or None.
        
        Tags:
            fetch, profile, relationship, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/lists/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_segments(self, id, fields_segment=None) -> dict[str, Any]:
        """
        Retrieve profile segments for a specified ID by making a GET request to the API endpoint.
        
        Args:
            id: The unique identifier of the profile to fetch segments for.
            fields_segment: (Optional) Comma-separated fields to include in the segment data. If not specified, all fields are returned by default.
        
        Returns:
            A dictionary containing the parsed JSON response from the API, representing the profile segments.
        
        Raises:
            ValueError: Raised when the required parameter 'id' is not provided.
            requests.exceptions.HTTPError: Raised when the API request returns a non-successful status code.
        
        Tags:
            retrieve, api, profile, segments, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/segments/"
        query_params = {k: v for k, v in [('fields[segment]', fields_segment)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_relationships_segments(self, id) -> dict[str, Any]:
        """
        Retrieve relationship segments for a profile ID from the API.
        
        Args:
            id: Profile identifier (cannot be None).
        
        Returns:
            Dictionary containing relationship segments data from the API response.
        
        Raises:
            ValueError: Raised when 'id' parameter is None.
            requests.exceptions.HTTPError: Raised if the API request fails (non-2xx status code).
        
        Tags:
            retrieve, api, profile, relationships, segments, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/segments/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job_lists(self, id, fields_list=None) -> dict[str, Any]:
        """
        Fetches a list of profiles for a bulk import job based on the provided ID and optional field specifications.
        
        Args:
            id: Required ID of the bulk import job.
            fields_list: Optional list of fields to include in the response.
        
        Returns:
            A dictionary containing the profile lists for the specified bulk import job.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is not provided.
        
        Tags:
            fetch, profiles, bulk-import, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/lists/"
        query_params = {k: v for k, v in [('fields[list]', fields_list)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job_relationships_lists(self, id) -> dict[str, Any]:
        """
        Retrieves relationship lists associated with a specific bulk profile import job by ID.
        
        Args:
            id: The unique identifier of the bulk profile import job (required)
        
        Returns:
            A dictionary containing the relationship lists data returned from the API
        
        Raises:
            ValueError: Raised when no ID is provided for the bulk profile import job
            HTTPError: Raised when the API request fails (e.g., invalid ID or network issues)
        
        Tags:
            retrieve, profile-import, relationships, lists, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/lists/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job_profiles(self, id, additional_fields_profile=None, fields_profile=None, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
        Retrieve profiles associated with a bulk import job by its ID, with optional pagination and field selection.
        
        Args:
            id: The unique identifier of the bulk import job.
            additional_fields_profile: Optional list of additional profile fields to include in the response.
            fields_profile: Optional list of profile fields to include in the response (exclusive selection).
            page_cursor: Optional pagination cursor for result navigation.
            page_size: Optional maximum number of profiles to return per page.
        
        Returns:
            Dictionary containing profile data and metadata from the API response.
        
        Raises:
            ValueError: When the 'id' parameter is not provided.
            requests.exceptions.HTTPError: When the API request fails (e.g., invalid ID or server error).
        
        Tags:
            retrieve, profiles, bulk-import, pagination, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/profiles/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job_relationships_profiles(self, id, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
        Retrieves the relationships between a bulk profile import job and its associated profiles.
        
        Args:
            id: The ID of the bulk profile import job.
            page_cursor: Optional page cursor for pagination.
            page_size: Optional number of profiles to include per page.
        
        Returns:
            A dictionary containing the relationships data.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            fetch, import, job, profile, bulk, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/profiles/"
        query_params = {k: v for k, v in [('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_profile_import_job_import_errors(self, id, fields_import_error=None, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
        Retrieves import errors for a bulk profile import job by ID, optionally filtering by specific import error fields and paginating the results.
        
        Args:
            id: The ID of the bulk profile import job.
            fields_import_error: Optional fields to filter import errors by specific import error.
            page_cursor: Optional cursor for pagination.
            page_size: Optional size for pagination.
        
        Returns:
            A dictionary containing import error details for the specified job.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
        
        Tags:
            list, error, profile, import, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/import-errors/"
        query_params = {k: v for k, v in [('fields[import-error]', fields_import_error), ('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_campaign_values(self, data, page_cursor=None) -> dict[str, Any]:
        """
        Queries campaign values based on provided data and returns the response as a dictionary.
        
        Args:
            data: Required data to be queried for campaign values.
            page_cursor: Optional cursor for pagination; defaults to None.
        
        Returns:
            A dictionary containing campaign value reports.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing.
        
        Tags:
            query, campaign, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-values-reports/"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_values(self, data, page_cursor=None) -> dict[str, Any]:
        """
        Queries flow values reports by sending a POST request with provided data and optional page cursor.
        
        Args:
            data: Required data payload for the request
            page_cursor: Optional page cursor for pagination
        
        Returns:
            A dictionary of query results
        
        Raises:
            ValueError: Raised if the required 'data' parameter is missing
        
        Tags:
            query, api, pagination, important, batch, report
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-values-reports/"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_series(self, data, page_cursor=None) -> dict[str, Any]:
        """
        Queries the flow series reports by posting the provided data and handling pagination.
        
        Args:
            data: The required data to be posted to the API.
            page_cursor: Optional cursor for pagination; if provided, it facilitates fetching subsequent pages of results.
        
        Returns:
            A dictionary containing the response from the flow series reports API.
        
        Raises:
            ValueError: Raised when the 'data' argument is missing.
        
        Tags:
            query, reports, api, async_job, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-series-reports/"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segments(self, fields_segment=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieves segment data from a specified API endpoint.
        
        Args:
            fields_segment: Optional fields to include in the segment data.
            fields_tag: Optional fields to include in the tag data.
            filter: Optional filter criteria for segment data.
            include: Optional data to include in the response.
            page_cursor: Optional cursor for pagination.
            sort: Optional sort criteria for the response.
        
        Returns:
            Dictionary containing segment data.
        
        Raises:
            requests.HTTPError: If the HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, api_call, data_retrieval, important
        """
        url = f"{self.base_url}/api/segments/"
        query_params = {k: v for k, v in [('fields[segment]', fields_segment), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_segment(self, data) -> dict[str, Any]:
        """
        Creates a new segment by sending a POST request with the provided data.
        
        Args:
            data: Data payload required for segment creation. Must not be None.
        
        Returns:
            Parsed JSON response from the API as a dictionary.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
            HTTPError: Raised for bad requests (4XX) or server errors (5XX) from the API.
        
        Tags:
            create, segment, post, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment(self, id, additional_fields_segment=None, fields_segment=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
        Retrieves a specific segment's data from an API endpoint with customizable field selection.
        
        Args:
            id: The unique identifier of the segment to retrieve (required)
            additional_fields_segment: Optional additional fields to include for the segment
            fields_segment: Field inclusion filters for the segment
            fields_tag: Field inclusion filters for associated tags
            include: Related resources to include in the response
        
        Returns:
            Dictionary containing the segment data as returned by the API
        
        Raises:
            ValueError: When required parameter 'id' is not provided
            HTTPError: When API request fails (e.g., 4XX/5XX status code)
        
        Tags:
            retrieve, api, segment, data-fetch, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/"
        query_params = {k: v for k, v in [('additional-fields[segment]', additional_fields_segment), ('fields[segment]', fields_segment), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_segment(self, id, data) -> dict[str, Any]:
        """
        Updates a segment's data via a PATCH request to the API endpoint.
        
        Args:
            id: Unique identifier of the segment to update (required)
            data: Dictionary containing updated segment properties (required)
        
        Returns:
            Dictionary containing the API response data after successful update
        
        Raises:
            ValueError: When 'id' or 'data' parameter is None
            requests.HTTPError: When the API returns a failed HTTP status code
        
        Tags:
            update, segment, async_job, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_segment(self, id) -> Any:
        """
        Deletes a segment by its ID and returns the JSON response.
        
        Args:
            id: The ID of the segment to be deleted.
        
        Returns:
            The JSON response from the delete operation.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing or None.
        
        Tags:
            delete, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_relationships_tags(self, id) -> dict[str, Any]:
        """
        Retrieve tag relationships for a specific segment from the API.
        
        Args:
            id: The unique identifier of the segment for which to retrieve tag relationships. Must not be None.
        
        Returns:
            A dictionary containing the tag relationships associated with the specified segment, parsed from the API response.
        
        Raises:
            ValueError: Raised when 'id' is None.
            HTTPError: Raised when the API request fails (e.g., 4xx/5xx status codes).
        
        Tags:
            retrieve, relationships, tags, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/tags/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_tags(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieve tags for a specific segment by ID, with optional field filtering for tag data
        
        Args:
            id: Unique identifier of the segment to fetch tags for
            fields_tag: Optional comma-separated fields to include in the tag response data (None returns all fields)
        
        Returns:
            Dictionary containing the retrieved tag data from the API response
        
        Raises:
            ValueError: When no ID is provided for the segment
            requests.HTTPError: When the API request fails (from response.raise_for_status())
        
        Tags:
            retrieve, segment-tags, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/tags/"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_relationships_profiles(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieve relationship profiles associated with a specific segment using pagination and filtering.
        
        Args:
            id: Unique identifier of the segment to query (required)
            filter: Optional filtering criteria for the relationship profiles (default: None)
            page_cursor: Pagination cursor from the previous response (default: None)
            page_size: Number of items per page (default: None)
            sort: Sorting criteria for the results (default: None)
        
        Returns:
            Dictionary containing the paginated relationship profile data from the API response
        
        Raises:
            ValueError: Raised when the 'id' parameter is not provided
            requests.HTTPError: Raised when the API request fails (e.g., invalid ID or server error)
        
        Tags:
            retrieve, profiles, segments, pagination, async_job, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/profiles/"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_profiles(self, id, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
        Retrieves segment profiles from the specified API endpoint based on the provided ID and optional query parameters.
        
        Args:
            id: Required ID of the segment.
            additional_fields_profile: Additional fields to include in the profile. Optional.
            fields_profile: Specific fields to retrieve in the profile. Optional.
            filter: Filter criteria for the profiles. Optional.
            page_cursor: Cursor for pagination. Optional.
            page_size: Number of items to include per page. Optional.
            sort: Sorting criteria for the profiles. Optional.
        
        Returns:
            A dictionary containing the retrieved segment profiles.
        
        Raises:
            ValueError: Raised if the required 'id' parameter is missing.
        
        Tags:
            fetch, profiles, id-based, important, api
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/profiles/"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags(self, fields_tag_group=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Fetches a list of tags from the API with optional filtering and sorting.
        
        Args:
            fields_tag_group: Tag group fields to include in the response.
            fields_tag: Specific tag fields to include in the response.
            filter: Filter criteria for selecting tags.
            include: Related resources to include in the response.
            page_cursor: Pagination cursor for fetching the next page of results.
            sort: Sorting criteria for the tags.
        
        Returns:
            A dictionary containing the tags data.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters a status error.
        
        Tags:
            fetch, tags, api, management, important
        """
        url = f"{self.base_url}/api/tags/"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag(self, data) -> dict[str, Any]:
        """
        Creates a new tag by sending a POST request to the tag API endpoint with the provided data.
        
        Args:
            data: Required dictionary containing data for the new tag; cannot be None.
        
        Returns:
            A dictionary containing the response from the server after creating a new tag.
        
        Raises:
            ValueError: Raised when the 'data' parameter is missing or None.
        
        Tags:
            create, tag, important, management
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag(self, id, fields_tag_group=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
        Retrieves a tag by its ID, optionally including additional fields and related data.
        
        Args:
            id: The unique identifier of the tag to retrieve.
            fields_tag_group: Optional filter to include specific fields related to the tag group.
            fields_tag: Optional filter to include specific fields related to the tag itself.
            include: Optional parameter for including additional related data.
        
        Returns:
            A dictionary containing the retrieved tag and any specified fields or included data.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, tag-retrieval, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag(self, id, data) -> Any:
        """
        Updates a tag's data using a PATCH request to the API endpoint.
        
        Args:
            id: The unique identifier of the tag to update (required).
            data: The new data to update the tag with (required).
        
        Returns:
            The JSON response containing updated tag details from the API call.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' parameter is None.
            HTTPError: Raised if the API request fails (handled via response.raise_for_status()).
        
        Tags:
            update, patch, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag(self, id) -> Any:
        """
        Deletes a tag specified by its ID from the API.
        
        Args:
            id: The unique identifier of the tag to delete.
        
        Returns:
            The JSON response from the API after deleting the tag.
        
        Raises:
            ValueError: Raised when the 'id' parameter is None.
        
        Tags:
            delete, tags, api-management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_groups(self, fields_tag_group=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieve paginated tag groups from the API with optional filtering, sorting, and field selection.
        
        Args:
            fields_tag_group: Comma-separated fields to include for tag-group resources (default: None).
            filter: Filter criteria to apply to tag groups (default: None).
            page_cursor: Pagination cursor for offset-based navigation (default: None).
            sort: Sorting criteria for results (default: None).
        
        Returns:
            Dictionary containing API response data including tag groups and pagination metadata.
        
        Raises:
            HTTPError: If the API request fails (non-2xx status code).
        
        Tags:
            list, pagination, api-client, management, important
        """
        url = f"{self.base_url}/api/tag-groups/"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_group(self, data) -> dict[str, Any]:
        """
        Creates a new tag group by sending the provided payload to the API endpoint.
        
        Args:
            data: Payload containing tag group details. Must not be None.
        
        Returns:
            Dictionary containing the created tag group's data from the API response.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
            requests.HTTPError: Raised if the API request fails (4XX/5XX status code).
        
        Tags:
            create, tag-group, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
        Fetches details of a tag group from the API by its ID.
        
        Args:
            id: The unique identifier of the tag group to retrieve.
            fields_tag_group: (Optional) A comma-separated string of fields to include in the response for the tag group.
        
        Returns:
            A dictionary containing the tag group data, structured according to the API response.
        
        Raises:
            ValueError: Raised when the 'id' parameter is None.
            HTTPError: Raised when the API request fails, typically due to invalid ID or network issues.
        
        Tags:
            fetch, api, tag-group, details, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag_group(self, id, data) -> dict[str, Any]:
        """
        Updates a tag group by ID using the provided data via a PATCH request.
        
        Args:
            id: The unique identifier of the tag group to update (required)
            data: Dictionary containing the fields and values to update (required)
        
        Returns:
            Dictionary containing the updated tag group data from the API response
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameters are None
            requests.HTTPError: Raised when the API request fails (handled by response.raise_for_status())
        
        Tags:
            update, tag-group, patch, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_group(self, id) -> dict[str, Any]:
        """
        Deletes a tag group with the specified ID using an HTTP DELETE request and returns the JSON response.
        
        Args:
            id: The unique identifier of the tag group to delete. Must be provided; cannot be None.
        
        Returns:
            A dictionary containing the JSON response body from the API.
        
        Raises:
            ValueError: Raised when the 'id' parameter is None.
            HTTPError: Raised for unsuccessful HTTP responses (non-2xx status codes).
        
        Tags:
            delete, async-job, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_relationships_flows(self, id) -> dict[str, Any]:
        """
        Fetch tag-flow relationships by tag ID from the API.
        
        Args:
            id: The unique identifier of the tag whose flow relationships are being retrieved
        
        Returns:
            Dictionary containing API response data with tag-flow relationships
        
        Raises:
            ValueError: Raised when 'id' parameter is None
            requests.exceptions.HTTPError: Raised for failed API responses (non-2xx status codes)
        
        Tags:
            get, tag, relationships, flows, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/flows/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_relationships_flows(self, id, data) -> Any:
        """
        Creates relationships between a tag and multiple flows by sending a POST request to the API.
        
        Args:
            id: The unique identifier of the tag to which flows will be related.
            data: A dictionary containing the flow relationship data to be associated with the tag.
        
        Returns:
            JSON response from the API containing the result of the relationship creation operation.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameter is not provided.
            HTTPError: Raised when the API request fails, typically due to invalid parameters or server errors.
        
        Tags:
            create, tag, relationships, flows, api, post, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_relationships_flows(self, id, data) -> Any:
        """
        Deletes tag relationships flows by the provided id and data.
        
        Args:
            id: The identifier for the tag.
            data: The data associated with the relationship.
        
        Returns:
            A JSON response object containing the results of the deletion operation.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameter is missing.
        
        Tags:
            delete, relationship, management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_relationships_campaigns(self, id) -> dict[str, Any]:
        """
        Retrieve campaigns associated with a specific tag by ID.
        
        Args:
            id: The unique identifier of the tag to fetch associated campaigns for
        
        Returns:
            Dictionary containing campaign data associated with the specified tag
        
        Raises:
            ValueError: Raised when no ID is provided
            requests.HTTPError: Raised for HTTP request failures (e.g., 404 Not Found or 500 Internal Server Error)
        
        Tags:
            get, relationships, campaigns, api, tags, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_relationships_campaigns(self, id, data) -> Any:
        """
        Creates relationships between a tag and campaigns by sending a POST request to the API.
        
        Args:
            id: The identifier of the tag to link with campaigns.
            data: The relationship data payload to link campaigns to the tag (e.g., campaign IDs).
        
        Returns:
            The JSON response from the API containing the created relationships.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' parameters are None.
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., 4XX/5XX status codes).
        
        Tags:
            create, tag-relationships, campaigns, api, async_job, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_relationships_campaigns(self, id, data) -> Any:
        """
        Deletes relationships between a tag and campaigns using the specified tag ID and request data.
        
        Args:
            id: The unique identifier of the tag whose campaign relationships will be modified.
            data: The payload containing campaign relationship data to be removed.
        
        Returns:
            Parsed JSON response data from the API endpoint.
        
        Raises:
            ValueError: When either 'id' or 'data' parameters are None.
            requests.HTTPError: If the HTTP request fails (handled by response.raise_for_status()).
        
        Tags:
            delete, relationships, campaigns, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_relationships_lists(self, id) -> dict[str, Any]:
        """
        Retrieves a list of tag relationships for the specified ID.
        
        Args:
            id: The ID for which to fetch tag relationships
        
        Returns:
            A dictionary containing the tag relationships for the given ID
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing
        
        Tags:
            fetch, tag-relationships, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/lists/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_relationships_lists(self, id, data) -> Any:
        """
        Creates relationships between tags and lists by sending a POST request with the provided data to the specified URL.
        
        Args:
            id: The ID of the tag to create relationships for.
            data: The data to be sent in the request body to establish tag relationships.
        
        Returns:
            A JSON response from the server after establishing the tag relationships.
        
        Raises:
            ValueError: Raised when either the 'id' or 'data' parameter is missing.
        
        Tags:
            create, tag-relationship, management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_relationships_lists(self, id, data) -> Any:
        """
        Deletes tag relationships with lists for a specified tag ID using the provided data.
        
        Args:
            id: The ID of the tag from which relationships are to be deleted.
            data: Data used in the request to handle the deletion of tag relationships.
        
        Returns:
            JSON data from the server response after deletion.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' is None.
        
        Tags:
            delete, tag, important, api-call
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_relationships_segments(self, id) -> dict[str, Any]:
        """
        Retrieve segment relationships associated with a specified tag ID by querying the API endpoint.
        
        Args:
            id: The unique identifier of the tag for which to retrieve segment relationships. Must not be None.
        
        Returns:
            A dictionary containing the segment relationships data returned by the API. The structure matches the API's JSON response.
        
        Raises:
            ValueError: Raised if the 'id' parameter is None, indicating a missing required argument.
            requests.exceptions.HTTPError: Raised if the API request fails with an unsuccessful status code.
        
        Tags:
            retrieve, tag-relationships, segments, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/segments/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_relationships_segments(self, id, data) -> Any:
        """
        Creates relationships between a tag and segments.
        
        Args:
            id: The unique identifier for the tag.
            data: Data required for creating the relationships.
        
        Returns:
            JSON response from the server, containing details about the created relationships.
        
        Raises:
            ValueError: Raised when either 'id' or 'data' is missing. Indicates that a required parameter is absent.
        
        Tags:
            create, relationship, segment, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_relationships_segments(self, id, data) -> Any:
        """
        Delete segments associated with a specific tag by making a DELETE request to the API endpoint.
        
        Args:
            id: The unique identifier of the tag whose associated segments will be deleted.
            data: The data payload containing segment information for deletion.
        
        Returns:
            JSON response containing the result of the deletion operation from the API.
        
        Raises:
            ValueError: Raised if either 'id' or 'data' parameter is None.
            HTTPError: Raised if the API request fails (handled via response.raise_for_status()).
        
        Tags:
            delete, tag-relationships, segments, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_relationships_tag_group(self, id) -> dict[str, Any]:
        """
        Retrieve tag group relationships associated with a specified tag ID.
        
        Args:
            id: The unique identifier of the tag whose relationships should be retrieved. Must not be None.
        
        Returns:
            A dictionary containing the tag group relationships data in JSON format from the API response.
        
        Raises:
            ValueError: Raised when the required parameter 'id' is not provided (None).
            HTTPError: Raised for HTTP request failures (e.g., 404 Not Found, 500 Internal Server Error).
        
        Tags:
            tag-relationships, tag-group, api-call, json-response, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/tag-group/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_relationships_tags(self, id) -> dict[str, Any]:
        """
        Retrieve tag relationships for a specified tag group by ID.
        
        Args:
            id: The unique identifier of the tag group to fetch relationships for.
        
        Returns:
            A dictionary containing tag relationship data as returned by the API.
        
        Raises:
            ValueError: Raised if 'id' parameter is missing or None.
            HTTPError: Raised if the API request fails with a non-2XX response.
        
        Tags:
            retrieve, tag-group, relationships, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/relationships/tags/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_tag_group(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
        Retrieve a tag group associated with a specific tag ID, with optional field filtering.
        
        Args:
            id: The unique identifier of the tag for which to fetch the associated tag group.
            fields_tag_group: Optional string specifying which fields of the tag-group to include in the response (comma-separated or as per API format).
        
        Returns:
            Dictionary containing the tag group data as returned by the API.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is not provided.
            HTTPError: Raised when the API request fails (e.g., invalid ID, server error).
        
        Tags:
            retrieve, tag-group, api, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/tag-group/"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_tags(self, id, fields_tag=None) -> dict[str, Any]:
        """
        Retrieves tags for a specified tag group by ID.
        
        Args:
            id: The ID of the tag group.
            fields_tag: Optional parameter to specify which fields of the tag to include.
        
        Returns:
            A dictionary containing the retrieved tags.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            tag, fetch, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/tags/"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_templates(self, fields_template=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
        Retrieve template entries from the API with optional filtering, pagination, and field selection.
        
        Args:
            fields_template: Comma-separated fields to include in the template response, or None for all fields
            filter: API-specific filter string to limit returned templates, or None
            page_cursor: Pagination cursor for batch retrieval, or None
            sort: Sorting criteria as an API-compatible string, or None
        
        Returns:
            Dictionary containing API response data with template entries
        
        Raises:
            requests.HTTPError: Raised for non-2xx HTTP status codes during the API request
        
        Tags:
            list, templates, pagination, api-client, important
        """
        url = f"{self.base_url}/api/templates/"
        query_params = {k: v for k, v in [('fields[template]', fields_template), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template(self, data) -> dict[str, Any]:
        """
        Creates a new template by sending data to the API endpoint and returning the parsed JSON response.
        
        Args:
            data: Required dictionary containing template configuration data to be sent in the request body.
        
        Returns:
            Dictionary containing the parsed JSON response from the API.
        
        Raises:
            ValueError: When the 'data' parameter is None, indicating missing required input.
            requests.HTTPError: When the API request fails (e.g., 4XX/5XX status code).
        
        Tags:
            create, template, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template(self, id, fields_template=None) -> dict[str, Any]:
        """
        Retrieves a template by its ID, optionally specifying the fields to include in the template.
        
        Args:
            id: The identifier of the template to retrieve.
            fields_template: An optional list of fields to include in the retrieved template.
        
        Returns:
            A dictionary containing the retrieved template data.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, template, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}/"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_template(self, id, data) -> dict[str, Any]:
        """
        Updates a template with the provided ID by sending a patch request to the API with the given data.
        
        Args:
            id: The unique identifier of the template to be updated.
            data: A dictionary containing the data to update in the template.
        
        Returns:
            A dictionary containing the updated template data.
        
        Raises:
            ValueError: Raised if either the 'id' or 'data' parameter is missing.
        
        Tags:
            update, edit, api-call, important, async
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template(self, id) -> Any:
        """
        Deletes a template resource by ID and returns the server's JSON response.
        
        Args:
            id: Unique identifier of the template to delete (required)
        
        Returns:
            Parsed JSON data from the server's response upon successful deletion
        
        Raises:
            ValueError: Raised when 'id' parameter is None
            requests.HTTPError: Raised for HTTP request failures (4XX/5XX status codes)
        
        Tags:
            delete, template, management, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template_render(self, data) -> dict[str, Any]:
        """
        Creates a rendered template using provided data.
        
        Args:
            data: The data to be used in rendering the template.
        
        Returns:
            A dictionary containing the rendered template data.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None.
        
        Tags:
            render, template, api-call, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-render/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template_clone(self, data) -> dict[str, Any]:
        """
        Creates a clone of a template by sending a POST request with provided data to the template-clone API endpoint.
        
        Args:
            data: Configuration data required for cloning the template. Must not be None.
        
        Returns:
            Dictionary containing the cloned template's response data from the API.
        
        Raises:
            ValueError: Raised when the 'data' parameter is None, indicating missing required input.
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP responses (status code ≥ 400).
        
        Tags:
            create, template, clone, post, async_job, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-clone/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhooks(self, fields_webhook=None, include=None) -> dict[str, Any]:
        """
        Retrieve webhooks configuration from the API endpoint.
        
        Args:
            fields_webhook: Optional comma-separated field names to include in webhook data
            include: Optional related resources to include in the response
        
        Returns:
            JSON-parsed response containing webhooks data as a dictionary
        
        Raises:
            requests.HTTPError: When the API request fails with a 4XX/5XX status code
        
        Tags:
            retrieve, webhook, api, management, important
        """
        url = f"{self.base_url}/api/webhooks/"
        query_params = {k: v for k, v in [('fields[webhook]', fields_webhook), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook(self, data) -> dict[str, Any]:
        """
        Creates a webhook by sending a POST request with the provided data to the specified API endpoint.
        
        Args:
            data: A dictionary containing the data for the webhook; cannot be None
        
        Returns:
            A dictionary containing the response data from the API.
        
        Raises:
            ValueError: Raised when the required 'data' parameter is missing or None.
        
        Tags:
            create, webhook, api, management, important
        """
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook(self, id, fields_webhook=None, include=None) -> dict[str, Any]:
        """
        Fetches a webhook by ID with optional fields and includes.
        
        Args:
            id: The ID of the webhook to fetch (required).
            fields_webhook: Optional fields to include in the webhook response.
            include: Optional related objects or data to include in the response.
        
        Returns:
            A dictionary containing the webhook details.
        
        Raises:
            ValueError: Raised when the 'id' parameter is missing.
        
        Tags:
            fetch, webhook, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}/"
        query_params = {k: v for k, v in [('fields[webhook]', fields_webhook), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_webhook(self, id, data) -> dict[str, Any]:
        """
        Updates an existing webhook configuration by sending a PATCH request to the specified endpoint.
        
        Args:
            id: Unique identifier of the webhook to update
            data: Dictionary containing the updated webhook configuration values
        
        Returns:
            Dictionary containing the updated webhook configuration from the API response
        
        Raises:
            ValueError: Raised when either 'id' or 'data' parameter is None
            requests.HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes) from the API
        
        Tags:
            webhook, update, patch-request, management, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook(self, id) -> Any:
        """
        Deletes a webhook by its ID.
        
        Args:
            id: The ID of the webhook to be deleted.
        
        Returns:
            The JSON response from the server after deleting the webhook.
        
        Raises:
            ValueError: Raised when the required 'id' parameter is missing.
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, webhook, api-call, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topics(self) -> dict[str, Any]:
        """
        Retrieve a dictionary of available webhook topics and their associated data from the API endpoint.
        
        Returns:
            A dictionary containing webhook topics and their metadata as returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            webhook, retrieve, api, topics, management, important
        """
        url = f"{self.base_url}/api/webhook-topics/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topic(self, id) -> dict[str, Any]:
        """
        Retrieves details of a specific webhook topic by ID.
        
        Args:
            id: The unique identifier of the webhook topic to retrieve (required).
        
        Returns:
            A dictionary containing the webhook topic's details, parsed from the JSON response.
        
        Raises:
            ValueError: Raised when the required parameter 'id' is not provided.
            requests.HTTPError: Raised for HTTP 4XX/5XX errors from the API request.
        
        Tags:
            retrieve, webhook, api, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhook-topics/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_subscription(self, company_id, data) -> Any:
        """
        Creates a client subscription by sending a POST request with provided data and company ID.
        
        Args:
            company_id: The ID of the company for which the subscription is being created.
            data: The data required for creating the client subscription.
        
        Returns:
            The JSON response from the server after creating the subscription.
        
        Raises:
            ValueError: Raised when either 'company_id' or 'data' is missing.
        
        Tags:
            create, subscription, client-management, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/subscriptions/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_push_token(self, company_id, data) -> Any:
        """
        Creates a client push token by sending a POST request with the provided company ID and data.
        
        Args:
            company_id: The ID of the company for which the push token is being created.
            data: The data payload to be included in the request.
        
        Returns:
            The JSON response from the server containing the newly created push token.
        
        Raises:
            ValueError: Raised when either 'company_id' or 'data' is missing.
        
        Tags:
            create, client, push-token, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-tokens/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unregister_client_push_token(self, company_id, data) -> Any:
        """
        Unregisters a client push token for a company by sending a POST request.
        
        Args:
            company_id: Required identifier of the company.
            data: Required data associated with the push token.
        
        Returns:
            JSON response from the server after successful unregistration.
        
        Raises:
            ValueError: Raised if the 'company_id' or 'data' parameter is missing.
        
        Tags:
            unregister, push-token, management, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-token-unregister/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_event(self, company_id, data) -> Any:
        """
        Creates a client event by sending a POST request with provided data and company ID.
        
        Args:
            company_id: Unique identifier for the company associated with the event.
            data: Event data payload to be sent in the request body.
        
        Returns:
            Parsed JSON response from the API containing event details or operation results.
        
        Raises:
            ValueError: Raised when 'company_id' or 'data' parameters are None.
            requests.exceptions.HTTPError: Raised for non-2xx HTTP responses from the API.
        
        Tags:
            client, event, post, api, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/events/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_profile(self, company_id, data) -> Any:
        """
        Creates a client profile by sending a POST request with the provided data and company ID.
        
        Args:
            company_id: The ID of the company for which the client profile is created.
            data: Dictionary containing data for the client profile.
        
        Returns:
            JSON response from the server after successfully creating the client profile.
        
        Raises:
            ValueError: Raised if either 'company_id' or 'data' is None.
        
        Tags:
            create, client, profile, important, management
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/profiles/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_client_events(self, company_id, data) -> Any:
        """
        Bulk creates client events for a specified company by sending data to the API endpoint.
        
        Args:
            company_id: The ID of the company for which events are being created.
            data: The event data to be created, typically a list or dictionary of event details.
        
        Returns:
            Parsed JSON response from the API containing the results of the bulk creation operation.
        
        Raises:
            ValueError: Raised when either 'company_id' or 'data' is None.
            HTTPError: Raised if the API request fails, typically due to invalid data or server errors.
        
        Tags:
            client-events, bulk-create, api, async_job, management, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/event-bulk-create/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_back_in_stock_subscription(self, company_id, data) -> Any:
        """
        Creates a subscription for back-in-stock notifications by sending a POST request to the server.
        
        Args:
            company_id: The ID of the company for which the subscription is being created.
            data: The data required for creating the back-in-stock subscription.
        
        Returns:
            A JSON object containing the response from the server.
        
        Raises:
            ValueError: Raised if either 'company_id' or 'data' is missing.
        
        Tags:
            subscription, back-in-stock, client, important
        """
        if company_id is None:
            raise ValueError("Missing required parameter 'company_id'")
        if data is None:
            raise ValueError("Missing required parameter 'data'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/back-in-stock-subscriptions/"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.get_accounts,
            self.get_account,
            self.get_campaigns,
            self.create_campaign,
            self.get_campaign,
            self.update_campaign,
            self.delete_campaign,
            self.get_campaign_message,
            self.update_campaign_message,
            self.get_campaign_send_job,
            self.update_campaign_send_job,
            self.get_campaign_recipient_estimation_job,
            self.get_campaign_recipient_estimation,
            self.create_campaign_clone,
            self.create_campaign_message_assign_template,
            self.create_campaign_send_job,
            self.create_campaign_recipient_estimation_job,
            self.get_campaign_message_relationships_campaign,
            self.get_campaign_message_campaign,
            self.get_campaign_message_relationships_template,
            self.get_campaign_message_template,
            self.get_campaign_relationships_tags,
            self.get_campaign_tags,
            self.get_campaign_relationships_campaign_messages,
            self.get_campaign_campaign_messages,
            self.get_catalog_items,
            self.create_catalog_item,
            self.get_catalog_item,
            self.update_catalog_item,
            self.delete_catalog_item,
            self.get_catalog_variants,
            self.create_catalog_variant,
            self.get_catalog_variant,
            self.update_catalog_variant,
            self.delete_catalog_variant,
            self.get_catalog_categories,
            self.create_catalog_category,
            self.get_catalog_category,
            self.update_catalog_category,
            self.delete_catalog_category,
            self.get_create_items_jobs,
            self.spawn_create_items_job,
            self.get_create_items_job,
            self.get_update_items_jobs,
            self.spawn_update_items_job,
            self.get_update_items_job,
            self.get_delete_items_jobs,
            self.spawn_delete_items_job,
            self.get_delete_items_job,
            self.get_create_variants_jobs,
            self.spawn_create_variants_job,
            self.get_create_variants_job,
            self.get_update_variants_jobs,
            self.spawn_update_variants_job,
            self.get_update_variants_job,
            self.get_delete_variants_jobs,
            self.spawn_delete_variants_job,
            self.get_delete_variants_job,
            self.get_create_categories_jobs,
            self.spawn_create_categories_job,
            self.get_create_categories_job,
            self.get_update_categories_jobs,
            self.spawn_update_categories_job,
            self.get_update_categories_job,
            self.get_delete_categories_jobs,
            self.spawn_delete_categories_job,
            self.get_delete_categories_job,
            self.create_back_in_stock_subscription,
            self.get_catalog_category_items,
            self.get_catalog_item_variants,
            self.get_catalog_item_categories,
            self.get_catalog_category_relationships_items,
            self.create_catalog_category_relationships_items,
            self.update_catalog_category_relationships_items,
            self.delete_catalog_category_relationships_items,
            self.get_catalog_item_relationships_categories,
            self.create_catalog_item_relationships_categories,
            self.update_catalog_item_relationships_categories,
            self.delete_catalog_item_relationships_categories,
            self.get_coupons,
            self.create_coupon,
            self.get_coupon,
            self.update_coupon,
            self.delete_coupon,
            self.get_coupon_codes,
            self.create_coupon_code,
            self.get_coupon_code,
            self.update_coupon_code,
            self.delete_coupon_code,
            self.get_coupon_code_bulk_create_jobs,
            self.spawn_coupon_code_bulk_create_job,
            self.get_coupon_code_bulk_create_job,
            self.get_coupon_for_coupon_code,
            self.get_coupon_relationships_coupon_codes,
            self.get_coupon_codes_for_coupon,
            self.get_coupon_code_relationships_coupon,
            self.request_profile_deletion,
            self.get_events,
            self.create_event,
            self.get_event,
            self.bulk_create_events,
            self.get_event_metric,
            self.get_event_profile,
            self.get_event_relationships_metric,
            self.get_event_relationships_profile,
            self.get_flows,
            self.get_flow,
            self.update_flow,
            self.delete_flow,
            self.get_flow_action,
            self.get_flow_message,
            self.get_flow_flow_actions,
            self.get_flow_relationships_flow_actions,
            self.get_flow_relationships_tags,
            self.get_flow_tags,
            self.get_flow_action_flow,
            self.get_flow_action_relationships_flow,
            self.get_flow_action_messages,
            self.get_flow_action_relationships_messages,
            self.get_flow_message_action,
            self.get_flow_message_relationships_action,
            self.get_flow_message_relationships_template,
            self.get_flow_message_template,
            self.get_forms,
            self.get_form,
            self.get_form_version,
            self.get_versions_for_form,
            self.get_version_ids_for_form,
            self.get_form_id_for_form_version,
            self.get_form_for_form_version,
            self.get_images,
            self.get_image,
            self.update_image,
            self.get_lists,
            self.create_list,
            self.get_list,
            self.update_list,
            self.delete_list,
            self.get_list_relationships_tags,
            self.get_list_tags,
            self.get_list_relationships_profiles,
            self.create_list_relationships,
            self.delete_list_relationships,
            self.get_list_profiles,
            self.get_metrics,
            self.get_metric,
            self.query_metric_aggregates,
            self.get_profiles,
            self.create_profile,
            self.get_profile,
            self.update_profile,
            self.get_bulk_profile_import_jobs,
            self.spawn_bulk_profile_import_job,
            self.get_bulk_profile_import_job,
            self.create_or_update_profile,
            self.merge_profiles,
            self.suppress_profiles,
            self.unsuppress_profiles,
            self.subscribe_profiles,
            self.unsubscribe_profiles,
            self.create_push_token,
            self.get_profile_lists,
            self.get_profile_relationships_lists,
            self.get_profile_segments,
            self.get_profile_relationships_segments,
            self.get_bulk_profile_import_job_lists,
            self.get_bulk_profile_import_job_relationships_lists,
            self.get_bulk_profile_import_job_profiles,
            self.get_bulk_profile_import_job_relationships_profiles,
            self.get_bulk_profile_import_job_import_errors,
            self.query_campaign_values,
            self.query_flow_values,
            self.query_flow_series,
            self.get_segments,
            self.create_segment,
            self.get_segment,
            self.update_segment,
            self.delete_segment,
            self.get_segment_relationships_tags,
            self.get_segment_tags,
            self.get_segment_relationships_profiles,
            self.get_segment_profiles,
            self.get_tags,
            self.create_tag,
            self.get_tag,
            self.update_tag,
            self.delete_tag,
            self.get_tag_groups,
            self.create_tag_group,
            self.get_tag_group,
            self.update_tag_group,
            self.delete_tag_group,
            self.get_tag_relationships_flows,
            self.create_tag_relationships_flows,
            self.delete_tag_relationships_flows,
            self.get_tag_relationships_campaigns,
            self.create_tag_relationships_campaigns,
            self.delete_tag_relationships_campaigns,
            self.get_tag_relationships_lists,
            self.create_tag_relationships_lists,
            self.delete_tag_relationships_lists,
            self.get_tag_relationships_segments,
            self.create_tag_relationships_segments,
            self.delete_tag_relationships_segments,
            self.get_tag_relationships_tag_group,
            self.get_tag_group_relationships_tags,
            self.get_tag_tag_group,
            self.get_tag_group_tags,
            self.get_templates,
            self.create_template,
            self.get_template,
            self.update_template,
            self.delete_template,
            self.create_template_render,
            self.create_template_clone,
            self.get_webhooks,
            self.create_webhook,
            self.get_webhook,
            self.update_webhook,
            self.delete_webhook,
            self.get_webhook_topics,
            self.get_webhook_topic,
            self.create_client_subscription,
            self.create_client_push_token,
            self.unregister_client_push_token,
            self.create_client_event,
            self.create_client_profile,
            self.bulk_create_client_events,
            self.create_client_back_in_stock_subscription
        ]
