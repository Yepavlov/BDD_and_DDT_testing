
import requests


class LambdaTestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    def _send_request(self, path, input_key, input_str):
        url = self.BASE_URL + path
        response = requests.post(url, data={input_key: input_str})
        return response

    def convert_json_to_xml(self, input_str: str) -> str:
        response = self._send_request("json-to-xml", "input-str", input_str).text
        return response

    def minify_xml(self, input_str: str) -> str:
        response = self._send_request("minify-xml", "input-str", input_str).json()[
            "minify_data"
        ]
        return response

    def extract_text_from_json(self, input_str: str) -> str:
        response = self._send_request(
            "extract-text-json", "input-str", input_str
        ).json()["data"]
        return response

    def yaml_validator(self, input_str: str) -> str:
        response = self._send_request("yaml-validator", "yaml-str", input_str).json()[
            "message"
        ]
        return response

    def convert_json_to_yaml(self, input_str: str) -> str:
        response = self._send_request("json-to-yaml", "json-str", input_str).json()[
            "data"
        ]
        return response

    def convert_xml_to_yaml(self, input_str: str) -> str:
        response = self._send_request("xml-to-yaml", "xml-str", input_str).json()[
            "data"
        ]
        return response

    def convert_yaml_to_json(self, input_str: str) -> str:
        response = self._send_request("yaml-to-json", "yaml-str", input_str).json()
        response_data = response.get("data")
        return response_data
