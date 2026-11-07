from zenml import pipeline
from steps.etl.crawl_links import crawl_links


@pipeline
def school_data_etl(name: str, links: list[str]) -> str:
    last_step = crawl_links(name=name, links=links)

    return last_step.invocation_id