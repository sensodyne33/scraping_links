from requests_html import HTMLSession
import pandas as pd

for i in range(0,20,10):
    url = 'https://www.indeed.com/jobs?q=python&l=Brooklyn%2C%20NY&start={i}&vjk=d18dbc9fbda53b3f'
    session = HTMLSession()
    r = session.get(url)
    print(r.status_code)

    links = r.html.xpath('//*[@id="mosaic-provider-jobcards"]', first=True)

    joblist = []
    #create a loop for each link
    for item in links.absolute_links:
        response = session.get(item)
        try:
            title = response.html.find('h1.jobsearch-JobInfoHeader-title', first=True).text.strip().replace('\n', ' ')
            company = response.html.find('div.jobsearch-CompanyInfoWithoutHeaderImage', first=True).text.strip().replace('\n', ' ')
            salary = response.html.find('span.icl-u-xs-mr--xs', first=True).text.strip().replace('\n', ' ')
            qualifications = response.html.find('ul.jobsearch-ReqAndQualSection-item--closedBullets', first=True).text.strip().replace('\n', ' ')
            job = {'title': title, 'company': company, 'salary': salary, 'qualifications': qualifications}
            joblist.append(job)
        except:
            pass


    df = pd.DataFrame(joblist)
    print(df.head())
    df.to_csv('last.csv', mode='a', index='False')