import dataclasses
from redisearch.client import TextField

from sitesearch.models import SiteConfiguration, SynonymGroup
from sitesearch.scorers import boost_pages, boost_top_level_pages
from sitesearch.validators import skip_404_page, skip_release_notes
from sitesearch.sites.redis_labs_landing_pages import LANDING_PAGES


SYNONYMS = [
    SynonymGroup(
        group_id='insight',
        synonyms={'redisinsight', 'insight'}
    ),
    SynonymGroup(
        group_id='active',
        synonyms={'active', 'active-active', 'active active'}
    ),
    SynonymGroup(
        group_id='json',
        synonyms={'json', 'RedisJSON', 'redis json'}
    ),
    SynonymGroup(
        group_id='timeseries',
        synonyms={'timeseries', 'RedisTimeSeries', 'redis timeseries'}
    ),
    SynonymGroup(
        group_id='ai',
        synonyms={'ai', 'RedisAI', 'redis ai'}
    ),
    SynonymGroup(
        group_id='graph',
        synonyms={'graph', 'RedisGraph', 'redis graph'}
    ),
    SynonymGroup(
        group_id='gears',
        synonyms={'gears', 'RedisGears', 'redis gears'}
    ),
    SynonymGroup(
        group_id='search',
        synonyms={'redisearch', 'readisearch', 'search'}
    ),
    SynonymGroup(
        group_id='enterprise',
        synonyms={'enterprise', 'redis enterprise'}
    ),
    SynonymGroup(
        group_id='cloud',
        synonyms={"cloud", "redis enterprise cloud"}
    ),
    # This is to avoid doing a fuzzy search on 'redis' -- the
    # API does exact match searches on synonym terms.
    SynonymGroup(
        group_id='redis',
        synonyms={'redis'}
    )
]

DOCS_PROD = SiteConfiguration(
    url="https://docs.redislabs.com/latest/",
    synonym_groups=SYNONYMS,
    landing_pages=LANDING_PAGES,
    allowed_domains=('docs.redislabs.com',),
    schema=(
        TextField("title", weight=10),
        TextField("section_title"),
        TextField("body", weight=1.5),
        TextField("url"),
        TextField("s", no_stem=True),
    ),
    scorers=(
        boost_pages,
        boost_top_level_pages
    ),
    validators=(
        skip_release_notes,
        skip_404_page
    ),
    deny=(r'\/release-notes\/', r'.*\.tgz'),
    allow=(),
    content_classes=(".main-content",)
)

DOCS_STAGING = dataclasses.replace(
    DOCS_PROD,

    # Uncomment and use your branch to index staging content.
    # url="https://docs.redislabs.com/staging/<your-branch>"
)

DEVELOPERS = SiteConfiguration(
    url="https://developer.redislabs.com",
    synonym_groups=SYNONYMS,
    landing_pages={},
    allowed_domains=('developer.redislabs.com',),
    schema=(
        TextField("title", weight=10),
        TextField("section_title"),
        TextField("body", weight=1.5),
        TextField("url"),
        TextField("s", no_stem=True),
    ),
    scorers=(),
    validators=(
        skip_404_page,
    ),
    allow=(),
    deny=(
        r'.*\.pdf',
        r'.*\.tgz',
    ),
    content_classes=(".markdown", ".margin-vert--md", ".main-wrapper")
)

CORPORATE = SiteConfiguration(
    url="https://redislabs.com",
    synonym_groups=SYNONYMS,
    landing_pages=LANDING_PAGES,
    allowed_domains=('redislabs.com',),
    schema=(
        TextField("title", weight=10),
        TextField("section_title"),
        TextField("body", weight=1.5),
        TextField("url"),
        TextField("s", no_stem=True),
    ),
    scorers=(
        boost_pages,
        boost_top_level_pages
    ),
    validators=(
        skip_404_page,
    ),
    deny=(
        r'.*\.pdf',
        r'.*\.tgz',
        r'\/tag\/.*',
    ),
    allow=(),
    content_classes=(".bounds-content", ".bounds-inner")
)

OSS = SiteConfiguration(
    url="https://redis.io",
    synonym_groups=SYNONYMS,
    landing_pages=LANDING_PAGES,
    allowed_domains=("redis.io",),
    schema=(
        TextField("title", weight=10),
        TextField("section_title"),
        TextField("body", weight=1.5),
        TextField("url"),
        TextField("s", no_stem=True),
    ),
    scorers=(
        boost_pages,
        boost_top_level_pages
    ),
    validators=(
        skip_404_page,
    ),
    deny=(
        r'.*\.pdf',
        r'.*\.tgz',
    ),
    allow=(),
    content_classes=(".site-content",)
)
