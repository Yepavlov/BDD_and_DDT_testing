Feature: Lambdatest
  As a user
  I want to convert some files format to another files format
  So have to make sure the conversion is correct

    Scenario Outline: Testing the converter JSON to XML
    Given prepare a JSON file: <json_file_name>
    And prepare a XML file: <xml_file_name>
    When converting JSON to XML
    Then comparison of expected and actual XML
    Examples:
      | json_file_name     | xml_file_name    |
      | 1.json             | 1.xml            |
      | 2.json             | 2.xml            |


    Scenario Outline: Testing extract text from JSON
    Given prepare a JSON file: <json_file_name>
    And prepare a TXT file: <txt_file_name>
    When extract text from JSON
    Then comparison of expected and actual text
    Examples:
      | json_file_name     | txt_file_name    |
      | 1.json             | 1.txt            |
      | 2.json             | 2.txt            |

    Scenario Outline: Test YAML validator
    Given prepare a YAML file: <yaml_file_name>
    When validation YAML
    Then comparison of expected and actual string
    Examples:
      | yaml_file_name      |
      | 1.yaml              |
      | 2.yaml              |


    Scenario Outline: Test JSON to YAML
    Given prepare a JSON file: <json_file_name>
    And prepare a YAML file: <yaml_file_name>
    When converting JSON to YAML
    Then comparison of expected and actual YAML
    Examples:
      | json_file_name     | yaml_file_name     |
      | 1.json             | 1.yaml             |
      | 2.json             | 2.yaml             |


    Scenario Outline: Test XML to YAML
    Given prepare a XML file: <xml_file_name>
    And prepare a YAML file: <yaml_file_name>
    When converting XML to YAML
    Then comparison of expected and actual YAML
    Examples:
      | xml_file_name      | yaml_file_name     |
      | 1.xml              | 1.yaml             |
      | 2.xml              | 2.yaml             |

    Scenario Outline: Test YAML to JSON
    Given prepare a YAML file: <yaml_file_name>
    And prepare a JSON file: <json_file_name>
    When converting YAML to JSON
    Then comparison of expected and actual JSON
    Examples:
      | yaml_file_name     | json_file_name      |
      | 1.yaml              | 1.json             |
      | 2.yaml              | 2.json             |