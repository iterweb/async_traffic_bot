import asyncio
import random
import lxml.html
import tldextract
from pyppeteer import launch
from class_proxy import GetProxy
from class_header import Header


class RateUp(Header, GetProxy):

    def __init__(self):
        self.min_time = 62
        self.max_time = 146
        self.browser_path = r''
        self.good = 0
        self.bad = 0

    async def go_to_url(self, proxy, header, url_list, resolution, semaphore):
        width, height = resolution.split('×')
        site_url = random.choice(url_list)
        links_from_site = []
        ext = tldextract.extract(site_url)
        async with semaphore:
            try:
                status = await self.validation_proxy(proxy, header)
                if status['status']:
                    self.good += 1
                    browser = await launch(
                        executablePath=self.browser_path,
                        args=[
                            f'--window-size={width},{height}',
                            f'--proxy-server={proxy}',
                        ],
                        headless=True
                    )
                    page = await browser.newPage()
                    await page.setViewport({'width': int(width), 'height': int(height)})
                    await page.setExtraHTTPHeaders(headers=header)
                    domain = site_url

                    for i in range(0, random.choice([2, 3, 4, 5, 6])):
                        if ext.subdomain:
                            header['host'] = f'{ext.subdomain}.{ext.domain}.{ext.suffix}'
                        else:
                            header['host'] = f'{ext.domain}.{ext.suffix}'
                        try:
                            try:
                                await page.goto(domain)
                            except:
                                pass
                            content = await page.content()

                            print(f'{resolution} | {status["country"]} | {domain} | {proxy} | {header}')
                            header['referer'] = domain
                            html = lxml.html.fromstring(content)
                            all_urls = html.xpath('//a/@href')
                            # print(all_urls)
                            await asyncio.sleep(random.uniform(self.min_time, self.max_time))
                            for u in all_urls:
                                if f'{ext.domain}.{ext.suffix}' in u:
                                    links_from_site.append(u)
                            if domain in links_from_site:
                                links_from_site.remove(domain)
                            domain = random.choice(links_from_site)
                        except:
                            domain = random.choice(url_list)
            except:
                self.bad += 1

            await browser.close()

    async def main(self, proxy_list_for_site, header_list, url_list):
        semaphore = asyncio.Semaphore(20)
        queue = asyncio.Queue()
        task_list = []

        for proxy in proxy_list_for_site:
            resolution = random.choice(Header.screen_resolution)
            header = random.choice(header_list)
            task = asyncio.create_task(self.go_to_url(proxy, header, url_list, resolution, semaphore))
            task_list.append(task)
            await asyncio.sleep(0.5)

        await queue.join()
        await asyncio.gather(*task_list, return_exceptions=True)
        print(f'Good visits: {self.good}')
        print(f'Bad visits: {self.bad}')

    def start(self, proxies, header_list, site_url):
        asyncio.run(self.main(proxies, header_list, site_url))
