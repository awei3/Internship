from loguru import logger
from tqdm import tqdm
from typing_extensions import Annotated
from zenml import get_step_context, step


@step
def crawl_links(name: str, links: list[str]) -> Annotated[list[str], "crawled_links"]:
    logger.info(f"Starting to crawl {len(links)} link(s) for school {name}.")

    metadata = {}
    successful_crawls = 0
    for link in tqdm(links):
        logger.info(f"Crawling {link}")
        successful_crawl = True
        successful_crawls += successful_crawl

        metadata = _add_to_metadata(metadata, name, successful_crawl)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="crawled_links", metadata=metadata)

    logger.info(f"Successfully crawled {successful_crawls} / {len(links)} links.")

    return links


"""
def _crawl_link(dispatcher: CrawlerDispatcher, link: str, user: UserDocument) -> tuple[bool, str]:
    crawler = dispatcher.get_crawler(link)
    crawler_domain = urlparse(link).netloc

    try:
        crawler.extract(link=link, user=user)

        return (True, crawler_domain)
    except Exception as e:
        logger.error(f"An error occurred while crowling: {e!s}")

        return (False, crawler_domain)
"""


def _add_to_metadata(metadata: dict, school_name: str, successful_crawl: bool) -> dict:
    if school_name not in metadata:
        metadata[school_name] = {}
    metadata[school_name]["successful"] = metadata[school_name].get("successful", 0) + successful_crawl
    metadata[school_name]["total"] = metadata[school_name].get("total", 0) + 1

    return metadata