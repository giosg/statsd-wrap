from typing import Dict, List, Optional, Any
import datetime
import datadog


Tags = Dict[str, str]


class StatsD:
    def __init__(self, host: str, port: int, namespace: Optional[str] = None, tags: Tags = {}) -> None:

        self._client = datadog.DogStatsd(
            host, port,
            namespace=namespace,
            constant_tags=self._tag_dict_to_list(tags)
        )

    @staticmethod
    def _tag_dict_to_list(tags: Tags) -> List[str]:
        return [
            "%s:%s" % (key, value)
            for key, value in sorted(tags.items())
        ]

    def gauge(self, metric: str, value: float, tags: Tags = {}) -> None:
        self._client.gauge(
            metric, value,
            tags=self._tag_dict_to_list(tags),
        )

    def increment(self, metric: str, value: float = 1.0, tags: Tags = {}) -> None:
        self._client.increment(
            metric, value,
            tags=self._tag_dict_to_list(tags),
        )

    def decrement(self, metric: str, value: float = 1.0, tags: Tags = {}) -> None:
        self._client.decrement(
            metric, value,
            tags=self._tag_dict_to_list(tags),
        )

    def timing(self, metric: str, value: datetime.timedelta, tags: Tags = {}) -> None:
        self._client.timing(
            metric, value.total_seconds() * 1000.0,
            tags=self._tag_dict_to_list(tags),
        )

    def timed(self, metric: str, tags: Tags = {}) -> Any:
        return self._client.timed(
            metric,
            tags=self._tag_dict_to_list(tags),
            use_ms=True,
        )
