"""Probe SciPy/NumPy availability in the existing Discovery CI runner.
Do not claim a continuous-time result from this environment check.
"""
import importlib.util
import platform
import unittest

class TimeframeEnvironmentTest(unittest.TestCase):
    def test_runner_capabilities(self):
        numpy=importlib.util.find_spec("numpy") is not None
        scipy=importlib.util.find_spec("scipy") is not None
        print("ICO_TIMEFRAME_ENV: "+str({"python":platform.python_version(),"numpy_present":numpy,"scipy_present":scipy}),flush=True)
        self.assertTrue(True)
