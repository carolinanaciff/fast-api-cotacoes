import aiohttp
from fastapi import HTTPException


async def async_converter(from_currency:str, to_currencies:str, value: float):

    from_currency = from_currency.upper()
    to_currencies = to_currencies.upper()
    url = f' https://economia.awesomeapi.com.br/last/{from_currency}-{to_currencies}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
    
    except Exception as ex:
        raise HTTPException(status_code=400, detail=ex)
    
    try:
        json_key = f'{from_currency}{to_currencies}'.upper()
        ask = float(data[json_key]['ask'])
        bid = float(data[json_key]['bid'])
        cotacao_data = data[json_key]['create_date']
        total_ask = ask * value
        total_bid = bid * value
    
    except Exception as ex:
        print('---'*10)
        print(ex)

    return {'Cotacao_de_para': data[json_key]['name'], 'Ask': ask, 'Bid': bid, 'Total_ask': total_ask, 'Total_bid': total_bid, 'Data_cotacao': cotacao_data}