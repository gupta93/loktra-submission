import requests,json,sys
from BeautifulSoup import BeautifulSoup


def getTotalCount(keyword):

    url = 'http://www.shopping.com/products?KW=' + keyword
    resp = requests.get(url)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text)
        total = soup.find('span', {'class': 'numTotalResults'})
        total = total.text
        total = total.split(' ')
        totalResult = total[-1]
        if '1500' in totalResult:
            print '1500+'
        else:
            print totalResult
    else:
        print 'Invalid Url'

def getAllResults(keyword,pageNo):

    url = 'http://www.shopping.com/products~PG-' + str(pageNo) + '?KW=' + keyword
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text)
        value = soup.findAll("span", {"class": "quickLookGridItemFullName hide"})

        for item in value:
            print item.text

    else:
        print 'Invalid Url'

def loktra():

    if len(sys.argv[1:])==1:
        keyword = sys.argv[1]
        getTotalCount(keyword)

    else:
        arguments = sys.argv[1:]
        if arguments[-1].isdigit()==True:
            keyword = '+'.join(arg for arg in arguments[:-1])
            pageNo  = arguments[-1]
            getAllResults(keyword,pageNo)

        else:
            keyword = '+'.join(arg for arg in arguments)
            getTotalCount(keyword)




if __name__=="__main__":
    loktra()
