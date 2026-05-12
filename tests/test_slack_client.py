import pytest
from slack_sdk import WebClient
from unittest.mock import MagicMock
from services.slack_client import SlackClient, build_slack_msg
from tests.mock_event import mock_event
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.mark.skip(reason="Uses actual service. Need to implement with MagicMock")
def test_connection():
    client = WebClient()
    api_response = client.api_test()


# Creates a mock message in slack (need to delete manually)
@pytest.mark.skip(reason="Uses actual service. Need to implement with MagicMock")
def test_send_msg():
    mock_client = MagicMock()
    sc = SlackClient(client=mock_client)
    e = mock_event
    msg_schema = build_slack_msg(event=e)
    response = sc.send_msg(msg_schema)
    msg_response = json.loads(response["message"]["blocks"][1]["elements"][0]["value"])

    assert response.status_code == 200
    assert response["ok"]
    assert msg_response["title"] == e.title
