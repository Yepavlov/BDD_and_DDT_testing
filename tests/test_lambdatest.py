import json
import os

from pytest_bdd import parsers, scenarios, given, when, then

from utils.file_utils import read_data_file, get_root_path

feature_path = os.path.join(get_root_path(), "tests", "features", "lambdatest.feature")

scenarios(feature_path)


@given(parsers.parse("prepare a JSON file: {json_file_name}"), target_fixture="context")
def a_json_file_is_prepared(json_file_name, context):
    input_json = read_data_file(f"json/{json_file_name}")
    context["input_json"] = input_json

    return context


@given(parsers.parse("prepare a XML file: {xml_file_name}"), target_fixture="context")
def a_xml_file_is_prepared(xml_file_name, context):
    expected_xml = read_data_file(f"xml/{xml_file_name}")
    context["expected_xml"] = expected_xml

    return context


@given(parsers.parse("prepare a TXT file: {txt_file_name}"), target_fixture="context")
def a_txt_file_is_prepared(txt_file_name, context):
    expected_txt = read_data_file(f"txt/{txt_file_name}")
    context["expected_txt"] = expected_txt

    return context


@when("converting JSON to XML", target_fixture="context")
def convert_json_to_xml(context, lambda_test_service):
    actual_xml = lambda_test_service.convert_json_to_xml(context["input_json"])
    context["actual_xml"] = actual_xml

    return context


@when("extract text from JSON", target_fixture="context")
def extract_text_from_json(context, lambda_test_service):
    actual_txt = lambda_test_service.extract_text_from_json(context["input_json"])
    context["actual_txt"] = actual_txt

    return context


@then("comparison of expected and actual XML", target_fixture="context")
def compare_expected_and_actual_xml(context, lambda_test_service):
    expected_xml = context["expected_xml"]
    actual_xml = context["actual_xml"]
    minify_expected_xml = lambda_test_service.minify_xml(expected_xml)
    minify_actual_xml = lambda_test_service.minify_xml(actual_xml)

    assert minify_expected_xml == minify_actual_xml


@then("comparison of expected and actual text", target_fixture="context")
def compare_expected_and_actual_txt(context):
    context["actual_txt"] = context["actual_txt"].replace(" \n", "\n")
    context["expected_txt"] = context["expected_txt"].replace(" \n", "\n")
    assert context["actual_txt"] == context["expected_txt"]


@given(parsers.parse("prepare a YAML file: {yaml_file_name}"), target_fixture="context")
def a_yaml_file_is_prepared(yaml_file_name, context):
    input_yaml = read_data_file(f"yaml/{yaml_file_name}")
    context["yaml"] = input_yaml

    return context


@when("validation YAML", target_fixture="context")
def validation_yaml(context, lambda_test_service):
    response = lambda_test_service.yaml_validator(context["yaml"])
    context["response"] = response

    return context


@then("comparison of expected and actual string", target_fixture="context")
def compare_expected_and_actual_string(context):
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
    assert context["actual_yaml"] == context["yaml"]


@when("converting YAML to JSON", target_fixture="context")
def convert_yaml_to_json(context, lambda_test_service):
    actual_json = lambda_test_service.convert_yaml_to_json(context["input_json"])
    context["actual_json"] = actual_json

    return context


@then("comparison of expected and actual JSON", target_fixture="context")
def compare_expected_and_actual_json(context):
    expected_json = json.loads(context["input_json"])
    assert context["actual_json"] == expected_json
