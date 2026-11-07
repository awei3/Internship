import datetime as dt
from pathlib import Path

import click

from pipelines.school_data_etl import school_data_etl


@click.command()
@click.option(
    "--run-etl",
    is_flag=True,
    help="Run the school data ETL pipeline.",
)
@click.option(
    "--etl-config-filename",
    default="school_data_etl.yaml",
    help="Name of the ETL configuration file.",
)
def main(run_etl: bool, etl_config_filename: str):
    if run_etl:
        root_dir = Path(__file__).resolve().parent.parent
        config_path = root_dir / "configs" / etl_config_filename

        pipeline_args = {
            "config_path": str(config_path),
            "run_name": f"school_data_etl_{dt.datetime.now():%Y%m%d_%H%M%S}",
        }

        school_data_etl.with_options(**pipeline_args)()


if __name__ == "__main__":
    main()