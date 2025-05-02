from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class KlaviyoApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='klaviyoapp', integration=integration, **kwargs)
        self.base_url = "https://a.klaviyo.com"

    def create_client_review(self, company_id=None, data=None) -> Any:
        """
Create Client Review

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '<string>'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "author": "<string>",
                      "content": "<string>",
                      "custom_questions": [
                        {
                          "answers": [
                            "<string>",
                            "<string>"
                          ],
                          "id": "<string>"
                        },
                        {
                          "answers": [
                            "<string>",
                            "<string>"
                          ],
                          "id": "<string>"
                        }
                      ],
                      "email": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "incentive_type": "free_product",
                      "product": {
                        "external_id": "<string>",
                        "integration_key": "woocommerce"
                      },
                      "rating": 2,
                      "review_type": "rating",
                      "title": "<string>"
                    },
                    "relationships": {
                      "order": {
                        "data": {
                          "id": "<string>",
                          "type": "order"
                        }
                      }
                    },
                    "type": "review"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/reviews"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_accounts(self, fields_account=None) -> dict[str, Any]:
        """
Get Accounts

        Args:
            fields_account (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'contact_information.street_address.address1,contact_information.street_address.city'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/accounts"
        query_params = {k: v for k, v in [('fields[account]', fields_account)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_account(self, id, fields_account=None) -> dict[str, Any]:
        """
Get Account

        Args:
            id (string): id
            fields_account (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'contact_information.street_address.address1,contact_information.street_address.city'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/accounts/{id}"
        query_params = {k: v for k, v in [('fields[account]', fields_account)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaigns(self, fields_campaign_message=None, fields_campaign=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Campaigns

        Args:
            fields_campaign_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'send_time,send_options.use_smart_sending'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            filter (string): (Required) For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`messages.channel`: `equals`<br>`name`: `contains`<br>`status`: `any`, `equals`<br>`archived`: `equals`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`scheduled_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tags,tags'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated_at'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/campaigns"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign(self, data=None) -> dict[str, Any]:
        """
Create Campaign

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "audiences": {
                        "excluded": [
                          "<string>",
                          "<string>"
                        ],
                        "included": [
                          "<string>",
                          "<string>"
                        ]
                      },
                      "campaign-messages": {
                        "data": [
                          {
                            "attributes": {
                              "definition": {
                                "channel": "email",
                                "content": {
                                  "bcc_email": "<string>",
                                  "cc_email": "<string>",
                                  "from_email": "<string>",
                                  "from_label": "<string>",
                                  "preview_text": "<string>",
                                  "reply_to_email": "<string>",
                                  "subject": "<string>"
                                },
                                "label": "<string>"
                              }
                            },
                            "relationships": {
                              "image": {
                                "data": {
                                  "id": "<string>",
                                  "type": "image"
                                }
                              }
                            },
                            "type": "campaign-message"
                          },
                          {
                            "attributes": {
                              "definition": {
                                "channel": "email",
                                "content": {
                                  "bcc_email": "<string>",
                                  "cc_email": "<string>",
                                  "from_email": "<string>",
                                  "from_label": "<string>",
                                  "preview_text": "<string>",
                                  "reply_to_email": "<string>",
                                  "subject": "<string>"
                                },
                                "label": "<string>"
                              }
                            },
                            "relationships": {
                              "image": {
                                "data": {
                                  "id": "<string>",
                                  "type": "image"
                                }
                              }
                            },
                            "type": "campaign-message"
                          }
                        ]
                      },
                      "name": "<string>",
                      "send_options": {
                        "use_smart_sending": true
                      },
                      "send_strategy": {
                        "datetime": "<dateTime>",
                        "method": "static",
                        "options": {
                          "is_local": true,
                          "send_past_recipients_immediately": false
                        }
                      },
                      "tracking_options": {
                        "add_utm": "<boolean>",
                        "is_tracking_clicks": "<boolean>",
                        "is_tracking_opens": "<boolean>",
                        "utm_params": [
                          {
                            "name": "<string>",
                            "value": "<string>"
                          },
                          {
                            "name": "<string>",
                            "value": "<string>"
                          }
                        ]
                      }
                    },
                    "type": "campaign"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign(self, id, fields_campaign_message=None, fields_campaign=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
Get Campaign

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'send_time,send_options.use_smart_sending'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tags,tags'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_campaign(self, id) -> Any:
        """
Delete Campaign

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign(self, id, data=None) -> dict[str, Any]:
        """
Update Campaign

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "audiences": {
                        "excluded": [
                          "<string>",
                          "<string>"
                        ],
                        "included": [
                          "<string>",
                          "<string>"
                        ]
                      },
                      "name": "<string>",
                      "send_options": {
                        "use_smart_sending": true
                      },
                      "send_strategy": {
                        "datetime": "<dateTime>",
                        "method": "static",
                        "options": {
                          "is_local": true,
                          "send_past_recipients_immediately": false
                        }
                      },
                      "tracking_options": {
                        "add_utm": "<boolean>",
                        "is_tracking_clicks": "<boolean>",
                        "is_tracking_opens": "<boolean>",
                        "utm_params": [
                          {
                            "name": "<string>",
                            "value": "<string>"
                          },
                          {
                            "name": "<string>",
                            "value": "<string>"
                          }
                        ]
                      }
                    },
                    "id": "<string>",
                    "type": "campaign"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaigns/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation(self, id, fields_campaign_recipient_estimation=None) -> dict[str, Any]:
        """
Get Campaign Recipient Estimation

        Args:
            id (string): id
            fields_campaign_recipient_estimation (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'estimated_recipient_count,estimated_recipient_count'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimations/{id}"
        query_params = {k: v for k, v in [('fields[campaign-recipient-estimation]', fields_campaign_recipient_estimation)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_campaign_clone(self, data=None) -> dict[str, Any]:
        """
Create Campaign Clone

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "new_name": "<string>"
                    },
                    "id": "<string>",
                    "type": "campaign"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-clone"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_campaign(self, id, fields_tag=None) -> dict[str, Any]:
        """
Get Tags for Campaign

        Args:
            id (string): id
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/tags"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_campaign(self, id) -> dict[str, Any]:
        """
Get Tag IDs for Campaign

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_messages_for_campaign(self, id, fields_campaign_message=None, fields_campaign=None, fields_image=None, fields_template=None, include=None) -> dict[str, Any]:
        """
Get Messages for Campaign

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'send_time,send_options.use_smart_sending'.
            fields_image (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'image_url,name'.
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'campaign,template'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/campaign-messages"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[image]', fields_image), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_message_ids_for_campaign(self, id) -> dict[str, Any]:
        """
Get Message IDs for Campaign

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaigns/{id}/relationships/campaign-messages"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_message(self, id, fields_campaign_message=None, fields_campaign=None, fields_image=None, fields_template=None, include=None) -> dict[str, Any]:
        """
Get Campaign Message

        Args:
            id (string): id
            fields_campaign_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.content.subject,created_at'.
            fields_campaign (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'send_time,send_options.use_smart_sending'.
            fields_image (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'image_url,name'.
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'campaign,template'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}"
        query_params = {k: v for k, v in [('fields[campaign-message]', fields_campaign_message), ('fields[campaign]', fields_campaign), ('fields[image]', fields_image), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_campaign_message(self, id, data=None) -> dict[str, Any]:
        """
Update Campaign Message

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "channel": "email",
                        "content": {
                          "bcc_email": "<string>",
                          "cc_email": "<string>",
                          "from_email": "<string>",
                          "from_label": "<string>",
                          "preview_text": "<string>",
                          "reply_to_email": "<string>",
                          "subject": "<string>"
                        },
                        "label": "<string>"
                      }
                    },
                    "id": "<string>",
                    "relationships": {
                      "image": {
                        "data": {
                          "id": "<string>",
                          "type": "image"
                        }
                      }
                    },
                    "type": "campaign-message"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-messages/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def assign_template_to_campaign_message(self, data=None) -> dict[str, Any]:
        """
Assign Template to Campaign Message

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "relationships": {
                      "template": {
                        "data": {
                          "id": "<string>",
                          "type": "template"
                        }
                      }
                    },
                    "type": "campaign-message"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-message-assign-template"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_for_campaign_message(self, id, fields_campaign=None) -> dict[str, Any]:
        """
Get Campaign for Campaign Message

        Args:
            id (string): id
            fields_campaign (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'send_time,send_options.use_smart_sending'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/campaign"
        query_params = {k: v for k, v in [('fields[campaign]', fields_campaign)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
Get Campaign ID for Campaign Message

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/campaign"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_for_campaign_message(self, id, fields_template=None) -> dict[str, Any]:
        """
Get Template for Campaign Message

        Args:
            id (string): id
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/template"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
Get Template ID for Campaign Message

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/template"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_for_campaign_message(self, id, fields_image=None) -> dict[str, Any]:
        """
Get Image for Campaign Message

        Args:
            id (string): id
            fields_image (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'image_url,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/image"
        query_params = {k: v for k, v in [('fields[image]', fields_image)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_id_for_campaign_message(self, id) -> dict[str, Any]:
        """
Get Image ID for Campaign Message

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/image"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image_for_campaign_message(self, id, data=None) -> Any:
        """
Update Image for Campaign Message

        Args:
            id (string): id
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "image"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-messages/{id}/relationships/image"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_send_job(self, id, fields_campaign_send_job=None) -> dict[str, Any]:
        """
Get Campaign Send Job

        Args:
            id (string): id
            fields_campaign_send_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-send-jobs/{id}"
        query_params = {k: v for k, v in [('fields[campaign-send-job]', fields_campaign_send_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancel_campaign_send(self, id, data=None) -> Any:
        """
Cancel Campaign Send

        Args:
            id (string): id
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "action": "cancel"
                    },
                    "id": "<string>",
                    "type": "campaign-send-job"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_recipient_estimation_job(self, id, fields_campaign_recipient_estimation_job=None) -> dict[str, Any]:
        """
Get Campaign Recipient Estimation Job

        Args:
            id (string): id
            fields_campaign_recipient_estimation_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs/{id}"
        query_params = {k: v for k, v in [('fields[campaign-recipient-estimation-job]', fields_campaign_recipient_estimation_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_campaign(self, data=None) -> dict[str, Any]:
        """
Send Campaign

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "campaign-send-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-send-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def refresh_campaign_recipient_estimation(self, data=None) -> dict[str, Any]:
        """
Refresh Campaign Recipient Estimation

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "type": "campaign-recipient-estimation-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-recipient-estimation-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_items(self, fields_catalog_item=None, fields_catalog_variant=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Catalog Items

        Args:
            fields_catalog_item (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'variants,variants'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-items"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_item(self, data=None) -> dict[str, Any]:
        """
Create Catalog Item

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "custom_metadata": {},
                      "description": "<string>",
                      "external_id": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "integration_type": "$custom",
                      "price": "<number>",
                      "published": true,
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "relationships": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_item(self, id, fields_catalog_item=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
Get Catalog Item

        Args:
            id (string): id
            fields_catalog_item (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_item(self, id) -> Any:
        """
Delete Catalog Item

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_item(self, id, data=None) -> dict[str, Any]:
        """
Update Catalog Item

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_metadata": {},
                      "description": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "price": "<number>",
                      "published": "<boolean>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_catalog_items_jobs(self, fields_catalog_item_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Bulk Create Catalog Items Jobs

        Args:
            fields_catalog_item_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-create-job]', fields_catalog_item_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_items(self, data=None) -> dict[str, Any]:
        """
Bulk Create Catalog Items

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "price": "<number>",
                              "published": true,
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "price": "<number>",
                              "published": true,
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_catalog_items_job(self, job_id, fields_catalog_item_bulk_create_job=None, fields_catalog_item=None, include=None) -> dict[str, Any]:
        """
Get Bulk Create Catalog Items Job

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_item (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'images,external_id'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'items,items'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-create-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-create-job]', fields_catalog_item_bulk_create_job), ('fields[catalog-item]', fields_catalog_item), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_update_catalog_items_jobs(self, fields_catalog_item_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Bulk Update Catalog Items Jobs

        Args:
            fields_catalog_item_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-update-job]', fields_catalog_item_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_items(self, data=None) -> dict[str, Any]:
        """
Bulk Update Catalog Items

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "price": "<number>",
                              "published": "<boolean>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          },
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "price": "<number>",
                              "published": "<boolean>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "categories": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-category"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-update-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_update_catalog_items_job(self, job_id, fields_catalog_item_bulk_update_job=None, fields_catalog_item=None, include=None) -> dict[str, Any]:
        """
Get Bulk Update Catalog Items Job

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_item (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'images,external_id'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'items,items'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-update-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-update-job]', fields_catalog_item_bulk_update_job), ('fields[catalog-item]', fields_catalog_item), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_delete_catalog_items_jobs(self, fields_catalog_item_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Bulk Delete Catalog Items Jobs

        Args:
            fields_catalog_item_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-delete-job]', fields_catalog_item_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_items(self, data=None) -> dict[str, Any]:
        """
Bulk Delete Catalog Items

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-item-bulk-delete-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_delete_catalog_items_job(self, job_id, fields_catalog_item_bulk_delete_job=None) -> dict[str, Any]:
        """
Get Bulk Delete Catalog Items Job

        Args:
            job_id (string): job_id
            fields_catalog_item_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-item-bulk-delete-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-item-bulk-delete-job]', fields_catalog_item_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_for_catalog_category(self, id, fields_catalog_item=None, fields_catalog_variant=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Items for Catalog Category

        Args:
            id (string): id
            fields_catalog_item (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'images,external_id'.
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'variants,variants'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/items"
        query_params = {k: v for k, v in [('fields[catalog-item]', fields_catalog_item), ('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_category_ids_for_catalog_item(self, id, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Category IDs for Catalog Item

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_categories_to_catalog_item(self, id, data=None) -> Any:
        """
Add Categories to Catalog Item

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-category'}, {'id': '<string>', 'type': 'catalog-category'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_categories_from_catalog_item(self, id, data=None) -> Any:
        """
Remove Categories from Catalog Item

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-category'}, {'id': '<string>', 'type': 'catalog-category'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_categories_for_catalog_item(self, id, data=None) -> Any:
        """
Update Categories for Catalog Item

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-category'}, {'id': '<string>', 'type': 'catalog-category'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-category"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/categories"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variants(self, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Catalog Variants

        Args:
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-variants"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_variant(self, data=None) -> dict[str, Any]:
        """
Create Catalog Variant

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "custom_metadata": {},
                      "description": "<string>",
                      "external_id": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "integration_type": "$custom",
                      "inventory_policy": 0,
                      "inventory_quantity": "<number>",
                      "price": "<number>",
                      "published": true,
                      "sku": "<string>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "relationships": {
                      "item": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-item"
                        }
                      }
                    },
                    "type": "catalog-variant"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_variant(self, id, fields_catalog_variant=None) -> dict[str, Any]:
        """
Get Catalog Variant

        Args:
            id (string): id
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_variant(self, id) -> Any:
        """
Delete Catalog Variant

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_variant(self, id, data=None) -> dict[str, Any]:
        """
Update Catalog Variant

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_metadata": {},
                      "description": "<string>",
                      "image_full_url": "<string>",
                      "image_thumbnail_url": "<string>",
                      "images": [
                        "<string>",
                        "<string>"
                      ],
                      "inventory_policy": 0,
                      "inventory_quantity": "<number>",
                      "price": "<number>",
                      "published": "<boolean>",
                      "sku": "<string>",
                      "title": "<string>",
                      "url": "<string>"
                    },
                    "id": "<string>",
                    "type": "catalog-variant"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variants/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_jobs(self, fields_catalog_variant_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Create Variants Jobs

        Args:
            fields_catalog_variant_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-create-job]', fields_catalog_variant_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_variants(self, data=None) -> dict[str, Any]:
        """
Bulk Create Catalog Variants

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": true,
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "item": {
                                "data": {
                                  "id": "<string>",
                                  "type": "catalog-item"
                                }
                              }
                            },
                            "type": "catalog-variant"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "custom_metadata": {},
                              "description": "<string>",
                              "external_id": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "integration_type": "$custom",
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": true,
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "relationships": {
                              "item": {
                                "data": {
                                  "id": "<string>",
                                  "type": "catalog-item"
                                }
                              }
                            },
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_variants_job(self, job_id, fields_catalog_variant_bulk_create_job=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
Get Create Variants Job

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-create-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-create-job]', fields_catalog_variant_bulk_create_job), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_jobs(self, fields_catalog_variant_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Update Variants Jobs

        Args:
            fields_catalog_variant_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-update-job]', fields_catalog_variant_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_variants(self, data=None) -> dict[str, Any]:
        """
Bulk Update Catalog Variants

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "inventory_policy": 2,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": "<boolean>",
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "type": "catalog-variant"
                          },
                          {
                            "attributes": {
                              "custom_metadata": {},
                              "description": "<string>",
                              "image_full_url": "<string>",
                              "image_thumbnail_url": "<string>",
                              "images": [
                                "<string>",
                                "<string>"
                              ],
                              "inventory_policy": 0,
                              "inventory_quantity": "<number>",
                              "price": "<number>",
                              "published": "<boolean>",
                              "sku": "<string>",
                              "title": "<string>",
                              "url": "<string>"
                            },
                            "id": "<string>",
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-update-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_variants_job(self, job_id, fields_catalog_variant_bulk_update_job=None, fields_catalog_variant=None, include=None) -> dict[str, Any]:
        """
Get Update Variants Job

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'variants,variants'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-update-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-update-job]', fields_catalog_variant_bulk_update_job), ('fields[catalog-variant]', fields_catalog_variant), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_jobs(self, fields_catalog_variant_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Delete Variants Jobs

        Args:
            fields_catalog_variant_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-delete-job]', fields_catalog_variant_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_variants(self, data=None) -> dict[str, Any]:
        """
Bulk Delete Catalog Variants

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "variants": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-variant"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-variant"
                          }
                        ]
                      }
                    },
                    "type": "catalog-variant-bulk-delete-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_variants_job(self, job_id, fields_catalog_variant_bulk_delete_job=None) -> dict[str, Any]:
        """
Get Delete Variants Job

        Args:
            job_id (string): job_id
            fields_catalog_variant_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-variant-bulk-delete-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-variant-bulk-delete-job]', fields_catalog_variant_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_variants_for_catalog_item(self, id, fields_catalog_variant=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Variants for Catalog Item

        Args:
            id (string): id
            fields_catalog_variant (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'title,price'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/variants"
        query_params = {k: v for k, v in [('fields[catalog-variant]', fields_catalog_variant), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_variant_ids_for_catalog_item(self, id, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Variant IDs for Catalog Item

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`sku`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/relationships/variants"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_categories(self, fields_catalog_category=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Catalog Categories

        Args:
            fields_catalog_category (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-categories"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_catalog_category(self, data=None) -> dict[str, Any]:
        """
Create Catalog Category

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "catalog_type": "$default",
                      "external_id": "<string>",
                      "integration_type": "$custom",
                      "name": "<string>"
                    },
                    "relationships": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_catalog_category(self, id, fields_catalog_category=None) -> dict[str, Any]:
        """
Get Catalog Category

        Args:
            id (string): id
            fields_catalog_category (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_catalog_category(self, id) -> Any:
        """
Delete Catalog Category

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_catalog_category(self, id, data=None) -> dict[str, Any]:
        """
Update Catalog Category

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "items": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-item"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_jobs(self, fields_catalog_category_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Create Categories Jobs

        Args:
            fields_catalog_category_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-create-job]', fields_catalog_category_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_catalog_categories(self, data=None) -> dict[str, Any]:
        """
Bulk Create Catalog Categories

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "external_id": "<string>",
                              "integration_type": "$custom",
                              "name": "<string>"
                            },
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          },
                          {
                            "attributes": {
                              "catalog_type": "$default",
                              "external_id": "<string>",
                              "integration_type": "$custom",
                              "name": "<string>"
                            },
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_create_categories_job(self, job_id, fields_catalog_category_bulk_create_job=None, fields_catalog_category=None, include=None) -> dict[str, Any]:
        """
Get Create Categories Job

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_category (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'categories,categories'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-create-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-create-job]', fields_catalog_category_bulk_create_job), ('fields[catalog-category]', fields_catalog_category), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_jobs(self, fields_catalog_category_bulk_update_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Update Categories Jobs

        Args:
            fields_catalog_category_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-update-job]', fields_catalog_category_bulk_update_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_catalog_categories(self, data=None) -> dict[str, Any]:
        """
Bulk Update Catalog Categories

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "attributes": {
                              "name": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          },
                          {
                            "attributes": {
                              "name": "<string>"
                            },
                            "id": "<string>",
                            "relationships": {
                              "items": {
                                "data": [
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  },
                                  {
                                    "id": "<string>",
                                    "type": "catalog-item"
                                  }
                                ]
                              }
                            },
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-update-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_update_categories_job(self, job_id, fields_catalog_category_bulk_update_job=None, fields_catalog_category=None, include=None) -> dict[str, Any]:
        """
Get Update Categories Job

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_update_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_catalog_category (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'categories,categories'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-update-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-update-job]', fields_catalog_category_bulk_update_job), ('fields[catalog-category]', fields_catalog_category), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_jobs(self, fields_catalog_category_bulk_delete_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Delete Categories Jobs

        Args:
            fields_catalog_category_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-delete-job]', fields_catalog_category_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_delete_catalog_categories(self, data=None) -> dict[str, Any]:
        """
Bulk Delete Catalog Categories

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "categories": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          },
                          {
                            "id": "<string>",
                            "type": "catalog-category"
                          }
                        ]
                      }
                    },
                    "type": "catalog-category-bulk-delete-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_delete_categories_job(self, job_id, fields_catalog_category_bulk_delete_job=None) -> dict[str, Any]:
        """
Get Delete Categories Job

        Args:
            job_id (string): job_id
            fields_catalog_category_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/catalog-category-bulk-delete-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[catalog-category-bulk-delete-job]', fields_catalog_category_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_item_ids_for_catalog_category(self, id, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Item IDs for Catalog Category

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`category.id`: `equals`<br>`title`: `contains`<br>`published`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_items_to_catalog_category(self, id, data=None) -> Any:
        """
Add Items to Catalog Category

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-item'}, {'id': '<string>', 'type': 'catalog-item'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_items_from_catalog_category(self, id, data=None) -> Any:
        """
Remove Items from Catalog Category

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-item'}, {'id': '<string>', 'type': 'catalog-item'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_items_for_catalog_category(self, id, data=None) -> Any:
        """
Update Items for Catalog Category

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'catalog-item'}, {'id': '<string>', 'type': 'catalog-item'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    },
                    {
                      "id": "<string>",
                      "type": "catalog-item"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/catalog-categories/{id}/relationships/items"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_categories_for_catalog_item(self, id, fields_catalog_category=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Categories for Catalog Item

        Args:
            id (string): id
            fields_catalog_category (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`ids`: `any`<br>`item.id`: `equals`<br>`name`: `contains` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/catalog-items/{id}/categories"
        query_params = {k: v for k, v in [('fields[catalog-category]', fields_catalog_category), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_back_in_stock_subscription(self, data=None) -> Any:
        """
Create Back In Stock Subscription

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "channels": [
                        "PUSH",
                        "SMS"
                      ],
                      "profile": {
                        "data": {
                          "attributes": {
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "variant": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-variant"
                        }
                      }
                    },
                    "type": "back-in-stock-subscription"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/back-in-stock-subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_subscription(self, company_id=None, data=None) -> Any:
        """
Create Client Subscription

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_source": "<string>",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "subscriptions": {
                              "email": {
                                "marketing": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                }
                              },
                              "sms": {
                                "marketing": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                },
                                "transactional": {
                                  "consent": "SUBSCRIBED",
                                  "consented_at": "<dateTime>"
                                }
                              }
                            },
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "subscription"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/subscriptions"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_client_push_token(self, company_id=None, data=None) -> Any:
        """
Create or Update Client Push Token

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "background": "AVAILABLE",
                      "device_metadata": {
                        "app_build": "<string>",
                        "app_id": "<string>",
                        "app_name": "<string>",
                        "app_version": "<string>",
                        "device_id": "<string>",
                        "device_model": "<string>",
                        "environment": "debug",
                        "klaviyo_sdk": "android",
                        "manufacturer": "<string>",
                        "os_name": "ipados",
                        "os_version": "<string>",
                        "sdk_version": "<string>"
                      },
                      "enablement_status": "AUTHORIZED",
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "apns"
                    },
                    "type": "push-token"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-tokens"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unregister_client_push_token(self, company_id=None, data=None) -> Any:
        """
Unregister Client Push Token

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "meta": {
                            "patch_properties": {
                              "append": {},
                              "unappend": {},
                              "unset": "<string>"
                            }
                          },
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "fcm"
                    },
                    "type": "push-token-unregister"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/push-token-unregister"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_event(self, company_id=None, data=None) -> Any:
        """
Create Client Event

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "metric": {
                        "data": {
                          "attributes": {
                            "name": "<string>",
                            "service": "<string>"
                          },
                          "type": "metric"
                        }
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "properties": {},
                      "time": "<dateTime>",
                      "unique_id": "<string>",
                      "value": "<number>",
                      "value_currency": "<string>"
                    },
                    "type": "event"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/events"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_client_profile(self, company_id=None, data=None) -> Any:
        """
Create or Update Client Profile

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "_kx": "<string>",
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/profiles"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_client_events(self, company_id=None, data=None) -> Any:
        """
Bulk Create Client Events

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "events": {
                        "data": [
                          {
                            "attributes": {
                              "metric": {
                                "data": {
                                  "attributes": {
                                    "name": "<string>",
                                    "service": "<string>"
                                  },
                                  "type": "metric"
                                }
                              },
                              "properties": {},
                              "time": "<dateTime>",
                              "unique_id": "<string>",
                              "value": "<number>",
                              "value_currency": "<string>"
                            },
                            "type": "event"
                          },
                          {
                            "attributes": {
                              "metric": {
                                "data": {
                                  "attributes": {
                                    "name": "<string>",
                                    "service": "<string>"
                                  },
                                  "type": "metric"
                                }
                              },
                              "properties": {},
                              "time": "<dateTime>",
                              "unique_id": "<string>",
                              "value": "<number>",
                              "value_currency": "<string>"
                            },
                            "type": "event"
                          }
                        ]
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "meta": {
                            "patch_properties": {
                              "append": {},
                              "unappend": {},
                              "unset": "<string>"
                            }
                          },
                          "type": "profile"
                        }
                      }
                    },
                    "type": "event-bulk-create"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/event-bulk-create"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_client_back_in_stock_subscription(self, company_id=None, data=None) -> Any:
        """
Create Client Back In Stock Subscription

        Args:
            company_id (string): (Required) Your Public API Key / Site ID. See [this article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details. Example: '{{companyId}}'.
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "channels": [
                        "SMS",
                        "PUSH"
                      ],
                      "profile": {
                        "data": {
                          "attributes": {
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "relationships": {
                      "variant": {
                        "data": {
                          "id": "<string>",
                          "type": "catalog-variant"
                        }
                      }
                    },
                    "type": "back-in-stock-subscription"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/client/back-in-stock-subscriptions"
        query_params = {k: v for k, v in [('company_id', company_id)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupons(self, fields_coupon=None, page_cursor=None) -> dict[str, Any]:
        """
Get Coupons

        Args:
            fields_coupon (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/coupons"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon(self, data=None) -> dict[str, Any]:
        """
Create Coupon

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "external_id": "<string>"
                    },
                    "type": "coupon"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon(self, id, fields_coupon=None) -> dict[str, Any]:
        """
Get Coupon

        Args:
            id (string): id
            fields_coupon (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon(self, id) -> Any:
        """
Delete Coupon

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon(self, id, data=None) -> dict[str, Any]:
        """
Update Coupon

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>"
                    },
                    "id": "<string>",
                    "type": "coupon"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupons/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes(self, fields_coupon_code=None, fields_coupon=None, filter=None, include=None, page_cursor=None) -> dict[str, Any]:
        """
Get Coupon Codes

        Args:
            fields_coupon_code (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,unique_code'.
            fields_coupon (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'coupon,coupon'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/coupon-codes"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('fields[coupon]', fields_coupon), ('filter', filter), ('include', include), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_coupon_code(self, data=None) -> dict[str, Any]:
        """
Create Coupon Code

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "expires_at": "<dateTime>",
                      "unique_code": "<string>"
                    },
                    "relationships": {
                      "coupon": {
                        "data": {
                          "id": "<string>",
                          "type": "coupon"
                        }
                      }
                    },
                    "type": "coupon-code"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code(self, id, fields_coupon_code=None, fields_coupon=None, include=None) -> dict[str, Any]:
        """
Get Coupon Code

        Args:
            id (string): id
            fields_coupon_code (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,unique_code'.
            fields_coupon (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'coupon,coupon'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('fields[coupon]', fields_coupon), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_coupon_code(self, id) -> Any:
        """
Delete Coupon Code

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_coupon_code(self, id, data=None) -> dict[str, Any]:
        """
Update Coupon Code

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "expires_at": "<dateTime>",
                      "status": "USED"
                    },
                    "id": "<string>",
                    "type": "coupon-code"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-codes/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_coupon_code_jobs(self, fields_coupon_code_bulk_create_job=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Bulk Create Coupon Code Jobs

        Args:
            fields_coupon_code_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs"
        query_params = {k: v for k, v in [('fields[coupon-code-bulk-create-job]', fields_coupon_code_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_coupon_codes(self, data=None) -> dict[str, Any]:
        """
Bulk Create Coupon Codes

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "coupon-codes": {
                        "data": [
                          {
                            "attributes": {
                              "expires_at": "<dateTime>",
                              "unique_code": "<string>"
                            },
                            "relationships": {
                              "coupon": {
                                "data": {
                                  "id": "<string>",
                                  "type": "coupon"
                                }
                              }
                            },
                            "type": "coupon-code"
                          },
                          {
                            "attributes": {
                              "expires_at": "<dateTime>",
                              "unique_code": "<string>"
                            },
                            "relationships": {
                              "coupon": {
                                "data": {
                                  "id": "<string>",
                                  "type": "coupon"
                                }
                              }
                            },
                            "type": "coupon-code"
                          }
                        ]
                      }
                    },
                    "type": "coupon-code-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_create_coupon_codes_job(self, job_id, fields_coupon_code_bulk_create_job=None, fields_coupon_code=None, include=None) -> dict[str, Any]:
        """
Get Bulk Create Coupon Codes Job

        Args:
            job_id (string): job_id
            fields_coupon_code_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'errors,failed_count'.
            fields_coupon_code (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,unique_code'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'coupon-codes,coupon-codes'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/coupon-code-bulk-create-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[coupon-code-bulk-create-job]', fields_coupon_code_bulk_create_job), ('fields[coupon-code]', fields_coupon_code), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_for_coupon_code(self, id, fields_coupon=None) -> dict[str, Any]:
        """
Get Coupon For Coupon Code

        Args:
            id (string): id
            fields_coupon (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'external_id,external_id'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/coupon"
        query_params = {k: v for k, v in [('fields[coupon]', fields_coupon)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_id_for_coupon_code(self, id) -> dict[str, Any]:
        """
Get Coupon ID for Coupon Code

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupon-codes/{id}/relationships/coupon"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_codes_for_coupon(self, id, fields_coupon_code=None, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Coupon Codes for Coupon

        Args:
            id (string): id
            fields_coupon_code (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,unique_code'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/coupon-codes"
        query_params = {k: v for k, v in [('fields[coupon-code]', fields_coupon_code), ('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_coupon_code_ids_for_coupon(self, id, filter=None, page_cursor=None) -> dict[str, Any]:
        """
Get Coupon Code IDs for Coupon

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`expires_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals`<br>`coupon.id`: `any`, `equals`<br>`profile.id`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/coupons/{id}/relationships/coupon-codes"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def request_profile_deletion(self, data=None) -> Any:
        """
Request Profile Deletion

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profile": {
                        "data": {
                          "attributes": {
                            "email": "<string>",
                            "phone_number": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      }
                    },
                    "type": "data-privacy-deletion-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/data-privacy-deletion-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events(self, fields_event=None, fields_metric=None, fields_profile=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Events

        Args:
            fields_event (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'uuid,datetime'.
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.country,location.zip'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`metric_id`: `equals`<br>`profile_id`: `equals`<br>`profile`: `has`<br>`datetime`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'attributions,metric'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'datetime'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/events"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[metric]', fields_metric), ('fields[profile]', fields_profile), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_event(self, data=None) -> Any:
        """
Create Event

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "metric": {
                        "data": {
                          "attributes": {
                            "name": "<string>",
                            "service": "<string>"
                          },
                          "type": "metric"
                        }
                      },
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "properties": {},
                      "time": "<dateTime>",
                      "unique_id": "<string>",
                      "value": "<number>",
                      "value_currency": "<string>"
                    },
                    "type": "event"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/events"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(self, id, fields_event=None, fields_metric=None, fields_profile=None, include=None) -> dict[str, Any]:
        """
Get Event

        Args:
            id (string): id
            fields_event (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'uuid,datetime'.
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.country,location.zip'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'attributions,metric'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[metric]', fields_metric), ('fields[profile]', fields_profile), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_create_events(self, data=None) -> Any:
        """
Bulk Create Events

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "events-bulk-create": {
                        "data": [
                          {
                            "attributes": {
                              "events": {
                                "data": [
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  },
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  }
                                ]
                              },
                              "profile": {
                                "data": {
                                  "attributes": {
                                    "_kx": "<string>",
                                    "anonymous_id": "<string>",
                                    "email": "<string>",
                                    "external_id": "<string>",
                                    "first_name": "<string>",
                                    "image": "<string>",
                                    "last_name": "<string>",
                                    "locale": "<string>",
                                    "location": {
                                      "address1": "<string>",
                                      "address2": "<string>",
                                      "city": "<string>",
                                      "country": "<string>",
                                      "ip": "<string>",
                                      "latitude": "<string>",
                                      "longitude": "<string>",
                                      "region": "<string>",
                                      "timezone": "<string>",
                                      "zip": "<string>"
                                    },
                                    "organization": "<string>",
                                    "phone_number": "<string>",
                                    "properties": {},
                                    "title": "<string>"
                                  },
                                  "id": "<string>",
                                  "meta": {
                                    "patch_properties": {
                                      "append": {},
                                      "unappend": {},
                                      "unset": "<string>"
                                    }
                                  },
                                  "type": "profile"
                                }
                              }
                            },
                            "type": "event-bulk-create"
                          },
                          {
                            "attributes": {
                              "events": {
                                "data": [
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  },
                                  {
                                    "attributes": {
                                      "metric": {
                                        "data": {
                                          "attributes": {
                                            "name": "<string>",
                                            "service": "<string>"
                                          },
                                          "type": "metric"
                                        }
                                      },
                                      "properties": {},
                                      "time": "<dateTime>",
                                      "unique_id": "<string>",
                                      "value": "<number>",
                                      "value_currency": "<string>"
                                    },
                                    "type": "event"
                                  }
                                ]
                              },
                              "profile": {
                                "data": {
                                  "attributes": {
                                    "_kx": "<string>",
                                    "anonymous_id": "<string>",
                                    "email": "<string>",
                                    "external_id": "<string>",
                                    "first_name": "<string>",
                                    "image": "<string>",
                                    "last_name": "<string>",
                                    "locale": "<string>",
                                    "location": {
                                      "address1": "<string>",
                                      "address2": "<string>",
                                      "city": "<string>",
                                      "country": "<string>",
                                      "ip": "<string>",
                                      "latitude": "<string>",
                                      "longitude": "<string>",
                                      "region": "<string>",
                                      "timezone": "<string>",
                                      "zip": "<string>"
                                    },
                                    "organization": "<string>",
                                    "phone_number": "<string>",
                                    "properties": {},
                                    "title": "<string>"
                                  },
                                  "id": "<string>",
                                  "meta": {
                                    "patch_properties": {
                                      "append": {},
                                      "unappend": {},
                                      "unset": "<string>"
                                    }
                                  },
                                  "type": "profile"
                                }
                              }
                            },
                            "type": "event-bulk-create"
                          }
                        ]
                      }
                    },
                    "type": "event-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/event-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_for_event(self, id, fields_metric=None) -> dict[str, Any]:
        """
Get Metric for Event

        Args:
            id (string): id
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/metric"
        query_params = {k: v for k, v in [('fields[metric]', fields_metric)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_id_for_event(self, id) -> dict[str, Any]:
        """
Get Metric ID for Event

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/metric"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_for_event(self, id, additional_fields_profile=None, fields_profile=None) -> dict[str, Any]:
        """
Get Profile for Event

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address2,subscriptions.sms.marketing.last_updated'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/profile"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_id_for_event(self, id) -> dict[str, Any]:
        """
Get Profile ID for Event

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/events/{id}/relationships/profile"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows(self, fields_flow_action=None, fields_flow=None, fields_tag=None, filter=None, include=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Flows

        Args:
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`status`: `equals`<br>`archived`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`trigger_type`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tags,flow-actions'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/flows"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow]', fields_flow), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_flow(self, additional_fields_flow=None, data=None) -> dict[str, Any]:
        """
Create Flow

        Args:
            additional_fields_flow (string): Request additional fields not included by default in the response. Supported values: 'definition' Example: 'definition,definition'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "actions": [
                          {
                            "id": "<string>",
                            "links": {
                              "next": "<string>"
                            },
                            "temporary_id": "<string>",
                            "type": "back-in-stock-delay"
                          },
                          {
                            "id": "<string>",
                            "links": {
                              "next": "<string>"
                            },
                            "temporary_id": "<string>",
                            "type": "back-in-stock-delay"
                          }
                        ],
                        "entry_action_id": "<string>",
                        "profile_filter": {
                          "condition_groups": [
                            {
                              "conditions": [
                                {
                                  "filter": {
                                    "operator": "not-starts-with",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                },
                                {
                                  "filter": {
                                    "operator": "not-equals",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                }
                              ]
                            },
                            {
                              "conditions": [
                                {
                                  "filter": {
                                    "operator": "equals",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                },
                                {
                                  "filter": {
                                    "operator": "not-starts-with",
                                    "type": "string",
                                    "value": "<string>"
                                  },
                                  "property": "<string>",
                                  "type": "profile-property"
                                }
                              ]
                            }
                          ]
                        },
                        "triggers": [
                          {
                            "id": "<string>",
                            "type": "list"
                          },
                          {
                            "id": "<string>",
                            "type": "list"
                          }
                        ]
                      },
                      "name": "<string>"
                    },
                    "type": "flow"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flows"
        query_params = {k: v for k, v in [('additional-fields[flow]', additional_fields_flow)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow(self, id, additional_fields_flow=None, fields_flow_action=None, fields_flow=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
Get Flow

        Args:
            id (string): id
            additional_fields_flow (string): Request additional fields not included by default in the response. Supported values: 'definition' Example: 'definition,definition'.
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'status,definition.triggers'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tags,flow-actions'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {k: v for k, v in [('additional-fields[flow]', additional_fields_flow), ('fields[flow-action]', fields_flow_action), ('fields[flow]', fields_flow), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_flow(self, id) -> Any:
        """
Delete Flow

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_flow_status(self, id, data=None) -> dict[str, Any]:
        """
Update Flow Status

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "status": "<string>"
                    },
                    "id": "<string>",
                    "type": "flow"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flows/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_action(self, id, fields_flow_action=None, fields_flow_message=None, fields_flow=None, include=None) -> dict[str, Any]:
        """
Get Flow Action

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'content.cc_email,content.reply_to_email'.
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-messages,flow-messages'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow-message]', fields_flow_message), ('fields[flow]', fields_flow), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_message(self, id, fields_flow_action=None, fields_flow_message=None, fields_template=None, include=None) -> dict[str, Any]:
        """
Get Flow Message

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            fields_flow_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'content.cc_email,content.reply_to_email'.
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'template,template'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('fields[flow-message]', fields_flow_message), ('fields[template]', fields_template), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_actions_for_flow(self, id, fields_flow_action=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Actions for Flow

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`<br>`action_type`: `any`, `equals`<br>`status`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'action_type'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/flow-actions"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_ids_for_flow(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Action IDs for Flow

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`<br>`action_type`: `any`, `equals`<br>`status`: `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'action_type'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/flow-actions"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_flow(self, id, fields_tag=None) -> dict[str, Any]:
        """
Get Tags for Flow

        Args:
            id (string): id
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/tags"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_flow(self, id) -> dict[str, Any]:
        """
Get Tag IDs for Flow

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flows/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_for_flow_action(self, id, fields_flow=None) -> dict[str, Any]:
        """
Get Flow for Flow Action

        Args:
            id (string): id
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_id_for_flow_action(self, id) -> dict[str, Any]:
        """
Get Flow ID for Flow Action

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_messages_for_flow_action(self, id, fields_flow_message=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Messages For Flow Action

        Args:
            id (string): id
            fields_flow_message (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'content.cc_email,content.reply_to_email'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/flow-messages"
        query_params = {k: v for k, v in [('fields[flow-message]', fields_flow_message), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_message_ids_for_flow_action(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Message IDs for Flow Action

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 50. Min: 1. Max: 50. Example: '50'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-actions/{id}/relationships/flow-messages"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_for_flow_message(self, id, fields_flow_action=None) -> dict[str, Any]:
        """
Get Action for Flow Message

        Args:
            id (string): id
            fields_flow_action (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'render_options.add_org_prefix,send_options.is_transactional'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/flow-action"
        query_params = {k: v for k, v in [('fields[flow-action]', fields_flow_action)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_action_id_for_flow_message(self, id) -> dict[str, Any]:
        """
Get Action ID for Flow Message

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/flow-action"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_for_flow_message(self, id, fields_template=None) -> dict[str, Any]:
        """
Get Template for Flow Message

        Args:
            id (string): id
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/template"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_id_for_flow_message(self, id) -> dict[str, Any]:
        """
Get Template ID for Flow Message

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/flow-messages/{id}/relationships/template"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_forms(self, fields_form=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Forms

        Args:
            fields_form (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,ab_test'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `contains`, `equals`<br>`ab_test`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`status`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-created_at'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/forms"
        query_params = {k: v for k, v in [('fields[form]', fields_form), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form(self, id, fields_form_version=None, fields_form=None, include=None) -> dict[str, Any]:
        """
Get Form

        Args:
            id (string): id
            fields_form_version (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated_at,form_type'.
            fields_form (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,ab_test'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'form-versions,form-versions'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version), ('fields[form]', fields_form), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_version(self, id, fields_form_version=None) -> dict[str, Any]:
        """
Get Form Version

        Args:
            id (string): id
            fields_form_version (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated_at,form_type'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_versions_for_form(self, id, fields_form_version=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Versions for Form

        Args:
            id (string): id
            fields_form_version (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated_at,form_type'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`form_type`: `any`, `equals`<br>`status`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-created_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/form-versions"
        query_params = {k: v for k, v in [('fields[form-version]', fields_form_version), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_version_ids_for_form(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Version IDs for Form

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`form_type`: `any`, `equals`<br>`status`: `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`created_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-created_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/forms/{id}/relationships/form-versions"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_for_form_version(self, id, fields_form=None) -> dict[str, Any]:
        """
Get Form for Form Version

        Args:
            id (string): id
            fields_form (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,ab_test'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/form"
        query_params = {k: v for k, v in [('fields[form]', fields_form)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_form_id_for_form_version(self, id) -> dict[str, Any]:
        """
Get Form ID for Form Version

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/form-versions/{id}/relationships/form"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_images(self, fields_image=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Images

        Args:
            fields_image (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'image_url,name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`, `equals`<br>`updated_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`format`: `any`, `equals`<br>`name`: `any`, `contains`, `ends-with`, `equals`, `starts-with`<br>`size`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`hidden`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-format'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/images"
        query_params = {k: v for k, v in [('fields[image]', fields_image), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_image_from_url(self, data=None) -> dict[str, Any]:
        """
Upload Image From URL

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "hidden": false,
                      "import_from_url": "<string>",
                      "name": "<string>"
                    },
                    "type": "image"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/images"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image(self, id, fields_image=None) -> dict[str, Any]:
        """
Get Image

        Args:
            id (string): id
            fields_image (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'image_url,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/images/{id}"
        query_params = {k: v for k, v in [('fields[image]', fields_image)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image(self, id, data=None) -> dict[str, Any]:
        """
Update Image

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "hidden": "<boolean>",
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "image"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/images/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

  
        """
Upload Image From File

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/image-upload"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_lists(self, fields_flow=None, fields_list=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Lists

        Args:
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `any`, `equals`<br>`id`: `any`, `equals`<br>`created`: `greater-than`<br>`updated`: `greater-than` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,tags'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/lists"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow), ('fields[list]', fields_list), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_list(self, data=None) -> dict[str, Any]:
        """
Create List

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "type": "list"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list(self, id, additional_fields_list=None, fields_flow=None, fields_list=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
Get List

        Args:
            id (string): id
            additional_fields_list (string): Request additional fields not included by default in the response. Supported values: 'profile_count' Example: 'profile_count,profile_count'.
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,tags'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {k: v for k, v in [('additional-fields[list]', additional_fields_list), ('fields[flow]', fields_flow), ('fields[list]', fields_list), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_list(self, id) -> Any:
        """
Delete List

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_list(self, id, data=None) -> dict[str, Any]:
        """
Update List

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "list"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_list(self, id, fields_tag=None) -> dict[str, Any]:
        """
Get Tags for List

        Args:
            id (string): id
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/tags"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_list(self, id) -> dict[str, Any]:
        """
Get Tag IDs for List

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_list(self, id, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Profiles for List

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address1,first_name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/profiles"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_list(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Profile IDs for List

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_profiles_to_list(self, id, data=None) -> Any:
        """
Add Profiles to List

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'profile'}, {'id': '<string>', 'type': 'profile'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "profile"
                    },
                    {
                      "id": "<string>",
                      "type": "profile"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_profiles_from_list(self, id, data=None) -> Any:
        """
Remove Profiles from List

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'profile'}, {'id': '<string>', 'type': 'profile'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "profile"
                    },
                    {
                      "id": "<string>",
                      "type": "profile"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/lists/{id}/relationships/profiles"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_list(self, id, fields_flow=None) -> dict[str, Any]:
        """
Get Flows Triggered by List

        Args:
            id (string): id
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/flow-triggers"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_list(self, id) -> dict[str, Any]:
        """
Get IDs for Flows Triggered by List

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/lists/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metrics(self, fields_flow=None, fields_metric=None, filter=None, include=None, page_cursor=None) -> dict[str, Any]:
        """
Get Metrics

        Args:
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`integration.name`: `equals`<br>`integration.category`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,flow-triggers'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/metrics"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow), ('fields[metric]', fields_metric), ('filter', filter), ('include', include), ('page[cursor]', page_cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric(self, id, fields_flow=None, fields_metric=None, include=None) -> dict[str, Any]:
        """
Get Metric

        Args:
            id (string): id
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,flow-triggers'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow), ('fields[metric]', fields_metric), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_property(self, id, additional_fields_metric_property=None, fields_metric_property=None, fields_metric=None, include=None) -> dict[str, Any]:
        """
Get Metric Property

        Args:
            id (string): id
            additional_fields_metric_property (string): Request additional fields not included by default in the response. Supported values: 'sample_values' Example: 'sample_values,sample_values'.
            fields_metric_property (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'sample_values,property'.
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'metric,metric'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}"
        query_params = {k: v for k, v in [('additional-fields[metric-property]', additional_fields_metric_property), ('fields[metric-property]', fields_metric_property), ('fields[metric]', fields_metric), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_metric_aggregates(self, data=None) -> dict[str, Any]:
        """
Query Metric Aggregates

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "by": [
                        "$attributed_channel",
                        "Client Type"
                      ],
                      "filter": [
                        "<string>",
                        "<string>"
                      ],
                      "interval": "day",
                      "measurements": [
                        "unique",
                        "unique"
                      ],
                      "metric_id": "<string>",
                      "page_cursor": "<string>",
                      "page_size": 500,
                      "return_fields": [
                        "<string>",
                        "<string>"
                      ],
                      "sort": "-URL",
                      "timezone": "UTC"
                    },
                    "type": "metric-aggregate"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/metric-aggregates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_metric(self, id, fields_flow=None) -> dict[str, Any]:
        """
Get Flows Triggered by Metric

        Args:
            id (string): id
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/flow-triggers"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_metric(self, id) -> dict[str, Any]:
        """
Get IDs for Flows Triggered by Metric

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_properties_for_metric(self, id, additional_fields_metric_property=None, fields_metric_property=None) -> dict[str, Any]:
        """
Get Properties for Metric

        Args:
            id (string): id
            additional_fields_metric_property (string): Request additional fields not included by default in the response. Supported values: 'sample_values' Example: 'sample_values,sample_values'.
            fields_metric_property (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'sample_values,property'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/metric-properties"
        query_params = {k: v for k, v in [('additional-fields[metric-property]', additional_fields_metric_property), ('fields[metric-property]', fields_metric_property)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_property_ids_for_metric(self, id) -> dict[str, Any]:
        """
Get Property IDs for Metric

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metrics/{id}/relationships/metric-properties"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_for_metric_property(self, id, fields_metric=None) -> dict[str, Any]:
        """
Get Metric for Metric Property

        Args:
            id (string): id
            fields_metric (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'integration,created'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}/metric"
        query_params = {k: v for k, v in [('fields[metric]', fields_metric)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_metric_id_for_metric_property(self, id) -> dict[str, Any]:
        """
Get Metric ID for Metric Property

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/metric-properties/{id}/relationships/metric"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles(self, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Profiles

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`, `equals`<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`external_id`: `any`, `equals`<br>`_kx`: `equals`<br>`created`: `greater-than`, `less-than`<br>`updated`: `greater-than`, `less-than`<br>`subscriptions.email.marketing.list_suppressions.reason`: `equals`<br>`subscriptions.email.marketing.list_suppressions.timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`subscriptions.email.marketing.list_suppressions.list_id`: `equals`<br>`subscriptions.email.marketing.suppression.reason`: `equals`<br>`subscriptions.email.marketing.suppression.timestamp`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-subscriptions.email.marketing.suppression.timestamp'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/profiles"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_profile(self, additional_fields_profile=None, data=None) -> dict[str, Any]:
        """
Create Profile

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "type": "profile"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile(self, id, additional_fields_profile=None, fields_list=None, fields_profile=None, fields_segment=None, include=None) -> dict[str, Any]:
        """
Get Profile

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            fields_segment (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'is_processing,is_processing'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'lists,segments'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[list]', fields_list), ('fields[profile]', fields_profile), ('fields[segment]', fields_segment), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_profile(self, id, additional_fields_profile=None, data=None) -> dict[str, Any]:
        """
Update Profile

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profiles/{id}"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile)] if v is not None}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_suppress_profiles_jobs(self, fields_profile_suppression_bulk_create_job=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Bulk Suppress Profiles Jobs

        Args:
            fields_profile_suppression_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'completed_at,completed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals`<br>`list_id`: `equals`<br>`segment_id`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs"
        query_params = {k: v for k, v in [('fields[profile-suppression-bulk-create-job]', fields_profile_suppression_bulk_create_job), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_suppress_profiles(self, data=None) -> dict[str, Any]:
        """
Bulk Suppress Profiles

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      },
                      "segment": {
                        "data": {
                          "id": "<string>",
                          "type": "segment"
                        }
                      }
                    },
                    "type": "profile-suppression-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_suppress_profiles_job(self, job_id, fields_profile_suppression_bulk_create_job=None) -> dict[str, Any]:
        """
Get Bulk Suppress Profiles Job

        Args:
            job_id (string): job_id
            fields_profile_suppression_bulk_create_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'completed_at,completed_count'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-suppression-bulk-create-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[profile-suppression-bulk-create-job]', fields_profile_suppression_bulk_create_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_unsuppress_profiles_jobs(self, fields_profile_suppression_bulk_delete_job=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Bulk Unsuppress Profiles Jobs

        Args:
            fields_profile_suppression_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'completed_at,completed_count'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `equals`<br>`list_id`: `equals`<br>`segment_id`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs"
        query_params = {k: v for k, v in [('fields[profile-suppression-bulk-delete-job]', fields_profile_suppression_bulk_delete_job), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_unsuppress_profiles(self, data=None) -> dict[str, Any]:
        """
Bulk Unsuppress Profiles

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>"
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      },
                      "segment": {
                        "data": {
                          "id": "<string>",
                          "type": "segment"
                        }
                      }
                    },
                    "type": "profile-suppression-bulk-delete-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_unsuppress_profiles_job(self, job_id, fields_profile_suppression_bulk_delete_job=None) -> dict[str, Any]:
        """
Get Bulk Unsuppress Profiles Job

        Args:
            job_id (string): job_id
            fields_profile_suppression_bulk_delete_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'completed_at,completed_count'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-suppression-bulk-delete-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[profile-suppression-bulk-delete-job]', fields_profile_suppression_bulk_delete_job)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_profile(self, additional_fields_profile=None, data=None) -> dict[str, Any]:
        """
Create or Update Profile

        Args:
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            data (object): data

        Returns:
            dict[str, Any]: Profile Updated Successfully

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "_kx": "<string>",
                      "anonymous_id": "<string>",
                      "email": "<string>",
                      "external_id": "<string>",
                      "first_name": "<string>",
                      "image": "<string>",
                      "last_name": "<string>",
                      "locale": "<string>",
                      "location": {
                        "address1": "<string>",
                        "address2": "<string>",
                        "city": "<string>",
                        "country": "<string>",
                        "ip": "<string>",
                        "latitude": "<string>",
                        "longitude": "<string>",
                        "region": "<string>",
                        "timezone": "<string>",
                        "zip": "<string>"
                      },
                      "organization": "<string>",
                      "phone_number": "<string>",
                      "properties": {},
                      "title": "<string>"
                    },
                    "id": "<string>",
                    "meta": {
                      "patch_properties": {
                        "append": {},
                        "unappend": {},
                        "unset": "<string>"
                      }
                    },
                    "type": "profile"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-import"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def merge_profiles(self, data=None) -> dict[str, Any]:
        """
Merge Profiles

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "id": "<string>",
                    "relationships": {
                      "profiles": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "profile"
                          },
                          {
                            "id": "<string>",
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "type": "profile-merge"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-merge"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_or_update_push_token(self, data=None) -> Any:
        """
Create or Update Push Token

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "background": "AVAILABLE",
                      "device_metadata": {
                        "app_build": "<string>",
                        "app_id": "<string>",
                        "app_name": "<string>",
                        "app_version": "<string>",
                        "device_id": "<string>",
                        "device_model": "<string>",
                        "environment": "debug",
                        "klaviyo_sdk": "android",
                        "manufacturer": "<string>",
                        "os_name": "ipados",
                        "os_version": "<string>",
                        "sdk_version": "<string>"
                      },
                      "enablement_status": "AUTHORIZED",
                      "platform": "android",
                      "profile": {
                        "data": {
                          "attributes": {
                            "_kx": "<string>",
                            "anonymous_id": "<string>",
                            "email": "<string>",
                            "external_id": "<string>",
                            "first_name": "<string>",
                            "image": "<string>",
                            "last_name": "<string>",
                            "locale": "<string>",
                            "location": {
                              "address1": "<string>",
                              "address2": "<string>",
                              "city": "<string>",
                              "country": "<string>",
                              "ip": "<string>",
                              "latitude": "<string>",
                              "longitude": "<string>",
                              "region": "<string>",
                              "timezone": "<string>",
                              "zip": "<string>"
                            },
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "organization": "<string>",
                            "phone_number": "<string>",
                            "properties": {},
                            "title": "<string>"
                          },
                          "id": "<string>",
                          "type": "profile"
                        }
                      },
                      "token": "<string>",
                      "vendor": "apns"
                    },
                    "type": "push-token"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/push-tokens"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_lists_for_profile(self, id, fields_list=None) -> dict[str, Any]:
        """
Get Lists for Profile

        Args:
            id (string): id
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/lists"
        query_params = {k: v for k, v in [('fields[list]', fields_list)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_profile(self, id) -> dict[str, Any]:
        """
Get List IDs for Profile

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segments_for_profile(self, id, fields_segment=None) -> dict[str, Any]:
        """
Get Segments for Profile

        Args:
            id (string): id
            fields_segment (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'is_processing,is_processing'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/segments"
        query_params = {k: v for k, v in [('fields[segment]', fields_segment)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_ids_for_profile(self, id) -> dict[str, Any]:
        """
Get Segment IDs for Profile

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profiles/{id}/relationships/segments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_import_profiles_jobs(self, fields_profile_bulk_import_job=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Bulk Import Profiles Jobs

        Args:
            fields_profile_bulk_import_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'started_at,completed_at'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`status`: `any`, `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'created_at'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/profile-bulk-import-jobs"
        query_params = {k: v for k, v in [('fields[profile-bulk-import-job]', fields_profile_bulk_import_job), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_import_profiles(self, data=None) -> dict[str, Any]:
        """
Bulk Import Profiles

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "_kx": "<string>",
                              "anonymous_id": "<string>",
                              "email": "<string>",
                              "external_id": "<string>",
                              "first_name": "<string>",
                              "image": "<string>",
                              "last_name": "<string>",
                              "locale": "<string>",
                              "location": {
                                "address1": "<string>",
                                "address2": "<string>",
                                "city": "<string>",
                                "country": "<string>",
                                "ip": "<string>",
                                "latitude": "<string>",
                                "longitude": "<string>",
                                "region": "<string>",
                                "timezone": "<string>",
                                "zip": "<string>"
                              },
                              "organization": "<string>",
                              "phone_number": "<string>",
                              "properties": {},
                              "title": "<string>"
                            },
                            "id": "<string>",
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "_kx": "<string>",
                              "anonymous_id": "<string>",
                              "email": "<string>",
                              "external_id": "<string>",
                              "first_name": "<string>",
                              "image": "<string>",
                              "last_name": "<string>",
                              "locale": "<string>",
                              "location": {
                                "address1": "<string>",
                                "address2": "<string>",
                                "city": "<string>",
                                "country": "<string>",
                                "ip": "<string>",
                                "latitude": "<string>",
                                "longitude": "<string>",
                                "region": "<string>",
                                "timezone": "<string>",
                                "zip": "<string>"
                              },
                              "organization": "<string>",
                              "phone_number": "<string>",
                              "properties": {},
                              "title": "<string>"
                            },
                            "id": "<string>",
                            "meta": {
                              "patch_properties": {
                                "append": {},
                                "unappend": {},
                                "unset": "<string>"
                              }
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "lists": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "list"
                          },
                          {
                            "id": "<string>",
                            "type": "list"
                          }
                        ]
                      }
                    },
                    "type": "profile-bulk-import-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-bulk-import-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_bulk_import_profiles_job(self, job_id, fields_list=None, fields_profile_bulk_import_job=None, include=None) -> dict[str, Any]:
        """
Get Bulk Import Profiles Job

        Args:
            job_id (string): job_id
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.
            fields_profile_bulk_import_job (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'started_at,completed_at'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'lists,lists'.

        Returns:
            dict[str, Any]: Success
        """
        if job_id is None:
            raise ValueError("Missing required parameter 'job_id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{job_id}"
        query_params = {k: v for k, v in [('fields[list]', fields_list), ('fields[profile-bulk-import-job]', fields_profile_bulk_import_job), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_for_bulk_import_profiles_job(self, id, fields_list=None) -> dict[str, Any]:
        """
Get List for Bulk Import Profiles Job

        Args:
            id (string): id
            fields_list (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,opt_in_process'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/lists"
        query_params = {k: v for k, v in [('fields[list]', fields_list)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_bulk_import_profiles_job(self, id) -> dict[str, Any]:
        """
Get List IDs for Bulk Import Profiles Job

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_bulk_import_profiles_job(self, id, additional_fields_profile=None, fields_profile=None, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
Get Profiles for Bulk Import Profiles Job

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address2,subscriptions.sms.marketing.last_updated'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/profiles"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_bulk_import_profiles_job(self, id, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
Get Profile IDs for Bulk Import Profiles Job

        Args:
            id (string): id
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/relationships/profiles"
        query_params = {k: v for k, v in [('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_errors_for_bulk_import_profiles_job(self, id, fields_import_error=None, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
Get Errors for Bulk Import Profiles Job

        Args:
            id (string): id
            fields_import_error (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'code,original_payload'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/profile-bulk-import-jobs/{id}/import-errors"
        query_params = {k: v for k, v in [('fields[import-error]', fields_import_error), ('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_subscribe_profiles(self, data=None) -> Any:
        """
Bulk Subscribe Profiles

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "custom_source": "<string>",
                      "historical_import": false,
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "age_gated_date_of_birth": "<date>",
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  },
                                  "transactional": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                }
                              }
                            },
                            "id": "<string>",
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "age_gated_date_of_birth": "<date>",
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  },
                                  "transactional": {
                                    "consent": "SUBSCRIBED",
                                    "consented_at": "<dateTime>"
                                  }
                                }
                              }
                            },
                            "id": "<string>",
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "profile-subscription-bulk-create-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-create-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_unsubscribe_profiles(self, data=None) -> Any:
        """
Bulk Unsubscribe Profiles

        Args:
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "profiles": {
                        "data": [
                          {
                            "attributes": {
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  },
                                  "transactional": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                }
                              }
                            },
                            "type": "profile"
                          },
                          {
                            "attributes": {
                              "email": "<string>",
                              "phone_number": "<string>",
                              "subscriptions": {
                                "email": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                },
                                "sms": {
                                  "marketing": {
                                    "consent": "UNSUBSCRIBED"
                                  },
                                  "transactional": {
                                    "consent": "UNSUBSCRIBED"
                                  }
                                }
                              }
                            },
                            "type": "profile"
                          }
                        ]
                      }
                    },
                    "relationships": {
                      "list": {
                        "data": {
                          "id": "<string>",
                          "type": "list"
                        }
                      }
                    },
                    "type": "profile-subscription-bulk-delete-job"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/profile-subscription-bulk-delete-jobs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_campaign_values(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
Query Campaign Values

        Args:
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "statistics": [
                        "unsubscribe_rate",
                        "spam_complaint_rate"
                      ],
                      "timeframe": {
                        "key": "last_3_months"
                      }
                    },
                    "type": "campaign-values-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/campaign-values-reports"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_values(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
Query Flow Values

        Args:
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "statistics": [
                        "open_rate",
                        "conversion_value"
                      ],
                      "timeframe": {
                        "key": "this_week"
                      }
                    },
                    "type": "flow-values-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-values-reports"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_flow_series(self, page_cursor=None, data=None) -> dict[str, Any]:
        """
Query Flow Series

        Args:
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "conversion_metric_id": "<string>",
                      "filter": "<string>",
                      "interval": "hourly",
                      "statistics": [
                        "clicks_unique",
                        "conversion_rate"
                      ],
                      "timeframe": {
                        "key": "last_365_days"
                      }
                    },
                    "type": "flow-series-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/flow-series-reports"
        query_params = {k: v for k, v in [('page_cursor', page_cursor)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_form_values(self, data=None) -> dict[str, Any]:
        """
Query Form Values

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "group_by": [
                        "form_version_id",
                        "form_version_id"
                      ],
                      "statistics": [
                        "viewed_form_step",
                        "viewed_form"
                      ],
                      "timeframe": {
                        "key": "last_3_months"
                      }
                    },
                    "type": "form-values-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/form-values-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_form_series(self, data=None) -> dict[str, Any]:
        """
Query Form Series

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "group_by": [
                        "form_id",
                        "form_id"
                      ],
                      "interval": "weekly",
                      "statistics": [
                        "viewed_form_step_uniques",
                        "closed_form_uniques"
                      ],
                      "timeframe": {
                        "key": "last_week"
                      }
                    },
                    "type": "form-series-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/form-series-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_segment_values(self, data=None) -> dict[str, Any]:
        """
Query Segment Values

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "statistics": [
                        "members_added",
                        "net_members_changed"
                      ],
                      "timeframe": {
                        "key": "this_week"
                      }
                    },
                    "type": "segment-values-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segment-values-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_segment_series(self, data=None) -> dict[str, Any]:
        """
Query Segment Series

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "filter": "<string>",
                      "interval": "daily",
                      "statistics": [
                        "members_removed",
                        "members_added"
                      ],
                      "timeframe": {
                        "key": "last_week"
                      }
                    },
                    "type": "segment-series-report"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segment-series-reports"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_reviews(self, fields_event=None, fields_review=None, filter=None, include=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Reviews

        Args:
            fields_event (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'uuid,datetime'.
            fields_review (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'author,images'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`created`: `greater-or-equal`, `less-or-equal`<br>`rating`: `any`, `equals`, `greater-or-equal`, `less-or-equal`<br>`id`: `any`, `equals`<br>`item.id`: `any`, `equals`<br>`content`: `contains`<br>`status`: `equals`<br>`review_type`: `equals`<br>`verified`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'events,events'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/reviews"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[review]', fields_review), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_review(self, id, fields_event=None, fields_review=None, include=None) -> dict[str, Any]:
        """
Get Review

        Args:
            id (string): id
            fields_event (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'uuid,datetime'.
            fields_review (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'author,images'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'events,events'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/reviews/{id}"
        query_params = {k: v for k, v in [('fields[event]', fields_event), ('fields[review]', fields_review), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_review(self, id, data=None) -> dict[str, Any]:
        """
Update Review

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "status": {
                        "rejection_reason": {
                          "reason": "other",
                          "status_explanation": "<string>"
                        },
                        "value": "rejected"
                      }
                    },
                    "id": "<string>",
                    "type": "review"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/reviews/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segments(self, fields_flow=None, fields_segment=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Segments

        Args:
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_segment (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'is_processing,is_processing'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `any`, `equals`<br>`id`: `any`, `equals`<br>`created`: `greater-than`<br>`updated`: `greater-than`<br>`is_active`: `any`, `equals`<br>`is_starred`: `equals` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,tags'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/segments"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow), ('fields[segment]', fields_segment), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_segment(self, data=None) -> dict[str, Any]:
        """
Create Segment

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "condition_groups": [
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          },
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          }
                        ]
                      },
                      "is_starred": false,
                      "name": "<string>"
                    },
                    "type": "segment"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment(self, id, additional_fields_segment=None, fields_flow=None, fields_segment=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
Get Segment

        Args:
            id (string): id
            additional_fields_segment (string): Request additional fields not included by default in the response. Supported values: 'profile_count' Example: 'profile_count,profile_count'.
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.
            fields_segment (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'updated,is_active'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'flow-triggers,tags'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {k: v for k, v in [('additional-fields[segment]', additional_fields_segment), ('fields[flow]', fields_flow), ('fields[segment]', fields_segment), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_segment(self, id) -> Any:
        """
Delete Segment

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_segment(self, id, data=None) -> dict[str, Any]:
        """
Update Segment

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "condition_groups": [
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          },
                          {
                            "conditions": [
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              },
                              {
                                "group_ids": [
                                  "<string>",
                                  "<string>"
                                ],
                                "is_member": true,
                                "timeframe_filter": {
                                  "date": "<dateTime>",
                                  "operator": "before",
                                  "type": "date"
                                },
                                "type": "profile-group-membership"
                              }
                            ]
                          }
                        ]
                      },
                      "is_starred": "<boolean>",
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "segment"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/segments/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_segment(self, id, fields_tag=None) -> dict[str, Any]:
        """
Get Tags for Segment

        Args:
            id (string): id
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/tags"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_segment(self, id) -> dict[str, Any]:
        """
Get Tag IDs for Segment

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profiles_for_segment(self, id, additional_fields_profile=None, fields_profile=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Profiles for Segment

        Args:
            id (string): id
            additional_fields_profile (string): Request additional fields not included by default in the response. Supported values: 'subscriptions', 'predictive_analytics' Example: 'subscriptions,subscriptions'.
            fields_profile (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'location.address1,first_name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/profiles"
        query_params = {k: v for k, v in [('additional-fields[profile]', additional_fields_profile), ('fields[profile]', fields_profile), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_profile_ids_for_segment(self, id, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get Profile IDs for Segment

        Args:
            id (string): id
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`email`: `any`, `equals`<br>`phone_number`: `any`, `equals`<br>`push_token`: `any`, `equals`<br>`_kx`: `equals`<br>`joined_group_at`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-joined_group_at'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/profiles"
        query_params = {k: v for k, v in [('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flows_triggered_by_segment(self, id, fields_flow=None) -> dict[str, Any]:
        """
Get Flows Triggered by Segment

        Args:
            id (string): id
            fields_flow (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'created,status'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/flow-triggers"
        query_params = {k: v for k, v in [('fields[flow]', fields_flow)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ids_for_flows_triggered_by_segment(self, id) -> dict[str, Any]:
        """
Get IDs for Flows Triggered by Segment

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/segments/{id}/relationships/flow-triggers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags(self, fields_tag_group=None, fields_tag=None, filter=None, include=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Tags

        Args:
            fields_tag_group (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,exclusive'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with` Example: '<string>'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tag-group,tag-group'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'name'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/tags"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('fields[tag]', fields_tag), ('filter', filter), ('include', include), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag(self, data=None) -> dict[str, Any]:
        """
Create Tag

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "relationships": {
                      "tag-group": {
                        "data": {
                          "id": "<string>",
                          "type": "tag-group"
                        }
                      }
                    },
                    "type": "tag"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag(self, id, fields_tag_group=None, fields_tag=None, include=None) -> dict[str, Any]:
        """
Get Tag

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,exclusive'.
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'tag-group,tag-group'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('fields[tag]', fields_tag), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag(self, id) -> Any:
        """
Delete Tag

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag(self, id, data=None) -> Any:
        """
Update Tag

        Args:
            id (string): id
            data (object): data

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "tag"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_flow_ids_for_tag(self, id) -> dict[str, Any]:
        """
Get Flow IDs for Tag

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_flows(self, id, data=None) -> Any:
        """
Tag Flows

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'flow'}, {'id': '<string>', 'type': 'flow'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "flow"
                    },
                    {
                      "id": "<string>",
                      "type": "flow"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_flows(self, id, data=None) -> Any:
        """
Remove Tag from Flows

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'flow'}, {'id': '<string>', 'type': 'flow'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "flow"
                    },
                    {
                      "id": "<string>",
                      "type": "flow"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/flows"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_campaign_ids_for_tag(self, id) -> dict[str, Any]:
        """
Get Campaign IDs for Tag

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_campaigns(self, id, data=None) -> Any:
        """
Tag Campaigns

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'campaign'}, {'id': '<string>', 'type': 'campaign'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "campaign"
                    },
                    {
                      "id": "<string>",
                      "type": "campaign"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_campaigns(self, id, data=None) -> Any:
        """
Remove Tag from Campaigns

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'campaign'}, {'id': '<string>', 'type': 'campaign'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "campaign"
                    },
                    {
                      "id": "<string>",
                      "type": "campaign"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/campaigns"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_list_ids_for_tag(self, id) -> dict[str, Any]:
        """
Get List IDs for Tag

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_lists(self, id, data=None) -> Any:
        """
Tag Lists

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'list'}, {'id': '<string>', 'type': 'list'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "list"
                    },
                    {
                      "id": "<string>",
                      "type": "list"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_lists(self, id, data=None) -> Any:
        """
Remove Tag from Lists

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'list'}, {'id': '<string>', 'type': 'list'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "list"
                    },
                    {
                      "id": "<string>",
                      "type": "list"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/lists"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_segment_ids_for_tag(self, id) -> dict[str, Any]:
        """
Get Segment IDs for Tag

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tag_segments(self, id, data=None) -> Any:
        """
Tag Segments

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'segment'}, {'id': '<string>', 'type': 'segment'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "segment"
                    },
                    {
                      "id": "<string>",
                      "type": "segment"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_segments(self, id, data=None) -> Any:
        """
Remove Tag from Segments

        Args:
            id (string): id
            data (array): data Example: "[{'id': '<string>', 'type': 'segment'}, {'id': '<string>', 'type': 'segment'}]".

        Returns:
            Any: Success

        Request Body Example:
                ```json
                {
                  "data": [
                    {
                      "id": "<string>",
                      "type": "segment"
                    },
                    {
                      "id": "<string>",
                      "type": "segment"
                    }
                  ]
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tags/{id}/relationships/segments"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_for_tag(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
Get Tag Group for Tag

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,exclusive'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/tag-group"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group_id_for_tag(self, id) -> dict[str, Any]:
        """
Get Tag Group ID for Tag

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tags/{id}/relationships/tag-group"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_groups(self, fields_tag_group=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Tag Groups

        Args:
            fields_tag_group (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,exclusive'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `contains`, `ends-with`, `equals`, `starts-with`<br>`exclusive`: `equals`<br>`default`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: 'name'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/tag-groups"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag_group(self, data=None) -> dict[str, Any]:
        """
Create Tag Group

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "exclusive": false,
                      "name": "<string>"
                    },
                    "type": "tag-group"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_group(self, id, fields_tag_group=None) -> dict[str, Any]:
        """
Get Tag Group

        Args:
            id (string): id
            fields_tag_group (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,exclusive'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {k: v for k, v in [('fields[tag-group]', fields_tag_group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag_group(self, id) -> dict[str, Any]:
        """
Delete Tag Group

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag_group(self, id, data=None) -> dict[str, Any]:
        """
Update Tag Group

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>",
                      "return_fields": [
                        "<string>",
                        "<string>"
                      ]
                    },
                    "id": "<string>",
                    "type": "tag-group"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tag-groups/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_for_tag_group(self, id, fields_tag=None) -> dict[str, Any]:
        """
Get Tags for Tag Group

        Args:
            id (string): id
            fields_tag (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,name'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/tags"
        query_params = {k: v for k, v in [('fields[tag]', fields_tag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag_ids_for_tag_group(self, id) -> dict[str, Any]:
        """
Get Tag IDs for Tag Group

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tag-groups/{id}/relationships/tags"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_templates(self, fields_template=None, filter=None, page_cursor=None, sort=None) -> dict[str, Any]:
        """
Get Templates

        Args:
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `equals`<br>`created`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `equals`, `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/templates"
        query_params = {k: v for k, v in [('fields[template]', fields_template), ('filter', filter), ('page[cursor]', page_cursor), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_template(self, data=None) -> dict[str, Any]:
        """
Create Template

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "editor_type": "<string>",
                      "html": "<string>",
                      "name": "<string>",
                      "text": "<string>"
                    },
                    "type": "template"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template(self, id, fields_template=None) -> dict[str, Any]:
        """
Get Template

        Args:
            id (string): id
            fields_template (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'name,text'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {k: v for k, v in [('fields[template]', fields_template)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template(self, id) -> Any:
        """
Delete Template

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_template(self, id, data=None) -> dict[str, Any]:
        """
Update Template

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "html": "<string>",
                      "name": "<string>",
                      "text": "<string>"
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/templates/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def render_template(self, data=None) -> dict[str, Any]:
        """
Render Template

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "context": {}
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-render"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def clone_template(self, data=None) -> dict[str, Any]:
        """
Clone Template

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "template"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-clone"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_universal_content(self, fields_template_universal_content=None, filter=None, page_cursor=None, page_size=None, sort=None) -> dict[str, Any]:
        """
Get All Universal Content

        Args:
            fields_template_universal_content (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.data.content,definition.data.styles.color'.
            filter (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`id`: `any`, `equals`<br>`name`: `any`, `equals`<br>`created`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`updated`: `greater-or-equal`, `greater-than`, `less-or-equal`, `less-than`<br>`definition.content_type`: `equals`<br>`definition.type`: `equals` Example: '<string>'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 20. Min: 1. Max: 100. Example: '20'.
            sort (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sorting Example: '-updated'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/template-universal-content"
        query_params = {k: v for k, v in [('fields[template-universal-content]', fields_template_universal_content), ('filter', filter), ('page[cursor]', page_cursor), ('page[size]', page_size), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_universal_content(self, data=None) -> dict[str, Any]:
        """
Create Universal Content

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "content_type": "block",
                        "data": {
                          "content": "<string>",
                          "display_options": {
                            "content_repeat": {
                              "item_alias": "<string>",
                              "repeat_for": "<string>"
                            },
                            "show_on": "all",
                            "visible_check": "<string>"
                          }
                        },
                        "type": "html"
                      },
                      "name": "<string>"
                    },
                    "type": "template-universal-content"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-universal-content"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_universal_content(self, id, fields_template_universal_content=None) -> dict[str, Any]:
        """
Get Universal Content

        Args:
            id (string): id
            fields_template_universal_content (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'definition.data.content,definition.data.styles.color'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {k: v for k, v in [('fields[template-universal-content]', fields_template_universal_content)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_universal_content(self, id) -> Any:
        """
Delete Universal Content

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_universal_content(self, id, data=None) -> dict[str, Any]:
        """
Update Universal Content

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "definition": {
                        "content_type": "block",
                        "data": {
                          "content": "<string>",
                          "display_options": {
                            "content_repeat": {
                              "item_alias": "<string>",
                              "repeat_for": "<string>"
                            },
                            "show_on": "desktop",
                            "visible_check": "<string>"
                          }
                        },
                        "type": "html"
                      },
                      "name": "<string>"
                    },
                    "id": "<string>",
                    "type": "template-universal-content"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/template-universal-content/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tracking_settings(self, fields_tracking_setting=None, page_cursor=None, page_size=None) -> dict[str, Any]:
        """
Get Tracking Settings

        Args:
            fields_tracking_setting (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'utm_term.campaign.value,utm_medium.flow.type'.
            page_cursor (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#pagination Example: '<string>'.
            page_size (string): Default: 1. Min: 1. Max: 1. Example: '1'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/tracking-settings"
        query_params = {k: v for k, v in [('fields[tracking-setting]', fields_tracking_setting), ('page[cursor]', page_cursor), ('page[size]', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tracking_setting(self, id, fields_tracking_setting=None) -> dict[str, Any]:
        """
Get Tracking Setting

        Args:
            id (string): id
            fields_tracking_setting (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'utm_term.campaign.value,utm_medium.flow.type'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/tracking-settings/{id}"
        query_params = {k: v for k, v in [('fields[tracking-setting]', fields_tracking_setting)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tracking_setting(self, id, data=None) -> dict[str, Any]:
        """
Update Tracking Setting

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "auto_add_parameters": "<boolean>",
                      "custom_parameters": [
                        {
                          "campaign": {
                            "type": "dynamic",
                            "value": "campaign_name_id"
                          },
                          "flow": {
                            "type": "dynamic",
                            "value": "flow_id"
                          },
                          "name": "<string>"
                        },
                        {
                          "campaign": {
                            "type": "dynamic",
                            "value": "campaign_name"
                          },
                          "flow": {
                            "type": "dynamic",
                            "value": "message_type"
                          },
                          "name": "<string>"
                        }
                      ],
                      "utm_campaign": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "profile_external_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "profile_external_id"
                        }
                      },
                      "utm_id": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "group_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_id"
                        }
                      },
                      "utm_medium": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "campaign_name_id"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "message_name_id"
                        }
                      },
                      "utm_source": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "email_subject"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_id"
                        }
                      },
                      "utm_term": {
                        "campaign": {
                          "type": "dynamic",
                          "value": "link_alt_text"
                        },
                        "flow": {
                          "type": "dynamic",
                          "value": "flow_name"
                        }
                      }
                    },
                    "id": "<string>",
                    "type": "tracking-setting"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/tracking-settings/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhooks(self, fields_webhook=None, include=None) -> dict[str, Any]:
        """
Get Webhooks

        Args:
            fields_webhook (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'description,updated_at'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'webhook-topics,webhook-topics'.

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/webhooks"
        query_params = {k: v for k, v in [('fields[webhook]', fields_webhook), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook(self, data=None) -> dict[str, Any]:
        """
Create Webhook

        Args:
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "endpoint_url": "<string>",
                      "name": "<string>",
                      "secret_key": "<string>"
                    },
                    "relationships": {
                      "webhook-topics": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          },
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          }
                        ]
                      }
                    },
                    "type": "webhook"
                  }
                }
                ```
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook(self, id, fields_webhook=None, include=None) -> dict[str, Any]:
        """
Get Webhook

        Args:
            id (string): id
            fields_webhook (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#sparse-fieldsets Example: 'description,updated_at'.
            include (string): For more information please visit https://developers.klaviyo.com/en/v2025-01-15/reference/api-overview#relationships Example: 'webhook-topics,webhook-topics'.

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {k: v for k, v in [('fields[webhook]', fields_webhook), ('include', include)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook(self, id) -> Any:
        """
Delete Webhook

        Args:
            id (string): id

        Returns:
            Any: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_webhook(self, id, data=None) -> dict[str, Any]:
        """
Update Webhook

        Args:
            id (string): id
            data (object): data

        Returns:
            dict[str, Any]: Success

        Request Body Example:
                ```json
                {
                  "data": {
                    "attributes": {
                      "description": "<string>",
                      "enabled": "<boolean>",
                      "endpoint_url": "<string>",
                      "name": "<string>",
                      "secret_key": "<string>"
                    },
                    "id": "<string>",
                    "relationships": {
                      "webhook-topics": {
                        "data": [
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          },
                          {
                            "id": "<string>",
                            "type": "webhook-topic"
                          }
                        ]
                      }
                    },
                    "type": "webhook"
                  }
                }
                ```
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/webhooks/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topics(self) -> dict[str, Any]:
        """
Get Webhook Topics

        Returns:
            dict[str, Any]: Success
        """
        url = f"{self.base_url}/api/webhook-topics"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_topic(self, id) -> dict[str, Any]:
        """
Get Webhook Topic

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/webhook-topics/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.create_client_review,
            self.get_accounts,
            self.get_account,
            self.get_campaigns,
            self.create_campaign,
            self.get_campaign,
            self.delete_campaign,
            self.update_campaign,
            self.get_campaign_recipient_estimation,
            self.create_campaign_clone,
            self.get_tags_for_campaign,
            self.get_tag_ids_for_campaign,
            self.get_messages_for_campaign,
            self.get_message_ids_for_campaign,
            self.get_campaign_message,
            self.update_campaign_message,
            self.assign_template_to_campaign_message,
            self.get_campaign_for_campaign_message,
            self.get_campaign_id_for_campaign_message,
            self.get_template_for_campaign_message,
            self.get_template_id_for_campaign_message,
            self.get_image_for_campaign_message,
            self.get_image_id_for_campaign_message,
            self.update_image_for_campaign_message,
            self.get_campaign_send_job,
            self.cancel_campaign_send,
            self.get_campaign_recipient_estimation_job,
            self.send_campaign,
            self.refresh_campaign_recipient_estimation,
            self.get_catalog_items,
            self.create_catalog_item,
            self.get_catalog_item,
            self.delete_catalog_item,
            self.update_catalog_item,
            self.get_bulk_create_catalog_items_jobs,
            self.bulk_create_catalog_items,
            self.get_bulk_create_catalog_items_job,
            self.get_bulk_update_catalog_items_jobs,
            self.bulk_update_catalog_items,
            self.get_bulk_update_catalog_items_job,
            self.get_bulk_delete_catalog_items_jobs,
            self.bulk_delete_catalog_items,
            self.get_bulk_delete_catalog_items_job,
            self.get_items_for_catalog_category,
            self.get_category_ids_for_catalog_item,
            self.add_categories_to_catalog_item,
            self.remove_categories_from_catalog_item,
            self.update_categories_for_catalog_item,
            self.get_catalog_variants,
            self.create_catalog_variant,
            self.get_catalog_variant,
            self.delete_catalog_variant,
            self.update_catalog_variant,
            self.get_create_variants_jobs,
            self.bulk_create_catalog_variants,
            self.get_create_variants_job,
            self.get_update_variants_jobs,
            self.bulk_update_catalog_variants,
            self.get_update_variants_job,
            self.get_delete_variants_jobs,
            self.bulk_delete_catalog_variants,
            self.get_delete_variants_job,
            self.get_variants_for_catalog_item,
            self.get_variant_ids_for_catalog_item,
            self.get_catalog_categories,
            self.create_catalog_category,
            self.get_catalog_category,
            self.delete_catalog_category,
            self.update_catalog_category,
            self.get_create_categories_jobs,
            self.bulk_create_catalog_categories,
            self.get_create_categories_job,
            self.get_update_categories_jobs,
            self.bulk_update_catalog_categories,
            self.get_update_categories_job,
            self.get_delete_categories_jobs,
            self.bulk_delete_catalog_categories,
            self.get_delete_categories_job,
            self.get_item_ids_for_catalog_category,
            self.add_items_to_catalog_category,
            self.remove_items_from_catalog_category,
            self.update_items_for_catalog_category,
            self.get_categories_for_catalog_item,
            self.create_back_in_stock_subscription,
            self.create_client_subscription,
            self.create_or_update_client_push_token,
            self.unregister_client_push_token,
            self.create_client_event,
            self.create_or_update_client_profile,
            self.bulk_create_client_events,
            self.create_client_back_in_stock_subscription,
            self.get_coupons,
            self.create_coupon,
            self.get_coupon,
            self.delete_coupon,
            self.update_coupon,
            self.get_coupon_codes,
            self.create_coupon_code,
            self.get_coupon_code,
            self.delete_coupon_code,
            self.update_coupon_code,
            self.get_bulk_create_coupon_code_jobs,
            self.bulk_create_coupon_codes,
            self.get_bulk_create_coupon_codes_job,
            self.get_coupon_for_coupon_code,
            self.get_coupon_id_for_coupon_code,
            self.get_coupon_codes_for_coupon,
            self.get_coupon_code_ids_for_coupon,
            self.request_profile_deletion,
            self.get_events,
            self.create_event,
            self.get_event,
            self.bulk_create_events,
            self.get_metric_for_event,
            self.get_metric_id_for_event,
            self.get_profile_for_event,
            self.get_profile_id_for_event,
            self.get_flows,
            self.create_flow,
            self.get_flow,
            self.delete_flow,
            self.update_flow_status,
            self.get_flow_action,
            self.get_flow_message,
            self.get_actions_for_flow,
            self.get_action_ids_for_flow,
            self.get_tags_for_flow,
            self.get_tag_ids_for_flow,
            self.get_flow_for_flow_action,
            self.get_flow_id_for_flow_action,
            self.get_messages_for_flow_action,
            self.get_message_ids_for_flow_action,
            self.get_action_for_flow_message,
            self.get_action_id_for_flow_message,
            self.get_template_for_flow_message,
            self.get_template_id_for_flow_message,
            self.get_forms,
            self.get_form,
            self.get_form_version,
            self.get_versions_for_form,
            self.get_version_ids_for_form,
            self.get_form_for_form_version,
            self.get_form_id_for_form_version,
            self.get_images,
            self.upload_image_from_url,
            self.get_image,
            self.update_image,
            self.upload_image_from_file,
            self.get_lists,
            self.create_list,
            self.get_list,
            self.delete_list,
            self.update_list,
            self.get_tags_for_list,
            self.get_tag_ids_for_list,
            self.get_profiles_for_list,
            self.get_profile_ids_for_list,
            self.add_profiles_to_list,
            self.remove_profiles_from_list,
            self.get_flows_triggered_by_list,
            self.get_ids_for_flows_triggered_by_list,
            self.get_metrics,
            self.get_metric,
            self.get_metric_property,
            self.query_metric_aggregates,
            self.get_flows_triggered_by_metric,
            self.get_ids_for_flows_triggered_by_metric,
            self.get_properties_for_metric,
            self.get_property_ids_for_metric,
            self.get_metric_for_metric_property,
            self.get_metric_id_for_metric_property,
            self.get_profiles,
            self.create_profile,
            self.get_profile,
            self.update_profile,
            self.get_bulk_suppress_profiles_jobs,
            self.bulk_suppress_profiles,
            self.get_bulk_suppress_profiles_job,
            self.get_bulk_unsuppress_profiles_jobs,
            self.bulk_unsuppress_profiles,
            self.get_bulk_unsuppress_profiles_job,
            self.create_or_update_profile,
            self.merge_profiles,
            self.create_or_update_push_token,
            self.get_lists_for_profile,
            self.get_list_ids_for_profile,
            self.get_segments_for_profile,
            self.get_segment_ids_for_profile,
            self.get_bulk_import_profiles_jobs,
            self.bulk_import_profiles,
            self.get_bulk_import_profiles_job,
            self.get_list_for_bulk_import_profiles_job,
            self.get_list_ids_for_bulk_import_profiles_job,
            self.get_profiles_for_bulk_import_profiles_job,
            self.get_profile_ids_for_bulk_import_profiles_job,
            self.get_errors_for_bulk_import_profiles_job,
            self.bulk_subscribe_profiles,
            self.bulk_unsubscribe_profiles,
            self.query_campaign_values,
            self.query_flow_values,
            self.query_flow_series,
            self.query_form_values,
            self.query_form_series,
            self.query_segment_values,
            self.query_segment_series,
            self.get_reviews,
            self.get_review,
            self.update_review,
            self.get_segments,
            self.create_segment,
            self.get_segment,
            self.delete_segment,
            self.update_segment,
            self.get_tags_for_segment,
            self.get_tag_ids_for_segment,
            self.get_profiles_for_segment,
            self.get_profile_ids_for_segment,
            self.get_flows_triggered_by_segment,
            self.get_ids_for_flows_triggered_by_segment,
            self.get_tags,
            self.create_tag,
            self.get_tag,
            self.delete_tag,
            self.update_tag,
            self.get_flow_ids_for_tag,
            self.tag_flows,
            self.remove_tag_from_flows,
            self.get_campaign_ids_for_tag,
            self.tag_campaigns,
            self.remove_tag_from_campaigns,
            self.get_list_ids_for_tag,
            self.tag_lists,
            self.remove_tag_from_lists,
            self.get_segment_ids_for_tag,
            self.tag_segments,
            self.remove_tag_from_segments,
            self.get_tag_group_for_tag,
            self.get_tag_group_id_for_tag,
            self.get_tag_groups,
            self.create_tag_group,
            self.get_tag_group,
            self.delete_tag_group,
            self.update_tag_group,
            self.get_tags_for_tag_group,
            self.get_tag_ids_for_tag_group,
            self.get_templates,
            self.create_template,
            self.get_template,
            self.delete_template,
            self.update_template,
            self.render_template,
            self.clone_template,
            self.get_all_universal_content,
            self.create_universal_content,
            self.get_universal_content,
            self.delete_universal_content,
            self.update_universal_content,
            self.get_tracking_settings,
            self.get_tracking_setting,
            self.update_tracking_setting,
            self.get_webhooks,
            self.create_webhook,
            self.get_webhook,
            self.delete_webhook,
            self.update_webhook,
            self.get_webhook_topics,
            self.get_webhook_topic
        ]
