import json
import os
from logging import getLogger
from pytest_bdd import parsers, scenarios, given, when, then
import allure
from utils.file_utils import read_data_file, get_root_path
logger = getLogger(__name__)


feature_path = os.path.join(get_root_path(), "tests", "features", "lambdatest.feature")

scenarios(feature_path)


@given(parsers.parse("prepare a JSON file: {json_file_name}"), target_fixture="context")
def a_json_file_is_prepared(json_file_name, context):
    with allure.step("Prepare a JSON file: {json_file_name}"):
        logger.info(f"prepare a JSON file: {json_file_name}")
        input_json = read_data_file(f"json/{json_file_name}")
        context["input_json"] = input_json
        allure.attach(json_file_name, "JSON file name", allure.attachment_type.TEXT)
        allure.attach(json.dumps(input_json, indent=2), name="Input JSON", attachment_type=allure.attachment_type.TEXT)

        return context


@given(parsers.parse("prepare a XML file: {xml_file_name}"), target_fixture="context")
def a_xml_file_is_prepared(xml_file_name, context):
    with allure.step("Prepare a XML file: {xml_file_name}"):
        logger.info(f"Prepare a XML file: {xml_file_name}")
        expected_xml = read_data_file(f"xml/{xml_file_name}")
        context["expected_xml"] = expected_xml
        allure.attach(xml_file_name, "XML file name", allure.attachment_type.XML)
        allure.attach(json.dumps(expected_xml, indent=2), "Input XML", allure.attachment_type.TEXT)

        return context


@given(parsers.parse("prepare a TXT file: {txt_file_name}"), target_fixture="context")
def a_txt_file_is_prepared(txt_file_name, context):
    with allure.step("Prepare a TXT file: {txt_file_name}"):
        logger.info(f"prepare a TXT file: {txt_file_name}")
        expected_txt = read_data_file(f"txt/{txt_file_name}")
        context["expected_txt"] = expected_txt
        allure.attach(txt_file_name, "TXT file name", allure.attachment_type.TEXT)
        allure.attach(json.dumps(expected_txt, indent=2), "Input TEXT", allure.attachment_type.TEXT)

        return context


@when("converting JSON to XML", target_fixture="context")
def convert_json_to_xml(context, lambda_test_service):
    with allure.step("Convert JSON to XML"):
        actual_xml = lambda_test_service.convert_json_to_xml(context["input_json"])
        context["actual_xml"] = actual_xml
        logger.info(f"Convert JSON: {context['input_json']} to XML: {context['actual_xml']}")
        allure.attach(context["input_json"], "Input JSON", allure.attachment_type.JSON)
        allure.attach(context['actual_xml'], "Output XML", allure.attachment_type.XML)

        return context


@when("extract text from JSON", target_fixture="context")
def extract_text_from_json(context, lambda_test_service):
    with allure.step("Extract Text from JSON"):
        actual_txt = lambda_test_service.extract_text_from_json(context["input_json"])
        context["actual_txt"] = actual_txt
        logger.info(f"Extract Text: {context['input_json']} from JSON: {context['actual_txt']}")
        allure.attach(context['input_json'], "Input JSON", allure.attachment_type.JSON)
        allure.attach(context['actual_txt'], "Output TEXT", allure.attachment_type.TEXT)

        return context


@then("comparison of expected and actual XML", target_fixture="context")
def compare_expected_and_actual_xml(context, lambda_test_service):
    with allure.step("Compare expected and actual XML"):
        expected_xml = context["expected_xml"]
        actual_xml = context["actual_xml"]
        minify_expected_xml = lambda_test_service.minify_xml(expected_xml)
        minify_actual_xml = lambda_test_service.minify_xml(actual_xml)
        logger.info(f"Compare expected: {expected_xml} and actual XML: {actual_xml}")
        logger.info(f"Compare expected: {minify_expected_xml} and actual XML: {minify_actual_xml}")
        allure.attach(minify_expected_xml, "Minify expected XML", allure.attachment_type.XML)
        allure.attach(minify_actual_xml, "Minify actual XML", allure.attachment_type.XML)

        assert minify_expected_xml == minify_actual_xml


@then("comparison of expected and actual text", target_fixture="context")
def compare_expected_and_actual_txt(context):
    with allure.step("Compare expected and actual TEXT"):
        context["actual_txt"] = context["actual_txt"].replace(" \n", "\n")
        context["expected_txt"] = context["expected_txt"].replace(" \n", "\n")
        logger.info(f"Compare expected: {context['expected_txt']} and actual: {context['actual_txt']} TEXT")
        allure.attach(context["actual_txt"], "Actual TEXT", allure.attachment_type.TEXT)
        allure.attach(context["expected_txt"], "Expected TEXT", allure.attachment_type.TEXT)

        assert context["actual_txt"] == context["expected_txt"]


@given(parsers.parse("prepare a YAML file: {yaml_file_name}"), target_fixture="context")
def a_yaml_file_is_prepared(yaml_file_name, context):
    with allure.step("Prepare a YAML file"):
        context["yaml"] = read_data_file(f"yaml/{yaml_file_name}")
        logger.info(f"Prepare a YAML file: {context['yaml']}")
        allure.attach(yaml_file_name, "Name of YAML file name", allure.attachment_type.TEXT)
        allure.attach(json.dumps(context["yaml"], indent=2), "Input YAML", allure.attachment_type.YAML)

        return context


@when("validation YAML", target_fixture="context")
def validation_yaml(context, lambda_test_service):
    response = lambda_test_service.yaml_validator(context["yaml"])
    context["response"] = response

    return context


@then("comparison of expected and actual string", target_fixture="context")
def compare_expected_and_actual_string(context):
    with allure.step("Compare expected and actual string"):
        logger.info(f"Compare expected: {context['response']} and actual string")
        allure.attach(context["response"], "Expected Text", allure.attachment_type.TEXT)
        assert context["response"] == "Valid YAML"


@when("converting XML to YAML", target_fixture="context")
def convert_xml_to_yaml(context, lambda_test_service):
    actual_yaml = lambda_test_service.convert_xml_to_yaml(context["expected_xml"])
    context["actual_yaml"] = actual_yaml

    return context


@when("converting JSON to YAML", target_fixture="context")
def convert_json_to_yaml(context, lambda_test_service):
    actual_yaml = lambda_test_service.convert_json_to_yaml(context["input_json"])
    context["actual_yaml"] = actual_yaml

    return context


@then("comparison of expected and actual YAML", target_fixture="context")
def compare_expected_and_actual_yaml(context):
    with allure.step("Compare expected and actual YAML"):
        logger.info(f"Compare expected: {context['yaml']} and actual YAML: {context['actual_yaml']}")
        allure.attach(context["actual_yaml"], "Actual YAML", allure.attachment_type.YAML)
        allure.attach(context["yaml"], "Expected YAML", allure.attachment_type.YAML)

        assert context["actual_yaml"] == context["yaml"]


@when("converting YAML to JSON", target_fixture="context")
def convert_yaml_to_json(context, lambda_test_service):
    actual_json = lambda_test_service.convert_yaml_to_json(context["input_json"])
    context["actual_json"] = actual_json

    return context


@then("comparison of expected and actual JSON", target_fixture="context")
def compare_expected_and_actual_json(context):
    with allure.step("Compare expected and actual JSON"):
        expected_json = json.loads(context["input_json"])

        logger.info(f"Compare expected: {expected_json} and actual JSON: {context['actual_json']}")
        allure.attach(json.dumps(expected_json, indent=2), "Expected JSON", allure.attachment_type.JSON)
        allure.attach(json.dumps(context["actual_json"], indent=2), "Actual JSON", allure.attachment_type.JSON)

        assert context["actual_json"] == expected_json
