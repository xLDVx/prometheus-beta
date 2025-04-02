import pytest
import time
import logging
from src.database_query_logger import log_query_execution_time

class TestDatabaseQueryLogger:
    def test_log_query_execution_time_basic(self, caplog):
        """
        Test basic functionality of query execution time logging
        """
        caplog.set_level(logging.INFO)
        
        @log_query_execution_time()
        def test_query():
            time.sleep(0.1)  # Simulate a slow query
            return "Result"
        
        # Execute the query
        result = test_query()
        
        # Check return value
        assert result == "Result"
        
        # Check logging
        assert len(caplog.records) == 1
        log_record = caplog.records[0]
        assert log_record.levelno == logging.INFO
        assert "test_query" in log_record.getMessage()
        assert "0.1" in log_record.getMessage()

    def test_log_query_execution_time_with_custom_logger(self, caplog):
        """
        Test logging with a custom logger
        """
        # Create a custom logger
        custom_logger = logging.getLogger('custom_db_logger')
        custom_logger.setLevel(logging.INFO)
        
        @log_query_execution_time(logger=custom_logger)
        def test_query_custom_logger():
            time.sleep(0.05)  # Simulate a query
            return "Custom Logger Result"
        
        # Capture logs for custom logger
        with caplog.at_level(logging.INFO, logger='custom_db_logger'):
            result = test_query_custom_logger()
        
        # Check return value
        assert result == "Custom Logger Result"
        
        # Check logging
        custom_logs = [record for record in caplog.records if record.name == 'custom_db_logger']
        assert len(custom_logs) == 1
        log_record = custom_logs[0]
        assert log_record.levelno == logging.INFO
        assert "test_query_custom_logger" in log_record.getMessage()
        assert "0.05" in log_record.getMessage()

    def test_log_query_execution_time_exception(self):
        """
        Test error handling and logging when an exception occurs
        """
        @log_query_execution_time()
        def query_with_error():
            raise ValueError("Simulated query error")
        
        # Expect the original exception to be raised
        with pytest.raises(ValueError, match="Simulated query error"):
            query_with_error()

    def test_log_query_execution_time_arguments(self, caplog):
        """
        Test that the decorator works with functions that have arguments
        """
        caplog.set_level(logging.INFO)
        
        @log_query_execution_time()
        def parameterized_query(param1, param2):
            time.sleep(0.02)
            return f"{param1} {param2}"
        
        # Execute with arguments
        result = parameterized_query("Hello", "World")
        
        # Check return value
        assert result == "Hello World"
        
        # Check logging
        assert len(caplog.records) == 1
        log_record = caplog.records[0]
        assert log_record.levelno == logging.INFO
        assert "parameterized_query" in log_record.getMessage()
        assert "0.02" in log_record.getMessage()