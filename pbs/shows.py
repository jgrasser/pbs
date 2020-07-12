from . import utils
import json

data = {
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
    "query": "query Shows($page: Int, $genre: String, $source: String, $stationId: String, $sortBy: String, $title: String, $alphabetically: Boolean) {shows(page: $page, genre: $genre, source: $source, stationId: $stationId, sortBy: $sortBy, title: $title, alphabetically: $alphabetically) {content { title genre description image url website cid __typename } meta { pageNumber totalPages totalResults __typename} stationCommonName __typename}}"
}


def graphql():
    try:
        resp = utils.client('POST', '/graphql', data=data)
        data['variables']['page'] += 1
        return resp['data']['shows']['content']
    except KeyError:
        return []

def list():
    shows = []
    for s in iter(graphql, []):
        shows += s
    return json.dumps({"shows": shows})
