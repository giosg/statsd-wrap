import unittest
from statsd_wrap.statsd import StatsD


class StatsDClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        host = "test-host"
        port = 8125
        namespace = "unittest"
        tags = {
            "is_unit_test": "yes"
        }
        self.client = StatsD(host, port, namespace=namespace, tags=tags)

    def test_can_call_method(self) -> None:
        self.client.increment("metric1", value=1.0, tags={})
