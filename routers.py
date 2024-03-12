from fastapi import APIRouter, Path, Query
from asyncio import gather
from converter import async_converter


router = APIRouter()


@router.get('/')
def hello_world ():
    return 'Hello world!'

@router.get('/cotacoes-moedas/')
async def cotacoes_moedas(
    from_currency: str = Query(max_length=3, regex='^[A-Z]{3}$'), 
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'), 
    value: float = Query(gt=0)):
    
    to_currencies = to_currencies.split(',')

    corotines = []

    for currency in to_currencies:
        response = async_converter(
            from_currency=from_currency,
            to_currencies=currency,
            value=value
        )
        print(response)
        corotines.append(response)
    
    result = await gather(*corotines)
    return result