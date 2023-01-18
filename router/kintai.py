from fastapi import APIRouter, Request

router = APIRouter(
	prefix="/kintai",
	tags=["kintai"],
	responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def echo_test(request: Request):
	form_data = await request.form()
	message = {
		# 下の1行を付け足すことによって、全体にメッセージが見えるようになる
		'response_type': 'in_channel',
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f"<@{form_data.get('user_id')}> さん、こんにちは！あるいはこんばんは :wave:"
				}
			}
		]
	}
	return message

@router.post("/start")
async def attendance(request: Request):
	form_data = await request.form()
	message = {
		'response_type': 'in_channel',
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f"<@{form_data.get('user_id')}> が {form_data.get('text')} の作業を開始しました！"
				}
			}
		]
	}
	return message

@router.post("/end")
async def leave(request: Request):
	form_data = await request.form()
	message = {
		'response_type': 'in_channel',
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f"<@{form_data.get('user_id')}> さんが頑張っていました！"
				}
			}
		]
	}
	return message
