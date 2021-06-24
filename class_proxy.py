import httpx
from httpx_socks import AsyncProxyTransport

class GetProxy:

    async def validation_proxy(self, proxy, header):
        transport = AsyncProxyTransport.from_url(proxy)
        async with httpx.AsyncClient(transport=transport, headers=header, timeout=10) as client:
            response = await client.get('http://ipwhois.app/json/')
            return {
                'status': response.json()['success'],
                'country': response.json()['country'],
                }

    def get_proxy(self, http=None, socks4=None, socks5=None, unknown=None):
        """Path to proxy file(s)"""
        proxy_list = []
        protocols = {}
        if http != None:
            protocols['http'] = http
        if socks4 != None:
            protocols['socks4'] = socks4
        if socks5 != None:
            protocols['socks5'] = socks5
        if unknown != None:
            protocols['unknown'] = unknown
        for key, value in protocols.items():
            with open(value) as file:
                f = file.readlines()
                for p in f:
                    d = p.replace(' ', '').replace('\n', '')
                    if key == 'unknown':
                        for prtcl in ['http', 'socks4', 'socks5']:
                            proxy_list.append(f"{prtcl}://{d}")
                    else:
                        proxy_list.append(f"{key}://{d}")
        return proxy_list