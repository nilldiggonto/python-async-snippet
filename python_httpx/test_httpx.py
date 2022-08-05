import httpx
import json
import asyncio

BASE_URL = 'http://127.0.0.1:8005'
headers = {'Content-Type': 'application/json'}

params = {'ice':'cream','red':'rose'}


#### DOING GET CALL
# sync
def get_call_using_httpx():
    r = httpx.get(BASE_URL + '/hi',params=params,timeout=10)
    data = {
        'status':r.status_code,
        'server':r.headers['server'],
        'content':r.json(),
        # 'cookies':r.cookies['coca']
    }
    return data


def post_call_using_httpx():
    # payload = json.dumps({"ok": "ok"}) 
    payload_without_dmups = {'ok':'ok'}

    # r_post = httpx.post(BASE_URL+'/write',data=payload,headers=headers) #sending data
    r_post = httpx.post(BASE_URL+'/write',json=payload_without_dmups,headers=headers)  #sending json directly

    data = {
        'status':'post call',
        'content':r_post.json()
    }
    return data

# print(post_call_using_httpx())
# print(get_call_using_httpx())

### ADVANCE METHOD
async def using_httpx_client():
    payload_without_dmups = {'ok':'ok'}


    # with httpx.Client(headers=headers) as c:

    async with httpx.AsyncClient(headers=headers) as c:
        #GET CALL
        r = await c.get(BASE_URL + '/hi',params=params,timeout=10)
        #POST CALL
        r_post = await c.post(BASE_URL+'/write',json=payload_without_dmups)  #sending json directly

    data = {
        'status':r.status_code,
        'server':r.headers['server'],
        'content':r.json(),
        'post_content':r_post.json()
        # 'cookies':r.cookies['coca']
    }
    return data

# print(using_httpx_client())
print(asyncio.run(using_httpx_client()))


#--- Multiple Request with asyncio
url_list = ['one.com','two.com','three.com']
async def get_result(client,url):
    res = await client.get(url)
    return res.json()

async def manyRequest():
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in url_list:
            tasks.append(asyncio.create_task(get_result(client,url)))
        all_result = await asyncio.gather(*tasks)
# asyncio.run(manyRequest())

