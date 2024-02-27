{
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Admin에 음원이 등록되었습니다.\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "rich_text",
			"elements": [
				{
					"type": "rich_text_section",
					"elements": [
						{
							"type": "text",
							"text": "음원명 ",
							"style": {
								"bold": true
							}
						},
						{
							"type": "emoji",
							"name": "musical_note"
						}
					]
				},
				{
					"type": "rich_text_list",
					"style": "bullet",
					"elements": [
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "음원 길이 : 00:00"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "분위기 : "
								},
								{
									"type": "text",
									"text": "#000 #000 #000"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "ISRC : "
								},
								{
									"type": "text",
									"text": "000000000"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "플레이: "
								},
								{
									"type": "link",
									"url": "https://slack.com/",
									"text": "미리 듣기",
									"style": {
										"bold": true
									}
								}
							]
						}
					]
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Admin 페이지에서 확인이 가능합니다."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Click Me",
					"emoji": true
				},
				"value": "click_me_123",
				"url": "https://google.com",
				"action_id": "button-action"
			}
		}
	]
}
