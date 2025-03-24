import os
import json
import pytest
import shutil
from src.multiple_choice_logger import MultipleChoiceLogger

class TestMultipleChoiceLogger:
    def setup_method(self):
        # Create a temporary log directory for each test
        self.test_log_dir = 'test_logs'
        os.makedirs(self.test_log_dir, exist_ok=True)
    
    def teardown_method(self):
        # Remove temporary log directory after each test
        if os.path.exists(self.test_log_dir):
            shutil.rmtree(self.test_log_dir)
    
    def test_log_response_basic(self):
        """Test basic logging of a response"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        log_entry = logger.log_response(
            question_id='q1', 
            user_id='user1', 
            response='A'
        )
        
        assert log_entry['question_id'] == 'q1'
        assert log_entry['user_id'] == 'user1'
        assert log_entry['response'] == 'A'
        
        # Check file was created
        log_filename = os.path.join(self.test_log_dir, 'q1_responses.json')
        assert os.path.exists(log_filename)
        
        # Check log file contents
        with open(log_filename, 'r') as f:
            entries = json.load(f)
            assert len(entries) == 1
            assert entries[0]['question_id'] == 'q1'
    
    def test_log_response_with_valid_options(self):
        """Test logging with valid options constraint"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        log_entry = logger.log_response(
            question_id='q2', 
            user_id='user2', 
            response='B',
            valid_options=['A', 'B', 'C']
        )
        
        assert log_entry['response'] == 'B'
    
    def test_log_response_invalid_option(self):
        """Test that an invalid option raises an error"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        with pytest.raises(ValueError, match="Invalid response"):
            logger.log_response(
                question_id='q3', 
                user_id='user3', 
                response='D',
                valid_options=['A', 'B', 'C']
            )
    
    def test_log_response_multiple_entries(self):
        """Test logging multiple responses for the same question"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        # Log two different responses
        logger.log_response('q4', 'user1', 'A')
        logger.log_response('q4', 'user2', 'B')
        
        log_filename = os.path.join(self.test_log_dir, 'q4_responses.json')
        with open(log_filename, 'r') as f:
            entries = json.load(f)
            assert len(entries) == 2
            assert entries[0]['user_id'] == 'user1'
            assert entries[1]['user_id'] == 'user2'
    
    def test_invalid_inputs(self):
        """Test various invalid input scenarios"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        # Empty question_id
        with pytest.raises(ValueError, match="Invalid question_id"):
            logger.log_response('', 'user1', 'A')
        
        # Empty user_id
        with pytest.raises(ValueError, match="Invalid user_id"):
            logger.log_response('q5', '', 'A')
        
        # None response
        with pytest.raises(ValueError, match="Response cannot be None"):
            logger.log_response('q6', 'user1', None)
    
    def test_non_string_inputs(self):
        """Test handling of non-string inputs"""
        logger = MultipleChoiceLogger(log_dir=self.test_log_dir)
        
        # Non-string inputs should be converted to strings
        log_entry = logger.log_response('q7', 'user1', 42)
        assert log_entry['response'] == '42'
        
        log_entry = logger.log_response('q8', 'user1', 3.14, valid_options=['3.14'])
        assert log_entry['response'] == '3.14'