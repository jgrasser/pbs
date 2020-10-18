import rest
import json
import time

def episodes(show, season_cid):

   status, data = rest.client('GET', f'/show/{show}/seasons/{season_cid}/episodes/?start=0&limit=24')

   return data


def seasons(show):
   
   status, data = rest.client('GET', f'/show/{show}/seasons-list/')

   return data


def shows():
    graphql = {
        "operationName": "Shows",
        "variables": {
            "page": 0,
            "genre": "all-genres",
            "sortBy": "popular",
            "source": "all-sources",
            "stationId": "8030a253-4b34-463e-82e2-ec0726e24e58",
            "title": "",
            "alphabetically": False
        },
        "query": "query Shows($page: Int, $genre: String, $source: String, \
                              $stationId: String, $sortBy: String, \
                              $title: String, $alphabetically: Boolean) {\
                            shows(page: $page, genre: $genre, source: $source, \
                                  stationId: $stationId, sortBy: $sortBy, \
                                  title: $title, \
                                  alphabetically: $alphabetically) {\
                                content { title \
                                      genre \
                                      description \
                                      image \
                                      url \
                                      website \
                                      cid \
                                      __typename } \
                            meta { pageNumber \
                                  totalPages \
                                  totalResults \
                                  __typename} \
                            stationCommonName \
                            __typename}}"
    }

    shows = []
    try:
        while True:
            print("Fetching shows page %02d" % (graphql['variables']['page']+1))
            status, data = rest.client('POST', '/graphql', data=graphql)

            if status == 200:
                graphql['variables']['page'] += 1
            else:
                print("Request failed... Sleeping %02d seconds" % (15))
                time.sleep(15)
                continue

            data = json.loads(data)

            pageNumber = data["data"]["shows"]["meta"]["pageNumber"]
            totalPages = data["data"]["shows"]["meta"]["totalPages"]
            content = data['data']['shows']['content']

            if(pageNumber < totalPages):
                shows += content
            else:
                break

    except Exception as e:
        print("Api was flaky. Such is life: %s" % e)

    finally:
        return shows
