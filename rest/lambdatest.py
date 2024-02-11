import json
from logging import getLogger

import requests

import allure


class LambdaTestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    def __init__(self):
        self._log = getLogger(__name__)

    @allure.step("Send a POST request to {path}")
    def _send_request(self, path, input_key, input_str):
        """
        Send Post request with data
        :param path: endpoint for url
        :param input_key: input_key for request
        :param input_str: string for key
        :return: response
        """
        url = self.BASE_URL + path
        response = requests.post(url, data={input_key: input_str})
        allure.attach(url, "Full url", allure.attachment_type.TEXT)
        self._log.info(f"Send request to url: {url} with data: {input_key}: {input_str}")

        return response

    @allure.step("Send a POST request to convert JSON to XML")
    def convert_json_to_xml(self, input_str: str) -> str:
        self._log.info(f"Send a Post request to endpoint: 'json-to-xml' with data: 'input-str': {input_str}")
        response = self._send_request("json-to-xml", "input-str", input_str).text
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output XML", allure.attachment_type.XML)
        return response

    @allure.step("Send a POST request to minify XML")
    def minify_xml(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'minify-xml' with data: 'input-str': {input_str}")
        response = self._send_request("minify-xml", "input-str", input_str).json()[
            "minify_data"
        ]
        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output minified XML", allure.attachment_type.XML)
        return response

    @allure.step("Send a POST request to extract Text from JSON")
    def extract_text_from_json(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'extract-text-json' with data: 'input-str': {input_str}")
        response = self._send_request(
            "extract-text-json", "input-str", input_str
        ).json()["data"]
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Extracted TEXT", allure.attachment_type.TEXT)
        return response

    @allure.step("Send a POST request to validate YAML")
    def yaml_validator(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'yaml-validator' with data: 'yaml-str': {input_str}")
        response = self._send_request("yaml-validator", "yaml-str", input_str).json()[
            "message"
        ]
        allure.attach(input_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(response, "Message about checking the entered YAML", allure.attachment_type.TEXT)
        return response

    @allure.step("Send a POST request to convert JSON to YAML")
    def convert_json_to_yaml(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'json-to-yaml' with data: 'json-str': {input_str}")
        response = self._send_request("json-to-yaml", "json-str", input_str).json()[
            "data"
        ]
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    @allure.step("Send a POST request to convert XML to YAML")
    def convert_xml_to_yaml(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'xml-to-yaml' with data: 'xml-str': {input_str}")
        response = self._send_request("xml-to-yaml", "xml-str", input_str).json()[
            "data"
        ]
        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    @allure.step("Send a POST request to convert YAML to XML")
    def convert_yaml_to_json(self, input_str: str) -> str:
        self._log.info(f"Send a POST request to endpoint: 'yaml-to-json' with data: 'yaml-str': {input_str}")
        response = self._send_request("yaml-to-json", "yaml-str", input_str).json()
        response_data = response.get("data")
        allure.attach(input_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(json.dumps(response_data), "Output JSON", allure.attachment_type.TEXT)
        return response_data
