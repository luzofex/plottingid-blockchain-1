from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "plottingid_harvester plottingid_timelord_launcher plottingid_timelord plottingid_farmer plottingid_full_node plottingid_wallet".split(),
    "node": "plottingid_full_node".split(),
    "harvester": "plottingid_harvester".split(),
    "farmer": "plottingid_harvester plottingid_farmer plottingid_full_node plottingid_wallet".split(),
    "farmer-no-wallet": "plottingid_harvester plottingid_farmer plottingid_full_node".split(),
    "farmer-only": "plottingid_farmer".split(),
    "timelord": "plottingid_timelord_launcher plottingid_timelord plottingid_full_node".split(),
    "timelord-only": "plottingid_timelord".split(),
    "timelord-launcher-only": "plottingid_timelord_launcher".split(),
    "wallet": "plottingid_wallet plottingid_full_node".split(),
    "wallet-only": "plottingid_wallet".split(),
    "introducer": "plottingid_introducer".split(),
    "simulator": "plottingid_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
