import aiohttp
import asyncio
import json, re, os

import aiohttp.client_exceptions

class SEARCH:
    def __init__(self, search):
        self.search = search
        self.results = tuple()

    def initialize(self):
        loop = asyncio.new_event_loop()
        search_result = loop.run_until_complete(self._start_process())
        loop.close()
        
        return search_result



    async def _start_process(self):
        async def request(website_name):
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(9)) as r:
                await asyncio.sleep(0.01)
                website_key = websites[website_name]['SEARCH_ENGINE']
                
                params = website_key['payload']['params']
                data =  website_key['payload']['data']
                url = website_key['payload']['url']
                method = website_key['payload']['method']
                headers = website_key['payload']['headers']
                results = website_key['results']

                params = json.loads(
                    str(params).replace("{{search}}", self.search).replace("'", '"')
                )

                if method == "get":
                    api_response = await r.get(url, data=data, params=params, headers=headers)
                
                else:
                    api_response = await r.post(url, data=data, params=params, headers=headers)

                if api_response.status == 500:
                    api_response[website_name] = None
                    return api_response                    


                results = tuple(results.items())[0]
                final_return = {website_name: []}

                if results[0] == "json":
                    json_api_response = await api_response.json()

                    if "error" in json_api_response.keys():
                        final_return[website_name] = None
                        return final_return
                    
                    for api_json_obj in json_api_response.items():   ## otimizar e simplificar isso aqui
                        on_work_process = {'search': self.search, 'website': website_name}
                        await asyncio.sleep(0.01)

                        for website_json_key in results[1]:
                            on_work_process[website_json_key] = api_json_obj[1][website_json_key]

                            final_return[website_name].append(on_work_process)
            
            return final_return
        
                

        async def async_builder():
            websites_url =  websites.keys()
            tasks = []

            for i in websites_url:
                tasks.append(asyncio.create_task(request(i)))
                
            
            x = await asyncio.gather(*tasks)
            return x


        with open(os.getcwd()+"\\databases\\websites.json", 'r', encoding='utf-8') as r:
            websites = json.load(r)

        return await async_builder()