import json
from urllib.parse import quote


_event_value = {
    "id_": "mock-email-id-001",
    "title": "Mock Community Dinner",
    "from_": "Mock Sender",
    "date": "2026-04-01",
    "time": "18:00",
    "duration_minutes": 120,
    "start": "2026-04-01T18:00:00+11:00",
    "end": "2026-04-01T20:00:00+11:00",
    "recurrence": None,
    "location": "Mock Venue",
    "description": "Synthetic event used for Slack handler tests.",
    "confidence": 1.0,
    "source_url": "https://example.test/mail/mock-email-id-001",
}

_payload = {
    "type": "block_actions",
    "user": {
        "id": "U_TEST_USER",
        "username": "test-user",
        "name": "test-user",
        "team_id": "T_TEST_TEAM",
    },
    "api_app_id": "A_TEST_APP",
    "token": "test-verification-token",
    "container": {
        "type": "message",
        "message_ts": "1774679011.057059",
        "channel_id": "C_TEST_CHANNEL",
        "is_ephemeral": False,
    },
    "trigger_id": "1111111111111.2222222222222.mock-trigger-id",
    "team": {"id": "T_TEST_TEAM", "domain": "mock-workspace"},
    "enterprise": None,
    "is_enterprise_install": False,
    "channel": {"id": "C_TEST_CHANNEL", "name": "mock-channel"},
    "message": {
        "subtype": "bot_message",
        "text": "*Mock Community Dinner*\nMock Sender | 2026-04-01 18:00 | 120 mins",
        "type": "message",
        "ts": "1774679011.057059",
        "bot_id": "B_TEST_BOT",
        "blocks": [
            {
                "type": "section",
                "block_id": "mock-section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Mock Community Dinner*\nMock Sender | 2026-04-01 18:00 | 120 mins",
                    "verbatim": False,
                },
            },
            {
                "type": "actions",
                "block_id": "mock-actions",
                "elements": [
                    {
                        "type": "button",
                        "action_id": "approve",
                        "text": {
                            "type": "plain_text",
                            "text": "Approve",
                            "emoji": True,
                        },
                        "style": "primary",
                        "value": json.dumps(_event_value),
                    },
                    {
                        "type": "button",
                        "action_id": "deny",
                        "text": {
                            "type": "plain_text",
                            "text": "Decline",
                            "emoji": True,
                        },
                        "style": "danger",
                        "value": json.dumps(_event_value),
                    },
                ],
            },
        ],
    },
    "state": {"values": {}},
    "response_url": "https://hooks.slack.test/actions/T_TEST_TEAM/1111111111111/mock-response",
    "actions": [
        {
            "action_id": "decline",
            "block_id": "mock-actions",
            "text": {"type": "plain_text", "text": "Deny", "emoji": True},
            "value": json.dumps(_event_value),
            "style": "danger",
            "type": "button",
            "action_ts": "1774679081.918584",
        }
    ],
}

# A mock Slack event payload from a user action declining a proposed synthetic calendar event.
mock_slack_event = {
    "resource": "/slack",
    "path": "/slack",
    "httpMethod": "POST",
    "headers": {
        "Accept": "application/json,*/*",
        "Accept-Encoding": "gzip,deflate",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-ASN": "00000",
        "CloudFront-Viewer-Country": "ZZ",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "example.execute-api.ap-southeast-2.amazonaws.com",
        "User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        "Via": "1.1 mock-cloudfront-id.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "mock-cloudfront-request-id",
        "X-Amzn-Trace-Id": "Root=1-00000000-000000000000000000000000",
        "X-Forwarded-For": "203.0.113.10",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
        "X-Slack-Request-Timestamp": "1774679081",
        "X-Slack-Signature": "v0=mock-signature",
    },
    "multiValueHeaders": {
        "Content-Type": ["application/x-www-form-urlencoded"],
        "User-Agent": ["Slackbot 1.0 (+https://api.slack.com/robots)"],
        "X-Slack-Request-Timestamp": ["1774679081"],
        "X-Slack-Signature": ["v0=mock-signature"],
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "mock-resource",
        "resourcePath": "/slack",
        "httpMethod": "POST",
        "extendedRequestId": "mock-extended-request-id",
        "requestTime": "28/Mar/2026:06:24:42 +0000",
        "path": "/Prod/slack",
        "accountId": "000000000000",
        "protocol": "HTTP/1.1",
        "stage": "Prod",
        "domainPrefix": "example",
        "requestTimeEpoch": 1774679082436,
        "requestId": "00000000-0000-0000-0000-000000000000",
        "identity": {
            "sourceIp": "203.0.113.10",
            "userAgent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        },
        "domainName": "example.execute-api.ap-southeast-2.amazonaws.com",
        "deploymentId": "mock-deployment",
        "apiId": "mock-api-id",
    },
    "body": "payload=" + quote(json.dumps(_payload)),
    "isBase64Encoded": False,
}
