# test_kubeflowpipelines.py
"""
Tests for KubeflowPipelines module.
"""

import unittest
from kubeflowpipelines import KubeflowPipelines

class TestKubeflowPipelines(unittest.TestCase):
    """Test cases for KubeflowPipelines class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KubeflowPipelines()
        self.assertIsInstance(instance, KubeflowPipelines)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KubeflowPipelines()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
