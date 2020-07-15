# pbs

Search and play video content from PBS.org

There's not much here in the way of features or pizzazz. This is a dumb CLI tool that makes basic API calls; it doesn't even format the output nicely!

## Installation

Installation is managed via the Makefile. The makefile just installs some python packages. It's simple.

```shell
git clone https://github.com/jgrasser/pbs.git
cd pbs
make install
```

## Usage

## API Documentation

### Get Member Stations

**Parameters**

| Parameter | Description |
| --------- | ----------- |
| statecode | 2 character code for a US State. Examples include IL, CA, NY, etc.|

**Request**

	GET - https://jaws.pbs.org/localization/member/state/:statecode/

**Response**
```json
{
    "stations_list": [
        {
            "address": "Urbana, IL",
            "callsign": "WILL",
            "common_name": "Illinois Public Media",
            "common_name_short": "WILL-TV",
            "flagship": "WILL",
            "membership_url": "https://willpledge.org/",
            "pbs_id": "11bd36cd-46d5-4c3a-bdc8-ae497a23c712",
            "pdp": false
        },
        ...
```

### Query PBS Shows

**Parameters**

| Parameter | Description |
| --------- | ----------- |
| pbs-id | 36 character identifier obtained from member station api call above |

**Request**

	POST - https://www.pbs.org/graphql

**BODY**
```json
{
    "operationName": "Shows",
    "variables": {
        "page": 0,
        "genre": "all-genres",
        "sortBy": "popular",
        "source": "all-sources",
        "stationId": :pbs-id,
        "title": "",
        "alphabetically": false
    },
    "query": "query Shows($page: Int, $genre: String, $source: String, $stationId: String, $sortBy: String, $title: String, $alphabetically: Boolean) {shows(page: $page, genre: $genre, source: $source, stationId: $stationId, sortBy: $sortBy, title: $title, alphabetically: $alphabetically) {content { title genre description image url website cid __typename } meta { pageNumber totalPages totalResults __typename} stationCommonName __typename}}"
}
```

**Response**
```json
{
    "shows": [
        {
            "__typename": "Show",
            "cid": "033db3e2-3d1f-4c0f-8cd7-746578cb74d8",
            "description": "Since its launch in 2012, the PBS Online Film Festival has featured diverse films from PBS member stations and ITVS and POV. This year's festival includes collaborations with a wide variety of public television producers. Starting July 13, viewers can once again watch, vote and share their favorites. Find out how to vote for your favorites at pbs.org/filmfestival",
            "genre": [
                "indie-films"
            ],
            "image": "https://image.pbs.org/contentchannels/XLtKO9n-show-poster2x3-H4SwmKp.jpg",
            "title": "PBS Short Film Festival",
            "url": "/show/pbs-online-film-festival/",
            "website": "https://www.pbs.org/filmfestival"
        },
        ...
```

### Get Show Seasons

**Parameters**

| Parameter | Description |
| --------- | ----------- |
| show-name | The name of the show you want to watch. Example is __nova__. |

**Request**

	GET - https://www.pbs.org/show/:show-name/seasons-list/

**Response**
```json
{
    "content": [
        {
            "ancestor_slug": null,
            "ancestor_title": null,
            "ancestor_type": null,
            "cid": "c0537bb4-2bf2-4876-82cd-cc3ac922a037",
            "flags": {
                "has_assets": true,
                "has_episodes": true
            },
            "image": "https://image.pbs.org/video-assets/sm4FufA-asset-mezzanine-16x9-3vXOfLV.jpg",
            "images": {
                "asset-mezzanine-16x9": "https://image.pbs.org/video-assets/sm4FufA-asset-mezzanine-16x9-3vXOfLV.jpg"
            },
            "item_type": "season",
            "legacy_tp_media_id": null,
            "ordinal": 47,
            "parent_type": null,
            "summary": "",
            "title": "",
            "title_sortable": "",
            "url": "https://content.services.pbs.org/v3/pbsorg/screens/shows/nova/seasons/c0537bb4-2bf2-4876-82cd-cc3ac922a037/"
        },
        ...
```

### Get Episodes in a Season

**Parameters**

| Parameter | Description |
| --------- | ----------- |
| show-name | The name of the show you want to watch. Example is __nova__. |
| season-cid | Unique identifier for a season of a show. Reference output of seasons-list above.|

**Request**

	GET - https://www.pbs.org/show/:show-name/seasons/:season-cid/episodes/

**Reponse**
```json
{
    "content": [
        {
            "ancestor_slug": "nova",
            "ancestor_title": "NOVA",
            "ancestor_type": "show",
            "availability": "available",
            "cid": "4255528e-0a63-4c52-b8fe-dc8c9353a3d2",
            "description_long": "The coronavirus SARS-CoV-2 has upended life as we know it in a matter of months. But at the same time, an unprecedented global effort to understand and contain the virus\u2014and find a treatment for the disease it causes\u2014is underway. Join doctors on the front lines of the fight against COVID-19 as they strategize to stop the spread, and meet the researchers racing to develop treatments and vaccines.",
            "description_short": "Scientists race to understand and defeat the coronavirus behind the COVID-19 pandemic.",
            "duration": 3218,
            "encore_date": "2020-05-13T00:00:00-04:00",
            "expire_date": "2023-05-13T03:59:59Z",
            "flags": {
                "has_captions": true,
                "is_expiring_soon": false,
                "is_fully_watched": null,
                "is_mvod": false,
                "is_new": false
            },
            "image": "https://image.pbs.org/video-assets/j2MoiWW-asset-mezzanine-16x9-nSazGBW.jpg",
            "images": {
                "asset-mezzanine-16x9": "https://image.pbs.org/video-assets/j2MoiWW-asset-mezzanine-16x9-nSazGBW.jpg"
            },
            "item_type": "video",
            "legacy_tp_media_id": 3042320248,
            "parent_type": "episode",
            "premiere_date": "2020-05-13T00:00:00-04:00",
            "seconds_watched": null,
            "show": {
                "display_episode_number": true,
                "episode": 9,
                "season": 47,
                "seasons_count": 22,
                "slug": "nova",
                "title": "NOVA"
            },
            "slug": "decoding-covid-19-hrfhb2",
            "summary": "S47 Ep9 | 53m 38s",
            "title": "Decoding COVID-19",
            "title_sortable": "Decoding COVID-19",
            "url": "https://content.services.pbs.org/v3/pbsorg/screens/video-assets/decoding-covid-19-hrfhb2/",
            "video_type": "episode"
        },
        ...
```

### Get Rich Episode Video Data

**Parameters**

| Parameter | Description |
| ---------------- | ----------- |
| legacy-tp-media-id |  A video's legacy identifier. Used to fetch video metadata sent to JWPlayer. |

**Reqeust**

	GET - https://player.pbs.org/portalplayer/:legacy-tp-media-id/

**Response**
```html
<!doctype html>
...
<body>
...
<script>
	window.staticUrl = "/static/";
	window.contextBridge = {"player_type": "portal_player", "callsign": null, "user_id": "", "country_id": "US", "viewing_history": {}, "player_framework": "Video.js", "features": {"nielsen": false, "videojs": false}};
	window.videoBridge = {"availability": "available", "encodings": ["https://urs.pbs.org/redirect/ceb9dea094b04baf9ebb22f726712d09/", "https://urs.pbs.org/redirect/4b3af54f7cda4fefa8459a99cd177333/"], "has_hls_encodings": true, "has_mp4_encodings": true, "cc": {"WebVTT": "https://ga.video.cdn.pbs.org/captions/nova/4255528e-0a63-4c52-b8fe-dc8c9353a3d2/captions/kUfgWv_caption.vtt", "SRT": "https://ga.video.cdn.pbs.org/captions/nova/4255528e-0a63-4c52-b8fe-dc8c9353a3d2/captions/Thxrj1_caption.srt", "DFXP": "https://ga.video.cdn.pbs.org/captions/nova/4255528e-0a63-4c52-b8fe-dc8c9353a3d2/captions/OCh5Ix_caption.dfxp", "Caption-SAMI": "https://ga.video.cdn.pbs.org/captions/nova/4255528e-0a63-4c52-b8fe-dc8c9353a3d2/captions/3nJKHG_caption.sami"}, "can_play_preroll": true, "image_url": "https://image.pbs.org/video-assets/j2MoiWW-asset-mezzanine-16x9-nSazGBW.jpg", "chapters": [], "mvod_info": {"show_mvod_icon": false, "show_upsell_overlay": false}, "program": {"title": "NOVA", "slug": "nova", "producer": "PBS"}, "related_videos": [{"id": 3042550069, "title": "Trailer", "images": {"mezzanine": "https://image.pbs.org/video-assets/8XmGmaI-asset-mezzanine-16x9-vm5hyEc.jpg"}, "program": {"funder_message": "Funding for MASTERPIECE is provided by Viking and Raymond James with additional support from public television viewers and contributors to The MASTERPIECE Trust, created to help ensure the series\u2019 future.", "cid": "31598537-8a0a-4441-95b0-6155d52dee28", "audience": [{"station": null, "scope": "national"}], "display_episode_number": true, "title": "Grantchester", "tracking_ga_page": "UA-3988763-1", "seasons_count": 5, "tracking_ga_event": "UA-3988763-2", "slug": "grantchester", "resource_type": "show", "franchise": {"funder_message": "Funding for MASTERPIECE is provided by Viking with additional support from public television viewers and contributors to The MASTERPIECE Trust, created to help ensure the series\u2019 future.", "title": "Masterpiece", "cid": "e08bf78d-e6a3-44b9-b356-8753d01c7327", "resource_type": "franchise", "slug": "masterpiece"}}, "slug": "trailer-1owamh"}, {"id": 3039879374, "title": "Extended Trailer | The Vote | American Experience", "images": {"mezzanine": "https://image.pbs.org/video-assets/zU2qsCH-asset-mezzanine-16x9-yCQVFSq.jpg"}, "program": {"title": "Part 1 | The Vote | American Experience", "ordinal": 9, "season": {"title": "", "cid": "acf1d226-027a-4032-8cb9-56618eab2467", "resource_type": "season", "ordinal": 32, "show": {"tracking_ga_page": "UA-3988626-1", "title": "American Experience", "resource_type": "show", "audience": [{"station": null, "scope": "national"}], "funder_message": "Corporate sponsorship for American Experience is provided by Liberty Mutual Insurance and Consumer Cellular. Major funding by the Alfred P. Sloan Foundation.", "seasons_count": 30, "cid": "1b91e824-10a2-4c3e-b054-74f78fcddcc7", "tracking_ga_event": "UA-3988626-2", "slug": "american-experience", "display_episode_number": true, "franchise": null}}, "cid": "2bad0e1b-ead2-4eb4-9a27-3478d6bee182", "resource_type": "episode", "slug": "vote-part-1"}, "slug": "trailer-vote-american-experience"}, {"id": 3042347034, "title": "Preview", "images": {"mezzanine": "https://image.pbs.org/video-assets/wPSEK08-asset-mezzanine-16x9-z2Gtd5J.jpg"}, "program": {"tracking_ga_page": "", "title": "Prehistoric Road Trip", "resource_type": "show", "audience": [{"station": null, "scope": "national"}], "seasons_count": 1, "tracking_ga_event": "", "cid": "a1ddde11-3f9f-4ddd-ab9f-7ae25fab5d1c", "funder_message": "", "slug": "prehistoric-road-trip", "display_episode_number": true, "franchise": null}, "slug": "preview-wwhtpl"}], "member_stations": [], "video_type": "full_length", "id": "3042320248", "cid": "4255528e-0a63-4c52-b8fe-dc8c9353a3d2", "slug": "decoding-covid-19-hrfhb2", "title": "Decoding COVID-19", "short_description": "Scientists race to understand and defeat the coronavirus behind the COVID-19 pandemic.", "long_description": "The coronavirus SARS-CoV-2 has upended life as we know it in a matter of months. But at the same time, an unprecedented global effort to understand and contain the virus\u2014and find a treatment for the disease it causes\u2014is underway. Join doctors on the front lines of the fight against COVID-19 as they strategize to stop the spread, and meet the researchers racing to develop treatments and vaccines.", "series_info": "Season 47 Episode 9", "duration": 3218, "air_date": "2020-05-13T00:00:00-04:00", "air_date_formatted": "May 13th, 2020", "air_date_nielsen": "20200513 00:00:00", "expire_date": "2023-05-13T03:59:59Z", "rating": null, "is_mvod": false, "allow_embed": true, "short_common_name": "", "full_common_name": null, "station_color_logo": null, "donation_url": null, "passport_url": null, "passport_learn_more_url": null, "dvd_link": null, "itunes_link": null, "GA_events_codes": ["UA-3988832-2"], "GA_national_codes": ["UA-1996666-7"]};
</script>
...
</body>
```
