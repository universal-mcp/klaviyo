# KlaviyoApp MCP Server

An MCP Server for the KlaviyoApp API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/klaviyoapp/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the KlaviyoApp API.


| Tool | Description |
|------|-------------|
| `get_accounts` | Retrieves account data via API request, returning parsed JSON response. |
| `get_account` | Retrieves account details from the API by ID. |
| `get_campaigns` | Retrieve campaign data with optional filtering, field selection, pagination, and sorting. |
| `create_campaign` | Creates a campaign by sending a POST request to the specified API endpoint with the given data. |
| `get_campaign` | Retrieves a campaign by its ID, allowing specification of fields and inclusion of additional data. |
| `update_campaign` | Updates an existing campaign with the provided data using a PATCH request. |
| `delete_campaign` | Deletes a campaign by its ID. |
| `get_campaign_message` | Retrieves a campaign message by ID, optionally including specified fields. |
| `update_campaign_message` | Updates a campaign message by sending a patch request to the specified API endpoint. |
| `get_campaign_send_job` | Retrieves a campaign send job by its ID, optionally specifying fields to include in the response. |
| `update_campaign_send_job` | Updates an existing campaign send job with the provided data. |
| `get_campaign_recipient_estimation_job` | Retrieve details for a specific campaign recipient estimation job by ID. |
| `get_campaign_recipient_estimation` | Retrieve campaign recipient estimation details for a specific campaign ID. |
| `create_campaign_clone` | Creates a clone of a campaign using the provided data. |
| `create_campaign_message_assign_template` | Creates a campaign message by assigning a template with provided data. |
| `create_campaign_send_job` | Creates a campaign send job by sending data to the API endpoint, handling request validation and response parsing. |
| `create_campaign_recipient_estimation_job` | Initiates an asynchronous job to estimate campaign recipients by submitting provided data to the API. |
| `get_campaign_message_relationships_campaign` | Retrieves campaign relationship data for a specific campaign message from the API. |
| `get_campaign_message_campaign` | Retrieve campaign details for a specific campaign message using its ID and optional field filtering. |
| `get_campaign_message_relationships_template` | Retrieve the template relationships for a specific campaign message. |
| `get_campaign_message_template` | Fetches the message template for a campaign based on the provided ID. |
| `get_campaign_relationships_tags` | Retrieve tag relationships for a specific campaign via API endpoint. |
| `get_campaign_tags` | Fetches tags associated with a campaign by ID from an API. |
| `get_campaign_relationships_campaign_messages` | Fetches campaign relationships for campaign messages by a given campaign ID. |
| `get_campaign_campaign_messages` | Retrieve campaign messages for a specified campaign ID, allowing for customizable field selection and inclusion. |
| `get_catalog_items` | Retrieves catalog items from the API, allowing for specification of fields, filters, and sorting. |
| `create_catalog_item` | Creates a new catalog item using provided data by sending a POST request to the catalog-items endpoint. |
| `get_catalog_item` | Retrieve a specific catalog item with optional field filtering and related data inclusion |
| `update_catalog_item` | Updates a catalog item by sending a PATCH request with the provided data to the specified catalog item ID. |
| `delete_catalog_item` | Deletes a catalog item based on the provided ID. |
| `get_catalog_variants` | Retrieves catalog variants from the API with optional filtering, sorting, and pagination. |
| `create_catalog_variant` | Creates a catalog variant using the provided data. |
| `get_catalog_variant` | Retrieves a catalog variant from the API based on its ID, optionally specifying fields to return. |
| `update_catalog_variant` | Updates a catalog variant by ID with provided data using a PATCH request. |
| `delete_catalog_variant` | Deletes a catalog variant by its ID. |
| `get_catalog_categories` | Retrieves catalog categories via API with optional filtering and pagination |
| `create_catalog_category` | Creates a new catalog category by sending a POST request with the provided data. |
| `get_catalog_category` | Retrieves a catalog category by its ID, optionally specifying fields to include. |
| `update_catalog_category` | Updates a catalog category by making a PATCH request to the API endpoint with provided data. |
| `delete_catalog_category` | Deletes a catalog category by its ID. |
| `get_create_items_jobs` | Retrieves a list of catalog item bulk create jobs from an API with optional filtering and pagination. |
| `spawn_create_items_job` | Initiates a job to create items in bulk using the provided data. |
| `get_create_items_job` | Retrieves details of a catalog item bulk creation job by its ID, including options for specifying which fields and related data to include. |
| `get_update_items_jobs` | Retrieve paginated list of catalog item bulk update jobs using REST API endpoint. |
| `spawn_update_items_job` | Spawns an asynchronous job to update catalog items in bulk. |
| `get_update_items_job` | Retrieves details of a catalog item bulk update job by its ID. |
| `get_delete_items_jobs` | Retrieves a list of catalog item bulk delete jobs with specified fields and filtering. |
| `spawn_delete_items_job` | Initiates a job to delete items in bulk. |
| `get_delete_items_job` | Retrieves a catalog item bulk delete job based on the provided job ID. |
| `get_create_variants_jobs` | Retrieves catalog variant bulk create jobs data from the API. |
| `spawn_create_variants_job` | Initiates an asynchronous job to bulk-create catalog variants using the provided data. |
| `get_create_variants_job` | Retrieves a Catalog Variant Bulk Create Job by its ID, allowing for customizable data fields and inclusions. |
| `get_update_variants_jobs` | Retrieve paginated catalog variant bulk update jobs via API endpoint with filtering and field selection. |
| `spawn_update_variants_job` | Spawns a job to update variants in bulk via an API request. |
| `get_update_variants_job` | Retrieves details of a specific catalog variant bulk update job using the provided job ID. |
| `get_delete_variants_jobs` | Retrieves catalog variant bulk delete jobs with optional filtering and pagination. |
| `spawn_delete_variants_job` | Initiates an asynchronous job to delete multiple catalog variants using bulk delete operation. |
| `get_delete_variants_job` | Retrieves the status and details of a specific catalog variant bulk delete job. |
| `get_create_categories_jobs` | Retrieves a list of catalog category bulk create jobs, optionally filtering by specified criteria or fields. |
| `spawn_create_categories_job` | Initiates an asynchronous job to create categories in the catalog by submitting a data payload. |
| `get_create_categories_job` | Retrieves information about a bulk category creation job based on the provided job ID. |
| `get_update_categories_jobs` | Retrieve paginated list of catalog category bulk update jobs from the API endpoint. |
| `spawn_update_categories_job` | Initiates an asynchronous bulk update job for categories using the provided data. |
| `get_update_categories_job` | Retrieves details of a catalog category bulk update job by its ID. |
| `get_delete_categories_jobs` | Retrieve paginated results of catalog category bulk deletion jobs from the API. |
| `spawn_delete_categories_job` | Initiates a job to delete categories in bulk by sending a POST request to the API endpoint. |
| `get_delete_categories_job` | Retrieves the details of a catalog category bulk delete job by ID. |
| `create_back_in_stock_subscription` | Creates a back-in-stock subscription by sending a POST request to the specified API endpoint. |
| `get_catalog_category_items` | Retrieve items belonging to a catalog category with optional filtering, sorting, and field selection. |
| `get_catalog_item_variants` | Fetches variant items for a catalog item by ID, optionally filtering, sorting, or pagination. |
| `get_catalog_item_categories` | Retrieve categories associated with a specific catalog item using filtering, pagination, and sorting parameters. |
| `get_catalog_category_relationships_items` | Fetches catalog category related items through paginated API request. |
| `create_catalog_category_relationships_items` | Creates a relationship between a catalog category and items. |
| `update_catalog_category_relationships_items` | Updates item relationships for a specific catalog category by sending a PATCH request to the API endpoint. |
| `delete_catalog_category_relationships_items` | Delete items related to a catalog category by ID and relationship data. |
| `get_catalog_item_relationships_categories` | Fetches the relationship categories for a catalog item using its ID. |
| `create_catalog_item_relationships_categories` | Creates relationships between a catalog item and categories by sending a POST request to the API. |
| `update_catalog_item_relationships_categories` | Updates the categories relationship for a specified catalog item. |
| `delete_catalog_item_relationships_categories` | Deletes category relationships for a catalog item by ID with specified data. |
| `get_coupons` | Fetches coupons from the API with optional filtering by fields and pagination. |
| `create_coupon` | Creates a new coupon using the provided data. |
| `get_coupon` | Retrieves a specific coupon's details from the API using the provided identifier. |
| `update_coupon` | Updates an existing coupon's data by sending a PATCH request to the API endpoint. |
| `delete_coupon` | Deletes a coupon from the server using its unique identifier. |
| `get_coupon_codes` | Fetches coupon codes from an API with optional filtering and pagination. |
| `create_coupon_code` | Creates a new coupon code by posting data to the coupon codes API endpoint. |
| `get_coupon_code` | Fetches a coupon code from the API by its ID, with optional fields and includes. |
| `update_coupon_code` | Updates a coupon code by sending a PATCH request with provided data to the coupon code API endpoint. |
| `delete_coupon_code` | Delete a coupon code by ID using the API endpoint. |
| `get_coupon_code_bulk_create_jobs` | Fetches bulk coupon code creation jobs with optional filtering and pagination. |
| `spawn_coupon_code_bulk_create_job` | Initiates a bulk creation job for coupon codes using provided data. |
| `get_coupon_code_bulk_create_job` | Retrieves a bulk coupon code creation job by job ID. |
| `get_coupon_for_coupon_code` | Retrieve coupon details associated with a specific coupon code ID. |
| `get_coupon_relationships_coupon_codes` | Fetches the coupon relationship data associated with a specific coupon code ID by making a GET request to the API endpoint. |
| `get_coupon_codes_for_coupon` | Fetches coupon codes for a specific coupon identified by ID. |
| `get_coupon_code_relationships_coupon` | Retrieves the relationships between a coupon and its codes. |
| `request_profile_deletion` | Initiates a profile deletion request by posting data to a privacy deletion endpoint. |
| `get_events` | Retrieves events data from the API with customizable field selection and filtering. |
| `create_event` | Creates a new event by sending a POST request with the provided data to the events API. |
| `get_event` | Retrieves event data from an API using the provided ID and optional field selectors. |
| `bulk_create_events` | Creates multiple events in bulk using a POST request to the event-bulk-create-jobs API endpoint. |
| `get_event_metric` | Retrieve detailed metric data for a specific event by ID. |
| `get_event_profile` | Retrieves an event profile by ID, including optional additional or specific fields. |
| `get_event_relationships_metric` | Fetches event relationships metric data from the API. |
| `get_event_relationships_profile` | Fetches and returns the event relationships profile data for the specified event ID. |
| `get_flows` | Retrieves flow data with optional filtering, pagination, and field selection from the API. |
| `get_flow` | Fetches flow data from the API for a given flow ID with optional fields for customization. |
| `update_flow` | Updates a flow by sending a PATCH request with the provided data to the specified flow ID. |
| `delete_flow` | Deletes a flow by its ID from the API endpoint. |
| `get_flow_action` | Retrieves a flow action's details by ID, with optional field filtering and related resource inclusion. |
| `get_flow_message` | Retrieves a flow message by its ID, optionally filtering fields and including related data. |
| `get_flow_flow_actions` | Retrieve flow actions for a specified flow via API, with optional filtering and pagination. |
| `get_flow_relationships_flow_actions` | Retrieves relationships between flows and flow actions for a specified flow ID |
| `get_flow_relationships_tags` | Retrieve tags associated with a specific flow's relationships by ID. |
| `get_flow_tags` | Retrieves tags for a specific flow identified by its ID. |
| `get_flow_action_flow` | Retrieves flow actions based on the provided ID and optional flow fields. |
| `get_flow_action_relationships_flow` | Retrieve relationships flow data for a specific flow action by ID from the API. |
| `get_flow_action_messages` | Retrieves flow action messages associated with a given ID. |
| `get_flow_action_relationships_messages` | Retrieves flow action relationships messages from a specified ID with optional filtering, pagination, and sorting. |
| `get_flow_message_action` | Retrieves a specific flow message action from the API using its ID and optional field filtering. |
| `get_flow_message_relationships_action` | Retrieve flow action relationships for a specified flow message ID by querying the API endpoint. |
| `get_flow_message_relationships_template` | Retrieves the template relationships data for a specific flow message. |
| `get_flow_message_template` | Retrieve a flow message template by ID, optionally specifying fields to include in the template. |
| `get_forms` | Retrieves forms from an API endpoint with optional filtering, pagination, and sorting. |
| `get_form` | Retrieves a form by its ID with optional parameters to specify form version, fields, and included data. |
| `get_form_version` | Retrieves a specific form version's details by ID from the API. |
| `get_versions_for_form` | Retrieves paginated form versions for a specified form ID with optional filtering, sorting, and field selection. |
| `get_version_ids_for_form` | Retrieves version IDs for a specific form identified by its ID. |
| `get_form_id_for_form_version` | Retrieves the form ID associated with a specific form version. |
| `get_form_for_form_version` | Fetches a form for a specified form version. |
| `get_images` | Retrieve a paginated list of images from the API endpoint with optional filtering, sorting, and field selection. |
| `get_image` | Retrieves an image by its ID from an API, allowing optional specification of image fields. |
| `update_image` | Updates an image's data via a PATCH request to the API endpoint. |
| `get_lists` | Retrieves a paginated collection of lists with optional filtering, sorting, and field selection. |
| `create_list` | Creates a list by sending a POST request to the API endpoint with the provided data. |
| `get_list` | Retrieves a specific list's details by ID from an API endpoint |
| `update_list` | Updates a list by sending a PATCH request to the specified API endpoint. |
| `delete_list` | Deletes a list by its ID and returns the response in JSON format. |
| `get_list_relationships_tags` | Retrieves tag relationships for a specified list ID by querying the API endpoint. |
| `get_list_tags` | Retrieve tags associated with a specific list by ID, with optional field filtering. |
| `get_list_relationships_profiles` | Retrieves the list of relationships between a specified list and profiles, optionally filtered, paginated, and sorted. |
| `create_list_relationships` | Creates relationships between a list and profiles by sending a POST request to the API endpoint. |
| `delete_list_relationships` | Deletes relationships between a list and associated profiles based on the provided ID and data. |
| `get_list_profiles` | Retrieves a list of profiles associated with a specified list id, including optional filtering and pagination. |
| `get_metrics` | Fetches metrics data from the API endpoint with optional filtering and pagination. |
| `get_metric` | Retrieve a specific metric's data by ID from the API endpoint. |
| `query_metric_aggregates` | Query metric aggregates by sending provided data to the API endpoint and returning the parsed JSON response. |
| `get_profiles` | Fetches profiles from the API with optional filtering and pagination. |
| `create_profile` | Creates a new profile by sending a POST request to the API endpoint with the provided data. |
| `get_profile` | Retrieves a profile by ID with optional additional fields. |
| `update_profile` | Updates a user profile by sending a PATCH request with the provided data to the specified profile ID. |
| `get_bulk_profile_import_jobs` | Retrieves a list of bulk profile import jobs with optional filtering, sorting, and pagination. |
| `spawn_bulk_profile_import_job` | Spawns a bulk profile import job by sending the provided data to the profile bulk import API endpoint. |
| `get_bulk_profile_import_job` | Retrieves details of a bulk profile import job by ID with optional field filtering. |
| `create_or_update_profile` | Creates or updates a user profile by sending data to a profile import API endpoint. |
| `merge_profiles` | Merges user profile data by sending a POST request to the profile-merge API endpoint. |
| `suppress_profiles` | Supresses profiles by creating a bulk job through a POST request. |
| `unsuppress_profiles` | Deletes suppressed profiles in bulk by issuing a POST request with the provided data. |
| `subscribe_profiles` | Initiates bulk profile subscription jobs by sending provided data to a specified API endpoint. |
| `unsubscribe_profiles` | Initiates a bulk unsubscribe job for profiles using provided data |
| `create_push_token` | Creates and registers a push token using the provided data. |
| `get_profile_lists` | Retrieve profile lists for a specified profile ID, with optional field filtering. |
| `get_profile_relationships_lists` | Fetches relationship lists for a profile based on the given ID. |
| `get_profile_segments` | Retrieve profile segments for a specified ID by making a GET request to the API endpoint. |
| `get_profile_relationships_segments` | Retrieve relationship segments for a profile ID from the API. |
| `get_bulk_profile_import_job_lists` | Fetches a list of profiles for a bulk import job based on the provided ID and optional field specifications. |
| `get_bulk_profile_import_job_relationships_lists` | Retrieves relationship lists associated with a specific bulk profile import job by ID. |
| `get_bulk_profile_import_job_profiles` | Retrieve profiles associated with a bulk import job by its ID, with optional pagination and field selection. |
| `get_bulk_profile_import_job_relationships_profiles` | Retrieves the relationships between a bulk profile import job and its associated profiles. |
| `get_bulk_profile_import_job_import_errors` | Retrieves import errors for a bulk profile import job by ID, optionally filtering by specific import error fields and paginating the results. |
| `query_campaign_values` | Queries campaign values based on provided data and returns the response as a dictionary. |
| `query_flow_values` | Queries flow values reports by sending a POST request with provided data and optional page cursor. |
| `query_flow_series` | Queries the flow series reports by posting the provided data and handling pagination. |
| `get_segments` | Retrieves segment data from a specified API endpoint. |
| `create_segment` | Creates a new segment by sending a POST request with the provided data. |
| `get_segment` | Retrieves a specific segment's data from an API endpoint with customizable field selection. |
| `update_segment` | Updates a segment's data via a PATCH request to the API endpoint. |
| `delete_segment` | Deletes a segment by its ID and returns the JSON response. |
| `get_segment_relationships_tags` | Retrieve tag relationships for a specific segment from the API. |
| `get_segment_tags` | Retrieve tags for a specific segment by ID, with optional field filtering for tag data |
| `get_segment_relationships_profiles` | Retrieve relationship profiles associated with a specific segment using pagination and filtering. |
| `get_segment_profiles` | Retrieves segment profiles from the specified API endpoint based on the provided ID and optional query parameters. |
| `get_tags` | Fetches a list of tags from the API with optional filtering and sorting. |
| `create_tag` | Creates a new tag by sending a POST request to the tag API endpoint with the provided data. |
| `get_tag` | Retrieves a tag by its ID, optionally including additional fields and related data. |
| `update_tag` | Updates a tag's data using a PATCH request to the API endpoint. |
| `delete_tag` | Deletes a tag specified by its ID from the API. |
| `get_tag_groups` | Retrieve paginated tag groups from the API with optional filtering, sorting, and field selection. |
| `create_tag_group` | Creates a new tag group by sending the provided payload to the API endpoint. |
| `get_tag_group` | Fetches details of a tag group from the API by its ID. |
| `update_tag_group` | Updates a tag group by ID using the provided data via a PATCH request. |
| `delete_tag_group` | Deletes a tag group with the specified ID using an HTTP DELETE request and returns the JSON response. |
| `get_tag_relationships_flows` | Fetch tag-flow relationships by tag ID from the API. |
| `create_tag_relationships_flows` | Creates relationships between a tag and multiple flows by sending a POST request to the API. |
| `delete_tag_relationships_flows` | Deletes tag relationships flows by the provided id and data. |
| `get_tag_relationships_campaigns` | Retrieve campaigns associated with a specific tag by ID. |
| `create_tag_relationships_campaigns` | Creates relationships between a tag and campaigns by sending a POST request to the API. |
| `delete_tag_relationships_campaigns` | Deletes relationships between a tag and campaigns using the specified tag ID and request data. |
| `get_tag_relationships_lists` | Retrieves a list of tag relationships for the specified ID. |
| `create_tag_relationships_lists` | Creates relationships between tags and lists by sending a POST request with the provided data to the specified URL. |
| `delete_tag_relationships_lists` | Deletes tag relationships with lists for a specified tag ID using the provided data. |
| `get_tag_relationships_segments` | Retrieve segment relationships associated with a specified tag ID by querying the API endpoint. |
| `create_tag_relationships_segments` | Creates relationships between a tag and segments. |
| `delete_tag_relationships_segments` | Delete segments associated with a specific tag by making a DELETE request to the API endpoint. |
| `get_tag_relationships_tag_group` | Retrieve tag group relationships associated with a specified tag ID. |
| `get_tag_group_relationships_tags` | Retrieve tag relationships for a specified tag group by ID. |
| `get_tag_tag_group` | Retrieve a tag group associated with a specific tag ID, with optional field filtering. |
| `get_tag_group_tags` | Retrieves tags for a specified tag group by ID. |
| `get_templates` | Retrieve template entries from the API with optional filtering, pagination, and field selection. |
| `create_template` | Creates a new template by sending data to the API endpoint and returning the parsed JSON response. |
| `get_template` | Retrieves a template by its ID, optionally specifying the fields to include in the template. |
| `update_template` | Updates a template with the provided ID by sending a patch request to the API with the given data. |
| `delete_template` | Deletes a template resource by ID and returns the server's JSON response. |
| `create_template_render` | Creates a rendered template using provided data. |
| `create_template_clone` | Creates a clone of a template by sending a POST request with provided data to the template-clone API endpoint. |
| `get_webhooks` | Retrieve webhooks configuration from the API endpoint. |
| `create_webhook` | Creates a webhook by sending a POST request with the provided data to the specified API endpoint. |
| `get_webhook` | Fetches a webhook by ID with optional fields and includes. |
| `update_webhook` | Updates an existing webhook configuration by sending a PATCH request to the specified endpoint. |
| `delete_webhook` | Deletes a webhook by its ID. |
| `get_webhook_topics` | Retrieve a dictionary of available webhook topics and their associated data from the API endpoint. |
| `get_webhook_topic` | Retrieves details of a specific webhook topic by ID. |
| `create_client_subscription` | Creates a client subscription by sending a POST request with provided data and company ID. |
| `create_client_push_token` | Creates a client push token by sending a POST request with the provided company ID and data. |
| `unregister_client_push_token` | Unregisters a client push token for a company by sending a POST request. |
| `create_client_event` | Creates a client event by sending a POST request with provided data and company ID. |
| `create_client_profile` | Creates a client profile by sending a POST request with the provided data and company ID. |
| `bulk_create_client_events` | Bulk creates client events for a specified company by sending data to the API endpoint. |
| `create_client_back_in_stock_subscription` | Creates a subscription for back-in-stock notifications by sending a POST request to the server. |


## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── klaviyoapp/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the KlaviyoApp app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 