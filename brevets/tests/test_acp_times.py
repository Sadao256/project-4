"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import arrow
import brevets.acp_times import open_time, close_time # important function open_time and close_time from acp_times

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_open_time():
    start_time = arrow.get("2023-11-04T09:20:00")
    assert acp_times.open_time(0, 200, start_time) == start_time
    assert acp_times.open_time(0, 1000, start_time) == start_time
    
    assert close_time(200,200, arrow.get("2023-11-04T12:00:00")) == arrow.get("2023-11-04T05:53:00")
    assert open_time(400,400, arrow.get("2023-11-04T12:00:00")) == arrow.get("2023-11-04T12:30:00")

def test_close_time():
    start_time = arrow.get("2023-11-04T12:00:00")
    assert close_time(0, 200, start_time) != start_time
    assert close_time(0, 200, start_time) == start_time.shift(hours=1)
    assert close_time(0, 1000, start_time) == start_time.shift(hours=1)

    assert close_time(200,200, start_time) == arrow.get("2023-11-04T01:30:00")
    assert close_time(200,200, start_time) != arrow.get("2023-11-04T01:20:00")
    assert close_time(400,400, start_time) == arrow.get("2023-11-04T03:00:00")
    assert close_time(1000,1000, start_time) ==  arrow.get("2023-11-04T03:00:00")











